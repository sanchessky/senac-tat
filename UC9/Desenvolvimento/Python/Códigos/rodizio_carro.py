
placa = int(input('Digite o final da placa do veículo:'))

if placa==1 or placa==2:
    print("Esse carro não pode rodar na Segunda-feira")
elif placa==3 or placa==4:
    print('Esse carro não pode rodar na Terça-feira')
elif placa==5 or placa==6:
    print('Esse carro não pode rodar na Quarta-feira')
elif placa==7 or placa==8:
    print('Esse carro não pode rodar na Quinta-feira')
elif placa==9 or placa==0:
    print('Esse carro não pode rodar na Sexta-feira')
else:
    print('Placa inválida')