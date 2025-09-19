import unittest
import random
from modules.BubbleSort import BubbleSort

class TestBubbleSort(unittest.TestCase):

    def test_lista_random(self):
        lista = [random.randint(10000, 99999) for _ in range(500)]
        lista_nueva = BubbleSort(lista.copy())
        self.assertEqual(lista_nueva, sorted(lista))

if __name__ == "__main__":
    unittest.main()
