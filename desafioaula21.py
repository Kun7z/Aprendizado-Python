"""
* Criar variáveis para nome (str), idade(int),
* Altura (float) e peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)

"""


nome = 'Eric'
idade = 22
altura = 1.80
peso = 80.0
ano = 2022
anonascimento = ano-idade 
#IMC = Peso ÷ Altura²
imc = peso/altura**2

print(f'Nome:{nome}')
print(f'Idade:{idade}')
print(f'Altura:{altura}')
print(f'Peso: {peso}')
print(f'Ano Atual:{ano}')
print(f'Ano de nascimento:{anonascimento}')
print(f'IMC = {imc:.2f}')




