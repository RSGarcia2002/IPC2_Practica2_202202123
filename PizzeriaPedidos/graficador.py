# graficador.py

from graphviz import Digraph
import os

def graficar_cola(cola, ruta="recursos/cola"):
    dot = Digraph(format='png')
    dot.attr(rankdir='LR')  # Apuntar de izquierda a derecha
    dot.attr('node', shape='box', style='filled', color='lightblue')

    if cola.esta_vacia():
        dot.node("vacio", "Cola Vacía")
    else:
        nodos = []
        for i, orden in enumerate(cola):
            nombre = f"nodo{i}"
            resumen = f"{orden.cliente}\\n{orden.total_pizzas()} pizzas"
            dot.node(nombre, resumen)
            nodos.append(nombre)
        
        for i in range(len(nodos) - 1):
            dot.edge(nodos[i], nodos[i+1])
    
    # Crear carpeta si no existe
    os.makedirs(os.path.dirname(ruta), exist_ok=True)

    dot.render(ruta, cleanup=True)
