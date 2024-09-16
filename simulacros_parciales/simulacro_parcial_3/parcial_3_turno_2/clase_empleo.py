class Ticket:
    def __init__(self, cod_vuelo: str, id_pasajero: int, id_pais_destino: int, num_asiento: int, importe_ticket: float):
        self.cod_vuelo = cod_vuelo
        self.id_pasajero = id_pasajero
        self.id_pais_destino = id_pais_destino
        self.num_asiento = num_asiento
        self.importe_ticket = importe_ticket

    def __str__(self):
        return(f'Código de vuelo: {self.cod_vuelo: <20}   -   '
               f'ID Pasajero: {self.id_pasajero: <10}   -   '
               f'ID Pais Destino: {self.id_pais_destino: <10}   -   '
               f'Número de asiento: {self.num_asiento: <10}   -   '
               f'Importe Ticket: {self.importe_ticket: <10}   -   ')
