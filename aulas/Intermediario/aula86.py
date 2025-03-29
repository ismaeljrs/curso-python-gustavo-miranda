# interador que gerador de funcoes  em python  
# gerador  = (n for n in range (10000))


# yield pausa a execução da função, salvando seu estado, e pode continuar do mesmo ponto quando for chamado novamente.

#Você deve usar yield quando quiser criar um gerador para processar grandes quantidades de dados de forma eficiente, sem carregar tudo na memória de uma vez.
def contador():
    for i in range(3):
        yield i 
        print('Continuando')

gen = contador()

print(next(gen))
print(next(gen))
print(next(gen))
