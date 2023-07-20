class Entrada:

    def __init__(self, id, estadio, partido, precio, sector) -> None:
        self.id = id
        self.estadio = estadio
        self.partido = partido
        self.precio = precio
        self.sector = sector

    def serialize(self):
        return {
            'id': self.id,
            'estadio': self.estadio,
            'partido': self.partido,
            'precio': self.precio,
            'sector': self.sector
        }
