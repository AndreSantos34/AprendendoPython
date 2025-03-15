kmPercorrido = float(input('Insira o valor do km percorrido: '))
dias = float(input('Insira quantos dias foi usado o Carro: '))

print(f'Voce usou o carro por {dias} e percorreu {kmPercorrido} '
      f'logo o valor a pagar sera de: R$ {(kmPercorrido * 0.15) + (dias * 60):.2f}')