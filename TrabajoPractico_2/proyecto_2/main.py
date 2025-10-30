from modules.temperatura_db import temperatura_db
import datetime
import random

db = temperatura_db()

#Las variables a configurar:

fecha_inicial = datetime.date(2023, 8, 1)
num_dias_a_generar = 15

#Ahora, probamos el algoritmo en si, normalmente se guardaria la fecha y su temperatura con el metodo correspondiente
temperaturas_a_guardar = [round(random.uniform(15.0, 35.0), 1) for i in range(num_dias_a_generar)] #Generamos una temperatura random entre al azar entre 15 y 35 para las pruebas