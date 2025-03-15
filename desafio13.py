wage = float(input('Coloque seu Salario: R$'))
increase = float(input('Insira o valor do aumento: '))

print(f'Seu salario atual: {wage:.2f}')

newWage = wage * (increase/100)
print(f'Seu aumento sera de: {newWage:.2f}')
print(f'Seu  novo salario é: {wage + newWage :.2f}')