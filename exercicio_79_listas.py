'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores 
únicos digitados, em ordem crescente.
'''

if __name__ == "__main__":

    numeros = []
    

    while True: # Loop infinito
                
        try:
            numero = float(input('Informe um numero: '))
            if numero not in numeros:
                numeros.append(numero)
            else:
                print('Numero ja informado anteriormente.')
        except:
            print('Numero invalido.')
        
        continuar = input('Deseja continuar? y/n: ').strip().upper() # corta os espaços e joga pra maiúsculas
        if continuar in ['N', 'NAO', 'NO', 'NÃO']:
            break

    print(f'Os numeros informados sem repeticao foram: {numeros}') # printa ao fim do loop
    print(f'Numeros ordenados de forma crescente: {sorted(numeros)}')