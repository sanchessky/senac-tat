#media escolar
media = float(input('Digite a nota média do aluno:'))

if media >= 6:
    print(f"O aluno com a nota {media} está APROVADO ")
elif media <= 4:
    print(f'O aluno com a nota {media} está REPROVADO ')
else:
    print(F'O aaluno com a nota {media} está de RECUPERAÇÃO')