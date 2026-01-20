def contador_vogais(texto: str) -> int:
    """Conta o número de vogais em uma string.

    Parâmetros:
        texto (str): A string a ser analisada.

    Retorna:
        int: O número de vogais na string.
    """

    vogais = "aeiou"
    contador = 0
    for char in texto.lower():
        if char in vogais:
            contador += 1
    return contador