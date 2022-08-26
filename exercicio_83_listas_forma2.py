'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos 
e fechados na ordem correta.
Forma 2: forma com pilhas
'''

pilha = []
# Expressão e processamento
expressao = input('Digite uma expressao matematica: ')
for caractere in expressao:
    if caractere == '(':
        pilha.append(caractere)
    elif caractere == ')': 
        if len(pilha)>0: # Se tiver '(' e caiu aqui, fechou o parentese
            pilha.pop() # Descarta 1 parentese fechado
        else:
            pilha.append(caractere) # Se cair aqui o parentese foi fechado sem abrir, indevido
            break

# Verificação
if len(pilha) == 0:
    print('Expressao valida')
else:
    print('Expressao invalida')