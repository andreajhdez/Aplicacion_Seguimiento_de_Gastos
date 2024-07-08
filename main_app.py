from seguimiento_gastos import SeguimientoGastos

def main():
    controlador = SeguimientoGastos()

    while True:
        print("\n---  BIENVENIDO ESTIMADO USUARIO  ---")
        print("\n En seguida encontrarás el menú con nuestras funcionalidades para que así puedas tener un control de tus finanzas!")
        print("\n--- Menú ---")
        print("1. Agregar Transacción")
        print("2. Listar Transacciones")
        print("3. Mostrar Balance")
        print("4. Exportar Balance a CSV")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            monto = float(input("Monto: "))
            fecha = input("Fecha (YYYY-MM-DD): ")
            descripcion = input("Descripción: ")
            tipo = input("Tipo (ingreso/gasto): ")
            controlador.agregar_transaccion(monto, fecha, descripcion, tipo)
        elif opcion == '2':
            controlador.listar_transacciones()
        elif opcion == '3':
            controlador.calcular_balance()
        elif opcion == '4':
            controlador.exportar_balance()
        elif opcion == '5':
            break
        else:
            print("Opción no admitida, intenta de nuevo con las opciones del menu")


if __name__ == "__main__":
    main()   

