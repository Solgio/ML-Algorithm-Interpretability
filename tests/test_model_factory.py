from src.core.infrastructure.models.exceptions import (
    ModelCreationError,
    ModelNotFoundError,
    ModelRegistrationError,
)
from src.core.infrastructure.models.model_factory import ModelFactory
from types import ModuleType

import pandas as pd
import pytest

from src.core.domain.enums import Algorithm, TaskType
from src.core.domain.value_object import AlgorithmRegistry


def test_model_factory_register_and_registry_views(monkeypatch):
    ModelFactory.clear()

    entry = AlgorithmRegistry(
        algorithm=Algorithm.LINEAR_REGRESSION,
        task_type=TaskType.REGRESSION,
        module_path="fake.module",
        class_name="FakeModel",
        prompt="prompt",
        description="description",
        param_grid={"alpha": [1]},
    )

    ModelFactory.register(entry)
    assert ModelFactory.is_registered(Algorithm.LINEAR_REGRESSION, TaskType.REGRESSION) is True
    assert ModelFactory.get_description(Algorithm.LINEAR_REGRESSION, TaskType.REGRESSION) == "description"
    assert ModelFactory.get_param_grid(Algorithm.LINEAR_REGRESSION, TaskType.REGRESSION) == {"alpha": [1]}
    assert ModelFactory.get_prompt(Algorithm.LINEAR_REGRESSION, TaskType.REGRESSION) == "prompt"
    assert ModelFactory.list_algorithms(TaskType.REGRESSION) == ["Linear Regression"]
    assert ModelFactory.list_algorithms() == ["Linear Regression"]
    info = ModelFactory.get_all_info(Algorithm.LINEAR_REGRESSION, TaskType.REGRESSION)
    assert info["class"] == "FakeModel"
    registry = ModelFactory.get_registry()
    assert "linear_regression_regression" in registry


def test_model_factory_register_invalid_entry_raises():
    ModelFactory.clear()
    entry = AlgorithmRegistry(
        algorithm=Algorithm.SVM,
        task_type=TaskType.CLASSIFICATION,
        module_path="",
        class_name="FakeModel",
    )

    with pytest.raises(ModelRegistrationError):
        ModelFactory.register(entry)


def test_model_factory_create_type_and_not_found_raises():
    ModelFactory.clear()

    with pytest.raises(TypeError):
        ModelFactory.create("not-enum", TaskType.CLASSIFICATION, "ds", ".")

    with pytest.raises(TypeError):
        ModelFactory.create(Algorithm.SVM, "not-task", "ds", ".")

    with pytest.raises(ModelNotFoundError):
        ModelFactory.create(Algorithm.SVM, TaskType.CLASSIFICATION, "ds", ".")


def test_model_factory_create_module_class_and_ctor_errors(monkeypatch):
    ModelFactory.clear()

    bad_module = ModuleType("fake_bad_module")
    monkeypatch.setitem(__import__("sys").modules, "fake_bad_module", bad_module)
    ModelFactory.register(
        AlgorithmRegistry(
            algorithm=Algorithm.SVM,
            task_type=TaskType.CLASSIFICATION,
            module_path="fake_bad_module",
            class_name="MissingClass",
            description="desc",
        )
    )

    with pytest.raises(ModelCreationError):
        ModelFactory.create(Algorithm.SVM, TaskType.CLASSIFICATION, "ds", ".")

    ModelFactory.clear()
    ctor_module = ModuleType("fake_ctor_module")

    class BadCtor:
        def __init__(self, dataset, dataset_path, param_grid):
            raise TypeError("bad ctor")

    ctor_module.BadCtor = BadCtor
    monkeypatch.setitem(__import__("sys").modules, "fake_ctor_module", ctor_module)
    ModelFactory.register(
        AlgorithmRegistry(
            algorithm=Algorithm.SVM,
            task_type=TaskType.CLASSIFICATION,
            module_path="fake_ctor_module",
            class_name="BadCtor",
            description="desc",
        )
    )

    with pytest.raises(ModelCreationError):
        ModelFactory.create(Algorithm.SVM, TaskType.CLASSIFICATION, "ds", ".")


def test_model_factory_get_all_info_missing_raises():
    ModelFactory.clear()
    with pytest.raises(ModelNotFoundError):
        ModelFactory.get_all_info(Algorithm.SVM, TaskType.CLASSIFICATION)
