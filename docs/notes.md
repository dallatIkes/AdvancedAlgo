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
- **optencorepossible :** faut-il poursuivre les appels récursifs dans cette branche ?
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

