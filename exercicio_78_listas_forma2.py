'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
Forma 2: usando métodos do python
'''

valores = []

for i in range (0, 5):
    try:
        valores.append(float(input('Digite um número: ')))
    except:
        print('valor inválido.') # interrompe o laço
        break
    
maior = max(valores)
menor = min(valores)
print('Os valores digitados foram: {}'.format(valores))
print('O maior valor digitado foi: {}, e se encontra no indice: {}'.format(maior, valores.index(maior)))
print('O menor valor digitado foi: {}, e se encontra no indice: {}'.format(menor, valores.index(menor)))