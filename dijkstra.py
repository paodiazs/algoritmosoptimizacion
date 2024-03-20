import sys

def dijkstra(grafo, nodo_inicio):#con def hacemos una funcion en python, y le pasamos como argumento el grafo y el inicio, que será el nodo inicio
#PARTE 1 - INICIALIZACIÓN DE DATOS
  
    # Inicializamos los conjuntos de nodos visitados y no visitados
    visitados = set()#set es una coleccion de datos en python, en este caso está vacía
    no_visitados = set(grafo.keys())#en unvisited guardaremos las claves de nuestro grafo, es decir [A,B,C,D,E,F]
    

    distances = {} #creamos diccionario vacio, es el cual guardará las distancias(los pesos de cada nodo) 
    """
    distances = {
    'A':0,
    'B': sys.maxsize
    }
    """
    nodos_previos = {} #creamos diccionario vacio
 

    for node in grafo: #vamos recorriendo las CLAVES de graph
        nodos_previos[node] = None #nodos_previos de cada nodo = NONE
        distances[node] = 0 if node == nodo_inicio else sys.maxsize
        
    """
    {
    'A': None,
    'B': 'A',
    'C': 'B',
    'D': 'A',
    'E': 'B',
    'F': 'D'
}
"""
#FINAL PARTE 1 - INICIALIZACIÓN   
        
#INICIO - PARTE 2        
    while no_visitados: # Mientras haya nodos no visitados
        # Seleccionamos el nodo no visitado con la distancia más corta
        nodo_actual = min(no_visitados, key=distances.get) #min toma como iterable(donde va a buscar el minimo) a unvisited, y tomara la menor distancia del diccionario de unvisited
        
        # Marcamos el nodo como visitado y lo eliminamos del conjunto de no visitados
        no_visitados.remove(nodo_actual) #remove quita el elemento que sea nodo_actual, es decir, eliminamos de novisitados al elemento nodo_actual
        visitados.add(nodo_actual) #añadimos a visitados nodo_actual
        
        # Actualizamos las distancias a los vecinos del nodo actual
        for neighbor, weight in grafo[nodo_actual].items(): #.items() nos duelve (vecino, peso) respecto al nodo actual que es nodo_actual
            if neighbor not in visitados: #si vecino no está en el set VISITED
                new_distance = distances[nodo_actual] + weight #nueva distancia es igual a la distancia del nodo actual + el peso
                #peso de la arista que conecta el nodo actual con el vecino (weight)
                if new_distance < distances[neighbor]: #si la nueva distancia es menor a distances[neighbor]
                    #distances[neighbor] es el VALOR asociado con la clave neighbor (número de la distancia)
                    distances[neighbor] = new_distance #actualizamos 
                    nodos_previos[neighbor] = nodo_actual #el nodo nodo_actual es el nodo previo de neighbor

    return distances, nodos_previos #final funcion dijkstra 
    #devolvemos dos diccionarios (distances: distancias más cortas conocidas desde el nodo inicial hasta cada nodo en el grafo) y 
    #(previous: nodos previos en el camino)

# Ejemplo de uso
 #graph es un diccionario, que esta relacionado con llave: valor, diccionario exterior son los {} inciales
grafo = {
    'A': { 'D': 5, 'B':2 },
    'B': { 'E':2, 'C':3},
    'C': { 'Z': 7},
    'D': {'E': 1, 'F': 6},
    'E':{ 'H': 5, 'G':2},
    'F':{ 'Z':5},
    'G' : {'Z': 3},
    'H':{ 'I':4},
    'I':{ 'Z':1},
    'Z':{}
}
 #Cada clave del diccionario exterior corresponde a un nodo del grafo, y el valor asociado a cada clave es otro diccionario que contiene los nodos vecinos y los pesos de las aristas que los conectan.

nodo_inicio = 'A'

resultados = dijkstra(grafo, nodo_inicio) #a resultados asignamos la tupla que devuelve dijkstra


distances = resultados[0] #a distances accedemos al primer elemento 
nodos_previos = resultados[1] # y a previous el segundo elemento


print("Distancias más cortas desde el nodo inicial:")
for node, distance in distances.items():
    print(f"Nodo: {node}, Distancia: {distance}")

print("\nNodos previos en el camino más corto:")
for node, prev_node in nodos_previos.items():
    print(f"Nodo: {node}, Nodo Previo: {prev_node}") #La f-string permite incrustar las variables node y distance dentro de la cadena de texto.






# Nodo de destino
target_node = 'Z'

# Inicializamos una lista para almacenar el camino
path = [target_node]



# Rastreamos el camino desde 'C' hasta el nodo inicial
while nodos_previos[target_node] is not None:
    target_node = nodos_previos[target_node]
    path.append(target_node)
    

# Invertimos la lista para obtener el camino desde el nodo inicial hasta 'C'
path.reverse()

# Creamos una cadena con las flechas "->" entre los nodos del camino
path_str = ' -> '.join(path)

# Imprimimos el camino
print("Camino desde nodo inicial hasta 'Z':")
print(path_str)
