operacao = input("Digite a operacao desejada 1-soma\n2-divisao\n3-subtraçao\n4-multiplicaçao\n")
numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")


if operacao == 1:
	resultado = int(numero1) + int(numero2)
	print("%d" % resultado)
	
if operacao == 2:
	resultado = int(numero1) - int(numero2)
	
if operacao == 3:
	resultado = int(numero1) * int(numero2)
	
if operacao == 4:
	resultado = int(numero1) / int(numero2)
	
else:
	resultado = "Operação não registrada"
    
print("O resultado da operação é: " + str(resultado))

