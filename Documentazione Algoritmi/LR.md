# Regressione Lineare (LR)

## Modello

```math
\displaystyle y= \sum_{i=0} \beta_{i} x_{i} \forall i \in F
```

Dove F è l'insieme degli input per le feature. L'obiettivo è vincolato ai pesi $\beta$:

```math
\displaystyle \hat{\beta} = arg min_{\beta_{0}...\beta_{p}} \sum_{i=1}^n(y^{(i)}-(\beta_{0}+\sum_{j=1}^p \beta_{j}x_{j}))^2
```

Viene minimizzato l'errore quadratico tra la previsione e la $y$ reale attraverso la soluzione analitica (forma chiusa):

```math
\displaystyle \hat{\beta} = (X^T X)^{-1} X^T y
```

dove X è la matrice dei dati aumentata della colonna di 1 per l'intercetta.

---

## Complessità Computazionale

### Training
- **Complessità principale:** $O(p^2 n + p^3)$
  - $O(p^2 n)$ per il calcolo della matrice $X^T X$
  - $O(p^3)$ per l'inversione della matrice
  
- **Memoria:** $O(p^2)$ per memorizzare la matrice quadrata X^T X

### Inference
- **Complessità:** $O(p)$ per istanza (moltiplicazione vettore-vettore)
- **Memoria:** $O(p)$ per il vettore dei coefficienti

### Considerazioni sulla Scalabilità
La dipendenza $O(p^3)$ dall'inversione matrice rende il modello computazionalmente **critico quando il numero di feature è elevato** (p >> 1000 diventa problematico). In questi scenari è preferibile usare metodi iterativi come Gradient Descent, che scalano meglio a costo di maggiore tempo di training.

La soluzione analitica è comunque vantaggiosa per dataset di **piccolo-medio volume** (n, p moderati) poiché:
- Garantisce convergenza in un unico passo
- Non richiede tuning di parametri (es. learning rate)
- Fornisce una soluzione globale ottimale

---

## Rappresentazione Interna

La regressione lineare rappresenta internamente il modello come un **vettore di pesi** $\beta = [\beta_0, \beta_1, ..., \beta_p]$.

**Implicazioni per la spiegabilità:**
- Rappresentazione **estremamente compatta e trasparente**: ogni feature ha un coefficiente direttamente interpretabile
- La previsione per una singola istanza è una combinazione lineare esplicita
- Non esiste una "scatola nera": il calcolo della predizione è completamente tracciabile
- Ogni peso corrisponde direttamente all'impatto della feature sulla predizione (impatto lineare e costante indipendentemente dal valore della feature)

**Contrasto con altri modelli:** Un albero di decisione rappresenta il modello come una struttura gerarchica complessa; un modello di regressione logistica introduce una trasformazione non lineare (logistica) dopo i pesi.

---

## Vincoli sui Dati

La regressione lineare richiede il rispetto di **6 assunzioni fondamentali**:

1. **Linearità dei vincoli:** le relazioni tra feature e target devono essere lineari. Interazioni o relazioni non lineari devono essere introdotte manualmente (es. termini quadratici $x^2$, interazioni $x_i \cdot x_j$)

2. **Normalità dei residui:** i residui $\epsilon_i = y_i - \hat{y}_i$ devono seguire una distribuzione normale. Violazioni gravi compromettono l'inferenza statistica (p-value, intervalli di confidenza)

3. **Omoschedasticità:** i residui devono avere varianza costante in tutti i livelli delle feature. In pratica, questa assunzione è **frequentemente violata**. Esempio: nel real estate, il prezzo di case molto grandi è estremamente variabile, mentre quello di case piccole è concentrato

4. **Indipendenza delle misure:** le osservazioni non devono essere correlate tra loro (es. non dati temporali consecutivi senza controllo). Dati dipendenti (come serie temporali) violano questa assunzione

5. **Feature fisse:** le feature devono essere considerate come costanti, non soggette a errori di misurazione significativi. Se le feature contengono errore di misura, i coefficienti sono distorti (attenuation bias)

6. **Assenza di multicollinearità:** le feature non devono essere fortemente correlate tra loro. Multicollinearità causa instabilità numerica durante l'inversione di $X^T X$ e pesi inflazionati in valore assoluto ma con segni incerti

---

## Capacità Predittive

**Punti di forza:**
- Eccellente per relazioni **linearmente separabili** tra feature e target
- Computazionalmente efficiente sia in training che in inference
- Soluzione **esatta e garantita** (non iterativa, senza convergenza incerta)

**Punti di debolezza:**
- **Assolutamente inadatto a pattern non lineari**: la forma funzionale rigida è un vincolo, non una feature
- Fortemente semplificativo: impone una struttura di relazione che spesso non esiste nei dati reali
- Sensibile agli **outlier**: errori grandi vengono quadrati nella loss function, amplificando l'effetto

**Limitazione strutturale:** Molti degli assunzioni su cui si basa risultano **non rispettati nella realtà**. L'omoschedasticità, ad esempio, è raramente verificata in problemi reali.

