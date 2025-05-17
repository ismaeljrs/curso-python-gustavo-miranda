try:
    pri_val = int(input('Digite o Primeiro valor: '))
    seg_val = int(input('Digite o Primeiro valor: '))

    if pri_val == seg_val:
        print('Valores iguais')
    elif pri_val > seg_val:
        print(f'{pri_val} e maior que {seg_val} ')
    elif pri_val < seg_val:
        print(f'{seg_val} e maior que {pri_val} ')
except:
    print('Voce não digitou nem e primeiro nem o segundo')

