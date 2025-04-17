class Cli():
    def __init__(self, points, taken, scale_x=7, height=30):
        """
        Affiche un graphe ASCII en console représentant une suite de points et
        une ligne brisée reliant certains de ces points.

        Arguments:
        points : liste d'entiers représentant les valeurs (ordonnées) des points.
        taken  : liste de 0 et 1 définissant quels points (entre le 1er et le dernier)
                seront retenus pour tracer les segments.
        scale_x : entier représentant le nombre de colonnes allouées par point sur l'axe X.
        height  : entier représentant le nombre total de lignes pour l'affichage (axe Y).
        """
        if len(points) < 2:
            print("Il faut au moins deux points pour tracer une ligne brisée.")
            return
        if len(taken) != len(points) - 2:
            print("La longueur de 'taken' doit être égale à len(points) - 2.")
            return

        poly_indices = [0] + [i + 1 for i, val in enumerate(taken) if val == 1] + [len(points) - 1]

        max_y = max(points)
        min_y = min(points)
        y_range = max_y - min_y if max_y != min_y else 1  # éviter division par zéro
        scale_y = int(height / y_range)

        width = (len(points) - 1) * scale_x + 1
        grid = [[' ' for _ in range(width)] for _ in range(height)]

        def y_to_row(y):
            return int(round((max_y - y) * scale_y))

        for i, y in enumerate(points):
            x = i * scale_x
            row = y_to_row(y)
            if 0 <= row < height:
                grid[row][x] = 'X'

        for idx in range(len(poly_indices) - 1):
            start = poly_indices[idx]
            end = poly_indices[idx + 1]
            x1, y1 = start * scale_x, points[start]
            x2, y2 = end * scale_x, points[end]

            dx = x2 - x1
            if dx == 0:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    row = y_to_row(y)
                    if 0 <= row < height:
                        grid[row][x1] = '*'
            else:
                for x in range(x1, x2 + 1):
                    t = (x - x1) / dx
                    y = y1 + t * (y2 - y1)
                    row = y_to_row(y)
                    if 0 <= row < height and 0 <= x < width and grid[row][x] == ' ':
                        grid[row][x] = '*'

        for line in grid:
            print('|' + ''.join(line))
        print('|' + '_' * width)
