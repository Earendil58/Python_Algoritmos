class Empleo:
    def __init__(self, id_empleo: int, descripcion: str, tipo_empleo: int, sueldo: float):
        self.id_empleo = id_empleo
        self.descripcion = descripcion
        self.tipo_empleo = tipo_empleo
        self.sueldo = sueldo


    def __str__(self):
        return (f'{"-" * 90} \n'
                f'El empleo tiene un ID: {self.id_empleo} \n'
                f'El empleo es: {self.descripcion} \n'
                f'El tipo de empleo (0/39) es: {self.tipo_empleo} \n'
                f'El sueldo para el empleo es: {self.sueldo}')
