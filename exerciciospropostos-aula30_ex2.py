"""
Faça um programa que pergunte a hora ao usuário e baseando-se no horário descrito, exiba a saudação aproriada. Ex:
Bom dia 0~11, Boa tarde 12~17 e Boa noite 18~23.

"""

horario=input(f'Qual o horário atual?')

if horario.isdigit():
    if int(horario) <=11:
        print(f"Bom dia")
    elif int(horario) >=18:
        print(f"Boa noite")
    else:
        print(f"Boa tarde")
else:
    print("Digite apenas um horário com valor inteiro")