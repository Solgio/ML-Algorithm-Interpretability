url_student_dataset = "https://www.kaggle.com/datasets/spscientist/students-placement-dataset"
path_student_dataset = "../data/student-salary/student_placement_salary_elite_v2.csv"
DATASETS = {
    "Student Salary Dataset": {
        "task": "regression",
        "description": "Dataset che raccoglie una serie di metriche relative a studenti universitari e alle loro skills, esperienze lavorative, caratteristiche e risultati in test. L'obiettivo è prevedere quale sarà lo stipendio di un neolaureato in base a queste caratteristiche.",
        "source": url_student_dataset,
        "path": path_student_dataset,
        "drop_columns": ['salary_lpa', 'placed', 'student_id'],
        "objective_column": "salary_lpa",
        "binary_categorical_features": ['student_id', 'branch', 'company_type', 'job_role', 'dsa_skill', 'ml_skill', 'web_dev_skill', 'placed'],
        "shap_dependence_variable": ["cgpa"]
    },
    "Student Company Type Dataset": {
        "task": "classification",
        "description": "Dataset che raccoglie una serie di metriche relative a studenti universitari e alle loro skills, esperienze lavorative, caratteristiche e risultati in test. L'obiettivo è prevedere quale in quale tipo di azienda un neolaureato verrà collocato in base a queste caratteristiche.",
        "source": url_student_dataset,
        "path": path_student_dataset,
        "drop_columns": ['salary_lpa', 'placed', 'student_id', 'job_role', 'company_type'],
        "objective_column": "company_type",
        "binary_categorical_features": ['student_id', 'branch', 'company_type', 'job_role', 'dsa_skill', 'ml_skill', 'web_dev_skill', 'placed'],
        "shap_dependence_variable": ["cgpa"]
    },
    "Student Placed-Not Placed Dataset": {
        "task": "classification",
        "description": "Dataset che raccoglie una serie di metriche relative a studenti universitari e alle loro skills, esperienze lavorative, caratteristiche e risultati in test. L'obiettivo è prevedere se un neolaureato sarà collocato in un'azienda in base a queste caratteristiche.",
        "source": url_student_dataset,
        "path": path_student_dataset,
        "drop_columns": ['salary_lpa', 'student_id', 'company_type', 'job_role', 'placed'],
        "objective_column": "placed",
        "binary_categorical_features": ['student_id', 'branch', 'company_type', 'job_role', 'dsa_skill', 'ml_skill', 'web_dev_skill', 'placed'],
        "shap_dependence_variable": ["cgpa"]
    },
    "Nasa Asteroid Dataset": {
        "task": "classification",
        "description": "Dataset che raccoglie una serie di metriche relative a studenti universitari e alle loro skills, esperienze lavorative, caratteristiche e risultati in test. L'obiettivo è prevedere se un neolaureato sarà collocato in un'azienda in base a queste caratteristiche.",
        "source": url_student_dataset,
        "path": path_student_dataset,
        "drop_columns": ['id', 'name', 'absolute_magnitude_h', 'relative_velocity_km_per_sec', 'miss_distance_kilometers', 'orbiting_body'],
        "objective_column": "hazardous",
        "binary_categorical_features": ['hazardous'],
        "shap_dependence_variable": ["estimated_diameter_min"]
    }
    
    
    
}