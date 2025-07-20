import numpy as np


class Polynom:

    def __init__(self, coefficients):
        self.coefficients = list(map(int, coefficients))
        self.degree = len(coefficients) - 1

    def __str__(self):
        ausgabe = ""
        for i in range(0, len(self.coefficients)):
            ausgabe += str(self.coefficients[i]) + " + "
        return ausgabe

    def __sub__(self, other):
        curr = self
        for i in range(0, len(self.coefficients)):
            curr.coefficients[i] -= other.coefficients[i]
        return curr

    def __add__(self, other):
        curr = self
        for i in range(0,len(self.coefficients)):
            curr.coefficients[i] += other.coefficients[i]
        return curr

    def __len__(self):
        return len(self.coefficients)

    def __eq__(self, other):
        for i in range(00, len(self.coefficients)):
            if not other.coefficients[i] == self.coefficients[i]:
                return False
        return True

    def null_stellen(self):
        return np.roots(self.coefficients)

    def evaluate(self, x: int):
        y = 0
        counter = 0
        for i in self.coefficients:
            y = y + i * pow(x, counter)
            counter = counter + 1
        return y

    def integration_trapez(self, beginning, ending, numberOfIntervalls):
        h = (ending - beginning) / numberOfIntervalls
        summe = self.evaluate(beginning) + self.evaluate(ending)
        for i in range(1, numberOfIntervalls):
            summe += (self.evaluate(beginning + h * i)) * 2
        return summe * (h / 2)
