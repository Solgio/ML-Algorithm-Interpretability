# Modello

```math
\displaystyle y= \sum_{i=0} \beta_{i} x_{i} \forall i \in F
```
Dove F è l'insieme degli input per le feature
L'obiettivo è vincolato ai pesi $\beta$:
```math
\displaystyle \hat{\beta} = arg min_{\beta_{0}...\beta_{p}} \sum_{i=1}^n(y^{(i)}-(\beta_{0}+\sum_{j=1}^p \beta_{j}x_{j}))^2
```
Viene minimizzato l'errore quadratico tra la previsione e la $y$ reale.

# Vincoli sui dati
Sono presenti 6 vincoli fondamentali sui dati:
- **Linearità dei vincoli:** le relazioni sono lineari e diverse interazioni devono essere applicate manualmente.
- **Normalità dei residui:** i residui devono seguire una distribuzione normale.
- **Omoschedasticità:** i residui devono avere varianza costante.
- **Indipendenza delle misure:** le misurazioni non devono influenzarsi a vicenda.
- **Feature fisse:** le feature vanno considerate come costanti e non soggette a errori di misurazione
- **Assenza di multicollinearità:** le feature non devono essere fortemente correllate tra loro.

Molti di questi vincoli risultano non rispettati nella realtà. L'omoschedasticità, per esempio è una condizione che spesso risulta non applicabita. Per esempio, nel mondo del real estate, il prezzo delle case di grandi dimensioni risulta molto variabile, rendendo difficile predirre i prezzi.

# Capacità predittive
I vincoli sui dati mostrano un forte limite. Le previsioni si basano sulla linearità, semplice da spiegare ma con forti limitazioni predittive. 
Spesso risulta un a forzatura e una semplificazione elevata.

# Metriche per la confidenza

## Metriche Pure
Insieme di metriche calcolabili
  ### $R^2$
  Quanto il modello spiega la varianza totale (0→modello non spiega i dati, 1→modello spiega i dati)
  ```math
    \displaystyle R^2=1-\frac{SSE}{SST}
  ```
    Dove:
  ```math
    \displaystyle SSE=\sum_{i=1}^n(y^{(i)}-(\beta_{0}+\sum_{j=1}^p \beta_{j}x_{j}))^2=\sum_{i=1}^n(y^{(i)}-\hat{y}^{(i)})^2
  ```
  Varianza rimanente dopo il modello
  ```math
    \displaystyle SST=\sum_{i=1}^n(y^{(i)}-\bar{y}^{(i)})^2
  ```
  Varianza totale 

  ### $\bar{R}^2$
  Variazione di $R^2$ che tiene conto del numero delle feature coinvolte. La versione standard cresce al crescere del numero delle feature, anche se inutili.
  ```math
    \displaystyle \bar{R}^2= R^2- (1-\frac{p}{n-p-1})
  ```
  Dove $p$ è il numero delle feature e $n$ è il numero delle istanze

  ### Feature importance (t-statistic)
  Peso scalato con l'errore standard.
 ```math
    \displaystyle t_{\hat{\beta}_{j}}=\frac{\hat{\beta}_{j}}{SE(\hat{\beta}_{j})}
  ```
  Cresce al crescere del peso, diminuisce all'aumentare della varianza.

  ### Mallows' Cp
  Criterio di scelta di modelli che confronta il numero di feature con la varianza spiegata. Un modello ideale ha $Cp=p+1$.
  ```math
    \displaystyle Cp=\frac{SSE}{\hat{\sigma}^2}-n+2p
  ```
  Dove $\hat{\sigma}^2$ è la stima della varianza dei residui del modello completo.

 ## Analisi dei Plot
 Insieme di tipologie di plot e loro interpretazioni
 
 ### Actual VS Predicted
 Utile per vedere se la retta rappresenta bene i dati reali

 ### Istogramma di distribuzione dei residui
 Come già detto, la distribuzine dei residui dovrebbe essere descritta da una distribuzione normale.

 ### Q-Q Plot
 Rappresentazione della distribuzione ideale vs quella effettiva degli errori. Qualsiasi variazione dalla retta di predizione indica una anormalità nella distribuzione dei dati

 ### Residual VS Fitted Values Plot
 Utilizzato per riconoscerere eteroschedasticità e/o non linearità. I grafici, x-fitted y-residual, non dovrebbero mostrare pattern.

# Metriche per la comprensione e spiegabilità dei risultati
 ### Feature Effect
 Rappresentazione dell'*effect*, contentente i valori nei quartili tra il 25%  e il 75% calcolato come:
  ```math
    \displaystyle effect_{j}^{(i)}=w_{j}x_{j}^{(i)}
  ```
  Maggiore l'importanza di una specifica feature, maggiore l'estensione dei box nel grafico. 
# Limiti di predizione

# Limiti di spiegabilità
- Se vi è non-linearità il modello diventa meno veritiero.
- Negli altri casi però, la linearità permette di identificare in modo semplice le relazioni e i pesi delle diverse feature.
- La selettività può essere raggiunta applicando scegliendo a priori un numero minore di metriche oppure sfruttando modelli *sparse*, come il Lasso, che limitano il numero di feature a quelle più rilevanti.

# Confronto con altri algoritmi e versioni alternative

## Selezione manuale
Un alternativa alla selezione automatica è l'affidamento a figure competenti nel campo di applicazione dell'algoritmo per facilitare a priori la scelta delle feature.

## Lasso
Variante non troppo dissimile dall'originale ma che permette di limitare il numero di feature a quelle più rilevanti con l'introduzione nella funzione di ottimizzazione del termine $\lambda||\beta||_{1}$.
Così facendo, aumentando il valore di $\lambda$ si spinge a diminuire forzatamente i pesi delle feature, riducendone man mano il numero.

## Coefficiente di correlazione univariato
Selezione automatica delle feature che superano una certa soglia del coefficiente di correlazione. Un esempio di questi coefficienti è il coeficiente di Pearson's tra le singole feature e i target, calcolato come:
  ```math
    \displaystyle r_{X,Y}=\frac{COV(X,Y)}{\sigma X \sigma Y}
  ```

## Metodi a step
- **Forward selection:** Aggiunta passo passo di feature selezionando man mano il modello con metrica di controllo, $R^2$ per esempio, migliore.
- **Backward selection:** Approccio simile può essere applicato partendo da un modello con tutte le feature e andando a sottrarre man mano un feature.

# Prompt
