"""

Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.


"""

valor=(input (f'Digite um número inteiro: '))

if valor.isdigit():

    if '.' in valor or ',' in valor:
        print("Digite apenas números inteiros")
    
    elif int(valor)%2 == 0:
        print(f"O número {valor} é par")
    else:
        print(f"O número {valor} é ímpar")
else:
    print(f"Digite apenas números inteiros")
