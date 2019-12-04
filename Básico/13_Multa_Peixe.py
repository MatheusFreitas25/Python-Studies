a = float(input('Digite quantos klg de peixe foi pescado : '))
b = 50

if a > b:
    multa= (a-b) * 5
    print(f'Multa de R${multa}')
elif a < b:
    print('Não possui multa !')
