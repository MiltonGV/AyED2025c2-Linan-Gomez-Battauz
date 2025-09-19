import random
lista = [random.randint(10000,99999) for _ in range(500)]
#lista = [31552,49899]
lista_test_prueba = sorted(lista)

#Dividimos en unidades, decenas, centenas...
def radix_sort (lista):
    unidad = 1 #Empezamos en las unidades    
    
    #5 digitos por numero en la lista
    for i in range(5):
        contenedores  = [[] for i in range (10)] #Diez contenedores (0-9)
        
        #Distribuimos los numeros en los contenedores
        for numero in lista:
            indice = (numero // unidad) % 10 #Extraemos el digito
            contenedores[indice].append(numero) #Ordeno cada numero en su contenedor correspondiente 
            
        #Armo la lista de nuevo con el orden obtenido de los contenedores
        lista = []
        for contenedor in contenedores:
            lista.extend(contenedor)
            
        
        unidad *=10
         
    return lista 
        

lista_ordenada = (radix_sort(lista))

