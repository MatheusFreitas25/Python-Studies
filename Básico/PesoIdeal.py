a = float(input('Digite sua altura : '))
b =  input('Digite seu sexo: (F) para feminino (M) para masculino : ')

while b != 'F' and b != 'M':
    print('Entrada invalida')
    b = input('Digite seu sexo: (F) para feminino (M) para masculino : ')
if b == 'M':
    peso = (72.7*a) - 58
    print(f'Peso ideal = {peso:1.2f}')
elif b == 'F':
    peso = (62.1*a) - 44.7
    print(f'Peso ideal = {peso:1.2f}')

