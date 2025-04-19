# Notes du compte-rendu du projet

**Question préliminaire :** $2^{n-2}$ lignes brisées avec un ensemble $S$ de $n$ points, car le nombre d'ensembles d' ensembles possibles avec $n$ points en prenant forcemment le premier et le dernier est le nombre d'ensembles d'ensembles de $n-2$ points.

## Essais successifs

### Question 1

- **$i$ :** abscice du point à prendre - 1 (parce que on décale tous les points vers la gauche si on ne prend pas le premier (on ne prend pas le dernier non plus mais ça n'a pas d'incidence)) :)
- **$X$ :** Liste de $n-2$ booléens (on utilisera 0 et 1 psk c'est plus court)
    ```python
    result = [False, True, False, ..., True]
    ```
- **$S_i$ :** $\{0,1\}$
- **satisfaisant :** 
    ```python
    def satisfaisant(xi):
        return True
    ```
    parce que notre modélisation ne prend que les $n-2$ points du milieu donc toutes les configurations possibles sont acceptantes).
- **enregistrer :** 
    ```python
    def enregistrer(xi):
        '''
        xi : boolean - is the i-th point taken ?
        '''
        result[i] = xi 
    ```
- **soltrouvée :** a-t-on une solution complète ?
    ```python
    if i == n-2:
        soltrouvee = True
    ```
- **optimal :** le coût $= (SD+mC)$ est minimale
- **optencorepossible :** faut-il poursuivre les appels récurssifs dans cette branche ?
    ```python
    if (SD+d(i-1, i)+d(i, i+1)-d(i-1, i+1)+(m+1)C) >= currentOpt:
        optEncorePossible = False
    ```
- **défaire :** remettre les variables d'état du problème comme elles étaient avant de choisir $x_i$
    ```python
    def defaire(xi):
        '''
        xi : int - index of the i-th point
        '''
        result[xi] = False
    ```

### Question 2

Complexité exponentielle (au pire cas : $O(2^n)$)

### Question 3
```python
    if (SD+d(i-1, i)+d(i, i+1)-d(i-1, i+1)+(m+1)C) >= currentOpt:
        optEncorePossible = False
```

### Question 4

Il est plus intéressant de commencer avec une valeur optimale temporaire et choisir arbitrairement la moitié des points semble intuitivement être une bonne idée. 

## Programmation dynamique
### Question 1
Cas de base : $\forall i \in \{1, ..., n\}, approx-opt(i, i) = 0$  
Cas général : $approx-opt(i, n) = \min\limits_{j = i+1}^{n} (SD_{i, j} + C + approx-opt(j, n))$ avec m relié à 1.

### Question 2
#### Structure tabulaire
On va dans un premier temps ranger les distances $SD_{i,j}$ dans un tableau à 2 dimensions tel que ```SD[i, j]``` = $SD_{i,j}$. Ainsi, l'accès aux distances au cours du traitement pourra s'effectuer en temps constant sans avoir à constamment recalculer toutes les distances.

On va également utiliser une liste ```approx-opt``` à 1 dimension tel que :  
```approx-opt[i]``` = $approx-opt(i, n)$.

Afin de reconsituter le chemin optimal, on utilise une liste auxiliaire ```next``` tel que ```next[i]``` contient l'indice du point inférieur à i relié à i (initialisé à ```(n - 1) * [None]```)
#### Stratégie de remplissage
On remplit notre tableau ```approx-opt``` de manière descendante :
```
pour i allant de n-1 à 1 faire:
    approx-opt[i] <- +∞
    pour j = i+1 à n faire:
        cost <- SD(i, j) + C + approx-opt[j]
        si cost < approx-opt[i] alors:
            approx-opt[i] <- cost
            next[i] <- j
```

