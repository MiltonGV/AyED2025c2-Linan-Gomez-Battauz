# 🐍Palomas Mensajeras: Optimización de Rutas de Mensajería

Breve descripción del proyecto:

Este proyecto aborda el problema de encontrar la forma más eficiente de llevar un mensaje desde una aldea de origen, "Peligros", a un grupo de otras 21 aldeas. El sistema se basa en palomas mensajeras que solo pueden viajar a aldeas vecinas.El objetivo es que cada aldea reciba la noticia una sola vez, minimizando los recursos (distancia total recorrida).El proyecto utiliza la información de rutas y distancias provista en el archivo `aldeas.txt`.

---
## 🏗Arquitectura General

El código está organizado de la siguiente manera:

* Módulo de Grafo: Contiene la implementación de la estructura de datos del grafo (por ejemplo, usando listas de adyacencia o una matriz de adyacencia) y las operaciones asociadas (agregar nodos, aristas, etc.).
* Módulo de Algoritmos: Implementa el algoritmo seleccionado para encontrar la ruta de difusión más eficiente (ej. Prim, Kruskal o similar para construir un Árbol de Expansión Mínima).
* Módulo de Procesamiento de Datos: Encargado de leer el archivo `aldeas.txt` y transformar los datos en un formato utilizable por el módulo de grafo.
* Script Principal (main.p):
    * Orquesta la lectura de datos, la construcción del grafo y la ejecución del algoritmo.
    * Presenta los resultados solicitados: lista de aldeas, plan de envío para cada aldea y la distancia total. [cite: 37, 39]

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

