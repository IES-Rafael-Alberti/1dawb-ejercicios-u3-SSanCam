import pytest 
from src.P3_0_Cadenas._311 import mostrar_lista

@pytest.mark.parametrize(
    'asignaturas, expected',
    [
        (['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua'], 'Matemáticas - Física - Química - Historia - Lengua')
    ]
)

def test_311(asignaturas, expected):
    assert mostrar_lista(asignaturas) == expected
