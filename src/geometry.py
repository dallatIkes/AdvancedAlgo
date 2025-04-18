from math import sqrt

def euclidian_distance(a: list[float], b: list[float]) -> float:
        """Returns the euclidian distance between the points a and b.

        Args:
            a (list[float]): coordinates of the first point. 
            b (list[float]): coordinates of the second point.

        Returns:
            float: euclidian distance between the two points.
        """
        # coordinates of the first point
        x1 = a[0]
        y1 = a[1]
        # coordinates of the second point
        x2 = b[0]
        y2 = b[1]
        return sqrt((y2-y1)**2+(x2-x1)**2)

def orth_projection(c: list[float], a: list[float], b: list[float]) -> list[float]:
        """Returns the coordinates of the orthographic projection of the point x on the [a,b] segment.

        Args:
            c (list[float]): coordinates of the point to project.
            a (list[float]): coordinates of the first extremity.
            b (list[float]): coordinates of the second extremity.

        Returns:
            list[float]: coordinates of the projection.
        """
        # Coordinates of the point A
        xa = a[0]
        ya = a[1]

        # Coordinates of the point B
        xb = b[0]
        yb = b[1]

        # Coordinates of the point C
        xc = c[0]
        yc = c[1]

        # Coordinates of the direction vector v
        xv = xb-xa
        yv = yb-ya

        # Coordinantes of the projection
        xh = xa + (((xc-xa)*xv+(yc-ya)*yv)/(xv**2+yv**2))*xv
        yh = ya + (((xc-xa)*xv+(yc-ya)*yv)/(xv**2+yv**2))*yv
        return [xh, yh]