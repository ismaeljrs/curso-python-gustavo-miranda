frase = 'oooaaa'

i = 0

qnts_aparceu_mais_vezes = 0
a_letra_q_aparceu_mais_vezes = ''

while i < len(frase):
    letras = frase[i]

    if letras == ' ':
        i += 1
        continue
    qnts_vezes_letra_apareceu = frase.count(letras)
    print(f'{letras}: {qnts_vezes_letra_apareceu}')

    if qnts_aparceu_mais_vezes < qnts_vezes_letra_apareceu:
        qnts_aparceu_mais_vezes = qnts_vezes_letra_apareceu
        a_letra_q_aparceu_mais_vezes = letras

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f' "{a_letra_q_aparceu_mais_vezes}" '
    f'{qnts_aparceu_mais_vezes}x'
)