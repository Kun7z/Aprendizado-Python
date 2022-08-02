"""

Tipos de dados
str - string = textos 'Assim' "Assim";
int - inteiro = 123456 0 -10 -20 -30 1500 = Qualquer número positivo ou negativo inteiro;
float - real/ponto flutuante = 10.5 -1.5 2.0 3,56 0.0 = Qualquer número positivo ou negativo com ponto, um ponto flutuante;
bool - booleano/lógico - Verifica a lógica das coisas = Apenas dois valores - True/False 10 == 10

"""

print('Luiz')  #interpretador do Python, já identifica que isso é uma string 
print('Luiz', type('Luiz'))  #função type retorna o tipo de classe, nesse caso retornando ser uma class str.


print('10', type('10'))  #interpretador do Python identifica que isso é uma string, caso eu queira realizar uma conta, ele não vai entender, se quiser botar valores de números, tem de ser sem aspas.

print(10, type(10))  #interpretador entende que isso é uma classe int, por ser um valor inteiro.

print(25.23, type(25.23)) #interpretador entende que isso é uma classe float, por ser um valor de ponto flutuante.

print(10 == 10, type(10 == 10)) #interpretador do python, entende que isso é classe bool. Dando valor true.

print(10 == 9, type(10 == 10)) # Interpretador do python, entende que isso é uma classe bool. Dando valor False.


#Mais sobre os valores booleanos. 

print(bool()) #Retorna o valor falso quando está vazio.
print('luiz',type('luiz'), bool('Luiz')) #Qualquer valor escrito, se não houver comparativo vai dar valor true. 
#também perceba que convertemos o tipo de classe, de string para booleano. 


#DESAFIO: Realizar um cadastro com Nome, idade, altura e se é maior de idade, mostrando os tipos de classe.


print('Eric', type('Eric'))
print(21, type(21))
print(1.80,type(1.80))
print(21>=18,type(21>=18))