"""
Tests unitarios para la solución en Python del Calculador de Presupuesto.
Utiliza el framework estándar unittest.
"""

import unittest
from unittest.mock import patch
from calculador_presupuesto import calcular_catering, pedir_invitados


class TestCalculadorPresupuesto(unittest.TestCase):

    def test_calcular_catering_cero_invitados(self):
        """0 invitados solo debe pagar el coste fijo de gestión (50.00 €)."""
        resultado = calcular_catering(0)
        self.assertAlmostEqual(resultado, 50.00, places=2)

    def test_calcular_catering_un_invitado(self):
        """1 invitado: 1 * 25.50 + 50.00 = 75.50 €."""
        resultado = calcular_catering(1)
        self.assertAlmostEqual(resultado, 75.50, places=2)

    def test_calcular_catering_diez_invitados(self):
        """10 invitados: 10 * 25.50 + 50.00 = 305.00 €."""
        resultado = calcular_catering(10)
        self.assertAlmostEqual(resultado, 305.00, places=2)

    def test_calcular_catering_cien_invitados(self):
        """100 invitados: 100 * 25.50 + 50.00 = 2600.00 €."""
        resultado = calcular_catering(100)
        self.assertAlmostEqual(resultado, 2600.00, places=2)

    def test_calcular_catering_decimal(self):
        """10.5 asistentes (promedio/fracción): 10.5 * 25.50 + 50.00 = 317.75 €."""
        resultado = calcular_catering(10.5)
        self.assertAlmostEqual(resultado, 317.75, places=2)

    @patch("builtins.input", return_value="25")
    def test_pedir_invitados_entero(self, mock_input):
        """Comprueba lectura y conversión de un entero como string."""
        self.assertEqual(pedir_invitados(), 25.0)

    @patch("builtins.input", return_value="15.5")
    def test_pedir_invitados_decimal_punto(self, mock_input):
        """Comprueba lectura y conversión con punto decimal."""
        self.assertEqual(pedir_invitados(), 15.5)

    @patch("builtins.input", return_value="15,5")
    def test_pedir_invitados_decimal_coma(self, mock_input):
        """Comprueba normalización de coma decimal a punto."""
        self.assertEqual(pedir_invitados(), 15.5)


if __name__ == "__main__":
    unittest.main()
