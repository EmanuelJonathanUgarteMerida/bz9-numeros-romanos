def validar_si_es_entero(numero):
    if isinstance(numero, int):
        return True
    else:
        raise ValueError("el parámetro de entrada debe ser un número entero")

# Tip: format se puede hacer como: f'{parametro} es nuevo'


def convertir_en_romano(n):
    """
    Resticciones:
    -es un entero
    -no sea negativo
    -no supere 3999
    """
    return validar_si_es_entero(n)


try:
    print(convertir_en_romano(45.5))
except ValueError as ex:
    print(ex)
except:
    print("Ha ocurrido una excepcion de tipo desconocido")
