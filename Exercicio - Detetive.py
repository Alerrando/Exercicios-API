resp = (input("Você telefonou para a vitima?\n"))
resp = (input("Você esteve no local do crime?\n"))
resp = (input("Você perto da vitima?\n"))
resp = (input("Devia para a vitima?\n"))
resp = (input("Já trabalhou com a vitima?\n"))

if resp == 'sim':
    cont+=1
    
        if cont == '2':
            print("Você é um suspeito")
        
        if resp == '3' and resp == '4':
            print("Você é um cumplice")
        
        if resp == '5':
            print("Você é o assasino")
            
if resp == 'nao':
    cont2+=1
        if cont2 == '4':
            print("Você é inocente")
            
        if cont2 == '5':
            print("Você é inocente")