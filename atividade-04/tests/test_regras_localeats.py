import pytest
from src.regras_localeats import pedido_atingiu_valor_minimo

def test_pedido_atinge_valor_minimo():
    """Valida se um pedido com valor igual ou superior a 30 retorna True."""
    resultado = pedido_atingiu_valor_minimo(50.0)
    assert resultado is True

def test_pedido_abaixo_valor_minimo():
    """Valida se um pedido abaixo de 30 retorna False."""
    resultado = pedido_atingiu_valor_minimo(20.0)
    assert resultado is False

@pytest.mark.parametrize("valor", [30.0, 45.50, 150.0])
def test_pedido_valores_validos_limite(valor):
    """Valida casos de borda e valores válidos (Diferencial opcional)."""
    assert pedido_atingiu_valor_minimo(valor) is True

def test_pedido_valor_negativo_lanca_excecao():
    """Valida se valores negativos geram ValueError (Diferencial opcional)."""
    with pytest.raises(ValueError):
        pedido_atingiu_valor_minimo(-5.0)
