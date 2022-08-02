"""
str - string
"""

#string é um texto dentro de aspas

#print(alguma coisa)
#vai dar erro na leitura desse comando, devido ao fato de que a parte, alguma coisa não é detectado como um texto


print('alguma coisa')
#agora o python ele entende que o alguma coisa é uma string e te informa o texto
#obs: a string pode ser tanto aspas duplas como aspas simples.

print(123456)
#o python nesse comando entende que não é uma string, e sim a uma variável.

print('Essa é uma string (str).')

print("Essa é uma 'string' (str).")

#também pode ser feito a string através de aspas duplas, fazendo com que seja possível utilizar aspas simples no meio do texto

print("Esse é meu \"texto\" (str).")

#Pode ser utilizado o caráctere de escape, sendo o \, fazendo com que ele ignore as aspas duplas para fechar o comando no meio. 


print('Esse é meu \n (str).')
#Nesse comando, o barra invertida não ignora o n, e o python entende que \n = quebra de linha, fazendo com que a string apareça em 2 linhas


print(r'Esse é meu \n (str).')
#Uma solução seria botar o r na frente da string para fazer com que o interpretador do python entenda que ele quer que tudo na string seja executado ao pé da letra. r = raw.






