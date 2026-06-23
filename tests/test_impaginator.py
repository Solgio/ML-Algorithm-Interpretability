import os
import json
import pandas as pd
import pytest
from src.core import impaginator

def test_load_metrics_and_coefficients(tmp_path, monkeypatch):
    # Set up simulated directory structure
    src_core = tmp_path / "src" / "core"
    src_output = tmp_path / "src" / "output"
    proj_dir = src_output / "test_proj"
    
    src_core.mkdir(parents=True)
    proj_dir.mkdir(parents=True)
    
    # Create mock metrics and coefficients files
    metrics_file = proj_dir / "metriche.json"
    metrics_file.write_text(json.dumps({"R_squared": 0.85, "MAE": 0.1, "RMSE": 0.12}))
    
    coef_file = proj_dir / "coefficienti.csv"
    pd.DataFrame({"Feature": ["x1"], "Coefficient": [1.5]}).to_csv(coef_file, index=False)
    
    # Change working directory to simulate running from src/core
    monkeypatch.chdir(src_core)
    
    # Test load functions
    m_path = impaginator.load_metrics("test_proj")
    c_path = impaginator.load_coefficients("test_proj")
    
    assert m_path is not None
    assert os.path.exists(m_path)
    assert c_path is not None
    assert os.path.exists(c_path)

def test_load_metrics_missing(tmp_path, monkeypatch):
    src_core = tmp_path / "src" / "core"
    src_core.mkdir(parents=True)
    monkeypatch.chdir(src_core)
    
    assert impaginator.load_metrics("non_existent") is None
    assert impaginator.load_coefficients("non_existent") is None

def test_generate_markdown_docs_success(tmp_path, monkeypatch):
    src_core = tmp_path / "src" / "core"
    src_output = tmp_path / "src" / "output"
    proj_dir = src_output / "test_proj"
    md_prompt_dir = src_output / "md_prompting" / "test_proj"
    
    src_core.mkdir(parents=True)
    proj_dir.mkdir(parents=True)
    md_prompt_dir.mkdir(parents=True)
    
    # Write mock data
    metrics_file = proj_dir / "metriche.json"
    metrics_file.write_text(json.dumps({"R_squared": 0.9, "MAE": 0.05, "RMSE": 0.07}))
    
    coef_file = proj_dir / "coefficienti.csv"
    pd.DataFrame({"Feature": ["x1", "x2"], "Coefficient": [0.5, -1.2]}).to_csv(coef_file, index=False)
    
    # Create a mock image
    img_file = md_prompt_dir / "residual_plot.png"
    img_file.write_text("png data")
    
    # Mock pandas to_markdown to avoid dependency on tabulate package
    monkeypatch.setattr(pd.DataFrame, "to_markdown", lambda self, *args, **kwargs: "mocked_markdown_table")
    
    # Run in simulated working directory
    monkeypatch.chdir(src_core)
    
    impaginator.generate_markdown_docs("test_proj")
    
    doc_path = src_core / "DOCUMENTATION_test_proj.md"
    assert doc_path.exists()
    
    content = doc_path.read_text(encoding="utf-8")
    assert "# Predictive Analysis Report: test_proj" in content
    assert "0.9000" in content  # R-squared value formatted
    assert "Residual Plot" in content
    assert "![Residual Plot]" in content
