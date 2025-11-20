from house import Casa, Habitacion

def test_atributos():
    casa = Casa("Calle 123", 3)

    # Valores
    assert casa.direccion == "Calle 123"
    assert len(casa.habitaciones) == 3
    for habitacion in casa.habitaciones:
        assert habitacion.area == 20.0
    
def test_descripcion():
    casa = Casa("Avenida 456", 4)

    descripcion_esperada = "Casa(direccion = Avenida 456, total de area = 80.0m2, numero de habitaciones = 4)"
    assert casa.descripcion() == descripcion_esperada

def test_verificar_tipo():
    casa = Casa("Boulevard 789", 2)

    assert isinstance(casa.direccion, str)
    assert isinstance(casa.habitaciones, list)
    for habitacion in casa.habitaciones:
        assert isinstance(habitacion, Habitacion)
        assert isinstance(habitacion.area, float)
