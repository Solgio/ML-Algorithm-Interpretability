# Modello
La regressione logistica è un modello utilizzato per problemi di classificazione, tipicamente per variabili di risposta binarie (es. "Sì" o "No", "Malato" o "Sano").
Per mantenere l'output tra 0 e 1, il modello inserisce una combinazione lineare di feature all'interno di una funzione logistica
```math
\displaystyle logistic(n)= \frac{1}{1+exp(-n)}
```
Che quindi si presenta così, nel caso $y^{(i)}=1$:

```math
\displaystyle P(y^{(i)}=1)= \frac{1}{1+exp(-(\beta_{0}+ \sum{\beta_{j}x_{j}^{(i)}}))}
```

Mentre in generale la probabilità può essere descritta come una funzione a tratti:
```math
\displaystyle P(y_{(i)},x_{(i)})= 
  
\begin{cases}
\frac{exp(-(\beta_{0}+ \sum{\beta_{j}x_{j}^{(i)}}))}{1+exp(-(\beta_{0}+ \sum{\beta_{j}x_{j}^{(i)}}))} & \text{Se } y_{(i)}=0 \\
\frac{1}{1+exp(-(\beta_{0}+ \sum{\beta_{j}x_{j}^{(i)}}))} & \text{Se } y_{(i)}=1 \\
0 & \text{Altrimenti}
\end{cases}
```

Il calcolo dei pesi $\beta$ è basato sulla funzione detta di *likelihood*, non sull'errore quadratico:

```math
\displaystyle L(\beta, Y, X )= \prod_{y_j =1} p(x_j)\prod_{y_i =0} p(1-x_i)
```
masimizzando questa funzione.

# Vincoli sui dati
La trasformazione della funzione logistica porta a una diversa interpretazione dei pesi.
```math
\displaystyle odds=\frac{P(y=1)}{P(y=0)}= exp(\beta_0+\sum_{i \in P} \beta_i x_i)
```
Aumentando di 1 una delle feature (j) è possibile variare come cambia il peso:
```math
 \displaystyle \frac {odds_{x_j +1}}{odds}= \frac {exp(\beta_0+\beta_1 x_1+\text{...}+\beta_j (x_j +1)+\text{...}+\beta_p x_p)}
{exp(\beta_0+ \sum_{i \in P} \beta_i x_i)
}
```
```math
=exp(\beta_j (x_j +1)-\beta_j (x_j))= exp(\beta_j)
```
L'incremento non è lineare ma moltiplicativo, pari a $exp(\beta_j)$.

- **Linearità del log degli odds:** $exp(\beta_0+\sum_{i \in P} \beta_i x_i) → log(odds)=\beta_0+\sum_{i \in P} \beta_i x_i$
- **Linearità dei vincoli:** l'assunzione di relazioni lineari rimane alla base del modello, come nella LR.
- **Separazione completa:** nel caso vi sia una feature che separa completamente i dati il modello non è in grado di identificarla in quanto il peso ideale per tale feature sarebbe $+\infty$.
- **Distribuzione binomiale:** la distribuzione della regressione logistica deve seguire quella binomiale
- **Indipendenza delle misure:** le misurazioni non devono influenzarsi a vicenda.
- **Feature fisse:** le feature vanno considerate come costanti e non soggette a errori di misurazione
- **Assenza di multicollinearità:** le feature non devono essere fortemente correllate tra loro.

L'omoschedasticità non è invece una condizione necessaria dal momento che i valori possono assumere unicamente valore 0 o 1.

# Capacità predittive
Limiti legati alla scelta di modellazione lineare. La logistic regression è soggetta agli stessi vincoli di LR: pattern non lineari e complessi non vengono identificati dal modello.
Vantaggio è però la formulazione che permette l'espressione della percentuale di appartenenza ad una categoria rispetto ad un'altra.

# Metriche per la confidenza
## Metriche Pure
### Confusion Matrix (Matrice di Confusione):
 Valuta le prestazioni confrontando le classi reali con quelle previste, estraendo metriche:
 - **Accuracy:** $ACC=\frac{TP+TN}{P+N}$(frazione di previsioni corrette), 
 - **Sensibilità** $Sens=\frac{TP}{TP+FN}$ (tasso di veri positivi),
 - **Specificità** $Spec=\frac{TN}{FP+TN}$ (tasso di veri negativi).
