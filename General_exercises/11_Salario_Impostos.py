a = float(input('Digite quanto você ganhar por hora : '))
b = float(input('Digite quantas horas voce trabalha por mês : '))

x = a * b
print(f'+ SALÁRIO BRUTO : {x}')

x = (a * b) * 0.11
print(f'- IR(11%) : {x}')

x = (a * b) * 0.08
print(f'- INSS(8%) : {x}')

x = (a * b) * 0.05
print(f'- SINDICATO(5%) : {x}')

x = (a * b) * 0.76
print(f'+ SALÁRIO LIQUIDO : {x}')
