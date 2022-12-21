'''Faça um programa que leia nome e peso de várias pessoas,                                      
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas. 
C) Uma listagem com as pessoas mais leves.
'''
cadastro = []
pessoa = []
mais_pesadas = []
mais_leves = []
soma_pesos = 0.0

while True:
    nome = input('Qual o seu nome? ')
    try:
        peso = float(input('Qual o seu peso? '))
    except:
        print('Numero invalido.') # Caso não digite um numero
        break
    pessoa.append(nome)
    pessoa.append(peso)
    cadastro.append(pessoa[:]) # Armazena uma cópia dos dados da pessoa na lista cadastro, evitando uma ligação entre os dados
    pessoa.clear() # Reseta a lista de pessoas, que é temporária

    soma_pesos += peso 
    
    continuar = input('Deseja continuar ? y/n ').strip().upper()
    if continuar in ['N', 'NAO', 'NãO', 'NN']:
        break

# A) 
print(f'Foram cadastradas {len(cadastro)} pessoas')

# B)
media_de_pesos = soma_pesos/len(cadastro)

for registro in cadastro: 
    if registro[1] > media_de_pesos: # registro[1] corresconde a informação de peso, registro[0] corresconde a informação de nome
        mais_pesadas.append(registro[0])
    elif registro[1] < media_de_pesos:
        mais_leves.append(registro[0])

print(f'A media de pesos foi: {media_de_pesos} ')
print(f'As pessoas mais pesadas foram: {mais_pesadas} ')

# C)
print(f'As pessoas mais leves foram: {mais_leves} ')