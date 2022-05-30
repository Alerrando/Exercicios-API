pesoP = float(input("Qual o peso do peixe:\n"))

if pesoP>50:
    pesoE = float(pesoP-50)
    Multa = float(pesoE*4.00)
    print("O peso excedente do peixe é %.2f, e a multa que tera de pagar é R$ %.2f\n" % (pesoE, Multa))

if pesoP<=50:
    print("Esta tudo nos conformes\n")

    