turno=input("digite a letra m ou v ou n para saber o seu turno: ")

if turno== 'm' or turno== 'M':
    print(f"o seu turno digitado a cima {turno} é matutino, Bom dia")
elif turno== 'v' or turno== 'V':
    print(f"o seu turno digitado a cima {turno} é vesperino, Boa tarde")
elif turno == 'n' or turno== 'N':
    print(f"o turno digitado a cima {turno} é noturno, Boa noite")
else:
    print(f"turno digitado {turno} nao existe")