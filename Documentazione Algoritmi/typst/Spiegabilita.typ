= Spiegabilità nei Modelli di Machine Learning
<spiegabilità-nei-modelli-di-machine-learning>
== Considerazioni Generali
<considerazioni-generali>
La spiegabilità (o interpretabilità) di un modello di ML è la capacità
di comunicare #strong[come e perché] il modello ha fatto una previsione,
in modo comprensibile a un essere umano non esperto di ML.

Contrariamente all\'intuizione, la spiegabilità #strong[non è un
attributo binario], ma uno spettro con molteplici dimensioni:

=== Dimensioni della Spiegabilità
<dimensioni-della-spiegabilità>
+ #strong[Trasparenza Intrinseca (Model-Level Interpretability)]

  - Il modello stesso è trasparente e interpretabile da design
  - Es.: coefficienti di regressione lineare, nodi di un albero
    decisionale
  - #strong[Proprietà:] la struttura del modello comunica direttamente
    come funziona

+ #strong[Tracciabilità Locale (Instance-Level Explainability)]

  - Per una singola previsione, è possibile tracciare #strong[come] il
    modello ha raggiunto quella conclusione
  - Es.: il cammino dalla radice alla foglia in un albero, i features
    attivati in una rete neurale
  - #strong[Proprietà:] ogni previsione è completamente rintracciabile

+ #strong[Interpretabilità dei Parametri]

  - I parametri del modello hanno un significato tangibile e
    interpretabile
  - Es.: il coefficiente $beta_j$ in LR significa \"aumentare $x_j$ di 1
    causa aumento di $y$ di $beta_j$\"
  - #strong[Proprietà:] la relazione tra parametri e comportamento è
    evidente

+ #strong[Fedeltà alla Logica Umana]

  - Le spiegazioni riflettono il ragionamento che un umano avrebbe fatto
  - Es.: \"il cliente ha defaultato perché: reddito basso (decisione
    umana plausibile) + punteggio di credito basso\"
  - #strong[Proprietà:] le spiegazioni suonano coerenti dal punto di
    vista del dominio



== Framework di Lipton (2016)
<framework-di-lipton-2016>
Il lavoro fondamentale \"The Mythos of Model Interpretability\" di
#strong[Ribeiro et al. (2016)] identifica due categorie orthogonali di
spiegabilità:

=== 1. Transparency (Trasparenza del Modello)
<1-transparency-trasparenza-del-modello>
Quanto trasparente è il #strong[modello stesso], indipendentemente dalle
predizioni:

- #strong[High:] Linear Regression, Logistic Regression, Decision Trees
  (piccoli)
- #strong[Medium:] Generalized Additive Models, Ensemble Methods (Random
  Forests)
- #strong[Low:] Neural Networks, SVM, Gradient Boosting complesso

=== 2. Post-hoc Explainability (Spiegabilità Post-Hoc)
<2-post-hoc-explainability-spiegabilità-post-hoc>
Tecniche applicate #strong[dopo il training] per spiegare previsioni di
modelli opachi:

- #strong[LIME (Local Interpretable Model-agnostic Explanations):]
  approssima il modello localmente con un modello lineare semplice
- #strong[SHAP (SHapley Additive exPlanations):] assegna ogni output tra
  le feature usando valori Shapley dalla teoria dei giochi
- #strong[Feature Importance:] quale feature ha più influenzato la
  previsione

=== Interazione tra le due:
<interazione-tra-le-due>
- Un modello #strong[altamente trasparente] non ha bisogno di post-hoc
  (spiegazione è diretta)
- Un modello #strong[opaco] usa post-hoc per compensare
- Ideale: trasparenza intrinseca + capacità predittiva



== Fattori che Facilitano la Comprensione
<fattori-che-facilitano-la-comprensione>
Sulla base di ricerca in interpretabilità (Lipton, Molnar, etc.), ci
sono #strong[molteplici aspetti] che facilitano la comprensione di una
spiegazione:

=== 1. Semplicità e Brevità
<1-semplicità-e-brevità>
- Spiegazioni corte sono preferite a quelle lunghe
- Un numero limitato di cause spieganti (es. 3-5 feature) è più
  memorizzabile di 10-20
- #strong[Trade-off:] brevità vs completezza; spesso un compromesso è
  necessario

=== 2. Confronto tra Istanze (Contrastive Explanations)
<2-confronto-tra-istanze-contrastive-explanations>
- \"Perché è stata predetta come positiva #emph[questa] istanza rispetto
  a #emph[quella]?\"
