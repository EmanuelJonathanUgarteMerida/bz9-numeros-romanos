# diccionario
conversion = {
    'millares': ['', 'M', 'MM', 'MMM'],
    'centenas': ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
    'decenas': ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
    'unidades': ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
}


def validar_es_numero(numero):
    if not isinstance(numero, int):
        raise ValueError("el parámetro de entrada debe ser un número entero")
    if 0 > numero or numero > 3999:
        raise ValueError(
            f"El número {numero} no es válido, debe comprender el rango entre 0 y 3999")


def descomponer_numero(numero):
    cadena = str(numero)
    millares = 0
    centenas = 0
    decenas = 0
    unidades = 0
    if len(cadena) >= 4:
        millares = int(cadena[-4])
    if len(cadena) >= 3:
        centenas = int(cadena[-3])
    if len(cadena) >= 2:
        decenas = int(cadena[-2])
    if len(cadena) >= 1:
        unidades = int(cadena[-1])

    r_millares = conversion['millares'][millares]
    r_centenas = conversion['centenas'][centenas]
    r_decenas = conversion['decenas'][decenas]
    r_unidades = conversion['unidades'][unidades]

    return f"{r_millares}{r_centenas}{r_decenas}{r_unidades}"

# Tip: format se puede hacer como: f'{parametro} es nuevo'


def convertir_en_romano(n):
    """
    Resticciones: ver validar_numero
    ejemplo: 1123, solución: descomponer número
    """
    try:
        validar_es_numero(n)
        print(descomponer_numero(n))
    except ValueError as ex:
        print("El número no cumple las restricciones", ex)
        return


romano_set = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}


def convertir_a_numero(romano):
    acumulador = 0
    anterior = 0
    # for x in romano:
    #   suma += romano_set[x]
    for x in romano:
        actual = romano_set[x]
        if anterior >= actual:
            acumulador += actual
        else:
            acumulador -= anterior
            acumulador += actual-anterior
        anterior = actual

    return acumulador


# convertir_en_romano(3000)
