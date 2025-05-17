# Esse código mostra como usar *args para aceitar múltiplos argumentos sem precisar saber quantos.
# Usos práticos:
def relatorio_gols(*jogadores):
    total = len(jogadores)
    


    print(f'Toral de jogadores {total}')

relatorio_gols(1,0,3,4,5)
    





    