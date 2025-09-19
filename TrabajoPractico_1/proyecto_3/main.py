
#Importo los algoritmos
from modules.BubbleSort import BubbleSort
from modules.Quicksort import quicksort
from modules.Radix_sort import radix_sort


#Importo librerias para graficar y medir tiempos
import time
import matplotlib.pyplot as plt
import random

#Donde estan los diferentes tamaños de las listas
tamaños_de_lista = range(1, 1001, 10)  # Listas desde 1 hasta 1000 elementos, en pasos de 10

#Listas de tiempos
tiempos_bubble = []
tiempos_quick = []
tiempos_radix = []
tiempos_sorted = []


#Esto es para saber de que tamaño son las distintas listas
for tamaño in tamaños_de_lista:
    lista = [random.randint(10000,99999) for _ in range(tamaño)]
    
    #Mediciones de tiempo 

    #Bubble_Sort
    Lista_copia = lista.copy() #Para no tener que generarla de nuevo para las otras pruebas
    inicio = time.time() #Guardo el tiempo de inicio
    BubbleSort(Lista_copia)
    tiempos_bubble.append(time.time() - inicio) #Agrego a la lista de tiempo de bubble lo que se demoro en ejecutar

    #Quicksort
    Lista_copia = lista.copy() #Para no tener que generarla de nuevo para las otras pruebas
    inicio = time.time() #Guardo el tiempo de inicio
    quicksort(Lista_copia)
    tiempos_quick.append(time.time() - inicio) #Agrego a la lista de tiempo de bubble lo que se demoro en ejecutar


    #Radix Sort
    Lista_copia = lista.copy() #Para no tener que generarla de nuevo para las otras pruebas
    inicio = time.time() #Guardo el tiempo de inicio
    radix_sort(Lista_copia)
    tiempos_radix.append(time.time() - inicio) #Agrego a la lista de tiempo de bubble lo que se demoro en ejecutar
    
    #Sorted
    Lista_copia = lista.copy()
    inicio = time.time()
    sorted(Lista_copia)
    tiempos_sorted.append(time.time() - inicio)
    




#Grafico de resultados

plt.figure(figsize=(10, 6))
plt.plot(tamaños_de_lista, tiempos_bubble, label='Bubble Sort (O(n²))')
plt.plot(tamaños_de_lista, tiempos_quick, label='Quick Sort (O(n log n) promedio)')
plt.plot(tamaños_de_lista, tiempos_radix, label='Radix Sort (O(nk))')
plt.plot(tamaños_de_lista, tiempos_sorted, label= 'Sorted (O(n log n)')
plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Comparación de Algoritmos de Ordenamiento')
plt.legend()
plt.grid(True)
plt.show()

#Aclacion de como correr los Test, se corren desde la consola cmd, posicionandose en la direccion
# del proyecto con cd y despues ejecutar python -m unittest discover -s tests
