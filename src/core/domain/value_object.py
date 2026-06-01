
from dataclasses import dataclass, field
from typing import Any, Dict, Optional

from domain.enums import TaskType, Algorithm
import logging
    
@dataclass
class AlgorithmRegistry:
    """Value object for the registry of algorithms."""
    
    algorithm: 'Algorithm'
    task_type: 'TaskType'
    module_path: str
    class_name: str
    prompt: Optional[str] = None
    description: Optional[str] = None
    param_grid: Optional[Dict[str, Any]] = None
    
    def validate(self):
        """Validate the registry entry."""
        if not self.module_path or not self.module_path.strip():
            raise ValueError("Module path must be provided.")
        if not self.class_name or not self.class_name.strip():
            raise ValueError("Class name cannot be empty.")
        
        if not all(c.isalnum() or c in '._' for c in self.module_path):
            raise ValueError(f"invalid module_path: {self.module_path}")
        
        if not self.class_name.isidentifier():
            raise ValueError(f"class_name is not a valid identifier: {self.class_name}")

        if self.param_grid and not isinstance(self.param_grid, dict):
            raise ValueError("param_grid must be a dictionary")
        
        logging.info(f"✓ Registry entry validated: {self.algorithm} ({self.task_type})")
    
    def __repr__(self):
        return (f"AlgorithmRegistry(algorithm={self.algorithm}, task_type={self.task_type}, "
                f"module_path='{self.module_path}', class_name='{self.class_name}', "
                f"prompt={self.prompt}, "
                f"description={self.description}, param_grid={self.param_grid})")
    