# execicio aula 

nom_usu = str(input('Qual e o seu Nome: '))
ida_usu = int(input('Qual e a sua idade: '))


if nom_usu == "" and ida_usu.isdigit():
    print('Desculpe')
else:
    print(f'Nome: {nom_usu}')
    print(f'Nome invertido: {nom_usu[::-1]}')
    if ' ' in nom_usu: 
        print('Contem ESPAÇOS ')
    else:
        print('Não contem ESPAÇOS ')
    print(f'Seu nome tem {len(nom_usu)} letras.')
    print(f'Sua primeira letra e {nom_usu[0]}')
    print(f'Sua primeira letra e {nom_usu[-1]}')

