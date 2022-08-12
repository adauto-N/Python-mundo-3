'''
Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras 
(não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

'''

words = ('Praticar', 'Produzir', 'Procastinar', 'Dormir', 'Comer', 'Programar', 'Chorar')

for word in words:

    print('Na palavra {} temos as vogais:'.format(word), end = ' ')

    for letter in word: # para cada letra da palavra vou checar se é vogal
        if letter.strip().lower() in 'aeiou':
            print(letter, end = ' ')
    print('\n')