---

## Metriche per la Confidenza

### Metriche Pure

#### $R^2$ (Coefficiente di determinazione)
Quantifica quanto il modello spiega la varianza totale dei dati (range: 0 → 1)

```math
\displaystyle R^2=1-\frac{SSE}{SST}
```

Dove:
- $SSE=\sum_{i=1}^n(y^{(i)}-\hat{y}^{(i)})^2$ è la somma dei quadrati dei residui (varianza non spiegata)
- $SST=\sum_{i=1}^n(y^{(i)}-\bar{y})^2$ è la varianza totale

Interpretazione: $R^2 = 0.85$ significa che il modello spiega l'85% della variabilità totale.

#### $\bar{R}^2$ (R² aggiustato)
Variazione di $R^2$ che penalizza l'aggiunta di feature non utili. A differenza di $R^2$ che cresce sempre al crescere del numero di feature, $\bar{R}^2$ diminuisce se la feature aggiunta non compensa la complessità:

```math
\displaystyle \bar{R}^2= 1 - (1 - R^2)\frac{n-1}{n-p-1}
```

Dove $p$ è il numero di feature e $n$ il numero di istanze.

#### Feature Importance (t-statistic)
Misura la significatività statistica di ogni coefficiente, calcolata come il peso scalato per il suo errore standard:

```math
\displaystyle t_{\hat{\beta}_{j}}=\frac{\hat{\beta}_{j}}{SE(\hat{\beta}_{j})}
```

**Interpretazione:**
- Valori assoluti grandi → la feature è statisticamente significativa nella previsione
- Cresce al crescere del peso, diminuisce all'aumentare della varianza
- Associato a un **p-value** che quantifica la probabilità che il coefficiente sia dovuto al caso

#### p-value
Per ogni coefficiente, il p-value risponde: "Se il vero coefficiente fosse 0, quale è la probabilità di osservare un valore così estremo per $t_{\hat{\beta}_j}$?". Convention: p < 0.05 indica significatività.

#### Mallows' Cp
Criterio per la **selezione del modello** che bilancia errore di training con complessità:

```math
\displaystyle Cp=\frac{SSE}{\hat{\sigma}^2}-n+2p
```

Dove $\hat{\sigma}^2$ è la stima della varianza dei residui del modello completo. Un modello ideale ha $Cp \approx p+1$.

#### RMSE (Root Mean Squared Error)
Misura la magnitudine media degli errori, nella stessa scala della variabile target:

```math
\displaystyle RMSE=\sqrt{\frac{SSE}{n}}
```

#### MAE (Mean Absolute Error)
Alternativa a RMSE, meno sensibile agli outlier:

```math
\displaystyle MAE=\frac{1}{n}\sum_{i=1}^n |y_i - \hat{y}_i|
```

### Analisi dei Plot

#### Actual vs Predicted
Grafico di dispersione (scatter plot) tra valori reali $y_i$ e predetti $\hat{y}_i$.
- **Interpretazione corretta:** punti concentrati intorno alla diagonale $y = \hat{y}$
- **Anomalie:** dispersione crescente con il valore predetto (eteroschedasticità), o pattern sistematico (non linearità)

#### Istogramma dei Residui
Distribuzione dei residui $\epsilon_i = y_i - \hat{y}_i$.
- **Interpretazione corretta:** distribuzione simmetrica e campanulare (normale)
- **Anomalie:** asimmetria o code pesanti indicano violazione della normalità

#### Q-Q Plot (Quantile-Quantile)
Rappresenta i quantili empirici dei residui vs i quantili di una distribuzione normale.
- **Interpretazione corretta:** punti seguono la retta diagonale
- **Anomalie:** deviazioni sistematiche (specialmente alle code) indicano non normalità

#### Residuals vs Fitted Values
Grafico di dispersione con asse x = valori predetti $\hat{y}_i$, asse y = residui $\epsilon_i$.
- **Interpretazione corretta:** nuvola di punti senza pattern, orizzontale attorno a 0
- **Anomalie:** 
  - Pattern sistematico (curva) → non linearità
  - Varianza crescente con x → eteroschedasticità
  - Bande orizzontali → outlier o dati discreti

---

## Metriche per la Comprensione e Spiegabilità

### Feature Effect
Rappresentazione dell'impatto di ogni feature sulla previsione, calcolato come:

```math
\displaystyle effect_{j}^{(i)}=\beta_{j}x_{j}^{(i)}
```

**Visualizzazione:** box plot per quartili (25%-75%) per ogni feature
- **Larghezza del box** = variabilità dell'effetto nei dati reali
- Una feature con box ampio ha un impatto medio elevato sulla previsione
- Utile per identificare quali feature contano di più

### Weight Plot
Rappresentazione grafica dei coefficienti $\beta_j$ ordinati per valore assoluto.
- Feature con barre lunghe hanno maggiore influenza sulla previsione
- Utile per comunicare rapidamente l'importanza relativa delle feature

