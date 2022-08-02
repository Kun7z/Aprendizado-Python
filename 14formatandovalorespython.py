"""

Formatando valores com modificadores 

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE) (> ou < ou ^)(QUANTIDADE)(tipo -s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num_1 = 10
num_2 = 3 
divisao = num_1 / num_2 

print(divisao) #Forma comum de apresentar o resultado da variavel, em que vai me apresentar o resultado da divisão enchuto, sem qualquer tipo de formatação

print('{:.2f}'.format(divisao)) #Formatação de valores através do .format, em que através .2f apresentará apenas 2 digitos após o .

print(f"{divisao:.2f}") #Formatação através de fstrings, utiliza o mesmo :.2f

####################


nome = 'Luiz Otávio' 
print(f'{nome:s}') #Estou utilizando o modificador :s por conta de que o valor é uma string, não estou formatando nada, apenas mostrando.


###################

num_1 = 1
print(f'{num_1:0>10}') #Nesse exemplo, estou formatando o número da minha variável num_1 para ter 10 casas preenchidas com 0 a esquerda, contando com o número que é mostrado na minha variável.

num_2 = 1150
print(f'{num_2:0>10}') #Outro exemplo, com mais caracteres de resultado da variável, mas que mostra a mesma quantidade de caracteres do outro exemplo, só é adicionado com menos 0, porque o total tem de ser 10 caracteres.

num_2 = 1150
print(f'{num_2:0<10}') #Caso eu queira botar para os zeros aparecerem a direita, só eu trocar o valor > para <, demonstrando que quero que os números apareçam a direita, depois da minha variável.

num_2 = 1150
print(f'{num_2:0>10.2f}') #Nesse exemplo estou combinando os modificadores .2f com o 0<10, para que seja utilizado apenas 2 casas depois da vírgula, e também que tenha um total de 10 caracteres, preenchidos com o número 0 
                          #depois da minha variável
                          
##################

nome = 'Otávio Miranda'
nome_formatado = '{:@>15}'.format(nome)  #Outra forma de formatar, no caso dentro das chaves {} vai estar a minha condição, minha formatação, dentro de aspas, e após o .format, vai ter a variável afetada pela formatação, nesse
                                         #caso a variavel nome.
print(nome_formatado)

#################


nome= 'eric matheus'

print(nome.lower()) # tudo minusculo
print(nome.upper()) # tudo maiúsculo
print(nome.title()) # Primeiras letras maiúsculas
