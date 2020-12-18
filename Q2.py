'''
[Questão criada por Pedro Vinicius (adaptada)] Crie um programa que leia o nome de n jogadores, o time que joga,
a quantidade de partidas que eles jogaram, a quantidade de gols feitos em cada partida e o total de gols.
Essas informações serão armazenadas em um dicionário.
O programa apresentará no final todas as informações dos jogadores e um ranking com os top 3 com mais gols. 
'''
gol = list()
jogador = dict()
clube = list()
lista=[]


while True:
    jogador['Nome'] = str(input('Nome do Jogador: ')).strip()
    jogador["time"]=str(input("time que joga:"))
    par = int(input(f'Quantas Partidas {jogador["Nome"]} jogou? '))

    if par > 0:
        for c in range(0, par):
            gol.append(int(input(f' --Quantos gols na {c+1}º partida? ')))
        jogador['Gols'] = gol[:]
        jogador['Total'] = sum(gol)
    clube.append(jogador.copy())

    while True:
        cont = str(input('Deseja Inserir outro Jogador? [S/N]')).upper().strip()[0]
        if cont in 'SN':
            jogador.clear()
            gol.clear()
            break
        print('Opção inválida! Tente novamente.')
    if cont == 'N':
        break
print('-='*20)
print(f'{"time":<10}{"NOME":<20}{"Total":<20}{"Gols":<20}')
for i, j in enumerate(clube):
    print(f'{j["time"]:<10}{j["Nome"]:<20}{j["Total"]:<20}{j["Gols"]}')
print('-='*20)
print(' ')

print('Selecione 3 valores dos totais de gols para ser feito um ranking(não precisa ser em ordem, o programa fará isso)')
for c in range(0,3):
    n=int(input('Insira 1 total de gols da tabela acima:'))
    if c == 0 or n> lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                break
            pos += 1

print('O 3º lugar fica com o jogador com',lista[0], 'gols')
print('O 2º lugar fica com o jogador com',lista[1], 'gols')
print('O 1º lugar fica com o jogador com',lista[2], 'gols')

