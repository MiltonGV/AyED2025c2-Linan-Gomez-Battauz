# test_lists.py
import unittest
from modules.lists import ListsBinario

class TestListsBinario(unittest.TestCase):

    def setUp(self):
        """Configuración inicial para cada test"""
        self.heap = ListsBinario()

    def test_initialization(self):
        """Test de inicialización de ListsBinario"""
        self.assertEqual(self.heap.listsbase, [0])
        self.assertEqual(self.heap.tamanioActual, 0)
        self.assertEqual(len(self.heap), 0)
        self.assertFalse(bool(self.heap))

    def test_insert_single_element(self):
        """Test de inserción de un solo elemento"""
        self.heap.insertar(5)
        
        self.assertEqual(len(self.heap), 1)
        self.assertEqual(self.heap.listsbase, [0, 5])
        self.assertTrue(bool(self.heap))

    def test_insert_multiple_elements(self):
        """Test de inserción de múltiples elementos"""
        elements = [3, 1, 6, 5, 2, 4]
        
        for elem in elements:
            self.heap.insertar(elem)
        
        self.assertEqual(len(self.heap), len(elements))
        # Verificar propiedad de heap mínimo
        self.assertEqual(self.heap.listsbase[1], min(elements))

    def test_eliminar_min(self):
        """Test de eliminación del elemento mínimo"""
        elements = [3, 1, 6, 5, 2, 4]
        
        for elem in elements:
            self.heap.insertar(elem)
        
        min_element = self.heap.eliminarMin()
        self.assertEqual(min_element, 1)
        self.assertEqual(len(self.heap), len(elements) - 1)
        
        # Eliminar todos los elementos y verificar el orden
        sorted_elements = []
        while self.heap:
            sorted_elements.append(self.heap.eliminarMin())
        
        self.assertEqual(sorted_elements, [2, 3, 4, 5, 6])

    def test_construirlists(self):
        """Test de construcción de heap desde una lista"""
        lista = [9, 6, 5, 2, 3]
        self.heap.construirlists(lista)
        
        self.assertEqual(len(self.heap), len(lista))
        self.assertEqual(self.heap.listsbase[1], min(lista))
        
        # Verificar que elimina en orden correcto
        elementos_ordenados = []
        while self.heap:
            elementos_ordenados.append(self.heap.eliminarMin())
        
        self.assertEqual(elementos_ordenados, [2, 3, 5, 6, 9])

    def test_hijo_min(self):
        """Test del método hijoMin"""
        self.heap.construirlists([5, 3, 8, 1, 2])
        
        # En un heap [0, 1, 2, 8, 5, 3], el hijo mínimo de la posición 2 es 5
        self.assertEqual(self.heap.hijoMin(2), 4)

    def test_eliminar_min_heap_vacio(self):
        """Test de eliminación en heap vacío"""
        with self.assertRaises(IndexError):
            self.heap.eliminarMin()

    def test_elementos_duplicados(self):
        """Test con elementos duplicados"""
        self.heap.insertar(5)
        self.heap.insertar(5)
        self.heap.insertar(5)
        
        self.assertEqual(len(self.heap), 3)
        self.assertEqual(self.heap.eliminarMin(), 5)
        self.assertEqual(self.heap.eliminarMin(), 5)
        self.assertEqual(self.heap.eliminarMin(), 5)
        self.assertEqual(len(self.heap), 0)

    def test_bool_representation(self):
        """Test de la representación booleana"""
        self.assertFalse(bool(self.heap))
        
        self.heap.insertar(1)
        self.assertTrue(bool(self.heap))
        
        self.heap.eliminarMin()
        self.assertFalse(bool(self.heap))

if __name__ == '__main__':
    unittest.main()