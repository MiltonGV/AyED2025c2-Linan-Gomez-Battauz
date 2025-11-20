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
        # Convertir strings a objetos fecha
        f1 = datetime.datetime.strptime(fecha1, "%d/%m/%Y").date()
        f2 = datetime.datetime.strptime(fecha2, "%d/%m/%Y").date()
        
        # Obtenemos la lista de NODOS 
        lista_nodos = self.arbol_temperatura.obtener_rangos(f1, f2)
        
        if not lista_nodos:
            return None
            
        # CREAMOS UNA LISTA SOLO CON LOS NUMEROS 
        lista_valores = [nodo.temperatura for nodo in lista_nodos]
        
        return max(lista_valores)

    def min_temp_rango(self, fecha1, fecha2):
        f1 = datetime.datetime.strptime(fecha1, "%d/%m/%Y").date()
        f2 = datetime.datetime.strptime(fecha2, "%d/%m/%Y").date()
        
        lista_nodos = self.arbol_temperatura.obtener_rangos(f1, f2)
        
        if not lista_nodos:
            return None
            
        # CREAMOS UNA LISTA SOLO CON LOS NUMEROS (FLOAT)
        lista_valores = [nodo.temperatura for nodo in lista_nodos]
        
        return min(lista_valores)

    def temp_extremos_rango(self, fecha1, fecha2):
        f1 = datetime.datetime.strptime(fecha1, "%d/%m/%Y").date()
        f2 = datetime.datetime.strptime(fecha2, "%d/%m/%Y").date()
        
        lista_nodos = self.arbol_temperatura.obtener_rangos(f1, f2)
        
        if not lista_nodos:
            return None, None # Retornamos dos Nones
            
        lista_valores = [nodo.temperatura for nodo in lista_nodos]
        
        return min(lista_valores), max(lista_valores)
    
    def borrar_temperatura(self, fecha: str):
        fecha_obj = datetime.datetime.strptime(fecha, "%d/%m/%Y").date()
        
        #Primero verificamos si existe el dato para saber si podemos borrarlo
        if self.arbol_temperatura.buscar(fecha_obj) is None:
            return False # No existe, devolvemos False
            
        # Si existe, llamamos al método eliminar del AVL
        self.arbol_temperatura.eliminar(fecha_obj)
        
        #Devolvemos True para indicar que el borrado fue exitoso
        return True

    def devolver_temperaturas(self, fecha1, fecha2):
        f1 = datetime.datetime.strptime(fecha1, "%d/%m/%Y").date()
        f2 = datetime.datetime.strptime(fecha2, "%d/%m/%Y").date()
        
        lista_nodos = self.arbol_temperatura.obtener_rangos(f1, f2)
        

        lista_formateada = [nodo.datos() for nodo in lista_nodos]
        
        return lista_formateada
    
    def cantidad_muestras(self):
        return self.arbol_temperatura.contar_nodos()
    
    def cargar_muestras_desde_archivo(self, nombre_archivo):

        try:
            with open(nombre_archivo, "r") as archivo:
                contador = 0
                for linea in archivo:
                    linea = linea.strip() # Eliminar espacios en blanco al inicio/final
                    if not linea:
                        continue # Saltar líneas vacías
                    
                    try:
                        # Separamos por punto y coma ';' según tu archivo muestras.txt
                        partes = linea.split(';') 
                        if len(partes) != 2:
                            continue # Si la línea no tiene 2 partes, la saltamos
                        
                        fecha_str = partes[0]
                        temperatura = float(partes[1])
                        
                        # Usamos el método guardar que ya creaste
                        self.guardar_temperatura(temperatura, fecha_str)
                        contador += 1
                        
                    except ValueError:
                        print(f"Error al procesar la línea: {linea}")
                        continue
                        
            print(f"--> Carga exitosa: Se cargaron {contador} muestras desde '{nombre_archivo}'.")
            
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo '{nombre_archivo}'.")