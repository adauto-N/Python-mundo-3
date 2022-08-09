'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma
tupla. No final, mostre:
a) Quantas vezes apareceu o valor 9
b) Em que posição foi digitado o primeiro valor 3
c) Quais foram os numeros pares
'''

if __name__ == "__main__":

    open = True
    i = 0

    while open:

        # Lógica de quebra do loop

        if i > 0: # depois da primeira iteração
            continuar = input('Deseja continuar ? y/n ').strip().upper()

            if (continuar == 'N') or ( continuar == 'NAO') or (continuar == 'NÃO'):
                open = False
                break # interrompe a iteração do while    

        # Lista pra receber os valores digitados
        valores = []

        # Testando se digita um int
            # Para o primeiro número:
        try:
            valores.append(int(input('Informe o primeiro valor inteiro: ')))

        except:
            print('Informe um numero inteiro valido')
            continue # quebra o laço while
        
        for j in range(0, 3):

            # Testando se digita um int
            try:
                valores.append(int(input('Informe outro valor inteiro: ')))

            except:
                print('Informe um numero inteiro valido')
                # Quebra o laço for e deixa o vetor de valores com o que foi digitado até então, caso digite um número inválido 
                break           
        
        # transforma de lista em tupla
        valores_tupla = tuple(valores)
        print('Valores informados: {}'.format(valores_tupla))

        # a) Quantas vezes apareceu o valor 9
        print("O numero 9 apareceu {} vezes".format(valores_tupla.count(9)))

        # b) Em que posição foi digitado o primeiro valor 3
        if 3 in valores_tupla:
            # Se o 3 não estiver na tupla dá erro.
            print("O numero 3 apareceu na {}ª posição a primeira vez".format(valores_tupla.index(3) + 1))
        else:
            print('O número 3 não foi informado.')

        # c) Quais foram os numeros pares
        pares = []
    
        for k in valores_tupla:
            if (k % 2) == 0:
                pares.append(k)

        pares_tupla = tuple(pares)

        if len(pares_tupla) > 0:
            print('Os numeros pares digitados foram:', end = ' ')
            for l in pares_tupla:
                print(l, end = ' ')
            print('\n')
        else:
            print('Não foram informados números pares.')

        i += 1

