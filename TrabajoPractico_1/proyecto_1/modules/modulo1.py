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

    def insertar(self, item, position):
        if position < 0:
            raise ValueError("La posición no puede ser negativa")
        
        # Caso: lista vacía o posición 0
        if self._head is None or position == 0:
            nuevo = Nodo(item)
            nuevo.next = self._head
            
            if self._head is not None:
                self._head.prev = nuevo
            
            self._head = nuevo
            
            if self.tail is None:
                self.tail = nuevo
            
            self.size += 1
            return
        
        # Caso: posición mayor o igual al tamaño (insertar al final)
        if position >= self._size:
            nuevo = Nodo(item)
            nuevo.prev = self.tail
            
            if self.tail is not None:
                self.tail.next = nuevo
            
            self.tail = nuevo
            
            # Si solo había un elemento
            if self._head is None:
                self._head = nuevo
            
            self.size += 1
            return
        
        # Caso: inserción en posición intermedia
        actual = self._head
        contador = 0
        
        # Recorrer hasta la posición deseada
        while actual is not None and contador < position:
            actual = actual.next
            contador += 1
        
        # Crear nuevo nodo
        nuevo = Nodo(item)
        nuevo.prev = actual.prev
        nuevo.next = actual
        
        # Reenlazar nodos adyacentes
        if actual.prev is not None:
            actual.prev.next = nuevo
        
        actual.prev = nuevo
        
        self.size += 1