'''Crie um programa onde o usuário possa digitar sete valores numéricos 
e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final,
 mostre os valores pares e ímpares em ordem crescente.
'''
numeros = [[], []]

for i in range(0, 7):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

# cadastro 
print(f'Lista de numeros {numeros}')
print(f'Pares em ordem crescente: {sorted(numeros[0])}')
print(f'Impares em ordem crescente: {sorted(numeros[1])}')