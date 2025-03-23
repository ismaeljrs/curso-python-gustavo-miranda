def determinante(matriz, n):
    if n == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    elif n == 3:
        return (matriz[0][0] * (matriz[1][1] * matriz[2][2] - matriz[1][2] * matriz[2][1])
                - matriz[0][1] * (matriz[1][0] * matriz[2][2] - matriz[1][2] * matriz[2][0])
                + matriz[0][2] * (matriz[1][0] * matriz[2][1] - matriz[1][1] * matriz[2][0]))
    elif n == 4:
        det = 0
        for i in range(4):
            submatriz = [[matriz[j][k] for k in range(4) if k != i] for j in range(1, 4+1)]
            det += ((-1) ** i) * matriz[0][i] * determinante(submatriz, 3)
        return det

def substituir_coluna(matriz, coluna, termos, n):
    nova_matriz = [linha[:] for linha in matriz]
    for i in range(n):
        nova_matriz[i][coluna] = termos[i][0]
    return nova_matriz

def cramer(n, A, B):
    if len(A) != n or any(len(linha) != n for linha in A) or len(B) != n:
        return "Erro: Matrizes mal definidas"
    
    det_A = determinante(A, n)
    if det_A == 0:
        return "Sistema sem solução única"
    
    solucoes = []
    for i in range(n):
        Ai = substituir_coluna(A, i, B, n)
        solucoes.append(determinante(Ai, n) / det_A)
    
    return tuple(solucoes)

# Exemplo de entrada
n = int(input("Digite o número de variáveis (2 a 4): "))
if n < 2 or n > 4:
    print("Número inválido!")
else:
    print("Digite a matriz dos coeficientes:")
    A = [list(map(float, input().split())) for _ in range(n)]
    print("Digite a matriz dos termos independentes:")
    B = [[float(input())] for _ in range(n)]
    
    print("Matriz A:", A)
    print("Matriz B:", B)
    resultado = cramer(n, A, B)
    print("Solução do sistema:", resultado)