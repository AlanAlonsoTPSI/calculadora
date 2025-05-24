def dividir(a, b):
    """
    Divide dos números y devuelve el resultado
    Lanza ZeroDivisionError si b es cero
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
