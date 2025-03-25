# cola.py

from orden import Orden

class Nodo:
    def __init__(self, orden):
        self.orden = orden
        self.siguiente = None

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamano = 0

    def esta_vacia(self):
        return self.frente is None

    def encolar(self, orden):
        nuevo = Nodo(orden)
        if self.esta_vacia():
            self.frente = self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo
        self.tamano += 1

    def desencolar(self):
        if self.esta_vacia():
            return None
        orden = self.frente.orden
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        self.tamano -= 1
        return orden

    def ver_primero(self):
        if self.esta_vacia():
            return None
        return self.frente.orden

    def __iter__(self):
        actual = self.frente
        while actual:
            yield actual.orden
            actual = actual.siguiente

    def __len__(self):
        return self.tamano
