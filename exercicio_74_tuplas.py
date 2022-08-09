'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois, mostre a listagem de números gerados e também indique o menor e o maior
valor que estão na tupla.
Obs: Como tuplas são imutáveis, não existe append()
'''

import random as rd

if __name__ == "__main__":

    # Criando uma lista pra receber o sorteio e depois passar de lista pra tupla
    sorteio = []
    numeros_aleatorios = ()

    for i in range(0, 5):

        sorteio.append(rd.randint(1, 10))
        # print(sorteio)

    numeros_aleatorios = tuple(sorteio)

    print('Numeros gerados: {}'.format(numeros_aleatorios))
    print('Maior valor sorteado: {}'.format(max(numeros_aleatorios)))
    print('Menor valor sorteado: {}'.format(min(numeros_aleatorios)))

    