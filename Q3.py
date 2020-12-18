'''
[Questão criada por Myllena Laís (adaptada)] Um novo funcionário de supermercado quer saber em qual corredor se encontra um produto. 
No sistema existem os seguintes produtos: 
Arroz - corredor 1, Feijão - corredor 1, Óleo de soja - corredor 2, Sal - corredor 3, Açúcar - corredor 3,
 Café- corredor 4, Molho de tomate -corredor 5, Macarrão- corredor 6. 
 O funcionário precisa encontrar em qual corredor está o produto para ajudar o cliente em sua compra. Use tupla para criar esse programa.
'''

produtos =('Arroz','correrdor 1','Feijão','correrdor 1','oléo de soja','correrdor 2','sal','correrdor 3','açúcar','correrdor 3',
'café','correrdor 4','molho de tomate','correrdor 5','macarrão','correrdor 6')


print('='*30)
for i in range(0,len(produtos)):
    if i % 2 == 0:
        print(f'{produtos[i]:.<30}', end='')
    else:
        print(f' {produtos[i]:>5}')
print('='*30)
