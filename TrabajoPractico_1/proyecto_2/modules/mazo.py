# mazo.py

from modules.LDE import ListaDobleEnlazada  # Importa la clase ListaDobleEnlazada

class DequeEmptyError(Exception):
    pass  # Define una excepción personalizada para cuando el mazo está vacío

from modules.LDE import ListaDobleEnlazada  # Importa la clase ListaDobleEnlazada

class DequeEmptyError(Exception):
    pass  # Define una excepción personalizada para cuando el mazo está vacío

class Mazo:
    def __init__(self):
        self._cartas = ListaDobleEnlazada()
    
    def __len__(self):
        """Devuelve la cantidad de cartas en el mazo"""
        return len(self._cartas)
    
    def poner_carta_arriba(self, carta):
        """Agrega una carta en la parte superior del mazo"""
        self._cartas.insertar_al_inicio(carta)
    
    def poner_carta_abajo(self, carta):
        """Agrega una carta en la parte inferior del mazo"""
        self._cartas.insertar_al_final(carta)
    
    def sacar_carta_arriba(self, mostrar=False):
        """Saca y devuelve la carta de la parte superior del mazo"""
        if len(self._cartas) == 0:
            raise DequeEmptyError("No hay cartas en el mazo")
        
        carta = self._cartas.eliminar_del_inicio()
        if mostrar:
            carta.visible = True
        return carta
    
    def sacar_carta_abajo(self, mostrar=False):
        """Saca y devuelve la carta de la parte inferior del mazo"""
        if len(self._cartas) == 0:
            raise DequeEmptyError("No hay cartas en el mazo")
        
        carta = self._cartas.eliminar_del_final()
        if mostrar:
            carta.visible = True
        return carta
    
    def __str__(self):
        """Representación en string del mazo"""
        if len(self._cartas) == 0:
            return "Mazo vacío"
        
        # Mostrar solo las primeras cartas para no saturar la salida
        resultado = "["
        nodo_actual = self._cartas.cabeza
        contador = 0
        max_cartas_mostrar = 5
        
        while nodo_actual and contador < max_cartas_mostrar:
            resultado += str(nodo_actual.dato) + ", "
            nodo_actual = nodo_actual.siguiente
            contador += 1
        
        if len(self._cartas) > max_cartas_mostrar:
            resultado += f"... ({len(self._cartas)} cartas)]"
        else:
            resultado = resultado.rstrip(", ") + "]"
        
        return resultado
    
    def __repr__(self):
        return str(self)