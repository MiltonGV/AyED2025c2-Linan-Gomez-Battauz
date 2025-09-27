from modules.ListaDoblemmenteEnlazada import ListaDoblementeEnlazada
import time
import matplotlib.pyplot as plt
from random import randint
#lista = ListaDoblementeEnlazada()
#print("¿Está vacía?", lista.esta_vacia())

lista = ListaDoblementeEnlazada()

lista.agregar_al_inicio(10)

print("¿Está vacía?", lista.esta_vacia()) #Entonces, aca veo si mi lista enlazada tiene items o no.
print("Tamaño:", lista._size) #Veo el tamaño de mi lista en el caso de agregar algun elemento, en este caso por ejemplo agregué el 10
print("La cabeza:", lista._head.item) #Veo el item q esta en la primer posición
print("La cola:", lista._tail.item) #Veo el item q esta en la ultima posición.

#Pruebo agregar otro elemento más, para corroborar que lista._tail.item muestra correctamente el ultimo valor.

lista.agregar_al_inicio(20.4)

#Deberia mostrar en Head el 20 y en Tail el 10.

print("¿Está vacía?",lista.esta_vacia())
print("Tamaño:",lista.__len__())
print("La cabeza:",lista._head.item)
print("La cola:",lista._tail.item)

#De nuevo, corroboro que de verdad agrega el item al final.
lista.agregar_al_final("hola")
print("Tamaño:",lista.__len__())
print("La cabeza:",lista._head.item)
print("La cola:",lista._tail.item)

#Pruebo la función insertar
lista.insertar(4,0)

lista2 = ListaDoblementeEnlazada()
lista2.agregar_al_inicio(2)
lista2.agregar_al_final(4)
lista2.agregar_al_inicio(1)
lista2.agregar_al_inicio(5)
print(lista2)
print(lista)
print(lista.__len__())

import time
import matplotlib.pyplot as plt
from random import randint

def generar_lde(n):
    lde = ListaDoblementeEnlazada()
    for i in range(n):
        lde.insertar(i, lde._size)  # Inserta al final
    return lde

def medir_tiempo(metodo, *args, repeticiones=3):
    tiempos = []
    for _ in range(repeticiones):
        inicio = time.perf_counter()
        metodo(*args)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
    return sum(tiempos) / repeticiones

# 300 tamaños de N desde 100 hasta 30,000
Ns = list(range(100, 30100, 100))
tiempos_len = []
tiempos_copiar = []
tiempos_invertir = []

print("Midiendo tiempos para 300 tamaños distintos...")

for n in Ns:
    lde = generar_lde(n)

    t_len = medir_tiempo(len, lde)
    t_copiar = medir_tiempo(lde.copiar)
    t_invertir = medir_tiempo(lde.invertir)

    tiempos_len.append(t_len)
    tiempos_copiar.append(t_copiar)
    tiempos_invertir.append(t_invertir)

    print(f"N={n:<5} | len(): {t_len:.6f}s | copiar(): {t_copiar:.6f}s | invertir(): {t_invertir:.6f}s")

# Graficar los resultados
plt.figure(figsize=(14, 8))
plt.plot(Ns, tiempos_len, label='len()', linewidth=2)
plt.plot(Ns, tiempos_copiar, label='copiar()', linewidth=2)
plt.plot(Ns, tiempos_invertir, label='invertir()', linewidth=2)

plt.xlabel('Cantidad de elementos (N)', fontsize=12)
plt.ylabel('Tiempo de ejecución (segundos)', fontsize=12)
plt.title('Tiempo de ejecución vs N para len(), copiar() e invertir()', fontsize=14)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
