class CalcularMonto:
    TARIFA_POR_KILOMETRO = 0.30  # Constante para la tarifa

    def __init__(self, km_recorridos, monto_base):
        self._km_recorridos = self._comprobar_num(km_recorridos, "kilómetros recorridos")
        self._monto_base = self._comprobar_num(monto_base, "monto base")

    @staticmethod
    def _comprobar_num(num, nombre_campo):
        """
        Verifica que el número sea mayor a 0.
        Lanza una excepción si el valor no es válido.
        """
        if num <= 0:
            raise ValueError(f"El valor de {nombre_campo} debe ser mayor a 0.")
        return num

    def calcular_precio(self):
        """
        Calcula el precio total del boleto.
        """
        return self._monto_base + (self._km_recorridos * CalcularMonto.TARIFA_POR_KILOMETRO)

    def __str__(self):
        """
        Representación en texto del objeto, mostrando todos los detalles.
        """
        return (f"- Km recorridos: {self._km_recorridos} \n"
                f"- Monto base: ${self._monto_base:.2f} \n"
                f"- Precio del viaje: ${self.calcular_precio():.2f}")


def obtener_numero_positivo(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            if numero <= 0:
                raise ValueError("El número debe ser mayor a 0.")
            return numero
        except ValueError as e:
            print(f"Entrada inválida: {e}")

def main():
    print("Cálculo del precio del boleto:")
    # Validar datos antes de instanciar la clase
    km_recorridos = obtener_numero_positivo("Ingrese la cantidad de km recorridos: ")
    monto_base = obtener_numero_positivo("Ingrese el monto base: ")

    # Crear instancia y mostrar resultado
    boleto = CalcularMonto(km_recorridos, monto_base)
    print(boleto)

if __name__ == '__main__':
    main()