### Interpretazione Diretta dei Coefficienti
Ogni coefficiente $\beta_j$ ha un'interpretazione immediata: "aumentando la feature $x_j$ di 1 unità, la previsione cambia di $\beta_j$ unità" (mantenendo le altre feature costanti).

Questa **trasparenza è il vantaggio principale** della regressione lineare per la spiegabilità rispetto a modelli più complessi.

---

## Limiti di Predizione

### Sensibilità agli Outlier
L'errore quadratico nella loss function amplifica gli outlier: un errore di 10 unità contribuisce 100 alla loss, quindi il modello tende a distorcersi per minimizzare outlier singolari.

### Problemi di Extrapolazione
La regressione lineare assume che la relazione lineare continui al di fuori dell'intervallo osservato dei dati. Predizioni su valori di feature molto diversi dal training set sono estremamente inaffidabili.

### Instabilità Numerica in Caso di Multicollinearità
Se le feature sono altamente correlate, la matrice $X^T X$ diventa mal-condizionata (quasi singolare), rendendo l'inversione numericamente instabile e i coefficienti instabili.

### Insufficienza su Pattern Non Lineari
Non esiste modifica parametrica che possa far adattare un modello lineare a relazioni veramente non lineari senza inserire manualmente termini non lineari (e questo richiede conoscenza a priori della forma della relazione).

### Collasso su Dati ad Alta Dimensionalità
Quando il numero di feature è prossimo o superiore al numero di osservazioni ($p \approx n$ o $p > n$), il modello tende a sovradattarsi, con $R^2$ perfetto sul training e pessimo sul test.

---

## Limiti di Spiegabilità

### Non Linearità Nascosta nei Dati
Se la vera relazione è non lineare ma viene forzata in un modello lineare, i coefficienti rappresentano una "media" della relazione, non la relazione vera. Un coefficiente positivo in media potrebbe mascherare un effetto che è positivo per alcuni valori della feature e negativo per altri.

### Interazioni Non Modellate
La regressione lineare base assume indipendenza degli effetti delle feature: l'effetto di $x_1$ non dipende da $x_2$. Se esistono interazioni significative, il modello le ignora (a meno che non siano aggiunte manualmente).

### Sensibilità al Livello di Dettaglio
La scelta di quante feature includere è delicata: troppe causano overfitting e spiegabilità confusa, troppo poche rendono le spiegazioni superficiali e imprecise.

### Difficoltà con Feature Categoriche
Le feature categoriche devono essere codificate (es. one-hot encoding), il che aumenta $p$ e complessità interpretativa (un concetto logico diventa p variabili binarie).

### Selettività
La capacità di identificare solo le feature veramente rilevanti può essere raggiunta in due modi:
- **Selezione manuale a priori:** affidamento a esperti di dominio
- **Modelli sparse (Lasso):** introduzione di penalità L1 che forzano molti coefficienti a 0
- **Metodi stepwise:** aggiunta/rimozione iterativa di feature

---

## Confronto con altri Algoritmi

### Vs. Regressione Logistica
- **LR:** per relazioni lineari **continue**
- **Logistica:** per classificazione binaria, produce probabilità dirette
- La logistica non è un'estensione di LR, ma un modello distinto per un problema diverso

### Vs. Decision Tree
- **LR:** trasparente, coefficienti interpreti, ma rigida (niente non linearità)
- **DT:** flessibile, cattura non linearità e interazioni, ma rappresentazione complessa e instabile
- **Scelta:** dati lineari → LR; pattern complessi non lineari → DT

### Vs. Lasso / Ridge
- **LR standard:** minimizza SSE senza penalità
- **Ridge:** aggiunge penalità L2 $\lambda||\beta||_2^2$, riducendo i pesi ma mantenendo tutte le feature
- **Lasso:** aggiunge penalità L1 $\lambda||\beta||_1$, azzerando pesi (selezione automatica di feature)
- **Quando usare:** multicollinearità o alta dimensionalità → Ridge/Lasso

### Vs. Selezione Manuale di Feature
- **Selezione Lasso/Ridge:** automatica, basata sui dati
- **Selezione manuale:** richiede expertise di dominio, ma può catturare conoscenza esterna
- **Metodi stepwise (Forward/Backward):** compromesso automatico ma interpretabile

#### Forward Selection
Aggiunta passo-passo di feature: at ogni passo, aggiungere la feature che massimizza una metrica di controllo (es. $R^2$). Stop quando non c'è miglioramento significativo.

#### Backward Selection
Opposto: partire da tutte le feature, rimuovere iterativamente quella con contributo minore.

### Vs. Generalized Additive Models (GAM)
- **LR:** effetti lineari e additivi
- **GAM:** combina LR con funzioni non lineari flessibili (splines) per ogni feature
- Il modello rimane **additivo** (effetti indipendenti) ma **non lineare** (curve invece di rette)

---

## Prompt

