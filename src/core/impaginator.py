import os
import json
import pandas as pd

def generate_markdown_docs(project_name="LR_Salary"):
    json_path=load_metrics(project_name)
    csv_path=load_coefficients(project_name)
    
    if not json_path or not csv_path:
        print("Error: Impossible to generate documentation due to missing data.")
        return
    
    output_file = f"DOCUMENTATION_{project_name}.md"
    output_dir = os.path.join("..", "output", "md_prompting", project_name)


    with open(json_path, 'r') as f:
        metriche = json.load(f)
        
    coef_df = pd.read_csv(csv_path)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"# Predictive Analysis Report: {project_name}\n\n")
        
        # METRICHE
        f.write("## 1. Model Confidence Metrics\n")
        f.write("Linear Regression model trained on the subset of students entered.\n\n")
        
        f.write("| Metric | Value |\n| :--- | :--- |\n")
        f.write(f"| R-squared | {metriche.get('R_squared', 0):.4f} |\n")
        f.write(f"| Mean Absolute Error (MAE) | {metriche.get('MAE', 0):.4f} |\n")
        f.write(f"| Root Mean Squared Error (RMSE) | {metriche.get('RMSE', 0):.4f} |\n\n")

        # COEFFICIENTI
        f.write("## 2. Coefficient Analysis\n")
        f.write("Model coefficient values, divided for quick consultation (Bland's rule: maximum readability).\n\n")
        
        chunk_size = 10
        for i in range(0, len(coef_df), chunk_size):
            page = (i // chunk_size) + 1
            f.write(f"### Block {page} (Feature {i+1} - {min(i+chunk_size, len(coef_df))})\n")
            f.write(coef_df.iloc[i:i+chunk_size].to_markdown(index=False))
            f.write("\n\n---\n\n")

        # GRAFICI
        f.write("## 3. Visual and Diagnostic Analysis\n")
        f.write("Below are the diagnostic charts exported automatically during the model run.\n\n")
        
        if os.path.exists(output_dir):
            immagini = [img for img in os.listdir(output_dir) if img.endswith(".png")]
        else:
            immagini = []
        
        if immagini:
            for img in sorted(immagini):
                nome_grafico = img.replace(".png", "").replace("_", " ").title()
                
                path_relativo = f"{output_dir}/{img}".replace("\\", "/") 
                
                f.write(f"### {nome_grafico}\n")
                f.write(f"![{nome_grafico}]({path_relativo})\n\n")
        else:
            f.write("_No graphs found in the output folder._\n\n")
            
    print(f"Documentation created successfully in: {output_file}")

# def generate_markdown_docs(project_name="LogR_Salary"):
#    json_path=load_metrics(project_name)
#    csv_path=load_coefficients(project_name)
#    output_file = f"DOCUMENTATION_{project_name}.md"
#
#    with open(json_path, 'r') as f:
#        metriche = json.load(f)
#        
#    coef_df = pd.read_csv(csv_path)
#
#    with open(output_file, "w", encoding="utf-8") as f:
#        f.write(f"# Relazione Analisi Predittiva: {project_name}\n\n")
#        
#        # METRICHE
#        f.write("## 1. Metriche di Confidenza del Modello\n")
#        f.write("Modello di Regressione Lineare addestrato sul subset degli studenti inseriti.\n\n")
#        
#        f.write("| Metrica | Valore |\n| :--- | :--- |\n")
#        f.write(f"| R-squared | {metriche.get('R_squared', 0):.4f} |\n")
#        f.write(f"| Mean Absolute Error (MAE) | {metriche.get('MAE', 0):.4f} |\n")
#        f.write(f"| Root Mean Squared Error (RMSE) | {metriche.get('RMSE', 0):.4f} |\n\n")
#
#        # COEFFICIENTI
#        f.write("## 2. Analisi dei Coefficienti\n")
#        f.write("Valori dei coefficienti del modello, suddivisi per una consultazione rapida (Bland's rule: massima leggibilità).\n\n")
#        
#        chunk_size = 10
#        for i in range(0, len(coef_df), chunk_size):
#            page = (i // chunk_size) + 1
#            f.write(f"### Blocco {page} (Feature {i+1} - {min(i+chunk_size, len(coef_df))})\n")
#            f.write(coef_df.iloc[i:i+chunk_size].to_markdown(index=False))
#            f.write("\n\n---\n\n")
#
#        # GRAFICI
#        f.write("## 3. Analisi Visuale e Diagnostica\n")
#        f.write("Di seguito i grafici diagnostici esportati in automatico durante la run del modello.\n\n")
#        
#        immagini = [img for img in os.listdir(output_dir) if img.endswith(".png")]
#        
#        if immagini:
#            for img in sorted(immagini):
#                nome_grafico = img.replace(".png", "").replace("_", " ").title()
#                
#                path_relativo = f"{output_dir}/{img}".replace("\\", "/") 
#                
#                f.write(f"### {nome_grafico}\n")
#                f.write(f"![{nome_grafico}]({path_relativo})\n\n")
#        else:
#            f.write("_Nessun grafico trovato nella cartella di output._\n\n")
#            
#    print(f"Documentazione creata con successo in: {output_file}")

def load_metrics(project_name):
    output_dir = os.path.join("..", "output", project_name)
    
    json_path = os.path.join(output_dir, "metriche.json")
    
    if not os.path.exists(json_path):
        print(f"Error: Data not found in {output_dir}. Run the Notebook first to export files.")
        return None
    return json_path

def load_coefficients(project_name):
    output_dir = os.path.join("..", "output", project_name)
    csv_path = os.path.join(output_dir, "coefficienti.csv")
    if not os.path.exists(csv_path):
        print(f"Error: Data not found in {output_dir}. Run the Notebook first to export files.")
        return None
    return csv_path

if __name__ == "__main__":
    generate_markdown_docs("LR_Salary")