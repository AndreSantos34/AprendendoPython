preco = float(input('Coloque o preço do produto: '))

print(f'Seu produto custa: R$ {preco:.2f}')

newPreco = preco - (preco * 5/100)
print(f'\n Então com seu desconto de 5% seu novo preço sera:{newPreco:.2f}')