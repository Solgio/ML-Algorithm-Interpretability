import pytest

from src.core import selector
from src.core.domain.enums import Algorithm, AnalysisType, TaskType


def test_confirm_yes_no(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda prompt='': 's')
    assert selector._confirm("Proceed?") is True

    monkeypatch.setattr('builtins.input', lambda prompt='': 'n')
    assert selector._confirm("Proceed?") is False


def test_select_options_defaults_and_flags(monkeypatch):
    # sequence: empty (default test_size), 's' for SHAP, 'n' for LLM
    inputs = iter(["", "s", "n"])
    monkeypatch.setattr('builtins.input', lambda prompt='': next(inputs))

    opts = selector.select_options()
    assert opts['test_size'] == 0.2
    assert opts['run_shap'] is True
    assert opts['run_llm'] is False


def test_print_menu_retries_until_valid(monkeypatch, capsys):
    inputs = iter(["x", "2"])
    monkeypatch.setattr("builtins.input", lambda prompt='': next(inputs))

    idx = selector._print_menu("Menu", ["a", "b", "c"])

    assert idx == 1
    assert "Inserisci un numero" in capsys.readouterr().out


def test_select_analysis_type_both_branches(monkeypatch):
    monkeypatch.setattr(selector, "_print_menu", lambda title, options: 0)
    assert selector.select_analysis_type() == AnalysisType.COMPARATIVE

    monkeypatch.setattr(selector, "_print_menu", lambda title, options: 1)
    assert selector.select_analysis_type() == AnalysisType.SINGLE


def test_select_dataset_returns_config(monkeypatch):
    monkeypatch.setattr(selector, "_print_menu", lambda title, options: 0)
    name, cfg = selector.select_dataset()

    assert name in selector.DATASETS
    assert cfg == selector.DATASETS[name]


def test_select_algorithm_no_available_algorithms(monkeypatch):
    monkeypatch.setattr(selector.ModelFactory, "list_algorithms", lambda task: [])

    try:
        selector.select_algorithm(TaskType.CLASSIFICATION)
        assert False, "Expected ValueError"
    except ValueError as exc:
        assert "Nessun algoritmo disponibile" in str(exc)


def test_select_algorithm_retries_and_returns_valid_choice(monkeypatch):
    monkeypatch.setattr(selector.ModelFactory, "list_algorithms", lambda task: ["Logistic Regression"])
    monkeypatch.setattr(selector.ModelFactory, "get_description", lambda algo, task: "desc")
    inputs = iter(["0", "1"])
    monkeypatch.setattr("builtins.input", lambda prompt='': next(inputs))

    algo = selector.select_algorithm(TaskType.CLASSIFICATION)
    assert algo == Algorithm.LOGISTIC_REGRESSION


def test_select_options_retries_invalid_then_accepts(monkeypatch):
    inputs = iter(["abc", "1.5", "0.3", "s", "n"])
    monkeypatch.setattr("builtins.input", lambda prompt='': next(inputs))

    options = selector.select_options()
    assert options == {"test_size": 0.3, "run_shap": True, "run_llm": False}


def test_run_selector_single_and_comparative(monkeypatch):
    monkeypatch.setattr(selector, "_confirm", lambda q: True)
    monkeypatch.setattr(selector, "select_options", lambda: {"test_size": 0.2, "run_shap": False, "run_llm": False})
    monkeypatch.setattr(selector.ModelFactory, "get_all_info", lambda algo, task: {"prompt": "p"})

    monkeypatch.setattr(selector, "select_analysis_type", lambda: AnalysisType.SINGLE)
    monkeypatch.setattr(selector, "select_dataset", lambda: ("dataset", {"task": "classification", "description": "desc"}))
    monkeypatch.setattr(selector, "select_algorithm", lambda task: Algorithm.LOGISTIC_REGRESSION)
    single = selector.run_selector()
    assert single["algo_enum"] == Algorithm.LOGISTIC_REGRESSION
    assert single["algo_name"] == str(Algorithm.LOGISTIC_REGRESSION)

    monkeypatch.setattr(selector, "select_analysis_type", lambda: AnalysisType.COMPARATIVE)
    monkeypatch.setattr(selector.ModelFactory, "list_algorithms", lambda task: ["Logistic Regression", "SVM"])
    comparative = selector.run_selector()
    assert comparative["algorithms"] == [Algorithm.LOGISTIC_REGRESSION, Algorithm.SVM]


def test_run_selector_cancel_raises_system_exit(monkeypatch):
    monkeypatch.setattr(selector, "select_analysis_type", lambda: AnalysisType.SINGLE)
    monkeypatch.setattr(selector, "select_dataset", lambda: ("dataset", {"task": "classification", "description": "desc"}))
    monkeypatch.setattr(selector, "select_algorithm", lambda task: Algorithm.LOGISTIC_REGRESSION)
    monkeypatch.setattr(selector, "select_options", lambda: {"test_size": 0.2, "run_shap": False, "run_llm": False})
    monkeypatch.setattr(selector, "_confirm", lambda q: False)
    monkeypatch.setattr(selector.ModelFactory, "get_all_info", lambda algo, task: {"prompt": "p"})

    try:
        selector.run_selector()
        assert False, "Expected SystemExit"
    except SystemExit as exc:
        assert exc.code == 0
