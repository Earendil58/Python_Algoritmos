class Envio:
    def __init__(self, cod_postal, direccion_fisica, tipo_envio, forma_pago):
        self.cod_postal = cod_postal
        self.direccion_fisica = direccion_fisica
        self.tipo_envio = tipo_envio
        self.forma_pago = forma_pago

    def __str__(self):
        return (f'Código postal: {self.cod_postal} | Direccion: {self.direccion_fisica} | Pais: {self.pais()} | Tipo de envio: {self.tipo_envio} | Forma de pago: {self.forma_pago}')

    def pais(self):
        cp = self.cod_postal
        longitud_cp = len(cp)
        destino = ''

        if longitud_cp < 4 or longitud_cp > 9:
            destino = 'Otro'

        else:
            if longitud_cp == 8:
                if cp[0].isalpha() and cp[0] not in 'IO' and cp[1:5].isdigit() and cp[5:8].isalpha():
                    destino = 'Argentina'
                else:
                    destino = 'Otro'

            elif longitud_cp == 4:
                if cp.isdigit():
                    destino = 'Bolivia'
                else:
                    destino = 'Otro'

            elif longitud_cp == 9:
                if cp[:5].isdigit() and cp[5] == '-' and cp[6:].isdigit():
                    destino = 'Brasil'
                else:
                    destino = 'Otro'

            elif longitud_cp == 7:
                if cp.isdigit():
                    destino = 'Chile'
                else:
                    destino = 'Otro'

            elif longitud_cp == 6:
                if cp.isdigit():
                    destino = 'Paraguay'
                else:
                    destino = 'Otro'

            elif longitud_cp == 5:
                if cp.isdigit():
                    destino = 'Uruguay'
                else:
                    destino = 'Otro'

        return destino
