import java.util.Scanner;
import java.util.Locale;

/**
 * Desafío de Programación: El Calculador de Presupuesto para Eventos
 * Módulo: APOF - Comparativa Python vs Java
 *
 * Implementación en Java 21+ empleando:
 * - Unnamed Classes & Instance Main Methods (JEP 445 / 463 / 477 - Top-Level Statements).
 * - Métodos declarados directamente a nivel de archivo.
 * - Inferencia estática de tipos con 'var' para variables locales.
 * - Delimitación explícita de bloques mediante llaves { }.
 * - Captura de datos con Scanner (scanner.nextDouble()).
 * - Formateo de salida con System.out.println().
 */

/**
 * Calcula el coste total del catering para un número determinado de invitados.
 *
 * @param invitados Cantidad de personas (entero o decimal) que asistirán al evento.
 * @return El coste total calculado en euros (€).
 */
double calcularCatering(double invitados) {
    var costePorInvitado = 25.50;
    var costeFijoGestion = 50.00;

    var costeTotal = (invitados * costePorInvitado) + costeFijoGestion;
    return costeTotal;
}

/**
 * Solicita el número de asistentes por consola, captura la entrada desde el teclado
 * y la retorna convertida a un número decimal válido (double).
 *
 * @return El número de asistentes introducido por el usuario.
 */
double pedirInvitados() {
    var scanner = new Scanner(System.in);
    System.out.print("Introduce el número de asistentes al evento: ");

    // Se utiliza scanner.nextDouble() para la lectura del valor numérico
    if (scanner.hasNextDouble()) {
        return scanner.nextDouble();
    } else {
        // Soporte robusto ante variaciones de separador decimal (coma o punto)
        var entrada = scanner.next().replace(",", ".");
        return Double.parseDouble(entrada);
    }
}

/**
 * Flujo principal del programa:
 * 1. Muestra el mensaje inicial de presupuesto.
 * 2. Solicita el número de asistentes mediante pedirInvitados().
 * 3. Calcula el total mediante calcularCatering().
 * 4. Imprime el resultado formateado mediante System.out.println().
 */
void main() {
    System.out.println("--- Inicio del cálculo de presupuesto ---");

    var invitados = pedirInvitados();
    var presupuestoTotal = calcularCatering(invitados);

    System.out.println(String.format(Locale.US, "El presupuesto total es: %.2f €", presupuestoTotal));
}
