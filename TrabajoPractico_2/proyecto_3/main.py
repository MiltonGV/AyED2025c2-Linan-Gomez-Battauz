from modules.cola_de_prioridad import ColaDePrioridad
from modules.grafo import Grafo
from collections import defaultdict

def construirGrafo(archivoPalabras):
    d = {}
    g = Grafo()
    with open(archivoPalabras, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            partes = [p.strip() for p in linea.strip().split(',')]
            
            if len(partes) < 3:  # Saltar líneas incompletas
                continue
            print(partes)
            aldea1, aldea2, distancia = partes[0], partes[1], int(partes[2])
            
            g.agregarArista(aldea1, aldea2, distancia)
            g.agregarArista(aldea2, aldea1, distancia)
    return g

def prim(grafo, inicio):
    """Algoritmo de Prim para obtener el árbol de expansión mínima usando MonticuloBinario"""
    visitados = set([inicio])
    arbol = {}  
    distancia_total = 0
    
    # Crear cola de prioridad para manejar las aristas
    cola = ColaDePrioridad(clave=lambda x: x[0])  # Ordenar por peso
    
    inicio_vert = grafo.obtenerVertice(inicio)
    for vecino in inicio_vert.obtenerConexiones():
        peso = inicio_vert.obtenerPonderacion(vecino)
        cola.encolar((peso, inicio, vecino.id))  
    
    # Procesar hasta visitar todos los nodos
    while len(cola) > 0 and len(visitados) < len(grafo.listaVertices):
        peso, padre, nodo = cola.desencolar() 
        
        if nodo in visitados:
            continue
            
        visitados.add(nodo)
        arbol[nodo] = padre
        distancia_total += peso
        
        # Agregar vecinos del nuevo nodo
        nodo_vert = grafo.obtenerVertice(nodo)
        for vecino in nodo_vert.obtenerConexiones(): 
            if vecino.id not in visitados:
                peso_arista = nodo_vert.obtenerPonderacion(vecino)
                cola.encolar((peso_arista, nodo, vecino.id)) 
    
    return arbol, distancia_total

def main():
    # 1. Construir grafo desde archivo
    grafo = construirGrafo("data/aldeas.txt")
    aldeas = list(grafo.obtenerVertices())
    aldeas_ordenadas = sorted(aldeas)
    
    # 2. Aplicar algoritmo de Prim desde "Peligros"
    padre_de, distancia_total = prim(grafo, "Peligros")
    
    # Construir estructura de hijos
    hijos_de = defaultdict(list)
    for hijo, padre in padre_de.items(): 
        hijos_de[padre].append(hijo)
    
    # 3. Mostrar resultados
    print("Aldeas en orden alfabético:")
    for aldea in aldeas_ordenadas:
        print(f"- {aldea}")
    
    print("\nEstructura de envíos:")
    for aldea in aldeas_ordenadas:
        # Determinar quién envía la noticia a esta aldea
        if aldea == "Peligros":
            recibe_de = "Ninguno (inicio)"
        else:
            recibe_de = padre_de.get(aldea, "No alcanzada")
        
        # Determinar a quién reenvía esta aldea
        envia_a = hijos_de.get(aldea, [])
        envia_a_str = ", ".join(envia_a) if envia_a else "Ninguna"
        
        print(f"\nAldea: {aldea}")
        print(f"  Recibe de: {recibe_de}")
        print(f"  Envía a: {envia_a_str}")
    
    print(f"\nDistancia total recorrida: {distancia_total} leguas")


if __name__ == "__main__":
    main()