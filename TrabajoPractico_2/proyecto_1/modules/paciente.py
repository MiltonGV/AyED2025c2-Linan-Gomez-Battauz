from random import randint, choices

#voy a ir analizando linea por linea de codigo.
#se crean dos listas para contener tanto nombres como apellidos de los distintos pacientes.

nombres = ['Leandro','Mariela','Gastón','Andrea','Antonio','Estela','Jorge','Agustina']
apellidos = ['Perez','Colman','Rodriguez','Juarez','García','Belgrano','Mendez','Lopez']

#Clasificamos los niveles de riesgo de cada uno de los pacientes

niveles_de_riesgo = [1,2,3]
descripciones_de_riesgo = ['crítico','moderado','bajo']

#Definimos las probabilidades de aparición de cada tipo de paciente
probabilidades=[0.1, 0.3, 0.6]

#Ahora si, se define la clase Paciente:

class Paciente:
    def __init__(self):
        n=len(nombres)
        self.__nombre = nombres[randint(0, n-1)]
        self.__apellido = apellidos[randint(0, n-1)]
        self.__riesgo = choices(niveles_de_riesgo,probabilidades)[0]
        self.__descripcion = descripciones_de_riesgo[self.__riesgo-1]

    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_riesgo(self):
        return self.__riesgo
    
    def get_descripcion_riesgo(self):
        return self.__descripcion
    
    def __str__(self):
        cad = self.__nombre + ' '
        cad += self.__apellido + '\t -->'
        cad += str(self.__riesgo) + '-' + self.__descripcion
        return cad