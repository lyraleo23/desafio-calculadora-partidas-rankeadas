
def calcular_ranking(quantidade_vitorias, quantidade_derrotas):
    saldo_rankeadas = quantidade_vitorias - quantidade_derrotas
    nivel_heroi = 'Desconhecido'

    if (saldo_rankeadas <= 10):
        nivel_heroi = 'Ferro'
    elif (saldo_rankeadas > 10 and saldo_rankeadas <= 20):
        nivel_heroi = 'Bronze'
    elif (saldo_rankeadas > 20 and saldo_rankeadas <= 50):
        nivel_heroi = 'Prata'
    elif (saldo_rankeadas > 50 and saldo_rankeadas <= 80):
        nivel_heroi = 'Ouro'
    elif (saldo_rankeadas > 80 and saldo_rankeadas <= 90):
        nivel_heroi = 'Diamante'
    elif (saldo_rankeadas > 91 and saldo_rankeadas <= 100):
        nivel_heroi = 'Lendário'
    
    return print(f'O Herói tem saldo de {saldo_rankeadas} está no nível de {nivel_heroi}')

quantidade_vitorias = input('Digite a quantidade de vitórias: ')
quantidade_derrotas = input('Digite a quantidade de derrotas: ')

try:
    calcular_ranking(quantidade_vitorias, quantidade_derrotas)
except:
    print('Erro ao calcular o ranking')
