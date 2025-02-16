palavra = input("Digite uma palavra: ").strip().lower()

inversa = palavra[::-1]

if palavra == inversa:
  print("É um palíndromo")
else:
  print("Não é um palíndromo.")

