from src.core.domain.enums import Algorithm, TaskType
from src.core.infrastructure.models.model_factory import ModelFactory
from src.core.infrastructure.models.registry_initializer import initialize_model_registry

print("Test 1: Inizializzazione...")
initialize_model_registry()
print("✓ OK")

print("\nTest 2: Recupera prompt SVM...")
prompt = ModelFactory.get_prompt(Algorithm.SVM, TaskType.CLASSIFICATION)
print(f"Prompt: {prompt[:80]}...")
assert prompt is not None
print("✓ OK")

print("\nTest 3: Recupera param_grid SVM...")
param_grid = ModelFactory.get_param_grid(Algorithm.SVM, TaskType.CLASSIFICATION)
print(f"Param grid keys: {list(param_grid.keys())}")
assert param_grid is not None
assert 'C' in param_grid
print("✓ OK")

print("\nTest 4: Recupera info completa...")
info = ModelFactory.get_all_info(Algorithm.LINEAR_REGRESSION, TaskType.REGRESSION)
print(f"Info keys: {list(info.keys())}")
assert 'prompt' in info
assert 'param_grid' in info
print("✓ OK")

print("\n✓✓✓ TUTTI I TEST PASSATI ✓✓✓")