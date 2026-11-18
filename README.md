# 🎯 Desafío de Programación: El Calculador de Presupuesto para Eventos

[![CI - Verificación de Soluciones Python vs Java](https://github.com/aitorino2009/apof-python-vs-java/actions/workflows/ci.yml/badge.svg)](https://github.com/aitorino2009/apof-python-vs-java/actions/workflows/ci.yml)

Repositorio oficial para el desafío de programación del módulo **APOF**: Comparativa práctica y estudio de diferencias sintácticas entre **Python** y **Java 21+** (*usando Top-Level Statements / Unnamed Classes*).

---

## 📌 Contexto del Negocio

Una empresa de eventos necesita una aplicación ágil y precisa para calcular los costes básicos de contratación de catering en función del número de asistentes.

### Reglas de Tarificación:
- **Coste unitario por invitado:** `25.50 €`
- **Coste fijo de gestión:** `50.00 €`
- **Fórmula de cálculo:**
  $$\text{Presupuesto Total} = (\text{invitados} \times 25.50) + 50.00$$

---

## 📋 Checklist de Evaluación para el Alumno

| Requisito / Criterio | Estado | Python 🐍 | Java 21+ ☕ |
| :--- | :---: | :--- | :--- |
| **Límites de bloque correctos** | ✅ | Indentación con espacios (PEP 8, 4 espacios) | Delimitación explícita con llaves `{ }` |
| **Definición de funciones** | ✅ | Palabra reservada `def` y type hints (`float -> float`) | Firma con tipo de retorno estático (`double`) |
| **Captura de teclado** | ✅ | `input()` combinado con conversión explícita `float()` | Objeto `Scanner` y método `scanner.nextDouble()` |
| **Uso de Inferencia de Tipos** | ✅ | Tipado dinámico / variables locales implícitas | Empleo de `var` en Java Moderno en variables locales |
| **Salida por pantalla** | ✅ | `print()` con f-strings formateadas (`{presupuesto:.2f}`) | `System.out.println()` con formateo (`String.format()`) |
| **Punto de Entrada** | ✅ | Idiomático `if __name__ == "__main__": main()` | Top-Level Statement / Unnamed Class `void main()` |

---

## 🗂️ Estructura del Proyecto

```text
apof-python-vs-java/
├── .github/
│   └── workflows/
│       └── ci.yml                     # Pipeline CI (GitHub Actions) para Python y Java
├── .gitignore                         # Exclusiones de Git (binarios, caches, IDEs)
├── README.md                          # Documentación completa y comparativa técnica
├── python/
│   ├── calculador_presupuesto.py      # Solución en Python
│   └── test_calculador_presupuesto.py # Suite de pruebas unitarias (unittest)
└── java/
    ├── CalculadorPresupuesto.java     # Solución en Java 21+ (Unnamed Class)
    └── TestCalculadorPresupuesto.java # Suite de verificación con aserciones
```

---

## 🔍 Análisis Comparativo del Código

### 1. Definición de la función de cálculo

#### 🐍 Python
```python
def calcular_catering(invitados: float) -> float:
    coste_por_invitado: float = 25.50
    coste_fijo_gestion: float = 50.00
    coste_total: float = (invitados * coste_por_invitado) + coste_fijo_gestion
    return coste_total
```
* **Características:**
  - Sintaxis limpia y minimalista iniciada con `def`.
  - El bloque se delimita mediante `:` y un sangrado de 4 espacios.
  - Tipado anotado (`: float -> float`) para claridad y validación estática sin añadir sobrecarga en tiempo de ejecución.

#### ☕ Java 21+
```java
double calcularCatering(double invitados) {
    var costePorInvitado = 25.50;
    var costeFijoGestion = 50.00;
    var costeTotal = (invitados * costePorInvitado) + costeFijoGestion;
    return costeTotal;
}
```
* **Características:**
  - Método top-level sin necesidad de encapsularlo en una clase envolvente `public class`.
  - La firma especifica el tipo de retorno (`double`) y el tipo de parámetro (`double invitados`).
  - Empleo de la inferencia de tipos local `var` de Java moderno para evitar redundancia de tipos.
  - Bloque delimitado obligatoriamente por llaves `{ }` y sentencias finalizadas con `;`.

---

### 2. Captura de datos desde teclado

#### 🐍 Python
```python
def pedir_invitados() -> float:
    entrada_usuario: str = input("Introduce el número de asistentes al evento: ")
    valor_normalizado: str = entrada_usuario.strip().replace(",", ".")
    return float(valor_normalizado)
```
* `input()` lee la línea completa como cadena de texto (`str`).
* Se normaliza la coma decimal a punto antes de invocar `float()` para garantizar tolerancia a distintos formatos numéricos.

#### ☕ Java 21+
```java
double pedirInvitados() {
    var scanner = new Scanner(System.in);
    System.out.print("Introduce el número de asistentes al evento: ");

    if (scanner.hasNextDouble()) {
        return scanner.nextDouble();
    } else {
        var entrada = scanner.next().replace(",", ".");
        return Double.parseDouble(entrada);
    }
}
```
* Emplea `java.util.Scanner` conectado al flujo de entrada estándar `System.in`.
* Cumple el checklist utilizando `scanner.nextDouble()`.
* Incluye manejo adaptativo para aceptar tanto separador decimal por punto como por coma según la localización del sistema.

---

### 3. Flujo Principal y Salida por Pantalla

#### 🐍 Python
```python
def main() -> None:
    print("--- Inicio del cálculo de presupuesto ---")
    invitados: float = pedir_invitados()
    presupuesto_total: float = calcular_catering(invitados)
    print(f"El presupuesto total es: {presupuesto_total:.2f} €")

if __name__ == "__main__":
    main()
```
* Emplea `print()` con f-strings para formatear el resultado numérico a 2 decimales (`{presupuesto_total:.2f}`).

#### ☕ Java 21+
```java
void main() {
    System.out.println("--- Inicio del cálculo de presupuesto ---");

    var invitados = pedirInvitados();
    var presupuestoTotal = calcularCatering(invitados);

    System.out.println(String.format(Locale.US, "El presupuesto total es: %.2f €", presupuestoTotal));
}
```
* En Java 21+, el punto de entrada es directamente la función `void main()`.
* Uso intensivo de `var` para todas las variables locales (`invitados`, `presupuestoTotal`).
* Emplea `System.out.println()` junto con `String.format()` para un formateo consistente de moneda.

---

## 🚀 Guía de Ejecución

### Requisitos Previos
- **Python:** versión 3.10 o posterior instalada.
- **Java:** JDK 21 o posterior instalado (por ejemplo Java 21 LTS o Java 25 LTS).

### 🐍 Ejecutar la versión en Python
```bash
# Ejecutar aplicación interactiva
python python/calculador_presupuesto.py

# Ejecutar con valor simulado (ej. 10 invitados)
echo 10 | python python/calculador_presupuesto.py

# Ejecutar suite de pruebas unitarias
python -m unittest discover -s python -v
```

### ☕ Ejecutar la versión en Java 21+
```bash
# Ejecutar aplicación interactiva (Java 21+ ejecuta archivos fuente directamente)
java java/CalculadorPresupuesto.java

# En Java 21 (si se requiere bandera de preview explícita):
# java --enable-preview --source 21 java/CalculadorPresupuesto.java

# Ejecutar con valor simulado (ej. 10 invitados)
echo 10 | java java/CalculadorPresupuesto.java

# Ejecutar suite de verificación de Java
java java/TestCalculadorPresupuesto.java
```

---

## 🌿 Flujo de Trabajo en Git (Git Flow)

Este proyecto se desarrolló siguiendo buenas prácticas de control de versiones con ramas temáticas (*feature branches*):

1. `main`: Rama principal protegida y lista para producción.
2. `feature/python-implementation`: Implementación de la solución en Python junto con su suite de pruebas unitarias (`unittest`).
3. `feature/java-implementation`: Implementación de la solución en Java 21+ (*Unnamed Classes*) y pruebas de verificación.
4. `feature/ci-and-docs`: Pipeline de Integración Continua (GitHub Actions) y documentación exhaustiva del proyecto.
