"""

Função len me retorna a quantidade de caracteres de uma string
Não funciona com objetos de classe inteiro ou float 
O valor retornado da função len, é informado em classe int, pois retorna a quantidade de caracteres 
Pode ser usado uma função para contar, subtrair, dividir, etc estes caracteres.


"""



usuario = input ('Digite seu usuário: ')
qtd_caracteres = len(usuario)
#print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print('Você precisa digitar pelo menos 6 caracteres.')
else:
    print('Você está cadastrado.')


string1 = input("Digite alguma coisa: ")
string2=input("Digite outra coisa: ")
print(f'A quantidade total de caracteres digitados foi {len(string1) +len(string2)}')


print(len(string2))
print(string2.__len__())