- Spiegazione contrastiva è spesso più illuminante che assoluta
- Es.: \"il cliente A ha defaultato ma il cliente B no; la differenza
  principale è il reddito\" è più utile che \"il cliente A ha reddito
  basso\"
- #strong[Applicazione:] usare nearest neighbors di classe diversa per
  confronto

=== 3. Selezione di Cause Determinanti
<3-selezione-di-cause-determinanti>
- Non tutte le feature sono uguali; alcune causano la predizione, altre
  sono correlate ma non causali
- Una spiegazione dovrebbe identificare i #strong[fattori determinanti],
  non tutti i fattori

=== 4. Adattamento al Contesto e all\'Audience
<4-adattamento-al-contesto-e-allaudience>
- La spiegazione deve essere #strong[appropriata al livello di
  expertise] dell\'audience
- Spiegazione a un medico non è la stessa di quella a un paziente
- Spiegazione a un regolatore non è la stessa di quella a un cliente
- #strong[Proprietà:] la qualità di una spiegazione è relativa al
  contesto

=== 5. Gestione di Feature Anomali o Outlier
<5-gestione-di-feature-anomali-o-outlier>
- Se una feature ha un valore inusuale, dovrebbe essere segnalato
- Es.: \"il cliente ha un\'età di 250 anni (anomalia nei dati), quindi
  la predizione è inaffidabile\"
- #strong[Proprietà:] la spiegazione dovrebbe indicare quando il modello
  è #strong[al di fuori del dominio] di applicazione

=== 6. Feature Support (Copertura Applicativa)
<6-feature-support-copertura-applicativa>
La #strong[generalità] di una previsione può essere quantificata dal
#strong[feature support]:

$ upright("Feature Support")_i = frac(upright("#istanze nel training con valori simili a ") x_i, upright("#istanze totali nel training")) $

Es.: se stiamo predendo per un cliente di 35 anni, e il 70% del training
set era tra 30-40 anni, il support è alto (predizione affidabile). Se
era il 5%, il support è basso (predizione in zona extrapolazione).

#strong[Implicazione:] una spiegazione dovrebbe menzionare il support:
\"questa predizione è affidabile (support = 0.7)\" vs \"questa
predizione è incerta (support = 0.1)\"

=== 7. Causalità vs Correlazione
<7-causalità-vs-correlazione>
- Una feature può essere #strong[correlata] alla predizione ma non
  #strong[causale]
- Es.: \"il modello predice default perché il cliente è ricco\" potrebbe
  essere spurio se la ricchezza è correlata al credito score, che è il
  vero driver
- #strong[Proprietà:] la spiegazione ideale identifica la
  #strong[relazione causale], non solo quella correlativa
- #strong[Limite:] senza esperimento (es. A/B test), è difficile provare
  causalità dai dati osservazionali



== Applicabilità vs Generalità
<applicabilità-vs-generalità>
=== Non è il Parametro Più Importante
<non-è-il-parametro-più-importante>
Una spiegazione che è #strong[applicabile a molti casi] (alta copertura)
non è necessariamente la #strong[migliore] spiegazione:

- Una spiegazione generale (\"tutti i clienti giovani sono rischiosi\")
  ha alta applicabilità ma è imprecisa
- Una spiegazione specifica (\"questo cliente è rischioso a causa della
  combinazione unica di reddito basso + punteggio di credito basso +
  storia lavorativa instabile\") ha bassa applicabilità ma è molto più
  informativa

#strong[Principio:] la qualità di una spiegazione non si misura dalla
sua generalità, ma dalla sua #strong[utilità nel contesto specifico].



== Applicazione ai Tre Algoritmi: Matrice Comparativa
<applicazione-ai-tre-algoritmi-matrice-comparativa>
=== Linear Regression (LR)
<linear-regression-lr>
#figure(
  align(center)[#table(
    columns: 3,
    align: (auto,auto,auto,),
    table.header([Dimensione], [Valutazione], [Note],),
    table.hline(),
    [#strong[Transparency]], [⭐⭐⭐⭐⭐ Alta], [Coefficienti diretti e
    interpreti],
    [#strong[Tracciabilità Locale]], [⭐⭐⭐⭐⭐ Alta], [Calcolo
    lineare, completamente tracciabile],
    [#strong[Interpretabilità Parametri]], [⭐⭐⭐⭐⭐ Alta], [$beta_j$
    \= variazione attesa di y per aumento di 1 di $x_j$],
    [#strong[Fedeltà alla Logica Umana]], [⭐⭐⭐ Media], [Relazioni
    lineari non sempre riflettono ragionamento umano non lineare],
    [#strong[Feature Support]], [⭐⭐⭐⭐ Alta], [Facile da calcolare:
    distanza euclidea dai training],
    [#strong[Causalità]], [⭐⭐ Bassa], [Coefficienti sono
    correlazionali, non causali],
    [#strong[Necessità Post-Hoc]], [No], [Il modello è sufficientemente
    trasparente],
  )]
  , kind: table
  )

