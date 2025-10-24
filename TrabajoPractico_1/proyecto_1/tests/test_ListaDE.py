import unittest
from modules.ListaDobleEnlazada import ListaDobleEnlazada

class TestListaDobleEnlazada(unittest.TestCase):

    def setUp(self):
        self.lista = ListaDobleEnlazada()

    def test_lista_vacia(self):
        self.assertTrue(self.lista.esta_vacia())
        self.assertEqual(len(self.lista), 0)

    def test_agregar_al_inicio(self):
        self.lista.agregar_al_inicio(1)
        self.assertEqual(str(self.lista), "1")
        self.assertEqual(len(self.lista), 1)
        
        self.lista.agregar_al_inicio(2)
        self.assertEqual(str(self.lista), "2 <-> 1")
        self.assertEqual(len(self.lista), 2)

    def test_agregar_al_final(self):
        self.lista.agregar_al_final(1)
        self.assertEqual(str(self.lista), "1")
        self.assertEqual(len(self.lista), 1)
        
        self.lista.agregar_al_final(2)
        self.assertEqual(str(self.lista), "1 <-> 2")
        self.assertEqual(len(self.lista), 2)

    def test_insertar(self):
        # Insertar en lista vacía
        self.lista.insertar(1, 0)
        self.assertEqual(str(self.lista), "1")
        
        # Insertar al inicio
        self.lista.insertar(0, 0)
        self.assertEqual(str(self.lista), "0 <-> 1")
        
        # Insertar al final
        self.lista.insertar(3, 2)
        self.assertEqual(str(self.lista), "0 <-> 1 <-> 3")
        
        # Insertar en medio
        self.lista.insertar(2, 2)
        self.assertEqual(str(self.lista), "0 <-> 1 <-> 2 <-> 3")

    def test_extraer(self):
        self.lista.agregar_al_final(1)
        self.lista.agregar_al_final(2)
        self.lista.agregar_al_final(3)
        
        valor = self.lista.extraer()
        self.assertEqual(valor, 3)
        self.assertEqual(str(self.lista), "1 <-> 2")
        
        valor = self.lista.extraer(0)
        self.assertEqual(valor, 1)
        self.assertEqual(str(self.lista), "2")
        
        valor = self.lista.extraer(0)
        self.assertEqual(valor, 2)
        self.assertTrue(self.lista.esta_vacia())

    def test_copiar(self):
        self.lista.agregar_al_final(1)
        self.lista.agregar_al_final(2)
        self.lista.agregar_al_final(3)
        
        copia = self.lista.copiar()
        self.assertEqual(str(self.lista), str(copia))
        self.assertEqual(len(self.lista), len(copia))
        
        self.lista.agregar_al_final(4)
        self.assertEqual(str(self.lista), "1 <-> 2 <-> 3 <-> 4")
        self.assertEqual(str(copia), "1 <-> 2 <-> 3")

    def test_invertir(self):
        self.lista.agregar_al_final(1)
        self.lista.agregar_al_final(2)
        self.lista.agregar_al_final(3)
        
        self.lista.invertir()
        self.assertEqual(str(self.lista), "3 <-> 2 <-> 1")
        
        # Invertir de nuevo debería devolver a la original
        self.lista.invertir()
        self.assertEqual(str(self.lista), "1 <-> 2 <-> 3")

    def test_concatenar(self):
        lista1 = ListaDobleEnlazada()
        lista1.agregar_al_final(1)
        lista1.agregar_al_final(2)
        
        lista2 = ListaDobleEnlazada()
        lista2.agregar_al_final(3)
        lista2.agregar_al_final(4)
        
        lista1.concatenar(lista2)
        self.assertEqual(str(lista1), "1 <-> 2 <-> 3 <-> 4")
        self.assertEqual(len(lista1), 4)
        
        # Verificar que lista2 no fue modificada
        self.assertEqual(str(lista2), "3 <-> 4")

    def test_indices_invalidos(self):
        # Insertar en posición inválida
        with self.assertRaises(IndexError):
            self.lista.insertar(1, 5)
        
        with self.assertRaises(Exception):
            self.lista.extraer()
        
        self.lista.agregar_al_final(1)
        with self.assertRaises(IndexError):
            self.lista.extraer(5)

if __name__ == '__main__':
    unittest.main()