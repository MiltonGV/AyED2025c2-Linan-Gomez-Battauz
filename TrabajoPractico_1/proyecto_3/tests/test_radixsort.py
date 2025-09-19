import unittest
import random
from modules.Radix_sort import radix_sort

class TestRadixSort(unittest.TestCase):

    def test_lista_random(self):
        lista = [random.randint(10000, 99999) for _ in range(500)]
        lista_ordenada = radix_sort(lista.copy())
        self.assertEqual(lista_ordenada, sorted(lista))

if __name__ == "__main__":
    unittest.main()
