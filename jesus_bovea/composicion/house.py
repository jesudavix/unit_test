class Habitacion:
    def __init__(self, area: float):
        self.area = area
    
    def descripcion(self):
        return f"Habitacion de area = {self.area}m2)"
    

class Casa:
    def __init__(self, direccion: str, habitaciones: int):
        self.direccion = direccion
        self.habitaciones = [Habitacion(area=20.0) for _ in range(habitaciones)]
    
    def total_area(self):
        return sum(habitacion.area for habitacion in self.habitaciones)
    
    def descripcion(self):
        return f"Casa(direccion = {self.direccion}, total de area = {self.total_area()}m2, numero de habitaciones = {len(self.habitaciones)})"

