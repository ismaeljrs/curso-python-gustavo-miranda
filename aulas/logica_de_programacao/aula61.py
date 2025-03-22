# CPF = '746.824.940-70'

# codigo_limpo =  CPF.replace('.','').replace('-','')
# print(type(codigo_limpo))
# digito = int(codigo_limpo)
# print(type(digito))

# print(digito)

# soma = 10
# for digito in range(10,1,-1):
#     print(len(digito))
def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)
    
    
multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)
print('intermediario')
