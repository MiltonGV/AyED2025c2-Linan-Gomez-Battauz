import random
lista = [random.randint(10000,99999) for _ in range(500)]
#lista = [5,1,2,3,6]
lista_test = lista

def quicksort(lis):
    if len(lis) <= 1:
        return lis
    pivot = lis[len(lis)//2]
    #print(pivot)
    lis_izq = [x for x in lis if x < pivot]
    #print(lis_izq)
    lis_med = [x for x in lis if x == pivot]
    #print(lis_med)
    lis_der = [x for x in lis if x > pivot]
    #print(lis_der)
    return quicksort(lis_izq) + lis_med + quicksort(lis_der)

lista_ordenada = quicksort(lista)
#print(lista_ordenada)

