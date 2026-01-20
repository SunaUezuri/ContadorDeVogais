from contador_vogais import contador_vogais

texto: str = input("Digite um texto: ")
vogais: int = contador_vogais(texto)

print(f"O número de vogais no texto é: {vogais}")