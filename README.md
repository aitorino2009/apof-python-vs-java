# Desafío de Programación: El Calculador de Presupuesto para Eventos

Comparativa práctica entre **Python** y **Java 21+ (Top-Level Statements / Unnamed Classes)** desarrollada para el módulo de APOF.

---

## 📋 Descripción del Proyecto

Una empresa de eventos necesita calcular los costes básicos de contratación de catering según el número de asistentes.
Este repositorio contiene la solución implementada en dos lenguajes representativos:
1. **Python** (sintaxis concisa, tipado dinámico y delimitación de bloques por indentación).
2. **Java 21+** (uso de clases implícitas / métodos top-level `void main()`, inferencia de tipos con `var` y delimitación por llaves `{}`).

---

## 🎯 Reglas de Negocio

- **Coste por asistente:** `25.50 €`
- **Coste fijo de gestión:** `50.00 €`
- **Fórmula de cálculo:**
  $$\text{Coste Total} = (\text{invitados} \times 25.50) + 50.00$$

---

## 📁 Estructura del Repositorio

```text
apof-python-vs-java/
├── .gitignore
├── README.md
├── python/
│   └── calculador_presupuesto.py
└── java/
    └── CalculadorPresupuesto.java
```

---

## ⚖️ Comparativa Técnica (Checklist de Evaluación)

| Criterio de Evaluación | Python 🐍 | Java 21+ ☕ |
| :--- | :--- | :--- |
| **Límites de bloque** | Indentación con espacios (4 espacios) | Uso explícito de llaves `{ }` |
| **Definición de funciones** | Uso de `def` y type hints opcionales | Firma con tipo de retorno explícito (`double`) |
| **Captura de teclado** | `input()` combinado con conversión `float()` | Objeto `Scanner` y método `scanner.nextDouble()` |
| **Inferencia de tipos** | Dinámica / implícita | Inferencia estática de variables locales con `var` |
| **Salida por pantalla** | `print()` con f-strings | `System.out.println()` con formateo de cadenas |
| **Punto de entrada** | `if __name__ == "__main__":` | Método `void main()` (Unnamed Class / JEP 445+) |

---

## 🚀 Instrucciones de Ejecución

### 🐍 Python
Requiere Python 3.10 o superior.

```bash
# Desde la raíz del repositorio
python python/calculador_presupuesto.py
```

### ☕ Java 21+
Requiere JDK 21 o superior (ej. Java 21 LTS, Java 25 LTS).

```bash
# Desde la raíz del repositorio
java java/CalculadorPresupuesto.java
```
