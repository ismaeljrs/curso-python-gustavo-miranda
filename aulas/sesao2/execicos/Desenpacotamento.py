
# 🔹  Empacotamento e Desempacotamento de Dicionário + *args e **kwargs

# Exercícios:
# 1️⃣ Escreva uma função que aceite um número variável de argumentos (*args) e retorne a soma de todos eles.
def numero(*args):
    resultado = 0
    for i in args:
        resultado += i
    return resultado


soma = numero(3,5,2)
print(soma)
# 2️⃣ Crie uma função que aceite **kwargs e retorne uma string formatada com os valores recebidos. Exemplo de entrada: exibir_dados(nome="Ismael", idade=18) → Saída esperada: "Nome: Ismael, Idade: 18".

def caractere(**kwargs):
    return(kwargs)

nome = caractere(nome='ismael',sobrenome='jorge',idade=19)
print(nome)

# 3️⃣ Utilize desempacotamento (**) para passar um dicionário como argumento para uma função.
dados = {
    'nome':'ismael',
    'sobrenome':'jorge',
    'idade': 19
}

def mostra_valor_na_tela(nome, sobrenome, idade):
    return f'Nome: {nome} sobrenome {sobrenome} Idade:{idade}'
mostrar = mostra_valor_na_tela(**dados)
print(mostrar)

    



