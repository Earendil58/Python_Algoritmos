class Empleado:
    def __init__(self, nombre, edad, cargo, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.cargo = cargo
        self.sueldo = sueldo


empleado_1 = Empleado('Menem', 101, 'Jefazo', 123456789)

print(empleado_1.cargo)
