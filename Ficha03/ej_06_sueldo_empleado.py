def chequeo_string(mensaje):
    while True:
        valor = input(mensaje.strip()).strip()
        if valor.replace(" ", "").isalpha():  # Permitir nombres compuestos
            return valor
        print('Por favor, ingrese un nombre válido.')


def chequeo_salario_empleado(mensaje):
    while True:
        valor = input(mensaje.strip()).strip()
        try:
            salario = float(valor)
            if salario > 0:
                return salario
            else:
                print('El salario debe ser un número positivo.')
        except ValueError:
            print('Por favor, ingrese un monto válido.')



def calcular_nuevo_salario(salario):
    salario_aumentado = salario * 1.08  # Incremento del 8%
    salario_final = salario_aumentado * 0.975  # Descuento del 2.5%
    return salario_final



def main():
    nombre_emplado = chequeo_string('Por favor ingrese el nombre del emplado: ')
    salario_empleado = chequeo_salario_empleado('Por favor ingrese el salario del empleado: ')
    area_empleado = chequeo_string('Por favor describa el area del emplado: ')

    nuevo_salario = calcular_nuevo_salario(salario_empleado)

    print(f'Nombre Empleado: {nombre_emplado} \n'
            f'Salario Actual Empleado: {salario_empleado} \n'
            f'Area Empleado: {area_empleado} \n'
            f'Nuevo Salario Empleado: {nuevo_salario}')


if __name__ == '__main__':
    main()

