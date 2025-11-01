# test_cola_de_prioridad.py
import unittest
from modules.cola_de_prioridad import ColaDePrioridad
from modules.paciente import Paciente

class TestColaDePrioridad(unittest.TestCase):

    def setUp(self):
        # Cola simple de enteros, donde la prioridad es el valor mismo (menor = más prioritario)
        self.cola = ColaDePrioridad()
        # Cola de pacientes, donde la prioridad depende del riesgo (menor riesgo = menor prioridad)
        self.cola_pacientes = ColaDePrioridad(clave=lambda p: p.get_riesgo())

    def test_encolar_y_desencolar_enteros(self):
        elementos = [5, 2, 8, 1, 3]
        for e in elementos:
            self.cola.encolar(e)

        resultado = [self.cola.desencolar() for _ in range(len(elementos))]
        self.assertEqual(resultado, sorted(elementos))

    def test_desencolar_de_cola_vacia(self):
        self.assertIsNone(self.cola.desencolar())

    def test_len(self):
        self.assertEqual(len(self.cola), 0)
        self.cola.encolar(10)
        self.assertEqual(len(self.cola), 1)
        self.cola.desencolar()
        self.assertEqual(len(self.cola), 0)

    def test_iterador(self):
        elementos = [4, 1, 7]
        for e in elementos:
            self.cola.encolar(e)
        lista_iterada = list(self.cola)
        self.assertCountEqual(lista_iterada, elementos)

    def test_encolar_pacientes_por_riesgo(self):
        # Riesgo más bajo = más prioritario
        p1 = Paciente(id_paciente=1, riesgo=3)  # bajo
        p2 = Paciente(id_paciente=2, riesgo=1)  # crítico
        p3 = Paciente(id_paciente=3, riesgo=2)  # moderado

        self.cola_pacientes.encolar(p1)
        self.cola_pacientes.encolar(p2)
        self.cola_pacientes.encolar(p3)

        # El primero en salir debe ser el de menor riesgo numérico
        primero = self.cola_pacientes.desencolar()
        self.assertEqual(primero.get_riesgo(), 1)

        segundo = self.cola_pacientes.desencolar()
        self.assertEqual(segundo.get_riesgo(), 2)

        tercero = self.cola_pacientes.desencolar()
        self.assertEqual(tercero.get_riesgo(), 3)

if __name__ == '__main__':
    unittest.main()
