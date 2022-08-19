''' 
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de 0 a 20.
    Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso
'''

if __name__ == "__main__":

    while True:
        
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
        
        continuar = input('Deseja continuar ? y/n ').strip().upper()

        if continuar in ['N', 'NAO', 'NO', 'NÃO']:
            break # interrompe a iteração do while