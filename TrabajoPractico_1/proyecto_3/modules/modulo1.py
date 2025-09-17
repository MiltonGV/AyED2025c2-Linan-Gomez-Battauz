# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código

class Nodo:
    def __init__(self, item, prev=None, next=None):
        self.item = item #Dato que guarda el nodo.
        self.prev = prev #Referencia al nodo anterior.
        self.next = next #Referencia al nodo siguiente.

class ListaDoblementeEnlazada:
    def __init__(self):
        self._head = None #Primer nodo --> La cabeza
        self._tail = None #Ultimo nodo --> La cola
        self._size = 0 #Cantidad de elementos en la lista --> La creo vacia (?)

    def esta_vacia(self):
        """Devuelve True si la lista está vacía"""
        return self._size == 0
    
    def agregar_al_inicio(self, item):
        nuevo = Nodo(item, prev=None, next=self._head)

        if self._head is None:
            #La lista estaría vacía, por lo que ahora este seria el único nodo.
            self._head = self._tail = nuevo
        
        else:
            #Conecto el "viejo" head con el nuevo (?)
            self._head.prev = nuevo
            self._head = nuevo
        self._size += 1

    def agregar_al_final(self, item):
        nuevo = Nodo(item, prev=self._tail, next=None)

        if self._tail is None:
            #Nuevamente, la lista estaría vacía, por lo q este sería el único nodo, creo
            self._tail = self._head = nuevo
        else:
            #Ahora conecto el viejo tail con el nuevo
            self._tail.prev = nuevo
            self._tail = nuevo
        self._size += 1

    def insertar (self, item, posicion):
        nuevo = Nodo(item, ListaDoblementeEnlazada[posicion])
        
        
        if posicion == None:
            nuevo = Nodo(item, prev=self._tail, next=None)

        self._size += 1

#Bien, una vez que agregué el metodo "esta_vacia" ahora voy con el metodo para agregar al inicio de la lista un item.
