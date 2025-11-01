# test_lists.py
import unittest
from modules.lists import ListsBinario

class TestListsBinario(unittest.TestCase):

    def setUp(self):
        self.heap = ListsBinario()

    def test_insertar_y_eliminarMin(self):
        elementos = [5, 9, 3, 7, 1]
        for e in elementos:
            self.heap.insertar(e)
        # Debe devolver el menor elemento primero
        resultado = [self.heap.eliminarMin() for _ in range(len(elementos))]
        self.assertEqual(resultado, sorted(elementos))

    def test_construirlists(self):
        datos = [9, 5, 6, 2, 3]
        self.heap.construirlists(datos)
        resultado = [self.heap.eliminarMin() for _ in range(len(datos))]
        self.assertEqual(resultado, sorted(datos))

    def test_len_y_bool(self):
        self.assertEqual(len(self.heap), 0)
        self.assertFalse(bool(self.heap))
        self.heap.insertar(10)
        self.assertEqual(len(self.heap), 1)
        self.assertTrue(bool(self.heap))

    def test_hijoMin(self):
        self.heap.construirlists([4, 7, 9, 10, 8])
        self.assertEqual(self.heap.hijoMin(1), 2)
        self.assertEqual(self.heap.hijoMin(2), 5)


    def test_eliminarMin_en_heap_vacio(self):
        # No debería lanzar excepción si se maneja correctamente
        self.heap.insertar(1)
        self.heap.eliminarMin()
        self.assertEqual(len(self.heap), 0)
        with self.assertRaises(IndexError):
            self.heap.eliminarMin()  # No hay más elementos

if __name__ == '__main__':
    unittest.main()
