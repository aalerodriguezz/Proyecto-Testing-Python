import unittest
from app.modulo1.funciones import esPalindromo

class TestPalindromo(unittest.TestCase):
    

    def test_palabras_simples(self):
        """Prueba palabras básicas que son palíndromas."""
        self.assertTrue(esPalindromo("ana"))
        self.assertTrue(esPalindromo("radar"))
        self.assertTrue(esPalindromo("reconocer"))

    def test_frases_complejas(self):
        """Prueba frases con espacios, mayúsculas y puntuación."""
        self.assertTrue(esPalindromo("A ti no, bonita"))
        self.assertTrue(esPalindromo("Amad a la dama"))
        self.assertTrue(esPalindromo("No traces en ese cartón"))

    def test_tildes_y_dieresis(self):
        """Prueba la correcta eliminación de tildes y diéresis."""
        self.assertTrue(esPalindromo("Ánita lava la tina"))
        self.assertTrue(esPalindromo("Dábale arroz a la zorra el abad"))
        self.assertTrue(esPalindromo("Lügar a ragül")) 

    def test_no_palindromos(self):
   
        self.assertFalse(esPalindromo("python"))
        self.assertFalse(esPalindromo("esto no es un palindromo"))
        self.assertFalse(esPalindromo("ciberseguridad"))

    def test_cadenas_vacias(self):
        
        self.assertTrue(esPalindromo(""))
        self.assertTrue(esPalindromo("   "))
        self.assertTrue(esPalindromo("... ,,, ..."))

    def test_numeros(self):
        """Prueba con enteros y flotantes (conversión implícita)."""
        self.assertTrue(esPalindromo(12321))
        self.assertTrue(esPalindromo(11.11)) 
        self.assertFalse(esPalindromo(123))

    def test_tipos_invalidos(self):
        """Prueba robustez ante tipos que romperían un script normal."""
        self.assertFalse(esPalindromo(None))
        self.assertFalse(esPalindromo(["a", "n", "a"])) 
        self.assertFalse(esPalindromo({"clave": "valor"})) 
        
    def test_parametrizado(self):
        """Prueba masiva usando una lista de tuplas (input, esperado)."""
        casos = [
            ("Somos o no somos", True),
            ("Yo hago yoga hoy", True),
            ("Isaac no ronca así", True),
            ("123456", False),
            ("@#!!#@", True) 
        ]
        for cadena, resultado_esperado in casos:
            with self.subTest(cadena=cadena):
                self.assertEqual(esPalindromo(cadena), resultado_esperado)

if __name__ == '__main__':
    unittest.main()
