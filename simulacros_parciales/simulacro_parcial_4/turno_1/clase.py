class Lote:
    def __init__(self, nombre_completo, nro_mza, nro_lote, nro_orientacion, sup_terreno, monto_venta):
        self.nombre_completo = nombre_completo
        self.nro_mza = nro_mza
        self.nro_lote = nro_lote
        self.nro_orientacion = nro_orientacion
        self.sup_terreno = sup_terreno
        self.monto_venta = monto_venta

    def __str__(self):
        return (f'Nombre Completo: {self.nombre_completo: <20} \n'
               f'Número de Manzana: {self.nro_mza: <5} \n'
               f'Número de Lote: {self.nro_lote: <5} \n'
               f'Orientación: {self.nro_orientacion: <5} \n'
               f'Superficie del terreno: {self.sup_terreno} \n'
               f'Monto de la venta: {self.monto_venta}')