### Precision
$PREC=\frac{TP}{TP+FP}$ è interpretabile come il numero di istanze identificate come positive rispetto a quelle effettivamente positive.

### Recall
$REC=\frac{TP}{TP+FN}=Sens$ è interpretabile il numero di positivi identificati come tali

### F1-score
$F1=2\frac {PREC*REC}{PREC+REC}$

### ROC curves e AUC
Le ROC curves sono rappresentazioni delle metriche di True Positive Rate (TPR=Rec=Sens) e False Positive Rate (FPR=1-Spec). Un grafico di un modello ideale si avvicina all'angolo in alto a sinistra, mentre un modello casuale si avvicina alla diagonale. 
L'AUC (Area Under the Curve) quantifica la capacità del modello di distinguere tra le classi, con valori vicini a 1 che indicano ottime prestazioni, vicine a 0.5 per un modello casuale.

### Z-statistic e p-value
Un ruolo simile a quello della t-statistic nei modelli lineari è svolto dalla z-statistic (il peso del coefficiente diviso per il suo errore standard). Valori assoluti grandi della z-statistic indicano che c'è una forte evidenza per rifiutare l'ipotesi nulla, suggerendo che la feature è statisticamente significativa per variare la probabilità della classe.

# Metriche per la comprensione e spiegabilità dei risultati
## Effect Plot e Weight Plot
Come nella regressione lineare, si possono graficare gli effetti (peso moltiplicato per il valore della feature) per avere una percezione visiva dell'impatto di un predittore rispetto alla sua distribuzione sui dati

# Limiti di predizione
- **Non linearità:** la regressione logistica non è in grado di catturare pattern non lineari nei dati, a meno che non vengano introdotte manualmente interazioni o trasformazioni delle feature.
- **Separazione completa:** se una feature separa completamente le classi, il modello non è in grado di identificare un peso finito per quella feature, portando a problemi di stima.
- **Overfitting:** con un numero elevato di feature rispetto al numero di osservazioni, la regressione logistica può facilmente sovradattarsi ai dati di addestramento, riducendo la capacità di generalizzazione su nuovi dati.

# Limiti di spiegabilità
L'interpretazione probabilistica della regressione logistica è un vantaggio, dando una misura di confidenza della stima della classe.
Tuttavia, la natura moltiplicativa degli effetti può rendere più complessa l'interpretazione rispetto alla regressione lineare, soprattutto quando si considerano interazioni tra feature o quando i pesi sono piccoli, rendendo difficile valutare l'impatto di una singola feature sulla probabilità di appartenenza a una classe.

# Confronto con altri algoritmi e versioni alternative

## Regressione Lineare
 La regressione logistica risolve i difetti logici dell'uso di una retta su dati binari (evitando probabilità negative o stime sopra l'1) ed è specificamente concepita per il class setting.

## Linear Discriminant Analysis (LDA)
 Anche l'LDA crea confini decisionali lineari e, curiosamente, una regressione lineare classica su una risposta 0/1 genera gli stessi risultati di una LDA. Tuttavia, l'LDA fa ipotesi forti sulla normalità multivariata dei predittori. Spesso la regressione logistica e l'LDA producono risultati comparabili, ma la logistica si rivela preferibile se le assunzioni gaussiane vengono violate

## Regressione Logistica Multinomiale
 Estende l'algoritmo classico oltre il caso binario, permettendo la classificazione di eventi con K>2 classi. Si applica usando una categoria come base, oppure un approccio con funzione softmax, stimando la probabilità per ciascuna classe rispetto alle altre.

## Lasso/Ridge per Logistica
 Le penalità (come L1 Lasso) possono essere introdotte nella funzione di loss logistica. Questo è molto utile sia per isolare un numero "sparso" (limitato) di feature determinanti, sia per risolvere elegantemente i casi di "separazione completa" in cui l'algoritmo divergerebbe.
## Generalized Additive Models (GAM)
 Per superare i limiti di linearità del logit, si possono combinare la funzione logistica e il framework dei GAM, associando a ciascun predittore una funzione non-lineare flessibile (es. delle splines) per modellare scenari in cui la probabilità di default non sale linearmente ma con curve complesse, preservando la separazione additiva degli effetti.

# Prompt

Metriche per la confidenza


