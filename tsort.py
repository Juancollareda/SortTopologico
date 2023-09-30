from Grafo import Grafo  
from collections import deque  
import yaml
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
    nodos_originales = set(grafo_original.nodos)
    nodos_modificados = set(grafo_modificado.nodos)
    nodos_nuevos = nodos_modificados - nodos_originales
    nodos_eliminados = nodos_originales - nodos_modificados
    # Comparar arcos
    arcos_originales = set(grafo_original.arcos)
    arcos_modificados = set(grafo_modificado.arcos)
    arcos_nuevos = arcos_modificados - arcos_originales
    arcos_eliminados = arcos_originales - arcos_modificados
    if nodos_nuevos or nodos_eliminados or arcos_nuevos or arcos_eliminados:
        print("Se han realizado cambios en el grafo:")
        if nodos_nuevos or nodos_eliminados:
            print("Cambios en nodos:")
            print("Nodos Nuevos:", nodos_nuevos)
            print("Nodos Eliminados:", nodos_eliminados)
        if arcos_nuevos or arcos_eliminados:
            print("Cambios en arcos:")
            print("Arcos Nuevos:", arcos_nuevos)
            print("Arcos Eliminados:", arcos_eliminados)
    else:
        print("No se han realizado cambios en el grafo.")

def cargar_yaml_a_dict(ruta_archivo):
    try:
        with open(ruta_archivo, "r") as archivo:
            datos = yaml.safe_load(archivo)
        return datos
    except FileNotFoundError:
        print(f"El archivo '{ruta_archivo}' no fue encontrado.")
        return None
    except Exception as e:
        print(f"Se produjo un error al cargar el archivo YAML: {str(e)}")
        return None 

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
        "b": ["g"],
        "c": ["f", "g"],
        "g": ["h"],
        "h": ["f"],
        "f": [],
    }
    archivos2 = {
        "a": ["b"],
        "b": ["g"],
        "c": ["f", "g"],
        "g": ["h"],
        "h": []
    }
    dict3=cargar_yaml_a_dict('archivo.yaml')
    mi_grafo = crear_grafo_desde_diccionario(dict3)
    #mi_grafo2 = crear_grafo_desde_diccionario(archivos2)
   # comparar_grafos(mi_grafo,mi_grafo2)
    orden_topologico = tsort(mi_grafo)    
    if orden_topologico:
        print("Secuencia de archivos para el linker:")
        for archivo in orden_topologico:
            print(archivo)
    else:
        print("El grafo contiene un ciclo.")

if __name__ == "__main__":
    main()  


