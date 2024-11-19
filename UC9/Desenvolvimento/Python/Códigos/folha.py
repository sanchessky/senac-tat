salario = float(input("Digite seu salário e tecle Enter"))


if salario <= 280:
    valor_aumento = salario *(20.0/100)
    novo_salario = salario + valor_aumento
    print(f"o salário antigo é {salario} e foi ajustado em 20%. E o valor do aumento é {valor_aumento} e o novo salário é de {novo_salario}")

elif salario <= 700:
    valor_aumento = salario *(15.0/100)
    novo_salario = salario + valor_aumento
    print(f"o salário antigo é {salario} e foi ajustado em 15%. E o valor do aumento é {valor_aumento} e o novo salário é de {novo_salario}")
    
elif salario <= 1500:
    valor_aumento = salario *(10.0/100)
    novo_salario = salario + valor_aumento
    print(f"o salário antigo é {salario} e foi ajustado em 10%. E o valor do aumento é {valor_aumento} e o novo salário é de {novo_salario}")

else :
    valor_aumento = salario *(5.0/100)
    novo_salario = salario + valor_aumento
    print(f"o salário antigo é {salario} e foi ajustado em 20%. E o valor do aumento é {valor_aumento} e o novo salário é de {novo_salario}")
    