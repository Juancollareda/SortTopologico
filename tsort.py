from Grafo import Grafo  # Importa la clase Grafo del módulo Grafo
from collections import deque  # Importa la clase deque de la biblioteca collections

# Función para crear un grafo a partir de un diccionario de archivos y dependencias
def crear_grafo_desde_diccionario(diccionario):
    grafo = Grafo()  # Crea una instancia de la clase Grafo

    # Agrega nodos y arcos al grafo basados en el diccionario
    for archivo, dependencias in diccionario.items():
        grafo.agregar_nodo(archivo)
        for destino in dependencias:
            grafo.agregar_nodo(destino)
            grafo.agregar_arco(archivo, destino)

    return grafo  # Devuelve el grafo creado
def comparar_grafos(grafo_original, grafo_modificado):
    # Comparar nodos
    nodos_originales = grafo_original.nodos
    nodos_modificados = grafo_modificado.nodos
    nodos_nuevos = nodos_modificados - nodos_originales
    nodos_eliminados = nodos_originales - nodos_modificados

    # Comparar arcos
    arcos_originales = grafo_original.arcos
    arcos_modificados = grafo_modificado.arcos
    # Realiza la comparación de arcos según tus necesidades

    # Puedes personalizar esta función de comparación según lo que desees rastrear en tu grafo

    if nodos_nuevos or nodos_eliminados:
        print("Se han realizado cambios en los nodos del grafo:")
        print("Nodos Nuevos:", nodos_nuevos)
        print("Nodos Eliminados:", nodos_eliminados)
    else:
        print("No se han realizado cambios en los nodos del grafo.")

    # Puedes agregar lógica adicional para comparar arcos u otros aspectos del grafo


# Función para realizar una ordenación topológica utilizando BFS
def tsort(grafo):
    indegree = {nodo: 0 for nodo in grafo.nodos}  # Inicializa el grado de entrada para cada nodo

    # Calcula el grado de entrada de cada nodo
    for nodo in grafo.nodos:
        for vecino in grafo.arcos.get(nodo, []):
            indegree[vecino] += 1

    cola = deque([nodo for nodo, grado in indegree.items() if grado == 0])  # Inicializa la cola con nodos de grado de entrada cero
    orden_topologico = []  # Inicializa la lista para almacenar el orden topológico

    # Realiza el proceso BFS para encontrar el orden topológico
    while cola:
        nodo = cola.popleft()
        orden_topologico.append(nodo)

        for vecino in grafo.arcos.get(nodo, []):
            indegree[vecino] -= 1
            if indegree[vecino] == 0:
                cola.append(vecino)

    # Verifica si se encontró un orden topológico válido
    if len(orden_topologico) == len(grafo.nodos):
        return orden_topologico  # Devuelve el orden topológico encontrado
    else:
        return None  # Devuelve None si el grafo contiene un ciclo
    #esa parte del código que verifica si la longitud del orden topológico es igual a la cantidad de nodos en el grafo es una forma común de determinar si el grafo contiene un ciclo.



# Función principal
def main():
    archivos = {
        "a": ["b", "c"],
        "b": ["a", "e"],
        "c": ["f", "g"],
        "g": ["h"]
    }
    
    mi_grafo = crear_grafo_desde_diccionario(archivos)
    
    orden_topologico = tsort(mi_grafo)
    
    if orden_topologico:
        print("Secuencia de archivos para el linker:")
        for archivo in orden_topologico:
            print(archivo)
    else:
        print("El grafo contiene un ciclo.")

if __name__ == "__main__":
    main()  # Llama a la función principal si este script se ejecuta directamente


