class Libro:
    def __init__(self, nro_isbn, titulo, autor, cod_idioma, precio_venta):
        self.nro_isbn = nro_isbn
        self.titulo = titulo
        self.autor = autor
        self.cod_idioma = cod_idioma
        self.precio_venta = precio_venta


    def __str__(self):

        idiomas = ['Español', 'Ingles', 'Portugués', 'Francés', 'Italiano']
        idioma = idiomas[self.cod_idioma - 1]

        return(f'Nro_isbn: {self.nro_isbn: <10}  -  '
               f'Titulo: {self.titulo: <50}  -  '
               f'Autor: {self.autor: <20}  -  '
               f'Cod_idioma: {self.cod_idioma: <5} {idioma: <5} -  '
               f'Precio venta: {self.precio_venta: <10}')
