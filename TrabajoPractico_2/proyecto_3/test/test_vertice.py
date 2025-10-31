import unittest
from modules.vertice import Vertice

class TestVertice(unittest.TestCase):
    def setUp(self):
        # Crear vértices para pruebas
        self.vertice_a = Vertice("A")
        self.vertice_b = Vertice("B")
        self.vertice_c = Vertice("C")
        
        # Establecer conexiones
        self.vertice_a.agregarVecino(self.vertice_b, 5)
        self.vertice_a.agregarVecino(self.vertice_c, 8)
        self.vertice_b.agregarVecino(self.vertice_c, 3)

    def test_inicializacion(self):
        """Verifica creación correcta de vértices"""
        self.assertEqual(self.vertice_a.obtenerId(), "A")
        self.assertEqual(self.vertice_b.obtenerId(), "B")
        self.assertEqual(self.vertice_c.obtenerId(), "C")

    def test_agregar_vecino(self):
        """Verifica agregar conexiones entre vértices"""
        # Verificar conexiones del vértice A
        conexiones_a = list(self.vertice_a.obtenerConexiones())
        self.assertIn(self.vertice_b, conexiones_a)
        self.assertIn(self.vertice_c, conexiones_a)
        self.assertEqual(len(conexiones_a), 2)
        
        # Verificar conexiones del vértice B
        conexiones_b = list(self.vertice_b.obtenerConexiones())
        self.assertIn(self.vertice_c, conexiones_b)
        self.assertEqual(len(conexiones_b), 1)

    def test_ponderaciones(self):
        """Verifica almacenamiento correcto de pesos"""
        self.assertEqual(self.vertice_a.obtenerPonderacion(self.vertice_b), 5)
        self.assertEqual(self.vertice_a.obtenerPonderacion(self.vertice_c), 8)
        self.assertEqual(self.vertice_b.obtenerPonderacion(self.vertice_c), 3)
        
        # Verificar actualización de peso
        self.vertice_a.agregarVecino(self.vertice_b, 10)
        self.assertEqual(self.vertice_a.obtenerPonderacion(self.vertice_b), 10)

    def test_representacion_string(self):
        """Verifica representación en cadena"""
        self.assertEqual(
            str(self.vertice_a), 
            "A conectadoA: ['B', 'C']"  # O podría ser ['C', 'B'] dependiendo del orden
        )
        
        # Verificar que muestra IDs, no objetos
        self.assertIn("B", str(self.vertice_a))
        self.assertIn("C", str(self.vertice_a))
        self.assertNotIn("Vertice", str(self.vertice_a))

    def test_vecino_inexistente(self):
        """Verifica manejo de vecinos no conectados"""
        with self.assertRaises(KeyError):
            self.vertice_a.obtenerPonderacion(Vertice("D"))

    def test_conecciones_vacias(self):
        """Verifica vértice sin conexiones"""
        vertice_aislado = Vertice("X")
        self.assertEqual(len(list(vertice_aislado.obtenerConexiones())), 0)
        self.assertEqual(str(vertice_aislado), "X conectadoA: []")

if __name__ == "__main__":
    unittest.main()