''' Crie um programa que vai ler vários números e colocar em uma lista.                  
Depois disso, mostre:                                                                                                                                                
A) Quantos números foram digitados.                                                                                                                    
B) A lista de valores, ordenada de forma decrescente.                                                                                          
C) Se o valor 5 foi digitado e está ou não na lista.
'''

numeros = []

while True:
    try:
        numero = float(input('Digite um valor: '))
        numeros.append(numero)
    except:
        print('Numero invalido.')
    
    cont = input('Deseja continuar ? y/n ').strip().upper()
    if cont in ['N', 'NAO', 'NÃO', 'NO']:
        print('Encerrando')
        break

numeros.sort(reverse=True)

print(f'Foram digitados {len(numeros)} numeros.')
print(f'Os numeros em ordem decrescente sao: {numeros}')

if 5 in numeros:
    print(f'O numero 5 faz parte da lista!')
else:
    print(f'O numero 5 nao faz parte da lista!')