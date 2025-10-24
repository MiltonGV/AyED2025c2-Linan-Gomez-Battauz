# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código
from random import randint

class nodo:
    def __init__(self, dato, anterior=None, siguiente=None):
        self.dato = dato #Dato que guardo dentro del nodo.
        self.anterior = anterior #Referencia al nodo anterior.
        self.siguiente = siguiente #Referencia al nodo siguiente.

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None #Primer nodo --> La cabeza
        self.cola = None #Ultimo nodo --> La cola
        self.tamanio = 0 #Cantidad de elementos en la lista --> La creo vacia, la consigna dice que el Init tiene que crear una lista vacia.

    def __str__(self):
        # sirve para poder mostrar el contenido de una LDE por consola con la función print
        elementos = []
        actual = self.cabeza
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " <-> ".join(elementos)

    def esta_vacia(self):
        """Devuelve True si la lista está vacía"""
        return self.tamanio == 0
    
    def agregar_al_inicio(self, dato):
        nuevo = nodo(dato, anterior=None, siguiente=self.cabeza)

        if self.cabeza is None:
            #La lista estaría vacía, por lo que ahora este seria el único nodo.
            self.cabeza = self.cola = nuevo
        
        else:
            #Conecto el "viejo" head con el nuevo (?)
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo
        self.tamanio += 1

    def agregar_al_final(self, dato):
        nuevo = nodo(dato, anterior=self.cola, siguiente=None)

        if self.cola is None:
            #Nuevamente, la lista estaría vacía, por lo q este sería el único nodo, creo
            self.cola = self.cabeza = nuevo
        else:
            #Ahora conecto el viejo tail con el nuevo
            self.cola.siguiente = nuevo
            self.cola = nuevo
        self.tamanio += 1

    def insertar(self, dato, posicion: int):
        if posicion < 0 or posicion > self.tamanio:
            raise IndexError("La posición ingresada no es válida, se encuentra fuera de rango")

        if posicion == 0:
            self.agregar_al_inicio(dato)
            return

        if posicion == self.tamanio:
            self.agregar_al_final(dato)
            return

        # Posiciones intermedias
        actual = self.cabeza
        for _ in range(posicion):
            actual = actual.siguiente

    # Si actual.anterior es None significa que estamos insertando en la cabeza
        if actual.anterior is None:
            nuevo = nodo(dato, siguiente=actual)
            actual.anterior = nuevo
            self.cabeza = nuevo
        else:
            nuevo = nodo(dato, anterior=actual.anterior, siguiente=actual)
            actual.anterior.siguiente = nuevo
            actual.anterior = nuevo

        self.tamanio += 1


    def extraer(self, posicion=None):
        
        if self.cabeza is None:
            raise Exception("La lista está vacía")
        
        if posicion is None:
            posicion=self.tamanio -1
        
        if posicion < 0 or posicion >= self.tamanio:
            raise IndexError("Posición invalida")

        if posicion == 0:
            valor = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
            if self.cabeza:
                self.cabeza.anterior = None
            else:
                self.cola = None #lista quedó vacía
            self.tamanio -= 1
            return valor
        
        if posicion == self.tamanio - 1:
            valor = self.cola.dato
            self.cola = self.cola.anterior
            if self.cola:
                self.cola.siguiente = None
            else:
                self.cabeza = None
            self.tamanio -= 1
            return valor

        if posicion < self.tamanio // 2:
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
        else:
            actual = self.cola
            for _ in range(self.tamanio - 1 - posicion):
                actual = actual.anterior
        
        valor = actual.dato
        
        actual.anterior.siguiente = actual.siguiente
        actual.siguiente.anterior = actual.anterior

    def copiar(self):
        lista_nueva = ListaDobleEnlazada()
        actual = self.cabeza

        while actual is not None:
            if lista_nueva.esta_vacia():
                nodo_nuevo = nodo(actual.dato)
                lista_nueva.cabeza = nodo_nuevo
                lista_nueva.cola = nodo_nuevo
            else:
                nodo_nuevo = nodo(actual.dato, anterior= lista_nueva.cola)
                lista_nueva.cola.siguiente = nodo_nuevo
                lista_nueva.cola = nodo_nuevo

            lista_nueva.tamanio += 1
            actual = actual.siguiente
        
        return lista_nueva
    
    def invertir(self):
    #Empezamos desde la cabeza de la lista
        actual = self.cabeza
        #Recorremos todos los nodos hasta que no haya más
        while actual is not None:
            #Intercambiamos punteros anterior y siguiente de este nodo
            actual.anterior, actual.siguiente = actual.siguiente, actual.anterior
            #Avanzamos al siguiente nodo, que después del intercambio quedó en anterior
            actual = actual.anterior
    #Al terminar el recorrido, la cabeza y la cola deben intercambiarse
        self.cabeza, self.cola = self.cola, self.cabeza
    #Devolvemos la lista invertida (útil si queremos encadenar llamadas)
        return self

    def concatenar(self, lista):
        copia=lista.copiar()
        if not self.cabeza:
            self.cabeza = copia.cabeza   
            self.cola = copia.cola
        elif copia.cabeza:
            self.cola.siguiente = copia.cabeza
            copia.cabeza.anterior = self.cola
            self.cola = copia.cola
        self.tamanio += len(copia)
        self.lista + copia
        return self

    def __len__(self):
        return self.tamanio
    

    

    