from src.P3_0_Cadenas._301 import cadena_reves
import pytest

@pytest.mark.parametrize(
    'cadena, expected',
    [
        ('banana', 'a\nn\na\nn\na\nb\n')
    ]
)

def test_cadena_reves(cadena, expected):
    assert cadena_reves(cadena) == expected