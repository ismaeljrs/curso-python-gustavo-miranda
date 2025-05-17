# Peça ao usuário para digitar um número e mostre o resultado da divisão de 100 por esse número. Se o usuário digitar um valor que não seja um número ou tentar dividir por zero, trate o erro e exiba uma mensagem apropriada.
try:
    usu = int(input('Digite um número: '))
    r = usu / 100
    print(f'Reusltado e {r:.0f} .')
except ValueError:
    print('--'*10)
    print(f'Digite Apenas Números ERRO:{r}')
    print('--'*10)

# ----------------------------------------------