=== Logistic Regression (LogR)
<logistic-regression-logr>
#figure(
  align(center)[#table(
    columns: 3,
    align: (auto,auto,auto,),
    table.header([Dimensione], [Valutazione], [Note],),
    table.hline(),
    [#strong[Transparency]], [⭐⭐⭐⭐ Alta], [Coefficienti interpreti,
    ma con trasformazione moltiplicativa],
    [#strong[Tracciabilità Locale]], [⭐⭐⭐⭐ Alta], [Calcolo lineare +
    sigmoid, completamente tracciabile],
    [#strong[Interpretabilità Parametri]], [⭐⭐⭐
    Media], [$exp \( beta_j \)$ = fattore moltiplicativo di odds, meno
    intuitivo di LR],
    [#strong[Fedeltà alla Logica Umana]], [⭐⭐⭐ Media], [Probabilità è
    intuitiva, ma dipendenza dal contesto (sigmoid non lineare)],
    [#strong[Feature Support]], [⭐⭐⭐⭐ Alta], [Facile da calcolare],
    [#strong[Causalità]], [⭐⭐ Bassa], [Coefficienti sono
    correlazionali],
    [#strong[Necessità Post-Hoc]], [No], [Sufficiente trasparenza, anche
    se meno immediata di LR],
  )]
  , kind: table
  )

=== Decision Tree (DT)
<decision-tree-dt>
#figure(
  align(center)[#table(
    columns: 3,
    align: (auto,auto,auto,),
    table.header([Dimensione], [Valutazione], [Note],),
    table.hline(),
    [#strong[Transparency]], [⭐⭐⭐ Media (dipen da
    profondità)], [Trasparente per alberi piccoli, complesso per alberi
    grandi],
    [#strong[Tracciabilità Locale]], [⭐⭐⭐⭐⭐ Altissima], [Cammino
    radice-foglia è completamente trasparente],
    [#strong[Interpretabilità Parametri]], [⭐⭐⭐⭐ Alta], [Split
    (feature \<= threshold) sono diretti e interpreti],
    [#strong[Fedeltà alla Logica Umana]], [⭐⭐⭐⭐ Alta], [Decisioni
    sequenziali rispecchiano ragionamento umano],
    [#strong[Feature Support]], [⭐⭐⭐ Media], [Dipende dalla densità
    dei dati nelle regioni decisionali],
    [#strong[Causalità]], [⭐⭐⭐ Media], [Split non implicano causalità
    diretta, ma la struttura sequenziale suggerisce dipendenza],
    [#strong[Necessità Post-Hoc]], [Condizionato], [Piccoli alberi no;
    grandi alberi sì (es. SHAP per pesare feature)],
  )]
  , kind: table
  )



== Strategie Specifiche di Spiegabilità per Algoritmo
<strategie-specifiche-di-spiegabilità-per-algoritmo>
=== Linear Regression: Spiegabilità Diretta
<linear-regression-spiegabilità-diretta>
#strong[Metodo principale:] Visualizzazione dei Coefficienti + Feature
Effect Plot

```
Spiegazione di y per istanza i:
y_hat = β₀ + β₁·x₁ + β₂·x₂ + ... + βₚ·xₚ
      = 2.5 + 0.3·(Income) + (-0.15)·(Age) + ...
      = 2.5 + 0.3·50000 + (-0.15)·35 + ...
      = 2.5 + 15000 - 5.25 + ...
      = 17000
```

Componenti della spiegazione:

- #strong[Ordine di importanza:] mostrare quale feature contribuisce di
  più (in valore assoluto)
- #strong[Segno (direzione):] positivo (aumenta predizione) vs negativo
  (diminuisce)
- #strong[Magnitudo (effect size):] $beta_j times x_j$ è l\'impatto
  assoluto

=== Logistic Regression: Spiegabilità Probabilistica
<logistic-regression-spiegabilità-probabilistica>
#strong[Metodo principale:] Odds Ratio Interpretation + Probability
Threshold

```
Spiegazione di P(y=1) per istanza i:
log(odds) = β₀ + β₁·x₁ + β₂·x₂ + ...
          = 1.2 + 0.5·(CreditScore/100) + (-0.3)·(Age/10) + ...

Odds = exp(log(odds)) = ...
P(y=1) = Odds / (1 + Odds) = 0.72
```

