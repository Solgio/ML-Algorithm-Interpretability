url_student_dataset = "https://www.kaggle.com/datasets/spscientist/students-placement-dataset"
path_student_dataset = "src/data/student-salary/student_placement_salary_elite_v2.csv"

from src.core.domain.enums import TaskType

DATASETS = {
    "Student Salary Dataset": {
        "task": TaskType.REGRESSION,
        "description": "Dataset that collects a series of metrics relating to university students and their skills, work experiences, characteristics, and test results. The goal is to predict what a new graduate's salary will be based on these characteristics.",
        "source": url_student_dataset,
        "path": path_student_dataset,
        "drop_columns": ['placed', 'student_id'],
        "objective_column": "salary_lpa",
        "binary_categorical_features": ['student_id', 'branch', 'company_type', 'job_role', 'dsa_skill', 'ml_skill', 'web_dev_skill', 'placed'],
        "shap_dependence_variable": ["cgpa"]
    },
    "Student Company Type Dataset": {
        "task": TaskType.CLASSIFICATION,
        "description": "Dataset that collects a series of metrics relating to university students and their skills, work experiences, characteristics, and test results. The goal is to predict what type of company a new graduate will be placed in based on these characteristics.",
        "source": url_student_dataset,
        "path": path_student_dataset,
        "drop_columns": ['salary_lpa', 'placed', 'student_id', 'job_role'],
        "objective_column": "company_type",
        "binary_categorical_features": ['student_id', 'branch', 'company_type', 'job_role', 'dsa_skill', 'ml_skill', 'web_dev_skill', 'placed'],
        "shap_dependence_variable": ["cgpa"]
    },
    "Student Placed-Not Placed Dataset": {
        "task": TaskType.CLASSIFICATION,
        "description": "Dataset that collects a series of metrics relating to university students and their skills, work experiences, characteristics, and test results. The goal is to predict whether a new graduate will be placed in a company based on these characteristics.",
        "source": url_student_dataset,
        "path": path_student_dataset,
        "drop_columns": ['salary_lpa', 'student_id', 'company_type', 'job_role'],
        "objective_column": "placed",
        "binary_categorical_features": ['student_id', 'branch', 'company_type', 'job_role', 'dsa_skill', 'ml_skill', 'web_dev_skill', 'placed'],
        "shap_dependence_variable": ["cgpa"]
    },
    "Atelier Dataset": {
        "task": TaskType.CLASSIFICATION,
        "description": "...",
        "source": "...",
        "path": "src/data/atelier/prodotti_atelier.csv",
        "drop_columns": ['codice_cliente', 'nome_cliente'],
        "objective_column": "is_cloud",
        "binary_categorical_features": ['is_cloud', 'codice_ateco', 'provincia', 'mercato'],
        "shap_dependence_variable": ["dipendenti"]
    },
    "Nasa Asteroid Dataset": {
        "task": TaskType.CLASSIFICATION,
        "description": "Dataset containing metrics about asteroids. The goal is to predict if an asteroid is hazardous.",
        "source": url_student_dataset,
        "path": path_student_dataset,
        "drop_columns": ['id', 'name', 'absolute_magnitude_h', 'relative_velocity_km_per_sec', 'miss_distance_kilometers', 'orbiting_body'],
        "objective_column": "hazardous",
        "binary_categorical_features": ['hazardous'],
        "shap_dependence_variable": ["estimated_diameter_min"]
    }
    
    
    
}