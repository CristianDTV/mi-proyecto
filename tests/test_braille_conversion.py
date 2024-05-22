import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.braille_conversion import texto_a_braille

class TestBrailleConversion(unittest.TestCase):
    def test_basic_conversion(self):
        """Testea la conversión básica de caracteres alfabéticos a braille."""
        self.assertEqual(texto_a_braille('a'), '⠁')
        self.assertEqual(texto_a_braille('b'), '⠃')
        self.assertEqual(texto_a_braille('c'), '⠉')

    def test_string_conversion(self):
        """Testea la conversión de cadenas completas a braille."""
        self.assertEqual(texto_a_braille('abc'), '⠁⠃⠉')
        self.assertEqual(texto_a_braille('hello'), '⠓⠑⠇⠇⠕')

    def test_uppercase_conversion(self):
        """Testea la conversión de mayúsculas, que deberían incluir el indicador de mayúscula en braille."""
        self.assertEqual(texto_a_braille('A'), '⠨⠁')
        self.assertEqual(texto_a_braille('ABC'), '⠨⠁⠨⠃⠨⠉')

    def test_non_mapped_characters(self):
        """Testea la conversión de caracteres que no están mapeados, los cuales deberían retornar un espacio."""
        self.assertEqual(texto_a_braille('123'), '⠼⠁⠼⠃⠼⠉')  # Suponiendo que los números siguen un mapeo estándar en braille
        self.assertEqual(texto_a_braille('@#$'), '   ')  # Caracteres como @#$ no están mapeados

    def test_space_handling(self):
        """Testea que los espacios sean manejados correctamente."""
        self.assertEqual(texto_a_braille('a b c'), '⠁ ⠃ ⠉')

if __name__ == '__main__':
    unittest.main()
