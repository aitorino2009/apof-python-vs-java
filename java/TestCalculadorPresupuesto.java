/**
 * Suite de verificación para el cálculo de catering en Java.
 * Ejecutable directamente con: java java/TestCalculadorPresupuesto.java
 */

double calcularCatering(double invitados) {
    var costePorInvitado = 25.50;
    var costeFijoGestion = 50.00;
    return (invitados * costePorInvitado) + costeFijoGestion;
}

void assertAlmostEqual(String descripcion, double obtenido, double esperado) {
    var delta = 0.0001;
    if (Math.abs(obtenido - esperado) <= delta) {
        System.out.println("  [OK] " + descripcion + " -> Obtenido: " + obtenido + " €");
    } else {
        System.err.println("  [FALLO] " + descripcion + " -> Obtenido: " + obtenido + ", Esperado: " + esperado);
        System.exit(1);
    }
}

void main() {
    System.out.println("Ejecutando pruebas unitarias de Java...");

    assertAlmostEqual("0 invitados (solo coste fijo)", calcularCatering(0), 50.00);
    assertAlmostEqual("1 invitado (25.50 + 50.00)", calcularCatering(1), 75.50);
    assertAlmostEqual("10 invitados (255.00 + 50.00)", calcularCatering(10), 305.00);
    assertAlmostEqual("20 invitados (510.00 + 50.00)", calcularCatering(20), 560.00);
    assertAlmostEqual("100 invitados (2550.00 + 50.00)", calcularCatering(100), 2600.00);
    assertAlmostEqual("10.5 invitados (267.75 + 50.00)", calcularCatering(10.5), 317.75);

    System.out.println("Todas las pruebas de Java pasaron exitosamente.");
}
