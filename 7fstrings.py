nome = 'Eric'
idade = 21 
altura = 1.80
e_maior = idade >=18
peso = 80
imc = peso/altura**2


#fstrings é a formatação de strings.


print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)  #sem fstring

print(f'{nome}, tem {idade} anos de idade e seu imc é {imc}') #com fstring, não é mais necessário botar aspas simples em cada texto, apenas no começo e no fim do texto, e as variáveis marcar com chaves {}.

#perceba que se você rodar o código, o IMC ainda vai te dar um resultado gigante de retorno com relação ao resultado da conta do IMC, mas queremos apenas 2 casas decimais após o ponto, para isso realizar o seguinte:

print(f'{nome}, tem {idade} anos de idade e seu imc é {imc:.2f}')

print('{} tem {} anos de idade e seu imc é {}'.format(nome,idade,imc))  #outra forma de formatar, em que cada {} é preenchido por uma variável, da esquerda para direita.

print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome,idade,imc))  #caso eu queira limitar a quantidade de números depois do ponto, apenas fazer que nem no outro.

print('{0} tem {1} anos de idade e seu imc é {2:.2f}'.format(nome,idade,imc)) #essa seria a ordem, 0, 1 e 2 de consulta

print('{2} tem {1} anos de idade e seu imc é {1}'.format(nome,idade,imc)) #caso eu queira alterar a ordem das variáveis é possível também. 



