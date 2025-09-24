# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código

class Nodo:
    def __init__(self, item, prev=None, next=None):
        self.item = item #Dato que guardo dentro del nodo.
        self.prev = prev #Referencia al nodo anterior.
        self.next = next #Referencia al nodo siguiente.

class ListaDoblementeEnlazada:
    def __init__(self):
        self._head = None #Primer nodo --> La cabeza
        self._tail = None #Ultimo nodo --> La cola
        self._size = 0 #Cantidad de elementos en la lista --> La creo vacia, la consigna dice que el Init tiene que crear una lista vacia.

    def __str__(self):
        # sirve para poder mostrar el contenido de una LDE por consola con la función print
        elementos = []
        actual = self._head
        while actual is not None:
            elementos.append(str(actual.item))
            actual = actual.next
        return " <-> ".join(elementos)

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

    def insertar(self, item, posicion: int):
        if posicion < 0 or posicion > self._size:
            raise IndexError("La posición ingresada no es válida, se encuentra fuera de rango")

        if posicion == 0:
            self.agregar_al_inicio(item)
            return

        if posicion == self._size:
            self.agregar_al_final(item)
            return

        # Posiciones intermedias
        actual = self._head
        for _ in range(posicion):
            actual = actual.next

    # Si actual.prev es None significa que estamos insertando en la cabeza
        if actual.prev is None:
            nuevo = Nodo(item, next=actual)
            actual.prev = nuevo
            self._head = nuevo
        else:
            nuevo = Nodo(item, prev=actual.prev, next=actual)
            actual.prev.next = nuevo
            actual.prev = nuevo

        self._size += 1


    def extraer(self, posicion=None):
        
        if self._head is None:
            raise Exception("La lista está vacía")
        
        if posicion is None:
            posicion=self._size -1
        
        if posicion < 0 or posicion >= self._size:
            raise IndexError("Posición invalida")

        if posicion == 0:
            valor = self._head.item
            self._head = self._head.next
            if self._head:
                self._head.prev = None
            else:
                self._tail = None #lista quedó vacía
            self._size -= 1
            return valor

    def copiar(self):
        lista_nueva = ListaDoblementeEnlazada()
        actual = self._head

        while actual is not None:
            if lista_nueva.esta_vacia():
                nodo_nuevo = Nodo(actual.item)
                lista_nueva._head = nodo_nuevo
                lista_nueva._tail = nodo_nuevo
            else:
                nodo_nuevo = Nodo(actual.item, prev= lista_nueva._tail)
                lista_nueva._tail.next = nodo_nuevo
                lista_nueva._tail = nodo_nuevo

            lista_nueva._size += 1
            actual = actual.next
        
        return lista_nueva
    
    def invertir(self):
    #Empezamos desde la cabeza de la lista
        actual = self._head
        #Recorremos todos los nodos hasta que no haya más
        while actual is not None:
            #Intercambiamos punteros prev y next de este nodo
            actual.prev, actual.next = actual.next, actual.prev
            #Avanzamos al siguiente nodo, que después del intercambio quedó en prev
            actual = actual.prev
    #Al terminar el recorrido, la cabeza y la cola deben intercambiarse
        self._head, self._tail = self._tail, self._head
    #Devolvemos la lista invertida (útil si queremos encadenar llamadas)
        return self

    def concatenar(self, lista):
        copia=lista.copiar()
        if not self._head:
            self._head = copia._head   
            self._tail = copia._tail
        elif copia._head:
            self._tail.next = copia._head
            copia._head.prev = self._tail
            self._tail = copia._tail
        self._size += len(copia)
        return self


    def __len__(self, lista):
        contador = 0
        for i in lista:
            while lista._head is not None:
                contador += 1
            if lista._head == None:
                break
        return contador


    

    