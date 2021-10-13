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


def convertir_a_numero1(romano):
    acumulador = 0
    anterior = 0
    # for x in romano:
    #   suma += romano_set[x]
    for x in romano:
        actual = romano_set[x]
        if anterior >= actual:
            acumulador += actual
        else:
            if anterior in (5, 50, 500):
                raise ValueError("No se puede operar")
            else:
                acumulador -= anterior
                acumulador += actual-anterior
        anterior = actual

    return acumulador


def convertir_a_numero(romano):
    contador = 1
    anterior = 0
    acumulador = 0
    restado = False
    for x in romano:
        actual = romano_set[x]

        # Comprobamos si son iguales y si supera el límite de repetición
        if anterior == actual and contador == 3:
            raise ValueError(
                "No se puede operar números de más de 3 repeticiones")

        if anterior >= actual or anterior == 0:
            acumulador += actual
            restado = False
            if anterior == actual:
                if actual == 5:
                    raise ValueError(
                        "Tenemos el 5 reptido, no se puede proceder")
                else:
                    contador += 1
            else:
                contador = 1
        elif anterior in (5, 50, 500):
            raise ValueError("No se peude operar")
        elif contador > 1:
            raise ValueError(
                "No se puede operar un número mayor con varios repetidos anteriormente")
        elif 0 < anterior*10 < actual:
            raise ValueError("")
        else:
            if restado:
                raise ValueError("No se peude proceder, ya hemos restado")
            else:
                acumulador -= anterior
                acumulador += actual-anterior
                contador = 1
                restado = True
        anterior = actual
    return acumulador


print(convertir_a_numero(''))
# convertir_en_romano(3000)
