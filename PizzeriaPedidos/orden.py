# orden.py

class Orden:
    TIEMPOS = {
        "Pepperoni": 12,
        "Hawaiana": 15,
        "Vegetariana": 18,
        "Cuatro Quesos": 20
    }

    def __init__(self, cliente):
        self.cliente = cliente
        self.pizzas = []  # Lista de tuplas: (especialidad, cantidad)

    def agregar_pizza(self, especialidad, cantidad):
        if especialidad in self.TIEMPOS:
            self.pizzas.append((especialidad, cantidad))

    def eliminar_pizza(self, especialidad):
        self.pizzas = [p for p in self.pizzas if p[0] != especialidad]

    def total_pizzas(self):
        return sum(cantidad for _, cantidad in self.pizzas)

    def tiempo_total_orden(self):
        return sum(self.TIEMPOS[esp] * cant for esp, cant in self.pizzas)

    def __str__(self):
        desc = f"Cliente: {self.cliente}\n"
        for especialidad, cantidad in self.pizzas:
            desc += f"  - {cantidad}x {especialidad}\n"
        desc += f"Total pizzas: {self.total_pizzas()}\n"
        desc += f"Tiempo estimado: {self.tiempo_total_orden()} minutos\n"
        return desc
