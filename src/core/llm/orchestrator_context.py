from src.core.llm.interfaces import LLMService, OrchestrationStrategy

class LLMOrchestrator:
    """Context class that executes LLM evaluations using a specified Strategy."""
    
    def __init__(self, strategy: OrchestrationStrategy, llm_service: LLMService):
        self._strategy = strategy
        self._llm_service = llm_service

    @property
    def strategy(self) -> OrchestrationStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: OrchestrationStrategy):
        self._strategy = strategy

    @property
    def llm_service(self) -> LLMService:
        return self._llm_service

    @llm_service.setter
    def llm_service(self, llm_service: LLMService):
        self._llm_service = llm_service

    def run(self, tasks: list[dict], models: list[str]) -> dict:
        """Executes the analysis using the configured strategy and LLM service."""
        return self._strategy.execute(tasks, models, self._llm_service)
