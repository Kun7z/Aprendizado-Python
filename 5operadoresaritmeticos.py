"""

Operadores são:

+  = soma
-  = subtração
*  = multiplicação
/  = divisão 
// = divisão inteira, sem ponto flutuante, arredondando.
** = exponenciação, potenciação, um número elevado a outro.
%  = Não é porcentagem, retorna o módulo, o resto da divisão entre um número e outro.
() = Alterar a precedência nas contas.

"""



print(10*10)  #Vai multiplicar

print(10*'10') #Vai fazer com que apareça 10 vezes o número 10, pois está multiplicando o número inteiro 10, com uma string escrita em texto 10.

print('5'+'5') #Vai fazer com que apareça os valores impostos em type string duas vezes, somados. 

print(10.5 // 3) #Vai retornar um valor arredondado inteiro.

print (10.5 / 3) # Vai retornar o exato valor da divisão.

print (2**10) #2^10, dois elevado a 10, potenciação.

print (10 % 5) #10 dividido por 5 da 2, porém essa divisão não possui resto. 2*5 vai dar 10 inteiro, logo resultado o módulo vai dar 0. Mas caso seja um valor que não seja 0, vai retornar essa resposta.

print(5+2*10) #Vai estar realizando a conta na ordem matemática correta, primeiro multiplicação, depois a somatória, resultando 25.
print((5+2)*10)#Com o parênteses altera a precedência da conta, somando primeiro o que está entre parenteses e depois multiplicando o resultado por 10. 