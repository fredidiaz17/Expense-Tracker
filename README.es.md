[Proyecto Anterior (Proyecto #2 - GitHub User Activity)](https://github.com/fredidiaz17/github-user-activity)

> 🌐 [Read this in English](README.md)

# Proyecto #3 - Expense Tracker

Expense Tracker es un proyecto extraído de [Roadmap.sh](https://roadmap.sh/projects/expense-tracker).

## ¿De qué trata?

El proyecto permite gestionar gastos personales desde la línea de comandos. El usuario puede **agregar, actualizar, eliminar y consultar** sus gastos, así como ver resúmenes por mes o categoría, establecer **presupuestos mensuales** con alertas automáticas al excederlos, y exportar sus datos a **CSV**.

Toda la información se almacena en un archivo `expenses.json` generado automáticamente.

---

## Requisitos previos

- Python **3.10** o superior
- Instalar dependencias:

```powershell
pip install pandas
```

---

## Instalación y ejecución

1. Clonamos el repositorio.
```powershell
git clone https://github.com/fredidiaz17/Expense-Tracker
```

2. Nos ubicamos en la carpeta del proyecto:
```powershell
cd expense-tracker
```

3. Instalamos las dependencias:
```powershell
pip install pandas
```

4. Ejecutamos el programa:
```powershell
python expense_tracker.py <comando> [argumentos]
```

---

## Uso y comandos

### `add` — Agregar un gasto

Agrega un nuevo gasto. La **descripción** y el **monto** son obligatorios.

```powershell
python expense_tracker.py add --description "Lunch" --amount 20
```

#### Argumentos

| Argumento | Abreviatura | Requerido | Descripción | Ejemplo |
|-----------|-------------|-----------|-------------|---------|
| `--description` | `-d` | ✅ | Descripción del gasto (máx. 100 caracteres) | `--description "Lunch"` |
| `--amount` | `-a` | ✅ | Monto del gasto (entero positivo, máx. 999999) | `--amount 20` |
| `--category` | `-c` | ❌ | Categoría del gasto (máx. 30 caracteres) | `--category Food` |

---

### `list` — Listar gastos

Muestra todos los gastos registrados en formato de tabla.

```powershell
python expense_tracker.py list
```

#### Argumentos opcionales

| Argumento | Abreviatura | Descripción | Ejemplo |
|-----------|-------------|-------------|---------|
| `--category` | `-c` | Filtra los gastos por categoría | `python expense_tracker.py list --category Food` |

---

### `summary` — Resumen de gastos

Muestra el total de los gastos. Puede filtrarse por mes del año actual y/o por categoría.

```powershell
python expense_tracker.py summary
```

#### Argumentos opcionales

| Argumento | Abreviatura | Descripción | Ejemplo |
|-----------|-------------|-------------|---------|
| `--month` | `-m` | Mes del año actual (1-12) | `python expense_tracker.py summary --month 7` |
| `--category` | `-c` | Categoría a resumir | `python expense_tracker.py summary --category Food` |

Ambos argumentos son combinables entre sí.

---

### `update` — Actualizar un gasto

Actualiza uno o más campos de un gasto existente, identificado por su ID. Se requiere al menos un campo a actualizar.

```powershell
python expense_tracker.py update <id> --amount 30
```

#### Argumentos

| Argumento | Abreviatura | Requerido | Descripción |
|-----------|-------------|-----------|-------------|
| `id` | — | ✅ | ID del gasto a actualizar (posicional) |
| `--description` | `-d` | ❌ | Nueva descripción (máx. 100 caracteres) |
| `--amount` | `-a` | ❌ | Nuevo monto (entero positivo, máx. 999999) |
| `--category` | `-c` | ❌ | Nueva categoría (máx. 30 caracteres) |

---

### `delete` — Eliminar un gasto

Elimina un gasto existente por su ID.

```powershell
python expense_tracker.py delete <id>
```

| Argumento | Requerido | Descripción |
|-----------|-----------|-------------|
| `id` | ✅ | ID del gasto a eliminar (posicional) |

---

### `csv` — Exportar a CSV

Exporta todos los gastos a un archivo `expenses.csv` en el directorio actual.

```powershell
python expense_tracker.py csv
```

---

### `budget` — Gestión de presupuesto

Administra el presupuesto mensual. Tiene dos subcomandos: `set` y `list`.

#### `budget set` — Establecer presupuesto

Establece el presupuesto para un mes dado. Si ya existe un presupuesto para ese mes, lo sobreescribe. Si el monto es `0`, elimina el presupuesto existente.

```powershell
python expense_tracker.py budget set --month 7 --amount 500
```

| Argumento | Abreviatura | Requerido | Descripción |
|-----------|-------------|-----------|-------------|
| `--month` | `-m` | ✅ | Mes (1-12) |
| `--amount` | `-a` | ✅ | Monto del presupuesto (0 para eliminar) |
| `--year` | `-y` | ❌ | Año (entre 2000 y 10 años desde el actual). Si se omite, se usa el año actual. |

#### `budget list` — Listar presupuestos

Muestra todos los presupuestos existentes.

```powershell
python expense_tracker.py budget list
```

> ⚠️ **Alerta de presupuesto**: Al agregar o actualizar un gasto, el programa verifica automáticamente si el total del mes excede el presupuesto establecido, mostrando una advertencia en caso afirmativo.

---

## Estructura del proyecto

```text
expense-tracker/
├── expense_tracker.py       # Punto de entrada del programa
├── expense_functions.py     # Lógica principal de cada comando
├── json_manager.py          # Lectura, escritura y exportación a CSV
├── expenses.json            # Generado automáticamente al primer uso
├── expenses.csv             # Generado al ejecutar el comando csv
└── README.md
```

---

## Limitaciones

- Los montos de los gastos son enteros; no se admiten decimales.
- El filtro por mes en `summary` corresponde siempre al año actual.
- Los presupuestos con año omitido se asignan al año actual, independientemente del mes indicado.

---

## Retos durante el desarrollo

1. **Subparsers anidados en argparse**: El comando `budget` requirió anidar subparsers dentro de un subparser ya existente, una estructura más compleja que los argumentos mutuamente excluyentes usados en proyectos anteriores, pero que resulta más coherente con la experiencia de herramientas CLI reales.
2. **Uso simultáneo de Pandas y JSON**: La lista de gastos se imprime mediante un `DataFrame` de Pandas construido desde el JSON, lo que implicó pensar en cómo mantener el esquema del JSON compatible con las operaciones CRUD y la construcción del DataFrame al mismo tiempo.
3. **Closures en argparse**: Se utilizaron closures para las funciones de validación de argumentos, siendo la primera vez que se implementó este patrón, resultando especialmente útil para parametrizar validadores reutilizables.
4. **Diseño del sistema de presupuesto**: Definir el comportamiento del upsert, el manejo del año, los límites de validación y la lógica de alerta requirió varias decisiones de diseño no especificadas por el enunciado del proyecto.

---

## Licencia

Este es un **proyecto personal sin licencia definida**.

---

[Siguiente Proyecto (N/A)]()
