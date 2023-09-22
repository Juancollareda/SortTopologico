class Grafo:
    def __init__(self):
        self.nodos = set()
        self.arcos = {}
    
    def agregar_nodo(self, nodo):
        self.nodos.add(nodo)
        if nodo not in self.arcos:
            self.arcos[nodo] = []

    def agregar_arco(self, origen, destino):
        if origen in self.nodos and destino in self.nodos:
            self.arcos[origen].append(destino)
        else:
            raise ValueError("Los nodos de origen y destino deben estar en el grafo.")
        
        # Crear un grafo para representar archivos y dependencias
grafo = Grafo()

