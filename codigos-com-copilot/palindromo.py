palavra = input("Digite uma palavra: ")

if palavra == palavra[::-1]:
    print(f"'{palavra}' é um palíndromo")
else:
    print(f"'{palavra}' não é um palíndromo")
    print(f"A palavra invertida é: '{palavra[::-1]}'")