DATASETS = {
    "Student Placement Dataset": {
        "task": "regression",
        "description": "Dataset che raccoglie una serie di metriche relative a studenti universitari e alle loro skills, esperienze alvorative, caratteristiche e risultati in test. L'obiettivo è prevedere quale sarà lo stipendio di un neolaureato in base a queste caratteristiche.",
        "source": "https://www.kaggle.com/datasets/spscientist/students-placement-dataset",
        "path": "C:\\Users\\SOLLOR\\Documents\\ML-Algorithm-Interpretability\\src\\data\\student-salary\\student_placement_salary_elite_v2.csv",
        "drop_columns": ['salary_lpa', 'placed', 'student_id'],
        "objective_column": "salary_lpa",
        "binary_categorical_features": ['student_id', 'branch', 'company_type', 'job_role', 'dsa_skill', 'ml_skill', 'web_dev_skill', 'placed']
    }
    
}