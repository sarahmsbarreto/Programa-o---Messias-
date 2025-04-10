numero = int(input('Digite o número da tabuada:'))

print ('----Solucao com FOR----')
for m in range(1,11):
    print(f'{numero} x {m} = {numero * m}')

print ('----Solucao com WHILE----')
ciclos = 1

while ciclos <=10:
    resultado = numero * ciclos
    print(f'{numero} x {ciclos} = {resultado}')
    #incremento
    ciclos += 1
