from datetime import datetime

#En primer lugar se creará una clase que contenga la información de una transacción individual
#Se crea una instancia de una transacción individual.

class Transaccion:
    def __init__(self, monto: float, fecha: str, descripcion: str, tipo: str):
        self.monto = monto
        self.fecha = datetime.strptime(fecha, '%Y-%m-%d')
        self.descripcion = descripcion
        self.tipo = tipo

