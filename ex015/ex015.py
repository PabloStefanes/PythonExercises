km = float(input('Quantos Km rodados? '))
dia = int(input('Quantos dias alugado? '))
pago = (dia*60)+(km*0.15)
print(f'O total a pagar é de {pago:.2f}')