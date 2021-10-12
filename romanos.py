def validar_es_numero(numero):
    if not isinstance(numero, int):
        raise ValueError("el parámetro de entrada debe ser un número entero")
    if 0 > numero or numero > 3999:
        raise ValueError(
            f"El número {numero} no es válido, debe comprender el rango entre 0 y 3999")

# Tip: format se puede hacer como: f'{parametro} es nuevo'


def descomponer_numero(numero):
    cadena = str(numero)
    millares = 0
    centenas = 0
    decenas = 0
    unidades = 0
    if len(cadena) >= 4:
        millares = int(cadena[-4])
    if len(cadena) >= 3:
        millares = int(cadena[-3])
    if len(cadena) >= 2:
        millares = int(cadena[-2])
    if len(cadena) >= 1:
        millares = int(cadena[-1])


def convertir_en_romano(n):
    """
    Resticciones: ver validar_numero
    ejemplo: 1123, solución: descomponer número
    """
    try:
        validar_es_numero(n)
    except ValueError as ex:
        print("El número no cumple las restricciones", ex)
    except:
        print("Ha ocurrido una excepcion de tipo desconocido")


convertir_en_romano(4000)
print(6/5)
print(6//5)
