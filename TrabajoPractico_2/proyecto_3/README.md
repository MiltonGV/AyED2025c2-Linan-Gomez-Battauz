# 🐍Palomas Mensajeras: Optimización de Rutas de Mensajería

Breve descripción del proyecto:

Este proyecto aborda el problema de encontrar la forma más eficiente de llevar un mensaje desde una aldea de origen, "Peligros", a un grupo de otras 21 aldeas. El sistema se basa en palomas mensajeras que solo pueden viajar a aldeas vecinas. El objetivo es que cada aldea reciba la noticia una sola vez, minimizando los recursos (distancia total recorrida).El proyecto utiliza la información de rutas y distancias provista en el archivo `aldeas.txt`.

---
## 🏗Arquitectura General

El codigo se compone de la siguiente forma:

* Estructuras de Datos Fundamentales:

    vertice.py: Implementa la clase Vertice
    Almacena el ID del vértice y sus conexiones y maneja las relaciones con vértices vecinos y sus ponderaciones
    Métodos: agregarVecino(), obtenerConexiones(), obtenerPonderacion()
    grafo.py: Implementa la clase Grafo y contiene un diccionario de vértices (listaVertices) que permite agregar vértices y aristas de forma bidireccional
    Métodos: agregarVertice(), agregarArista(), obtenerVertice()

* Estructuras de Datos Auxiliares:

    lists.py: Implementa ListsBinario (Montículo Binario/Min-Heap), usado para la cola de prioridad con operaciones operaciones: insertar(), eliminarMin(), infiltArriba(), infiltAbajo()
    cola_de_prioridad.py: Implementa ColaDePrioridad    Envuelve el montículo binario con funcionalidad de cola de prioridad
    Permite encolar elementos con prioridad personalizable y envuelve el sistema binario con funcionalidad de cola de prioridad para tambien permitir encolar elementos con prioridad personalizable

* Algoritmo Principal:

    main.py: Orquesta todo el proceso
    construirGrafo(): Lee aldeas.txt y construye el grafo
    prim(): Implementa el algoritmo de Prim para encontrar el árbol de expansión mínima
    main(): Coordina la ejecución y muestra resultados
---
## 📑Dependencias

1. **Python 3.x**
2. **matplotlib** (`pip install matplotlib`)


---
## 🚀Cómo Ejecutar el Proyecto
1. **Clonar o descargar** el repositorio.

2. **Crear y activar** un entorno virtual.

3. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
   El archivo `requirements.txt` se encuentran en la carpeta [deps](./deps) del proyecto.

---
## 🙎‍♀️🙎‍♂️Autores

- Gomez Villon Milton
- Pedro Battauz
- Juan Linan

---

