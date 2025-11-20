import datetime

class nodoAVL: #Cada nodoAVL es un dato de temperatura y fecha en si
    
    def __init__(self, fecha:datetime.date, temperatura):

        if not isinstance(fecha,datetime.date):
            raise ValueError("La fecha debe venir en el formato correspondiente (Error en guardar_temp)")
        
        self.temperatura = float(temperatura)
        self.fecha = fecha
        #Logica nodo
        self.izquierda = None
        self.derecha = None
        self.altura = 1 #La altura de un nuevo nodo es 1.

    #Esta función devuelve los valores
    def datos(self):
        return f"{self.fecha.strftime('%d/%m/%Y')}: {self.temperatura}°C"
    

class AVL:
    #Constructir

    #def __init__(self, nodo):
     #   if not nodo:
      #      return 0
    # Construir
    def __init__(self, nodo=None):
        self.raiz = nodo
    
    #Devuelve altura
    def altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura
        
    #Devuelve Factor de eq
    def factor_eq(self,nodo): #agregar validaciones
        if not nodo:
            return 0
        return self.altura(nodo.izquierda) - self.altura(nodo.derecha)
    
    #Actualiza altura de los nodos
    def actualizar_altura(self, nodo):
        if not nodo: #Si el nodo es none
            return #No hacemos nada y salimos
    #Si el nodo SI existe, entonces:
        nodo.altura = 1 + max(self.altura(nodo.izquierda), self.altura(nodo.derecha))

    def rot_derecha(self, z): #Z es el nodo de arriba del todo pre rotación
        y = z.izquierda #Nueva raiz
        T2 = y.derecha

        #Rotación en si
        y.derecha = z
        z.izquierda = T2

        #Actualizamos alturas
        self.actualizar_altura(z)
        self.actualizar_altura(y)

        return y #Devuelvo la raiz nueva
    def rot_izquierda(self,z):
        y = z.derecha
        T2 = y.izquierda

        y.izquierda = z
        z.derecha = T2

        self.actualizar_altura(z)
        self.actualizar_altura(y)

        return y

    def rot_izq_der(self, z):
        z.izquierda = self.rot_izquierda(z.izquierda)
        return self.rot_derecha(z)

    def rot_der_izq(self, z):
        z.derecha = self.rot_derecha(z.derecha)
        return self.rot_izquierda(z)

    #Metodo publico de busquerda
    def buscar(self,fecha_obj:datetime.date):

        nodo_encontrado = self._buscar_nodo(self.raiz, fecha_obj)
        if nodo_encontrado:
            return nodo_encontrado.temperatura
        return None #Devuelve None si no se encuentra

    #Metodo privado de busqueda
    def _buscar_nodo(self, nodo_actual, fecha_obj):
        if not nodo_actual or nodo_actual.fecha == fecha_obj:
            return nodo_actual
        
        if fecha_obj < nodo_actual.fecha:
            return self._buscar_nodo(nodo_actual.izquierda, fecha_obj)
        else: #fecha_obj > nodo_actual.fecha
            return self._buscar_nodo(nodo_actual.derecha, fecha_obj)
        

    #Metodos del propio arbol, privado
    def _insertar(self, nodo_actual, fecha:datetime.date, temperatura:float):

        #Inseciones normales
        if not nodo_actual:
            return nodoAVL(fecha, temperatura)
        
        elif fecha > nodo_actual.fecha:
            nodo_actual.derecha = self._insertar(nodo_actual.derecha,fecha,temperatura)

        elif fecha < nodo_actual.fecha:
            nodo_actual.izquierda = self._insertar(nodo_actual.izquierda,fecha,temperatura)

        else:
            #Esto es paras las fechas duplicadas, actualizamos el valor de la temperatua
            nodo_actual.temperatura = temperatura
            return nodo_actual

        #PASO 2
        self.actualizar_altura(nodo_actual)
        #Obtenemos FE
        balance = self.factor_eq(nodo_actual)

        #Ahora dependiendo del valor del factor eq hacemos la rotacion correspondiente
        #Dos a la izquierda
        if balance > 1 and fecha < nodo_actual.izquierda.fecha:
            return self.rot_derecha(nodo_actual)
        
        #Dos a la derecha
        if balance < -1 and fecha > nodo_actual.derecha.fecha:
            return self.rot_izquierda(nodo_actual)
        
        #Izquierda y derecha
        if balance > 1 and fecha > nodo_actual.izquierda.fecha:
            nodo_actual.izquierda = self.rot_izquierda(nodo_actual.izquierda)
            return self.rot_derecha(nodo_actual)
        
        #Derecha e izquierda:
        if balance < -1 and fecha < nodo_actual.derecha.fecha:
            nodo_actual.derecha = self.rot_derecha(nodo_actual.derecha)
            return self.rot_izquierda(nodo_actual)

        return nodo_actual

    #Metodo publico de insersion
    def insertar(self,fecha:datetime.date, temperatura:float):
        self.raiz = self._insertar(self.raiz, fecha, temperatura)

    
    def obtener_rangos(self, fecha_inicio, fecha_fin):


        resultados = []
        self._obtener_rangos(self.raiz, fecha_inicio, fecha_fin, resultados)
        return resultados

    def _obtener_rangos(self, nodo, fecha_inicio, fecha_fin, resultados):

        if not nodo:
            return

        if fecha_inicio < nodo.fecha:
            self._obtener_rangos(nodo.izquierda, fecha_inicio, fecha_fin, resultados)


        if fecha_inicio <= nodo.fecha <= fecha_fin:
            resultados.append(nodo) # Guardamos el nodo completo para acceder a fecha y temperatura


        if fecha_fin > nodo.fecha:
            self._obtener_rangos(nodo.derecha, fecha_inicio, fecha_fin, resultados)

    
    def contar_nodos(self):
        return self._contar_nodos(self.raiz)

    def _contar_nodos(self, nodo):
        if not nodo:
            return 0
        return 1 + self._contar_nodos(nodo.izquierda) + self._contar_nodos(nodo.derecha)
    
    
    def eliminar(self, fecha: datetime.date):
        self.raiz = self._eliminar(self.raiz, fecha)
        
    def _eliminar(self, nodo, fecha):
        if not nodo:
            return nodo

        # 1. Búsqueda del nodo a eliminar
        if fecha < nodo.fecha:
            nodo.izquierda = self._eliminar(nodo.izquierda, fecha)
        elif fecha > nodo.fecha:
            nodo.derecha = self._eliminar(nodo.derecha, fecha)
        else:
            # Nodo encontrado
            
            # Caso A: Nodo con un solo hijo o sin hijos
            if nodo.izquierda is None:
                temp = nodo.derecha
                nodo = None
                return temp
            elif nodo.derecha is None:
                temp = nodo.izquierda
                nodo = None
                return temp

            # Caso B: Nodo con dos hijos
            # Obtenemos el sucesor in-order (el más pequeño del subárbol derecho)
            temp = self._nodo_minimo(nodo.derecha)
            
            # Copiamos los datos del sucesor
            nodo.fecha = temp.fecha
            nodo.temperatura = temp.temperatura
            
            # Eliminamos el sucesor
            nodo.derecha = self._eliminar(nodo.derecha, temp.fecha)

        if not nodo:
            return nodo

        # 2. Actualizar altura
        self.actualizar_altura(nodo)

        # 3. Balancear el árbol
        balance = self.factor_eq(nodo)

        # Caso 1: Izquierda - Izquierda
        if balance > 1 and self.factor_eq(nodo.izquierda) >= 0:
            return self.rot_derecha(nodo)

        # Caso 2: Izquierda - Derecha
        if balance > 1 and self.factor_eq(nodo.izquierda) < 0:
            nodo.izquierda = self.rot_izquierda(nodo.izquierda)
            return self.rot_derecha(nodo)

        # Caso 3: Derecha - Derecha
        if balance < -1 and self.factor_eq(nodo.derecha) <= 0:
            return self.rot_izquierda(nodo)

        # Caso 4: Derecha - Izquierda
        if balance < -1 and self.factor_eq(nodo.derecha) > 0:
            nodo.derecha = self.rot_derecha(nodo.derecha)
            return self.rot_izquierda(nodo)

        return nodo
        
    def _nodo_minimo(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual