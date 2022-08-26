'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos 
e fechados na ordem correta.
Forma 1: forma algoritimica que desenvolvi
'''
abriu = 0
fechou = 0

# Expressão e processamento
expressao = input('Digite uma expressao matematica: ')
for caractere in expressao:
    if caractere == '(':
        abriu += 1
    elif caractere == ')' and abriu != fechou: # Previne o caso )x+y(
        fechou += 1

# Verificação
if abriu == fechou:
    print('Expressao valida')
else:
    print('Expressao invalida')