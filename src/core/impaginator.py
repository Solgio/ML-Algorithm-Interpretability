import pandas as pd

# Importazione pulita: non aprirà i grafici di LR.py
from LR import model, X, r_squared, mae, root_mean_squared_error

def generate_markdown_docs(output_file="DOCUMENTATION.md"):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# Relazione Analisi Predittiva: Salary Dataset\n\n")
        
        f.write("## 1. Metriche di Confidenza del Modello\n")
        f.write("Modello di Regressione Lineare addestrato sul subset degli studenti inseriti (`placed == 1`).\n\n")
        
        metrics_table = (
            "| Metrica | Valore |\n"
            "| :--- | :--- |\n"
            f"| R-squared | {r_squared:.4f} |\n"
            f"| Mean Absolute Error (MAE) | {mae:.4f} |\n"
            f"| Root Mean Squared Error (RMSE) | {root_mean_squared_error:.4f} |\n\n"
        )
        f.write(metrics_table)

        f.write("## 2. Analisi dei Coefficienti\n")
        f.write("Valori dei coefficienti del modello di regressione, paginati per chiarezza di lettura.\n\n")
        
        coef_df = pd.DataFrame({'Feature': X.columns, 'Coefficiente': model.coef_})
        
        chunk_size = 10
        for i in range(0, len(coef_df), chunk_size):
            page = (i // chunk_size) + 1
            f.write(f"### Blocco {page} (Feature {i+1} - {min(i+chunk_size, len(coef_df))})\n")
            f.write(coef_df.iloc[i:i+chunk_size].to_markdown(index=False))
            f.write("\n\n---\n\n")

        f.write("## 3. Spiegabilità e SHAP Values\n")
        f.write("Le metriche di spiegabilità locale e globale sono state calcolate tramite campionamento di 100 record (`X100`).\n")
        f.write("Per l'interpretazione visiva dell'impatto delle variabili (es. `cgpa`), fare riferimento ai grafici Partial Dependence e Beeswarm generati dall'esecuzione principale dello script.\n")
        
    print(f"Documentazione creata con successo in: {output_file}")

if __name__ == "__main__":
    generate_markdown_docs()