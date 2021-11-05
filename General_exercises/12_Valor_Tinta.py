a = float(input('Informe quantos metros quadrados tem a área a ser pintada : '))

qntd = a/3

print(f'Será necessário {qntd} Litros de tinta')
print('Cada 18 litros custa R$80.00')

qntd2=qntd/18
valor = qntd2 * 80

print(f'Será necessário {qntd2} Lata(s) de tinta no valor de R${valor}')
