# Proyecto de Seguimiento de Gastos

Este proyecto es una aplicación de seguimiento de gastos personales. Permite a los usuarios agregar transacciones, listar transacciones, mostrar el balance financiero y exportar el balance a un archivo CSV. La aplicación está implementada en Python y utiliza la biblioteca pickle para almacenar los datos de las transacciones.

## Estructura del Proyecto

* main_app.py: El archivo principal que contiene el menú interactivo para el usuario.
* seguimiento_gastos.py: Contiene la clase SeguimientoGastos, la cual maneja las transacciones y las operaciones relacionadas.
* transaccion_class.py: Define la clase Transaccion, que representa una transacción individual.

## ¿Cómo usar el programa?
1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener Python instalado.
3. No se requieren bibliotecas adicionales más allá de las incluidas en la instalación estándar de Python.

### Uso

Para ejecutar la aplicación, simplemente ejecuta el archivo main_app.py:

python main_app.py

## Funcionalidades del Menú

### Agregar Transacción:

Permite al usuario agregar una nueva transacción especificando el monto, fecha, descripción y tipo (ingreso o gasto).

### Listar Transacciones:

Muestra una lista de todas las transacciones ordenadas por fecha.

### Mostrar Balance:

Calcula y muestra el total de ingresos, total de gastos y la capacidad de ahorro (ingresos - gastos).

### Exportar Balance a CSV:

Exporta el balance financiero y las transacciones del mes actual a un archivo CSV llamado balance_financiero.csv.

### Salir:

Sirve para cerrar y salir del programa. 

## Contribuir
Si deseas contribuir a este proyecto, por favor realiza un fork del repositorio y crea una pull request con tus cambios.

Sale de la aplicación.