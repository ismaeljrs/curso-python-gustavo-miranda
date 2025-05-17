#escopo de funções em Python

jogador = 1 

def escopo(): #escopo global 
    #global jogador <- nao e interesante fazer assim ok não faça assim
    jogador = 7
    print(jogador)
    def outra_funcao():# escopo local so vai poder ultilizar aqui 
        jogador = 9
        colete = 'Azul'
        print(jogador)
        print(colete)
    outra_funcao()
print(jogador)
escopo()
print(jogador)
    


    
