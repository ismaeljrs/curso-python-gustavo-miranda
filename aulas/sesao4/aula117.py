import json

pessoa = {
    'nome': 'Ismael'
}

# Criando e salvando o arquivo
with open('aula117.json', 'w', encoding='utf-8') as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)
    print(pessoa['nome'])



