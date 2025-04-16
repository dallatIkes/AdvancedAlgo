# Exemple de données
points = [3, 6, 4, 7, 2, 8, 5, 9, 4, 7, 3, 8, 6, 5, 2]
taken  = [1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1]


# Échelle (nombre de colonnes par point)
scale = 5

# Construction de la liste des indices retenus dans la ligne brisée
poly_indices = [0]
for i, val in enumerate(taken):
    if val == 1:
        poly_indices.append(i + 1)
poly_indices.append(len(points) - 1)

# Calcul des dimensions de la grille:
# - La largeur est égale à (nombre de points - 1) * scale + 1
# - La hauteur est déterminée par l'étendue des valeurs de 'points'
max_y = max(points)
min_y = min(points)
height = max_y - min_y + 1
width = (len(points) - 1) * scale + 1

# Création de la grille vide (remplie d'espaces)
grid = [[' ' for _ in range(width)] for _ in range(height)]

# Fonction pour convertir une coordonnée y "réelle" en indice de ligne
def y_to_row(y):
    return max_y - y

# Placer les points sur la grille (chaque point est placé à x = i*scale)
for i, y in enumerate(points):
    x = i * scale
    row = y_to_row(y)
    grid[row][x] = 'X'

# Tracer les segments (les segments passent par les points de poly_indices)
# Pour chaque segment entre (x1, y1) et (x2, y2), on parcourt l'axe x entre x1_scaled et x2_scaled
for idx in range(len(poly_indices) - 1):
    start = poly_indices[idx]
    end   = poly_indices[idx + 1]
    x1, y1 = start * scale, points[start]
    x2, y2 = end * scale, points[end]

    if x2 - x1 == 0:
        # Cas particulier : segment vertical
        for y in range(min(y1, y2), max(y1, y2) + 1):
            row = y_to_row(y)
            if grid[row][x1] == ' ':
                grid[row][x1] = '*'
    else:
        # Parcourir toutes les colonnes entre x1 et x2
        for x in range(x1, x2 + 1):
            # Calcule du rapport t le long du segment
            t = (x - x1) / (x2 - x1)
            # Interpoler la coordonnée y correspondante
            y = y1 + t * (y2 - y1)
            y_round = round(y)
            row = y_to_row(y_round)
            # Tracer le segment s'il n'écrase pas un point déjà marqué par "X"
            if grid[row][x] == ' ':
                grid[row][x] = '*'

# Affichage du graphe : chaque ligne est précédée d'une barre verticale pour représenter l'axe des ordonnées
for line in grid:
    print('|' + ''.join(line))
# Afficher l'axe horizontal en bas
print('|' + '_' * width)
