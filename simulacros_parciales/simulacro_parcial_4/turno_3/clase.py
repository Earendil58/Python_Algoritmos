class Pantalon:
    def __init__(self, cod_producto, nombre_modelo, largo_talle, cintura_talle, tipo_tela, stock_disponible):
        self.cod_producto = cod_producto
        self.nombre_modelo = nombre_modelo
        self.largo_talle = largo_talle
        self.cintura_talle = cintura_talle
        self.tipo_tela = tipo_tela
        self.stock_disponible = stock_disponible

    def __str__(self):

        tipos_telas = ['Jean', 'Gabardina', 'Denim']
        tipo_tela = tipos_telas[self.tipo_tela - 1]

        return(f'Cod_producto: {self.cod_producto:<15} - '
               f'Nombre Modelo: {self.nombre_modelo: <20} - '
               f'Largo talle: {self.largo_talle: <10} - '
               f'Cintura talle: {self.cintura_talle: <10} - '
               f'Tipo de tela: {self.tipo_tela: <5} {tipo_tela} - '
               f'Stock disponible: {self.stock_disponible: <10}')


