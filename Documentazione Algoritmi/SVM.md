# Modello
## Logica dell'algoritmo
Dividere in classi (-1, 1) inserendo un iperpiano:
```math
\displaystyle \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \ldots + \beta_p x_p = 0
```
Tra gli infiniti iperpiani scegliere quello che massimizza il margine, cioè la distanza tra i punti più vicini di ciascuna classe e l'iperpiano stesso.

```math
\displaystyle y_i (\beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \ldots + \beta_p x_{ip}) \geq 1
```

La distanza tra il punto più vicino e l'iperpiano è data da:

```math
\displaystyle r*=\frac{y_i(\beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \ldots + \beta_p x_{ip})}{||\beta||}
```
Che in base alla classe di appartenenza del punto più vicino è uguale a:

```math
r* =
\begin{cases}
\frac{1}{||\beta||} & \text{se } y_i = 1 \\
\frac{-1}{||\beta||} & \text{se } y_i = -1
\end{cases}
```
Il margine è quindi dato da:

```math
\displaystyle M = \frac{2}{||\beta||}
```
La ricerca dell'iperpiano ottimale è quindi equivalente alla minimizzazione di $||\beta||$, ed è formulata come segue:

```math
\displaystyle \min_{\beta} \frac{1}{2} ||\beta||^2
```
soggetto a $y_i (\beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \ldots + \beta_p x_{ip}) \geq 1$ per ogni punto di addestramento.

## Soft Margin SVM
Per gestire dati non linearmente separabili, SVM introduce variabili di slack $\xi_i$ che permettono a certi punti di violare il margine, con una penalizzazione proporzionale alla loro distanza dall'iperpiano. La formulazione diventa:


## Kernel SVM

# Vincoli sui dati
- **Linearità:** SVM è un classificatore lineare, quindi funziona meglio quando i dati sono linearmente separabili. Se i dati non sono linearmente separabili, è necessario utilizzare kernel per trasformare i dati in uno spazio di dimensioni superiori.
- **Bilanciamento delle classi:** SVM può essere influenzato da classi sbilanciate, poiché cerca di massimizzare il margine complessivo. Se una classe è molto più numerosa dell'altra, l'iperpiano potrebbe essere spostato verso la classe minoritaria, riducendo la capacità di classificazione.
- **Scalabilità:** SVM può essere computazionalmente costoso, soprattutto con grandi set di dati, poiché la complessità del training è generalmente quadratica rispetto al numero di campioni.

# Capacità predittive

# Metriche per la confidenza

# Metriche per la comprensione e spiegabilità dei risultati

# Limiti di predizione

# Limiti di spiegabilità

# Confronto con altri algoritmi e versioni alternative

# Prompt
