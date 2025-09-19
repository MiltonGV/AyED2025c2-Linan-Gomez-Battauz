from modules.modulo1 import ListaDoblementeEnlazada

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
print("Tamaño:",lista._size)
print("La cabeza:",lista._head.item)
print("La cola:",lista._tail.item)

#De nuevo, corroboro que de verdad agrega el item al final.
lista.agregar_al_final("hola")
print("Tamaño:",lista._size)
print("La cabeza:",lista._head.item)
print("La cola:",lista._tail.item)

lista.insertar(5,2)
print("Tamaño:",lista._size)