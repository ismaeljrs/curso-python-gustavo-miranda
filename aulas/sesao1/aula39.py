"""
Iterando uma String com while 

chat: execicio
Aqui está um exercício para você praticar a iteração de uma string usando while:
Exercício

Crie um programa que peça ao usuário para digitar uma palavra e, em seguida, exiba cada letra da palavra separadamente, uma por linha, utilizando um loop while.

📌 Bônus: No final, exiba também a palavra invertida.
"""
nome = 'Ismael'
max = ''
letras = ''
i = 0

while i < len(nome):
    max = nome[i]
    print(f'{letras}{max}')
    letras += max 
    i += 1
print(f'Nome invertido = {nome[::-1]}')


# --------------------------------------------------

