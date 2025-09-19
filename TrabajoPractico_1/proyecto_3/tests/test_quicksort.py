import unittest
import random
from modules.Quicksort import quicksort

class TestQuicksort(unittest.TestCase):

    def test_lista_random(self):
        lista = [random.randint(10000, 99999) for _ in range(500)]
        lista_ordenada = quicksort(lista.copy())
        self.assertEqual(lista_ordenada, sorted(lista))

if __name__ == "__main__":
    unittest.main()
