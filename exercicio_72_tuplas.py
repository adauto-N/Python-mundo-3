''' 
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de 0 a 20.
    Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso
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
        
        # Lógica do problema

        numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
                    'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

        try:
            n = int(input('Digite um numero entre 0 e 20 \n'))

        except:
            print('Informe um numero inteiro valido')
            continue

        if (n >= 0) and (n <= 20):
            # output
            print(numeros[n])

        else:
           print('Número fora do intervalo.')
        
        i += 1