"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# try:
#     usu_int = int(input('Digite um Número: '))
#     if usu_int % 2 == 0:
#         print(f'Número {usu_int} = Par')
#     else:
#         print(f'Número {usu_int} = Impar')
# except:
#     print('Número digitado não e inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# try:  
#     hr_usu = int(input('Quantas horas?: '))

#     if hr_usu >= 0 and hr_usu <= 11:
#         print('Bom Dia')
#     elif hr_usu >= 12 and hr_usu <= 17:
#         print('Boa tarde')
#     elif hr_usu >= 18 and hr_usu <= 23:
#         print('Boa noite')
#     else:
#         print('Não conheço essa Hora')
# except:
#     print('Digite apenas Números')

"""
Faça um programa que peça o primeiro nome do usuário.Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
try:
    usu = str(input('Digite apenas seu primeiro nome: '))

    if len(usu) <= 4:
        print('Seu nome e curto')
    elif len(usu) >= 5 and len(usu) <= 6:
        print('Seu nome e Normal')
    else:
        print('Seu nome e muito grande')
except:
    print('Digite apenas Letras')


