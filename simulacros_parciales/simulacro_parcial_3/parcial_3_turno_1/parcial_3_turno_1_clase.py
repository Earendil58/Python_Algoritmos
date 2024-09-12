class Empleo:
    def __init__(self, id_empleo: int, descripcion: str, tipo_empleo: int, sueldo: float):
        self.id_empleo = id_empleo
        self.descripcion = descripcion
        self.tipo_empleo = tipo_empleo
        self.sueldo = sueldo

    def __str__(self):
        return (f'Identificador: {self.id_empleo:<10}   -   '
                f'Descripción: {self.descripcion:<20}   -   '
                f'Tipo: {self.tipo_empleo:<5}   -   '
                f'Sueldo: ${self.sueldo:,.2f}')

