from random import randint, choices

nombres = ['Leandro','Mariela','Gastón','Andrea','Antonio','Estela','Jorge','Agustina']
apellidos = ['Perez','Colman','Rodriguez','Juarez','García','Belgrano','Mendez','Lopez']

niveles_de_riesgo = [1,2,3]
descripciones_de_riesgo = ['crítico','moderado','bajo']
probabilidades=[0.1, 0.3, 0.6]

class Paciente:
    def __init__(self, id_paciente=None, riesgo=None):  # CORREGIDO: parámetros correctos
        n = len(nombres)
        self.__nombre = nombres[randint(0, n-1)]
        self.__apellido = apellidos[randint(0, n-1)]
        self.__id = id_paciente if id_paciente is not None else randint(1000, 9999)
        
        if riesgo is not None and riesgo in niveles_de_riesgo:
            self.__riesgo = riesgo
        else:
            self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
            
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