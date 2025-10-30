from modules.AVL import AVL
import datetime

class temperatura_db:
    def __init__(self):
        self.arbol_temperatura = AVL() #Creamos la instancia en si

    def _formato_fecha(self,fecha:str):
        fecha_obj = datetime.datetime.strptime(fecha, "%d/%m/%Y").date()
        if not isinstance(fecha_obj,datetime.date):
            raise(f"Error: El formato de la fecha '{fecha}' no es valido. Use 'dd/mm/aaaa'.")
        
        return fecha_obj


    def guardar_temperatura(self, temperatura, fecha):

        fecha_obj = self._formato_fecha(fecha)

        #Nos aseguramos de que sea un flotante, podriamos agregar algun seguro aca tambien.
        temperatura_float = float(temperatura)

        self.arbol_temperatura.insertar(fecha_obj, temperatura_float)
        return(print(f"Dato guardado/actualizado: {fecha_obj.strftime('%d/%m/%Y')} - {temperatura_float}°C"))
    
    def devolver_temperatura(self,fecha:str):

        fecha_obj = self._formato_fecha(fecha)
        temperatura_encontrada = self.arbol_temperatura.buscar(fecha_obj)

        if temperatura_encontrada is not None:
            return temperatura_encontrada
        else:
            #Opcional: imprimir un mensaje si no se encuentra la fecha.
            print(f"Información: No se encontró temperatura para la fecha {fecha}.")

    
    def max_temp_rango(self, fecha1, fecha2):
        fecha1_obj = self._formato_fecha(fecha1)
        fecha2_obj = self._formato_fecha(fecha2)

        #La fecha 1 debe ser mayor a la 2
        if fecha1_obj > fecha2_obj:
            print("Error en max_temp_rango: La fecha 1 debe ser anterior o igual a la fecha 2")
            return None
        
        #Obtengo todas las temperaturas.

        temperaturas = self.arbol_temperatura.obtener_rangos(fecha1_obj, fecha2_obj)

        if not temperaturas: #Si la lista está vacía
            return None
        
        return min(temperaturas)
    
    def temp_extremos_rango(self,fecha1, fecha2):
        fecha1_obj = self._formato_fecha(fecha1)
        fecha2_obj = self._formato_fecha(fecha2)

        #La fecha 1 debe ser mayor a la 2
        if fecha1_obj > fecha2_obj:
            print("Error en max_temp_rango: La fecha 1 debe ser anterior o igual a la fecha 2")
            return None
        
        #Obtengo todas las temperaturas

        temperaturas = self.arbol_temperatura.obtener_rango(fecha1_obj, fecha2_obj)

        if not temperaturas: #Si la lista está vacía
            return None
        
        temperatura_minima = min(temperaturas)
        temperatura_maxima = max(temperaturas)

        return(temperatura_maxima,temperatura_minima)
    
    def borrar_temperatura(self,fecha):
        fecha_obj = self._formato_fecha(fecha)

        temperatura = self.arbol_temperatura-buscar(fecha_obj)

        if temperatura is None:
            print(False)


        self.arbol_temperatura.eliminar(fecha_obj)

        return True

    def devolver_temperatura(self, fecha1, fecha2):
        fecha1_obj = self._formato_fecha(fecha1)
        fecha2_obj = self._formato_fecha(fecha2)

        if fecha1_obj > fecha2_obj:
            print("Error en devolver_temperaturas: La fecha1 debe ser anterior o igual a la fecha2")
            return None
        
        datos_encontrados = self.arbol_temperatura.obtener_datos_en_rango_orden(fecha1_obj, fecha2_obj)
        lista = []
        for fecha, temperatura in datos_encontrados:
            lista.append(f"{fecha.strftime('%d/%m/%Y'): {temperatura}}°C")

        if not lista:
            print(f"Información: No se encontraron temperaturas en el rango {fecha1} - {fecha2}.")

        return lista
    
    def cantidad_muestras(self):
        return self.arbol_temperatura.contar_nodos()