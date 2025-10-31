#el modulo lista de listas esta compuesto por listas de python

class ListsBinario:
    def __init__(self):
        self.listsbase = [0]
        self.tamanioActual = 0


    def infiltArriba(self,i):
        while i // 2 > 0:
          if self.listsbase[i] < self.listsbase[i // 2]:
             tmp = self.listsbase[i // 2]
             self.listsbase[i // 2] = self.listsbase[i]
             self.listsbase[i] = tmp
          i = i // 2

    def insertar(self,k):
      self.listsbase.append(k)

      self.tamanioActual = self.tamanioActual + 1
      self.infiltArriba(self.tamanioActual) 

    def infiltAbajo(self,i):
      while (i * 2) <= self.tamanioActual:
          hm = self.hijoMin(i)
          if self.listsbase[i] > self.listsbase[hm]:
              tmp = self.listsbase[i]
              self.listsbase[i] = self.listsbase[hm]
              self.listsbase[hm] = tmp
          i = hm

    def hijoMin(self,i):
      if i * 2 + 1 > self.tamanioActual:
          return i * 2
      else:
          if self.listsbase[i*2] < self.listsbase[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def eliminarMin(self):
      valorSacado = self.listsbase[1]
      self.listsbase[1] = self.listsbase[self.tamanioActual]
      self.tamanioActual = self.tamanioActual - 1
      self.listsbase.pop()
      self.infiltAbajo(1)
      return valorSacado

    def construirlists(self,unaLista):
      i = len(unaLista) // 2
      self.tamanioActual = len(unaLista)
      self.listsbase = [0] + unaLista[:]
      while (i > 0):
          self.infiltAbajo(i)
          i = i - 1

    def __len__(self):
        return self.tamanioActual

    def __bool__(self):
        return self.tamanioActual > 0

    