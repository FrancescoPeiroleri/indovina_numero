import random


class Model(object):
    def __init__(self):
        self._NMax = 100 #fondo scala
        self._Tmax = 6 #numero massimo di tentativi
        self._Trim = self._Tmax
        self._segreto = None

    @property
    def segreto(self):
        return self._segreto

    @property
    def NMax(self):
        return self._NMax

    @property
    def TMax(self):
        return self._Tmax

    @property
    def Trim(self):
        return self._Trim

    def inizializza(self):
        self._segreto = random.randint(1, self._NMax)
        self._Mrim = self._Tmax
        print(self._segreto)

    def indovina(self, tentativo):

        if self._Trim == 0:
            return self._Trim, None
        else:
            self._Trim = self._Trim - 1

        if tentativo == self._segreto:
            return self._Trim, 0
        elif tentativo > self._segreto:
            return self._Trim, -1
        else:
            return self._Trim, 1
