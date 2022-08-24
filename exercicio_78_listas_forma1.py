'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
forma 1: puramente algoritimos
'''

valores = []

maior = 0
menor = 0

for i in range (0, 5):

    valores.append(float(input('Digite um número: ')))
    if i == 0:
        maior = menor = valores[i] # primeiro número digitado
    else:
        if valores[i] > maior:
            maior = valores[i]

        elif valores[i] < menor:
            menor = valores[i]

print('Os valores digitados foram: {}'.format(valores))
print('O maior valor digitado foi: {}, e se encontra no indice: '.format(maior), end = '')

'''
O print anterior se une com o print do índice, graças ao end = ''.
A vantagem de fazer assim é que se tiver mais que um valor maior (valores iguais), 
os índices de ambos serão printados
'''

for indice, item in enumerate(valores):
    if item == maior:
        print('{}...'.format(indice), end = ' ') # Se o valor for o maior, printa o índice
    
print() # pula linha
print('O menor valor digitado foi: {}, e se encontra no indice: '.format(menor), end = '')
    
# Mesma lógica anterior
for indice, item in enumerate(valores):
    if item == menor:
        print('{}...'.format(indice), end = ' ') 