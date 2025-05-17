def primeira_palavra_repetida(texto):
    palavras_vistas = set()
    palavras = texto.lower().split()  # Quebramos o texto em palavras

    for palavra in palavras:
        if palavra in palavras_vistas:
            return palavra  # Retorna a primeira palavra repetida
        palavras_vistas.add(palavra)
    
    return "Nenhuma palavra repetida"

texto = "A vida é bela e a natureza é linda"
resultado = primeira_palavra_repetida(texto)
print(resultado)  # Saída: "é"
