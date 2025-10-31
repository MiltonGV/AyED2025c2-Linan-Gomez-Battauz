import unittest
from modules.grafo import Grafo
from modules.vertice import Vertice

class TestGrafo(unittest.TestCase):
    def setUp(self):
        self.g = Grafo()
        
        # Agregar algunos vértices y aristas
        self.g.agregarVertice("A")
        self.g.agregarVertice("B")
        self.g.agregarArista("A", "B", 5)
        self.g.agregarArista("B", "C", 10)  # C se creará automáticamente

    def test_agregar_vertice(self):
        """Verifica agregar vértices individuales"""
        self.assertIn("A", self.g)
        self.assertIn("B", self.g)
        self.assertEqual(len(self.g), 3)  # A, B, C
        
        # Verificar objeto vertice
        vertice_a = self.g.obtenerVertice("A")
        self.assertIsInstance(vertice_a, Vertice)
        self.assertEqual(vertice_a.obtenerId(), "A")

    def test_agregar_arista(self):
        """Verifica agregar conexiones entre vértices"""
        # Verificar conexión A-B
        vertice_a = self.g.obtenerVertice("A")
        conexiones_a = [v.obtenerId() for v in vertice_a.obtenerConexiones()]
        self.assertIn("B", conexiones_a)
        self.assertEqual(vertice_a.obtenerPonderacion(self.g.obtenerVertice("B")), 5)
        
        # Verificar conexión B-C
        vertice_b = self.g.obtenerVertice("B")
        conexiones_b = [v.obtenerId() for v in vertice_b.obtenerConexiones()]
        self.assertIn("C", conexiones_b)
        self.assertEqual(vertice_b.obtenerPonderacion(self.g.obtenerVertice("C")), 10)
        
        # Verificar creación automática de vértices
        self.g.agregarArista("C", "D", 15)
        self.assertIn("D", self.g)
        self.assertEqual(len(self.g), 4)

    def test_conexiones_bidireccionales(self):
        """Verifica que las conexiones sean bidireccionales"""
        # A debe estar conectado con B y viceversa
        vertice_a = self.g.obtenerVertice("A")
        vertice_b = self.g.obtenerVertice("B")
        
        self.assertIn(vertice_b, vertice_a.obtenerConexiones())
        self.assertIn(vertice_a, vertice_b.obtenerConexiones())

    def test_obtener_vertices(self):
        """Verifica la lista de vértices"""
        vertices = list(self.g.obtenerVertices())
        self.assertCountEqual(vertices, ["A", "B", "C"])
        
        # Agregar nuevo vértice
        self.g.agregarVertice("D")
        self.assertIn("D", self.g.obtenerVertices())

    def test_vertice_inexistente(self):
        """Verifica manejo de vértices no existentes"""
        self.assertIsNone(self.g.obtenerVertice("X"))
        self.assertNotIn("X", self.g)

    def test_iterador_vertices(self):
        """Verifica iteración sobre vértices"""
        ids = [v.obtenerId() for v in self.g]
        self.assertCountEqual(ids, ["A", "B", "C"])

    def test_ponderaciones(self):
        """Verifica almacenamiento correcto de pesos"""
        # Agregar arista con peso diferente
        self.g.agregarArista("A", "C", 7)
        
        vertice_a = self.g.obtenerVertice("A")
        vertice_c = self.g.obtenerVertice("C")
        
        self.assertEqual(vertice_a.obtenerPonderacion(vertice_c), 7)
        self.assertEqual(vertice_c.obtenerPonderacion(vertice_a), 7)

if __name__ == "__main__":
    unittest.main()