from modules.lists import ListsBinario
import itertools

class ColaDePrioridad:
    def __init__(self, clave=None):
        self.lists = ListsBinario()
        self._counter = itertools.count()
        self.clave = clave or (lambda x: x)  # Función para obtener prioridad

    def encolar(self, elemento):
        prioridad = self.clave(elemento)
        llegada = next(self._counter)
        self.lists.insertar((prioridad, llegada, elemento))

    def desencolar(self):
        if not self.lists:
            return None
        return self.lists.eliminarMin()[2]  

    def __len__(self):
        return len(self.lists)

    def __iter__(self):
        return iter(item[2] for item in self.lists.listsbase[1:self.lists.tamanioActual+1])