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


    def importe_inicial(self):
        base_precio = [1100, 1800, 2450, 8300, 10900, 14300, 17900]
        precio = base_precio[self.tipo_envio]

        if self.pais() != 'Argentina':
            if self.pais() in ['Bolivia', 'Paraguay', 'Uruguay']:
                precio = precio * 120 // 100
            elif self.pais() in ['Chile', 'Brasil']:
                precio = precio * 125 // 100
            else:
                precio = precio * 150 // 100

        return precio


    def importe_final(self):
        importe = self.importe_inicial()
        if self.forma_pago == 1:  # Efectivo
            importe = importe * 90 // 100  # 10% de descuento
        return importe


    def es_direccion_valida(self):
        tiene_digitos = False
        no_mayusculas_seguidas = True
        solo_letras_y_digitos = True

        for i in range(len(self.direccion_fisica)):
            if self.es_digito(self.direccion_fisica[i]):
                tiene_digitos = True
            if i > 0:
                if self.es_letra(self.direccion_fisica[i]) and self.es_letra(self.direccion_fisica[i-1]):
                    if self.direccion_fisica[i].isupper() and self.direccion_fisica[i-1].isupper():
                        no_mayusculas_seguidas = False
            if not (self.es_letra(self.direccion_fisica[i]) or self.es_digito(self.direccion_fisica[i]) or self.direccion_fisica[i] == ' '):
                solo_letras_y_digitos = False

        return tiene_digitos and no_mayusculas_seguidas and solo_letras_y_digitos
