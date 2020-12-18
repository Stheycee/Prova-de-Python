'''
[Questão criada por Nicolas Mathias (adaptada)] Josemar trabalha numa revendedora de carros usados a cada 
carro vendido ele ganha 1,5 % de comissão. Utilizando lista composta guarde o nome e preço dos carros. 
Para vender o carro mostre uma tabela com os carros e os preços. Quando o carro for vendido deve modificar a lista de carros para vendido. 
A venda acaba quando os carros acabarem ou quando a pessoa não quiser continuar.
No final mostre: quantidade de carros vendidos e quanto Josemar lucrou no final em reais. Para essa questão use pelo menos duas funções. *
'''

def menu():
    print('='*30)
    print('*'*5,'REVENDEDORA DE CARROS','*'*5)
    print( 'Carros disponiveis')
    for c in carros:
        print(f'{c[0]} ------- R$ {c[1]}')
    print('='*30)

def menuvendido():
    print('=-'*30)
    for c in carros:
        print(f'{c[0]} ------- R$ {c[1]}')
    print('=-'*30)



carros = [['1-uno', 16000], ['2-Onix', 45000],
          ['3-fusca', 10000], ['4-Logan', 40000]]
vendidos = []
lucro = float(0)

menu() 

while True:
    escolha = int(input('Qual carro você deseja?'))
    if escolha == 1:
        lucro += 0.015 * carros[0][1]
        vendidos.append(carros[0:])
        carros[0] = 'V.'
    if escolha == 2:
        lucro += 0.015 * carros[1][1]
        vendidos.append(carros[1:])
        carros[1] = 'V.'
    if escolha == 3:
        lucro += 0.015 * carros[2][1]
        vendidos.append(carros[2:])
        carros[2] = 'V.'
    if escolha == 4:
        lucro += 0.015 * carros[3][1]
        vendidos.append(carros[3:])
        carros[3] = 'V.'
    if len(vendidos) == 4:
        break
    continua = str(input('Deseja continuar?(s/n)'))
    if continua == 'n':
        break
    menuvendido()

print('-'*30)
print(f'Josemar vendeu: {len(vendidos)} carro(s)')
print('Josemar lucrou com as vendas: R$', lucro)
print('-'*30)