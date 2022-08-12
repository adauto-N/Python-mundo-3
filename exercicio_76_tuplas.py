'''
Crie um programa que tenha uma tupla única com nomes de 
produtos e seus respectivos preços, na sequência. No final, mostre uma listagem 
de preços, organizando os dados em forma tabular.
'''

if __name__ == "__main__":
    
    compras = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 10.00, 'Estojo', 20.00)

    for i in range(len(compras)):
        if i % 2 == 0: # indice par
            print('{:.<30}'.format(compras[i]), end = '')
            
        else: # índice impar
            print('R$ {:>5}'.format(compras[i]))
