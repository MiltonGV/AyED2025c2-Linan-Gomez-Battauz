import random
lista = [random.randint(10000,99999) for _ in range(500)]

lista_test = lista

def BubbleSort(lis):
    n = len(lis)
    for i in range(n-1):
        for j in range(n-i-1):
            if lis[j] > lis[j+1]:
                lis[j],lis[j+1] = lis[j+1],lis[j]
    return lis

lista_nueva = BubbleSort(lista)
#print(lista_nueva)

