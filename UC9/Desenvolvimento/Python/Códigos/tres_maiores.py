numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número:"))
numero3 = int(input("Digite outro número:"))
if numero1 > numero2 > numero3:
    print(f"O valor {numero1} digitado é maior ")
elif numero2 > numero1 > numero3:
    print(f"O valor {numero2} digitado é maior ")
else: 
    print(f"O valor {numero3} digitado é maior")
