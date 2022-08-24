'''Crie um programa onde o usuário possa digitar cinco valores 
numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). 
No final, mostre a lista ordenada na tela.
'''

valores = []

for i in range(0, 5):

    valor = float(input('Digite um valor: '))

    if i==0 or valor>valores[-1]:  # Se for a primeira iteração ou o maior valor 
        valores.append(valor)
        print('Adicionado ao final da lista... ')

    elif valor < valores[0]: # O menor é sempre a primeira casa da lista
            valores.insert(0, valor) # Insere o valor na primeira casa
            print('Adicionado ao posição 0 da lista... ')

    else:
        for idx in range(0, len(valores)): # Se chegou aqui, o valor é maior que alguém e menor que alguém. Basta percorrer uma das condições
            if valor > valores[idx]: 
                    posicao = idx + 1 # Insere a direita do número
        valores.insert(posicao, valor) 
        print(f'Adicionado na posição {posicao} da lista')

print(f'Lista final ordenada: {valores}')
