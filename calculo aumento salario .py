salario = imput('Digite seu salário')
porcentagem = imput('Digite a porcentagem de aumento')
aumento = (porcentagem / 100) * salario
salarionovo = salario + aumento
print(f'Valor de aumento é de: R${aumento}')
print(f'Valor do novo salário é de: R${salarionovo}')