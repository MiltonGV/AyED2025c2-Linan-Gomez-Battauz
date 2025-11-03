# 🐍Sala de emergencias: Triaje

Breve descripción del proyecto:

Este proyecto aborda el problema de encontrar almacenar los pacientes conforme ingresan al centro de salud de modo tal que cuando se atiende un paciente siempre sea aquel cuyo nivel de riesgo es el más delicado en comparación con el resto de los pacientes que restan por ser atendidos. 
donde si dos pacientes poseen el mismo nivel de riesgo, adoptar un segundo criterio para seleccionar uno de ellos
Esto permite manejar correctamente el triaje que es un proceso que permite una gestión del riesgo clínico para poder manejar adecuadamente y con seguridad los flujos de pacientes cuando la demanda y las necesidades clínicas superan a los recursos.

---
## 🏗Arquitectura General

El codigo se compone de la siguiente forma:

Módulos Principales:

* paciente.py - Modelo de Datos
Define la clase Paciente con atributos: nombre, apellido, ID, nivel de riesgo (1-3) y descripción

Genera pacientes aleatorios con distribución probabilística:
Crítico (10%), Moderado (30%), Bajo (60%)

* lists.py - Estructura de Datos Base:

Implementa un min-heap binario (ListsBinario)
Operaciones esenciales: insertar, eliminarMin, infiltArriba, infiltAbajo
Sirve como base para la cola de prioridad

* cola_de_prioridad.py - Gestión de Prioridades

Implementa una cola de prioridad usando el heap de ListsBinario
Clave: prioridad basada en el riesgo del paciente (menor número = mayor prioridad)
Maneja empates usando un contador de llegada

* main.py - Simulador Principal
Ejecuta la simulación con n ciclos

En cada ciclo:

Genera un nuevo paciente aleatorio, con 50% de probabilidad atiende al paciente más prioritario ymuestra el estado de la cola

## 📑Dependencias

1. **Python 3.x**
2. **matplotlib** (`pip install matplotlib`)


---
## 🚀Cómo Ejecutar el Proyecto
1. **Clonar o descargar** el repositorio.

2. **Crear y activar** un entorno virtual.

3. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
   El archivo `requirements.txt` se encuentran en la carpeta [deps](./deps) del proyecto.

---
## 🙎‍♀️🙎‍♂️Autores

- Gomez Villon Milton
- Pedro Battauz
- Juan Linan

---

