def pedido_atingiu_valor_minimo(valor_pedido: float) -> bool:
    """
    - Pedidos de R$ 30,00 ou mais retornam True.
    - Pedidos abaixo de R$ 30,00 retornam False.
    - Valores negativos geram ValueError.
    """
    if valor_pedido < 0:
        raise ValueError("O valor do pedido não pode ser negativo.")
    return valor_pedido >= 30.0
