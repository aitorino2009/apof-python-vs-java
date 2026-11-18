"""
Desafío de Programación: El Calculador de Presupuesto para Eventos
Módulo: APOF - Comparativa Python vs Java

Implementación en Python siguiendo las mejores prácticas:
- PEP 8 (estilo de código, nomenclatura snake_case, indentación de 4 espacios).
- Type hints para verificación estática de tipos.
- Docstrings descriptivos en formato Google/Sphinx.
- Manejo robusto de entrada por teclado con reemplazo de separador decimal.
"""


def calcular_catering(invitados: float) -> float:
    """
    Calcula el coste total del catering según el número de asistentes.

    Parámetros:
        invitados (float | int): Cantidad de personas que asistirán al evento.

    Retorna:
        float: Coste total calculado en euros (€).
               Fórmula: (invitados * 25.50 €) + 50.00 € (coste fijo de gestión).
    """
    coste_por_invitado: float = 25.50
    coste_fijo_gestion: float = 50.00

    coste_total: float = (invitados * coste_por_invitado) + coste_fijo_gestion
    return coste_total


def pedir_invitados() -> float:
    """
    Solicita al usuario por consola el número de asistentes, captura la
    entrada mediante el teclado y la retorna convertida a float.

    Retorna:
        float: Número de asistentes como valor numérico decimal.
    """
    entrada_usuario: str = input("Introduce el número de asistentes al evento: ")
    # Normalizamos posibles comas introducidas por el usuario a puntos decimales
    valor_normalizado: str = entrada_usuario.strip().replace(",", ".")
    return float(valor_normalizado)


def main() -> None:
    """
    Flujo principal de la aplicación:
    1. Muestra el mensaje inicial de cálculo.
    2. Solicita el número de asistentes llamando a pedir_invitados().
    3. Calcula el importe llamando a calcular_catering().
    4. Muestra por consola el resultado con formato de dos decimales y símbolo €.
    """
    print("--- Inicio del cálculo de presupuesto ---")
    invitados: float = pedir_invitados()
    presupuesto_total: float = calcular_catering(invitados)
    print(f"El presupuesto total es: {presupuesto_total:.2f} €")


if __name__ == "__main__":
    main()
