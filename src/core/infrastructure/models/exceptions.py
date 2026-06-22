class ModelError(Exception):
    """Base class for exceptions in this module."""
    pass

class ModelNotFoundError(ModelError):
    """Exception raised when a model is not found in the registry."""
    def __init__(self, algorithm: str, task_type: str, available: list=None):
        self.algorithm = algorithm
        self.task_type = task_type
        
        message = f"Algorithm '{algorithm}' for task '{task_type}' not found"
        
        if available:
            message += "\nAvailable algorithms:\n"
            for algo in available:
                message += f"  - {algo}\n"
        super().__init__(message)
        
class ModelCreationError(ModelError):
    """Exception raised when there is an error during model creation."""
    def __init__(self, algorithm: str, task_type: str, original_exception: Exception):
        self.algorithm = algorithm
        self.task_type = task_type
        self.original_exception = original_exception
        
        message = (f"Failed to create model for algorithm '{algorithm}' "
                   f"and task '{task_type}'. Original error: {str(original_exception)}")
        super().__init__(message)

class ModelRegistrationError(ModelError):
    """Exception raised when there is an error during model registration."""
    def __init__(self, algorithm: str, task_type: str, reason: str):
        self.algorithm = algorithm
        self.task_type = task_type
        self.reason = reason
        
        message = (f"Failed to register model for algorithm '{algorithm}' "
                   f"and task '{task_type}'. Reason: {reason}")
        super().__init__(message)
        