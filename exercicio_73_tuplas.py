'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a) apenas os 5 primeiros colocados
b) Os últimos 4 colocados da tabela
c) Uma lista com os times em ordem alfabética
d) Em que posição da tabela está o time do Palmeiras
'''

colocacao = ('Palmeiras', 'Corinthians', 'Fluminense', 'Athletico - PR', 'Flamengo', 'Internacional', 'Atlético Mineiro', 
                'Bragantino', 'América - MG', 'Santos', 'São Paulo', 'Botafogo', 'Goiás', 'Ceará', 'Coritiba', 'Avaí', 'Fortaleza',
                'Cuiabá', 'Atlético Goiano', 'Juventude')
    
# 5 primeiros
a = colocacao[0:5]

# últimos 4
b = colocacao[-4:]

# ordem alfabética
c = sorted(colocacao)

# Posição Palmeiras
d = colocacao.index('Palmeiras') + 1
    
print('5 primeiros colocados: {}'.format(a))
print('4 últimos colocados: {}'.format(b))
print('Times em ordem alfabética: {}'.format(c))
print('O Palmeiras esta na {}ª posicao.'.format(d))
    