Componenti della spiegazione:

- #strong[Probabilità predetta:] \"il modello stima una probabilità del
  72%\"
- #strong[Odds Ratio:] \"aumentare il credit score di 100 punti
  moltiplica gli odds per exp(0.5) = 1.65 (aumento del 65%)\"
- #strong[Confidenza:] basata sulla probabilità stessa (più vicina a
  0.5, meno sicura; più vicina a 0 o 1, più sicura)

=== Decision Tree: Spiegabilità Strutturale
<decision-tree-spiegabilità-strutturale>
#strong[Metodo principale:] Tracciamento del Cammino + Feature
Importance

```
Spiegazione di previsione per istanza i:
1. Income <= 50000? SÌ → vai a Nodo 2
2. CreditScore <= 650? SÌ → vai a Nodo 4
3. Age <= 30? NO → vai a Nodo 8
4. Foglia: Predizione = "Default" (95% confidenza, 100 campioni)

Feature Importance:
  - Income: 0.35
  - CreditScore: 0.40
  - Age: 0.15
  - ... (altri: < 0.05)
```

Componenti della spiegazione:

- #strong[Cammino decisionale:] sequenza di regole che portano alla
  foglia
- #strong[Confidenza della foglia:] frazione di campioni della classe
  predetta nella foglia
- #strong[Feature importance globale:] quanto importante è ogni feature
  nell\'intero albero



== Gestione della Multicollinearità e Feature Correlate
<gestione-della-multicollinearità-e-feature-correlate>
Un aspetto raramente discusso ma importante: #strong[come spiegare
quando le feature sono correlate?]

=== Problema
<problema>
Se Income e Education sono correlate (persone più istruite hanno redditi
più alti):

- #strong[LR:] un modello potrebbe usare Income, l\'altro Education,
  entrambi con coefficienti grandi (instabili)
- #strong[DT:] potrebbe preferire Income al primo split, ignorando
  Education
- #strong[Spiegazione naïve:] \"il reddito è il fattore determinante\"
  --- potrebbe mascherare che è in realtà l\'istruzione

=== Soluzione
<soluzione>
- #strong[Documentare le correlazioni:] \"Income è correlato con
  Education (r = 0.7); le spiegazioni basate su Income potrebbero essere
  sostituite da Education\"
- #strong[Feature selection a priori:] scegliere una variabile del
  gruppo correlato
- #strong[Metodi sparse:] Lasso/Ridge, che azzerano automaticamente
  feature ridondanti



== Considerazioni Etiche e Normative
<considerazioni-etiche-e-normative>
Oltre alla comprensione tecnica, la spiegabilità ha implicazioni
#strong[etiche e legali]:

=== GDPR Right to Explanation
<gdpr-right-to-explanation>
Le normative come GDPR (EU) e CCPA (USA) richiedono spiegabilità per
#strong[decisioni automatizzate] che colpiscono diritti di individui:

- Un rifiuto di un prestito deve essere spiegabile al cliente
- La spiegazione deve essere in linguaggio umano, non jargon tecnico
- Implica una necessità di #strong[trasparenza intrinseca], non solo
  post-hoc

=== Fairness e Bias
<fairness-e-bias>
La spiegabilità aiuta anche a identificare #strong[bias ingiusti]:

- Es.: se il modello usa Age per denegare un prestito, e Age è proxy per
  Genere (illegale in molti contesti), la spiegabilità lo rivela
- #strong[Strumento:] spiegazioni contrastive mostrano se il modello
  discrimina



== Raccomandazioni per la Tesi
<raccomandazioni-per-la-tesi>
Sulla base di quanto discusso, suggerimenti per integrare queste
considerazioni:

+ #strong[Matrice comparativa:] includi la tabella sopra nei tuoi
  algoritmi (consente visione d\'insieme)

+ #strong[Per ogni algoritmo:] aggiungi una sezione \"Spiegabilità
  Tipica\" che descriva:

  - Come è naturalmente spiegabile
  - Quale metodo post-hoc usare se necessario
  - Limitazioni note

+ #strong[Caso di studio:] considera un dataset di esempio (es. credit
  scoring) e mostra come ogni algoritmo spiega la stessa previsione

+ #strong[Trade-off Interpretabilità-Accuratezza:] eplicita il fatto che
  algoritmi più interpretabili (LR, DT small) spesso hanno accuratezza
  minore, e viceversa

+ #strong[Contesto applicativo:] definisci che una spiegazione è
  \"buona\" sempre #strong[relative to context and audience] --- non
  esiste una spiegazione universalmente ottimale



== Prompt
<prompt>
