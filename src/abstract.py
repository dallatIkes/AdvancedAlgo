import random
from geometry import *
from cli import Cli


class Problem:
    def __init__(self, n: int):
        """Constructor for the Problem class.

        Args:
            n (int): number of points of the problem.
        """
        self.n: int            # number of points of the problem.
        self.SD: float         # sum of all the segments lengths (i.e. sum of the Euclidean distance between all the taken points).
        self.m: int            # number of segments.
        self.C: float          # multiplicative constant.
        self.score: float      # current score.
        self.optScore: float   # current optimal score.
        self.min: int          # minimum ordinate value.
        self.max: int          # maximum ordinate value.
        self.res: list[bool]   # solution vector: True means we take the point.
        self.optRes: list[bool]# optimal solution vector
        self.S: list[int]      # list of all the points ordinate values.

        self.n = n

        self.min = 1
        self.max = 5
        self.S = [random.randint(self.min, self.max) for _ in range(self.n)]
        self.res = [False] * (n - 2)  # initial solution vector (excluding first and last point)
        self.optRes = self.res[:]

        self.SD = self.calcSD()
        self.m = 1
        self.C = 1.5
        self.score = self.calcScore()
        self.optScore = self.score

        print(f"Initial points (S): {self.S}")

    def distance(self, i: int, j: int) -> float:
        """Returns the sum of the distances of points from i to j to the [i,j] segment.

        Args:
            i (int): first extremity of the segment.
            j (int): second extremity of the segment.

        Returns:
            float: sum of the distances.
        """
        sum = 0
        A = [i, self.S[i]]
        B = [j, self.S[j]]
        for k in range(i, j):
            P = [k, self.S[k]]
            H = orth_projection(P, A, B)
            sum += euclidian_distance(P, H)
        return sum
    
    def calcSD(self) -> float:
        """Returns the calculated sum of the Euclidean distances between the taken points and the segments.

        Returns:
            float: calculated SD value.
        """
        start = 0
        sum = 0
        for i in range(self.n - 2):
            if self.res[i]:
                end = i + 1
                sum += self.distance(start, end)
                start = end
        end = self.n - 1
        sum += self.distance(start, end)
        self.SD = sum
        return sum

    def calcScore(self):
        """Returns the current score of the approximation.
        """
        score = self.SD + self.m * self.C
        print(f"Score: {score}")  # Debugging output
        return score

    def satisfaisant(self, xi: int) -> bool:
        """This method returns True if the current vector is an accepted solution to the problem.
        Here it always returns True because every vector is a possible solution since the first and last point are always taken.

        Args:
            xi (int): index of the point (here not used).

        Returns:
            bool: is the current vector an accepted solution to the problem.
        """
        return True

    def enregistrer(self, xi: int, val: bool) -> None:
        """This method changes the state of the xi-th point: taken or not.

        Args:
            xi (int): index of the point.
            val (bool): is the xi-th point taken?
        """
        # if the state of the point doesn't change, we do nothing
        if self.res[xi] != val:
            # if the point is taken, we increment the number of segments
            if val:
                self.m += 1
            # if the point is not taken, we decrement the number of segments
            else:
                self.m -= 1
            self.res[xi] = val
            print(f"Updated res[{xi}] to {val}, m = {self.m}")  # Debugging output

    def soltrouvee(self, xi: int) -> bool:
        """This method returns True when we're done looking for a solution.

        Args:
            xi (int): index of the point.

        Returns:
            bool: is the current point the last one? If so, we're done.
        """
        return xi == self.n-2
    
    def optEncorePossible(self) -> bool:
        """This method returns True if we should continue exploring this branch.

        Returns:
            bool: is True if a better score is still possible.
        """
        return self.score <= self.optScore
    
    def défaire(self, xi: int) -> None:
        """This method leaves the xi-th point (normally taken).

        Args:
            xi (int): index of the point.
        """
        self.enregistrer(xi, False)
        print(f"Undid res[{xi}], m = {self.m}")  # Debugging output

    def solopt(self, i: int):
        """Backtracking method to find the optimal solution.

        Args:
            i (int): index of the current point being considered.
        """
        print(f"Exploring index {i}, res = {self.res}")  # Debugging output
        
        if self.soltrouvee(i):
            # Évaluer la solution complète
            self.SD = self.calcSD()
            eval = self.calcScore()
            print(f"Evaluation at end: {eval}, current best: {self.optScore}")  # Debugging output
            if eval < self.optScore:
                self.optScore = eval
                self.optRes = self.res.copy()  # Store the best solution found so far
                print(f"New optimal found: {self.optRes}")  # Debugging output
            return

        # On explore les deux choix possibles pour le i-ième point: pris ou non pris
        for xi in [True, False]:
            print(f"Trying xi={xi} at index {i}")  # Debugging output
            self.enregistrer(i, xi)  # Update the solution with the new choice
            if self.optEncorePossible():  # Only continue if a better solution is possible
                self.solopt(i + 1)  # Explore further by going to the next point
            self.défaire(i)  # Backtrack: undo the change and explore other possibilities
