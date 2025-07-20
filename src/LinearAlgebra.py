import numpy as np
import sympy as sp


def vector_multiply(vec1, vec2):
    vecRes = [[0 for _ in range(len(vec2[0]))] for _ in range(len(vec1))]
    if not (len(vec1[0]) == len(vec2)):
        print("Vector multiplication is not defined ont these vectors.")
        return -1
    for i in range(len(vec1)):
        for j in range(len(vec2[0])):
            for k in range(len(vec2)):
                vecRes[i][j] += vec1[i][k] * vec2[k][j]

    return vecRes


def solve_lgs(eq):
    a, b, c, d, e, f, g, h, x, y, z = sp.symbols('a b c d e f g h x y z')
    sol = sp.solve(eq, (a, b, c, d, e, f, g, h, x, y, z))
    return sol


class Matrix:

    def __init__(self, matrix):
        self.entries = matrix
        self.size = len(matrix), len(matrix[0])
        self.invertible = self.isInvertible()
        self.det = self.findDet()
        self.charply = self.findCharPoly()
        self.eigenwerte = self.findEigenwerte()

    def __str__(self):
        ausgabe = ""
        for i in range(0, len(self.entries)):
            ausgabe += str(self.entries[i]) + "\n"
        return ausgabe

    def __len__(self):
        return self.size[0] * self.size[1]

    def __getitem__(self, indizes):
        zeile, spalte = indizes
        return self.entries[zeile - 1][spalte - 1]

    def __pow__(self, power):
        stat = self
        curr = self
        for i in range(1, power):
            curr = curr * stat
        return curr

    def __contains__(self, item):
        for i in range(0, len(self.entries)):
            for j in range(0, len(self.entries[0])):
                if self.entries[i][j] == item:
                    return True
        return False

    def __mul__(self, m):
        # Überprüfe, ob die Anzahl der Spalten der ersten Matrix der Anzahl der Zeilen der zweiten Matrix entspricht
        if len(self.entries[0]) == len(m.entries):
            # Erstelle die Ergebnis-Matrix mit Nullen
            result = [[0 for _ in range(len(m.entries[0]))] for _ in range(len(self.entries))]
            curr = Matrix(result)

            # Matrixmultiplikation
            for i in range(len(self.entries)):  # Zeilen von self.entries
                for j in range(len(m.entries[0])):  # Spalten von m.entries
                    for k in range(len(m.entries)):  # Elemente der Spalten von self und Zeilen von m
                        result[i][j] += self.entries[i][k] * m.entries[k][j]

            return curr
        else:
            raise ValueError("Matrixmultiplikation nicht möglich: Falsche Dimensionen.")


    def __add__(self, m):
        result = [[0 for _ in range(len(self.entries[0]))] for _ in range(len(self.entries))]
        if Matrix.isSQR(self, m):
            for i in range(0, len(self.entries)):
                for j in range(0, len(self.entries[i])):
                    result[i][j] = self.entries[i][j] + m.entries[i][j]

        return Matrix(result)

    def __sub__(self, m):
        result = [[0 for _ in range(len(self.entries[0]))] for _ in range(len(self.entries))]
        if Matrix.isSQR(self, m):
            for i in range(0, len(self.entries)):
                for j in range(0, len(self.entries[i])):
                    result[i][j] = self.entries[i][j] - m.entries[i][j]

        return Matrix(result)

    def __eq__(self, m):
        if Matrix.isSQR(self, m):
            for i in range(0, len(self.entries)):
                for j in range(0, len(self.entries[0])):
                    if not self.entries[i][j] == m.entries[i][j]:
                        return 0
        return 1

    def __hash__(self):
        entries_as_tuple = tuple(tuple(row) for row in self.entries)
        return hash(entries_as_tuple)

    def isSQR(self, m):
        stateERRi = len(self.entries) != len(m.entries)
        stateERRj = 0

        if not stateERRi:
            for i in range(0, len(self.entries)):
                if len(self.entries[i]) != len(m.entries):
                    stateERRj = 1
        return not (stateERRi or stateERRj)

    def findCharPoly(self):
        A = np.array(self.entries)
        lambda_ = sp.symbols('x')
        A_sympy = sp.Matrix(A)
        I = sp.eye(A_sympy.shape[0])
        matrix_lambda = A_sympy - lambda_ * I
        determinante = matrix_lambda.det()

        return determinante

    def findDet(self):
        A = np.array(self.entries)
        A_sympy = sp.Matrix(A)
        return A_sympy.det()

    def isInvertible(self):
        return self.findDet() != 0

    def findEigenwerte(self):
        x = sp.symbols('x')
        return sp.solve(self.charply, x)

    def findEigenraum(self):
        # TODO
        return

    def solveLGSM(self, b):
        A = np.array(self.entries)
        b = np.array(b)
        x = np.linalg.solve(A, b)
        print(x)
        return Matrix([x])


class ComplexNumbers:
    real = 0
    complex = 0
    len = 0.0

    def __init__(self, re, im):
        self.real = re
        self.complex = im
        self.len = self.laenge()

    def __str__(self):
        return f"{self.real} + {self.complex}i"

    def __add__(self, other):
        return ComplexNumbers(self.real + other.real, self.complex + other.complex)

    def __mul__(self, other):
        newRe = self.real * other.real - self.complex * other.complex
        newIm = self.real * other.complex + self.complex * other.real
        return ComplexNumbers(newRe, newIm)

    def konjugation(self):
        return self.real, self.complex * -1

    def laenge(self):
        return np.sqrt(self.real * self.real + self.complex * self.complex)
