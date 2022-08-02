"""

Built-in 

Distribuições padrões do Python contém um grande número de módulos, geralmente conhecidos como módulos built-in. Cada módulo built-in contém recursos para certas funcionalidades específicas como gerenciamento de sistema
operacional, gerenciamento de disco, rede, conectividade de banco de dados e etc.


"""

num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")

if num1.isdigit() and num2.isdigit():  #módulo .isdigit retorna True se todos os dígitos são decimais e a sequência não é vazia.     
    num1=int(num1)
    num2=int(num2)  #transforma os números de classe de string para inteiro, pois todo valor retornado de uma variável vem em string.
    
    print(num1+num2)
else:
    print("Não pude converter os números para realizar as contas.")