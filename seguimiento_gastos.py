import pickle
from transaccion_class import Transaccion
from datetime import datetime
import csv


#Se creará una clase que contendrá todas las funciones que hacen que el programa de seguimiento de gastos funcione.
class SeguimientoGastos:
    #Se crea una instancia de transacciones que 
    def __init__(self):
        self.transacciones = self.cargar_datos()        

    #Esta función hace un append de una instancia de la clase transación
    #Es decir agrega valores a la lista que almacena los datos de transacciones
    def agregar_transaccion(self, monto: float, fecha: str, descripcion: str, tipo: str):
        nueva_transaccion = Transaccion(monto, fecha, descripcion, tipo)
        self.transacciones.append(nueva_transaccion)
        self.guardar_datos()

    #Esta función se encarga de cargar los datos de un archivo pickle, que es el mismo donde se almacenarán las transacciones ingresadas por el usuario.
    def cargar_datos(self):
        try:
            with open('datos_financieros.pkl', 'rb') as archivo:
                return pickle.load(archivo)
        except FileNotFoundError:
            return []
        
    #Esta función se encarga de guardar las transacciones en un archivo pickle
    def guardar_datos(self):
        with open('datos_financieros.pkl', 'wb') as archivo:
            pickle.dump(self.transacciones, archivo)

    #Esta función calcula el total de ingresos y el total de gastos para así reportarlos en consola, cuando el usuario active esta función.
    def calcular_balance(self):
        total_ingresos = sum(t.monto for t in self.transacciones if t.tipo == 'ingreso')
        total_gastos = sum(t.monto for t in self.transacciones if t.tipo == 'gasto')
        capacidad_ahorro = total_ingresos - total_gastos
        print(f"Total Ingresos: {total_ingresos}")
        print(f"Total Gastos: {total_gastos}")
        print(f"Capacidad de Ahorro: {capacidad_ahorro}")

    #Ordena las transacciones ingresadas por el usuario de acuerdo a la fecha y lo imprime en consola. 
    def listar_transacciones(self):
        transacciones_ordenadas = sorted(self.transacciones, key=lambda x: x.fecha)
        for transaccion in transacciones_ordenadas:
            print(f"{transaccion.fecha.strftime('%Y-%m-%d')} | {transaccion.tipo} | {transaccion.monto} | {transaccion.descripcion}")

    #La siguiente función se encarga de guardar los datos del balance y transacciones en un archivo csv
    def exportar_balance(self):
        total_ingresos = sum(t.monto for t in self.transacciones if t.tipo == 'ingreso')
        total_gastos = sum(t.monto for t in self.transacciones if t.tipo == 'gasto')
        capacidad_ahorro = total_ingresos - total_gastos

        # Obtener el mes y año actual
        mes_actual = datetime.now().month
        año_actual = datetime.now().year

        # Filtrar transacciones del mes actual
        transacciones_mes_actual = [t for t in self.transacciones if t.fecha.month == mes_actual and t.fecha.year == año_actual]

        with open('balance_financiero.csv', 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerow(['Concepto', 'Monto'])
            escritor_csv.writerow(['Total Ingresos', total_ingresos])
            escritor_csv.writerow(['Total Gastos', total_gastos])
            escritor_csv.writerow(['Capacidad de Ahorro', capacidad_ahorro])
            escritor_csv.writerow([])  # Línea en blanco para separar secciones

            escritor_csv.writerow(['Transacciones del Mes Actual'])
            escritor_csv.writerow(['Fecha', 'Tipo', 'Monto', 'Descripción'])

            for transaccion in transacciones_mes_actual:
                escritor_csv.writerow([transaccion.fecha.strftime('%Y-%m-%d'), transaccion.tipo, transaccion.monto, transaccion.descripcion])

        print("Balance exportado a balance_financiero.csv")