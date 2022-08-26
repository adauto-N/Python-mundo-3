'''Crie um programa que vai ler vários números e colocar em uma lista.
 Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores 
 ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''
valores = []
pares = []
impares = []

while True:

    # Leitura
    try:
        valores.append(float(input('Digite um numero: ')))
    except:
        print('Numero invalido. . .')

    # Quebra de loop
    continuar = input('Deseja continuar? y/n').strip().upper()
    if continuar in ['N', 'NAO', 'NÃO', 'NN']:
        break

# Pares e ímpares
for v in valores:
    if (v%2) == 0:
        pares.append(v)
    else:
        impares.append(v)
        
# Prints
print(f'Valores digitados: {valores}')
print(f'Valores pares: {pares}')
print(f'Valores impares: {impares}')