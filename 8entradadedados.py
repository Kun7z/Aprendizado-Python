"""
Entrada de dados 

"""


nome = input("Qual o seu nome? ")
idade = input("Qual sua idade? ")
ano_nascimento = 2022-int(idade)
print()
print(f'O usuário digitou {nome} e o tipo de variável é '
      f'{type(nome)}')
      
#obs: Sempre que o usuário digitar algo no comando input, será uma string, mesmo que eu digite um número inteiro ou um número quebrado. 

print()
print(f'O usuário {nome} tem idade de {idade} anos. '
      f' {nome} nasceu em {ano_nascimento}.')
      
      
      
      

