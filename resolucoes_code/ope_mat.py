# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

num1 = int(input("Digite um número: ")
num2 = int(input("Digite outro número: ")

operacao = input("Digite a operação que deseja realizar: ")

if operacao == "+":
  print(num1 + num2) 
elif operacao == "-":
  print(num1 - num2) 
elif operacao == "*":
  print(num1 * num2) 
elif operacao == "/":
  print(num1 / num2) 
else 
  print("Operação inválida")
