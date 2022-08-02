print(123456)
print('Eric','Luiz','Outra coisa')

#print demonstra as coisas em tela, da pra usar para debuggar também


print('Luiz', 'Otávio', sep='-')
print('João', 'e', 'Maria', sep='-')

#por padrão, as funções separadas por vírgulas são separadas por espaços, mas com o comando sep, eu posso definir o que eu quero que seja utilizado para separar, na string acima foi definido -

print('Luiz', 'Otávio', sep='-', end='')
print('João', 'e', 'Maria', sep='-', end='')

#comando end determina o que vai acontecer ao término desse print, por padrão ocorre uma quebra de linha, mas se eu quiser, posso deixar sem espaço que vai continuar direto a próxima string na mesma linha.

print('Luiz', 'Otávio', sep='-', end='######')
print('João', 'e', 'Maria', sep='-')

#aqui boto as cerquilhas no final do end, para separar as duas strings por cerquilhas, que continuam na mesma linha 


#DESAFIO:

#Fazer com que apareça o CPF 824.176.070-18 através do comando print 


print('CPF:', end=' ')
print('824','176','070', sep='.',end='-')
print('18')