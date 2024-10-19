class Lote:
    def __init__(self, nombre_completo, nro_mza, nro_lote, nro_orientacion, sup_terreno, monto_venta):
        self.nombre_completo = nombre_completo
        self.nro_mza = nro_mza
        self.nro_lote = nro_lote
        self.nro_orientacion = nro_orientacion
        self.sup_terreno = sup_terreno
        self.monto_venta = monto_venta



    def __str__(self):
        orientaciones = ["Norte", "Sur", "Este", "Oeste"]
        orientacion = orientaciones[self.nro_orientacion - 1]

        return (f'Cliente: {self.nombre_completo:<25} - '
                f'Manzana: {self.nro_mza:<3} - '
                f'Lote: {self.nro_lote:<2} - '
                f'Orientación: {self.nro_orientacion} ({orientacion:<5}) - '
                f'Superficie: {self.sup_terreno:7.2f} - '
                f'Importe: {self.monto_venta:9.2f}')





