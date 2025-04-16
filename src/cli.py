def displayCLI(points, taken, scale):
    """
    Affiche un graphe ASCII en console représentant une suite de points et
    une ligne brisée reliant certains de ces points.

    Arguments:
      points : liste d'entiers représentant les valeurs (ordonnées) des points.
      taken  : liste de 0 et 1 définissant quels points (entre le 1er et le dernier)
               seront retenus pour tracer les segments.
               sa longueur doit être égale à len(points) - 2.
      scale  : entier représentant le nombre de colonnes allouées par point sur l'axe X.
    """
    # Vérifier que les listes ont une taille cohérente
    if len(points) < 2:
        print("Il faut au moins deux points pour tracer une ligne brisée.")
        return
    if len(taken) != len(points) - 2:
        print("La longueur de 'taken' doit être égale à len(points) - 2.")
        return

    # Détermination des indices des points à relier : toujours le premier et le dernier,
    # et ceux indiqués par un 1 dans taken.
    poly_indices = [0]
    for i, val in enumerate(taken):
        if val == 1:
            poly_indices.append(i + 1)
    poly_indices.append(len(points) - 1)

    # Détermination de la taille de la grille.
    max_y = max(points)
    min_y = min(points)
    height = max_y - min_y + 1
    width = (len(points) - 1) * scale + 1

    # Création de la grille remplie d'espaces
    grid = [[' ' for _ in range(width)] for _ in range(height)]

    # Fonction pour convertir une coordonnée y en indice de ligne (affichage de haut en bas)
    def y_to_row(y):
        return max_y - y

    # Placement des points dans la grille
    for i, y in enumerate(points):
        x = i * scale
        row = y_to_row(y)
        grid[row][x] = 'X'

    # Tracé des segments entre les points de poly_indices
    for idx in range(len(poly_indices) - 1):
        start = poly_indices[idx]
        end   = poly_indices[idx + 1]
        x1, y1 = start * scale, points[start]
        x2, y2 = end * scale, points[end]

        if x2 - x1 == 0:
            # Traitement du cas vertical (rare)
            for y in range(min(y1, y2), max(y1, y2) + 1):
                row = y_to_row(y)
                if grid[row][x1] == ' ':
                    grid[row][x1] = '*'
        else:
            # Tracé du segment par interpolation linéaire sur l'axe x
            for x in range(x1, x2 + 1):
                t = (x - x1) / (x2 - x1)
                y = y1 + t * (y2 - y1)
                y_round = round(y)
                row = y_to_row(y_round)
                if grid[row][x] == ' ':
                    grid[row][x] = '*'

    # Affichage de la grille
    for line in grid:
        print('|' + ''.join(line))
    print('|' + '_' * width)


# Exemple d'utilisation :

points_example = [2, 4, 2, 6, 9, 5, 3, 7, 8, 1]
taken_example  = [1, 0, 0, 1, 0, 1, 1, 0]  # len(taken) == len(points) - 2
scale_example  = 3

displayCLI(points_example, taken_example, scale_example)
