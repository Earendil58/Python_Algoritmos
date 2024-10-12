import os

# Definición de la clase Envio
class Envio:
    def __init__(self, codigo_postal, direccion, tipo_envio, forma_pago):
        self.codigo_postal = codigo_postal
        self.direccion = direccion
        self.tipo_envio = tipo_envio
        self.forma_pago = forma_pago

    def __str__(self):
        return f"CP: {self.codigo_postal}, Dirección: {self.direccion}, Tipo: {self.tipo_envio}, Pago: {self.forma_pago}"

# Función para convertir un string en un objeto Envio
def procesar_fila_csv(fila):
    elementos = fila.split(',')
    codigo_postal = elementos[0].strip()
    direccion = elementos[1].strip()
    tipo_envio = int(elementos[2].strip())
    forma_pago = int(elementos[3].strip())
    return Envio(codigo_postal, direccion, tipo_envio, forma_pago)

# Función para leer el archivo CSV y convertirlo a binario
def crear_archivo_binario_desde_csv(csv_filename, bin_filename):
    if os.path.exists(bin_filename):
        os.remove(bin_filename)

    with open(csv_filename, 'r') as csv_file:
        with open(bin_filename, 'wb') as bin_file:
            # Leer todas las líneas del CSV
            lineas = csv_file.readlines()

            # Ignorar la primera (timestamp) y segunda línea (descriptores)
            for i in range(2, len(lineas)):
                fila = lineas[i]
                envio = procesar_fila_csv(fila)
                # Guardar en archivo binario
                bin_file.write(envio.codigo_postal.ljust(10).encode('utf-8'))
                bin_file.write(envio.direccion.ljust(20).encode('utf-8'))
                bin_file.write(str(envio.tipo_envio).encode('utf-8'))
                bin_file.write(str(envio.forma_pago).encode('utf-8'))

# Función para cargar un envío manualmente y guardarlo en el archivo binario
def agregar_envio(bin_filename):
    codigo_postal = input("Ingrese el código postal: ").ljust(10)
    direccion = input("Ingrese la dirección: ").ljust(20)
    tipo_envio = input("Ingrese el tipo de envío (0-6): ")
    forma_pago = input("Ingrese la forma de pago (1: efectivo, 2: tarjeta): ")

    with open(bin_filename, 'ab') as bin_file:
        bin_file.write(codigo_postal.encode('utf-8'))
        bin_file.write(direccion.encode('utf-8'))
        bin_file.write(tipo_envio.encode('utf-8'))
        bin_file.write(forma_pago.encode('utf-8'))

# Función para leer y mostrar todos los envíos desde el archivo binario
def mostrar_envios(bin_filename):
    if not os.path.exists(bin_filename):
        print("No hay envíos registrados.")
        return

    with open(bin_filename, 'rb') as bin_file:
        while True:
            # Leer datos en bloques correspondientes a cada campo
            codigo_postal = bin_file.read(10).decode('utf-8').strip()
            if not codigo_postal:
                break
            direccion = bin_file.read(20).decode('utf-8').strip()
            tipo_envio = bin_file.read(1).decode('utf-8')
            forma_pago = bin_file.read(1).decode('utf-8')
            print(f"CP: {codigo_postal}, Dirección: {direccion}, Tipo: {tipo_envio}, Pago: {forma_pago}")

# Función para buscar por código postal
def buscar_por_codigo_postal(bin_filename, codigo_postal):
    if not os.path.exists(bin_filename):
        print("No hay envíos registrados.")
        return

    encontrado = False
    with open(bin_filename, 'rb') as bin_file:
        while True:
            # Leer los datos del archivo binario
            cp = bin_file.read(10).decode('utf-8').strip()
            if not cp:
                break
            direccion = bin_file.read(20).decode('utf-8').strip()
            tipo_envio = bin_file.read(1).decode('utf-8')
            forma_pago = bin_file.read(1).decode('utf-8')

            if cp == codigo_postal:
                print(f"Envío encontrado: CP: {cp}, Dirección: {direccion}, Tipo: {tipo_envio}, Pago: {forma_pago}")
                encontrado = True

    if not encontrado:
        print(f"No se encontró ningún envío con el código postal: {codigo_postal}")

# Función para buscar por dirección
def buscar_por_direccion(bin_filename, direccion_buscar):
    if not os.path.exists(bin_filename):
        print("No hay envíos registrados.")
        return

    encontrado = False
    with open(bin_filename, 'rb') as bin_file:
        while True:
            # Leer los datos del archivo binario
            cp = bin_file.read(10).decode('utf-8').strip()
            if not cp:
                break
            direccion = bin_file.read(20).decode('utf-8').strip()
            tipo_envio = bin_file.read(1).decode('utf-8')
            forma_pago = bin_file.read(1).decode('utf-8')

            if direccion == direccion_buscar:
                print(f"Envío encontrado: CP: {cp}, Dirección: {direccion}, Tipo: {tipo_envio}, Pago: {forma_pago}")
                encontrado = True

    if not encontrado:
        print(f"No se encontró ningún envío con la dirección: {direccion_buscar}")

# Función para contar los envíos según tipo de envío y forma de pago
def contar_envios(bin_filename):
    if not os.path.exists(bin_filename):
        print("No hay envíos registrados.")
        return

    # Crear una matriz de 7x2 para contar envíos por tipo y forma de pago
    matriz = [[0] * 2 for _ in range(7)]

    with open(bin_filename, 'rb') as bin_file:
        while True:
            # Leer los datos del archivo binario
            cp = bin_file.read(10).decode('utf-8').strip()
            if not cp:
                break
            direccion = bin_file.read(20).decode('utf-8').strip()
            tipo_envio = int(bin_file.read(1).decode('utf-8'))
            forma_pago = int(bin_file.read(1).decode('utf-8'))

            matriz[tipo_envio][forma_pago - 1] += 1

    # Mostrar los resultados
    for i in range(7):
        for j in range(2):
            if matriz[i][j] > 0:
                print(f"Tipo de envío {i}, Forma de pago {j+1}: {matriz[i][j]} envíos")

# Función del menú principal
def menu():
    bin_filename = 'envios.bin'
    while True:
        print("\nMenú de opciones:")
        print("1. Crear archivo binario desde CSV")
        print("2. Agregar envío por teclado")
        print("3. Mostrar todos los envíos")
        print("4. Buscar por código postal")
        print("5. Buscar por dirección")
        print("6. Contar envíos por tipo y forma de pago")
        print("0. Salir")

        opcion = input("Elija una opción: ")

        if opcion == '1':
            crear_archivo_binario_desde_csv('envios-tp4.csv', bin_filename)
        elif opcion == '2':
            agregar_envio(bin_filename)
        elif opcion == '3':
            mostrar_envios(bin_filename)
        elif opcion == '4':
            codigo_postal = input("Ingrese el código postal: ")
            buscar_por_codigo_postal(bin_filename, codigo_postal)
        elif opcion == '5':
            direccion = input("Ingrese la dirección: ")
            buscar_por_direccion(bin_filename, direccion)
        elif opcion == '6':
            contar_envios(bin_filename)
        elif opcion == '0':
            break
        else:
            print("Opción no válida, intente nuevamente.")

# Ejecución del programa
if __name__ == "__main__":
    menu()
