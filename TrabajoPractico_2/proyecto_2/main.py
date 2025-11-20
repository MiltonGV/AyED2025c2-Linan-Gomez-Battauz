from modules.temperatura_db import temperatura_db
import datetime

db = temperatura_db()

print("--- INICIO DEL PROGRAMA ---")

print("\n-- 1. Cargando muestras desde archivo --")

db.cargar_muestras_desde_archivo("muestras.txt")

# Como los datos empiezan el 01/01/2025
fecha_inicial = datetime.date(2025, 1, 1) 

# Definimos fechas que sabemos que existen o no
fecha_test1 = "01/01/2025"
fecha_test2 = "15/01/2025"
fecha_no_existente = "01/01/1990"
# -----------------------------------------

print("\n-- 2. Devolviendo Temperaturas Especificas --")

# Prueba 1
temp1 = db.devolver_temperatura(fecha_test1)
print(f"Temperatura para {fecha_test1}: {temp1}°C" if temp1 is not None else f"No se encontro temperatura para {fecha_test1}")

# Prueba 2
temp2 = db.devolver_temperatura(fecha_test2)
print(f"Temperatura para {fecha_test2}: {temp2}°C" if temp2 is not None else f"No se encontro temperatura para {fecha_test2}")

# Prueba No Existente
temp_no_existente = db.devolver_temperatura(fecha_no_existente)
print(f"Temperatura para {fecha_no_existente}: {temp_no_existente}°C" if temp_no_existente is not None else f"No se encontro temperatura para {fecha_no_existente}")
print("-" * 30)

print("\n -- 3. Temperaturas en Rango --")
# Definimos un rango usando la fecha_inicial que creamos arriba
# Rango: 03/01/2025 al 09/01/2025
rango_fecha_inicio = (fecha_inicial + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
rango_fecha_fin = (fecha_inicial + datetime.timedelta(days=8)).strftime('%d/%m/%Y')

max_rango = db.max_temp_rango(rango_fecha_inicio, rango_fecha_fin)
print(f"Temperatura maxima en rango [{rango_fecha_inicio} - {rango_fecha_fin}]: {max_rango}°C" if max_rango is not None else "No hay datos en el rango.")

min_rango = db.min_temp_rango(rango_fecha_inicio, rango_fecha_fin)
print(f"Temperatura minima en rango [{rango_fecha_inicio} - {rango_fecha_fin}]: {min_rango}°C" if min_rango is not None else "No hay datos en el rango.")

min_ext, max_ext = db.temp_extremos_rango(rango_fecha_inicio, rango_fecha_fin)
if min_ext is not None and max_ext is not None:
    print(f"Extremos (min, max) en rango [{rango_fecha_inicio} - {rango_fecha_fin}]: {min_ext}°C, {max_ext}°C")
else:
    print(f"No hay datos suficientes para extremos en el rango [{rango_fecha_inicio} - {rango_fecha_fin}].")
print("-" * 30)

print("\n --4. Devolver listado de temperaturas en rango --")
print(f"Temperaturas entre {rango_fecha_inicio} - {rango_fecha_fin} (ordenadas):")
lista_temps1 = db.devolver_temperaturas(rango_fecha_inicio, rango_fecha_fin)
if lista_temps1:
    for item in lista_temps1:
        print(item)
print("-" * 30)

print("\n --5. Cantidad de muestras --")
total_muestras_antes_borrado = db.cantidad_muestras()
print(f"Cantidad total de muestras antes del borrado: {total_muestras_antes_borrado}")
print("-" * 30)

print("\n --6. Borrando temperaturas --")
# Borramos una fecha (08/01/2025) que sabemos que existe
fecha_a_borrar = (fecha_inicial + datetime.timedelta(days=7)).strftime("%d/%m/%Y")
print(f"Intentando borrar temperatura de la fecha: {fecha_a_borrar}")

resultado_borrado = db.borrar_temperatura(fecha_a_borrar)
print(f"Resultado del borrado: {'Exitoso' if resultado_borrado else 'Fallo o no encontrado'}")

temp_despues_borrar = db.devolver_temperatura(fecha_a_borrar)
# Si devuelve None, es que se borró bien
print(f"Verificacion: Temp para {fecha_a_borrar}: {temp_despues_borrar}" if temp_despues_borrar is not None else f"Verificacion: No se encontro temperatura para {fecha_a_borrar} (borrado correcto)")
print("-" * 30)

print("\n --7. Cantidad de muestras despues del borrado: --")
total_muestras_desp_borrado = db.cantidad_muestras()
print(f"Cantidad total de muestras despues del borrado: {total_muestras_desp_borrado}")

if total_muestras_antes_borrado - 1 == total_muestras_desp_borrado:
    print("Verificacion de cantidad de muestras: Correcto")
else:
    print("Verificacion de cantidad de muestras: Incorrecta")
print("-" * 30)

print("\n --8. Prueba de guardar temperatura duplicada (actualizacion) --")
# Elegimos una fecha para actualizar (06/01/2025)
fecha_duplicada = (fecha_inicial + datetime.timedelta(days=5)).strftime('%d/%m/%Y')
temp_original = db.devolver_temperatura(fecha_duplicada)
print(f"Temperatura original para {fecha_duplicada}: {temp_original}°C")

db.guardar_temperatura(99.9, fecha_duplicada) # Actualizamos con una nueva temperatura
temp_actualizada = db.devolver_temperatura(fecha_duplicada)
print(f"Temperatura actualizada para {fecha_duplicada}: {temp_actualizada}°C")

if temp_actualizada == 99.9:
    print("Verificacion de actualizacion: Correcta.")
else:
    print("Verificacion de actualizacion: Incorrecta")

print("-"*30)

print("\n FIN DE LAS PRUEBAS")