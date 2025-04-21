import json


pessoa  = {
    'nome': 'Ismael jorge ',
    'sobrenome': 'Brandão',
    'enderecos':[
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55}
    ],
    'altura': 1.8,
    'numeros_preferidos': (2,4,5,6,8,10),
    'dev': True,
    'nada': None,   
}

with open('aula118.json','w',encoding='utf-8') as arquivo:
    json.dump(pessoa, arquivo,ensure_ascii=False,indent=2)
    
