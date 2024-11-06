import json
from unidecode import unidecode

with open("dados.json","r") as r:
    dados = json.load(r)


opa='Empadão Camarão'

print(dados['salgado']['empadao'][unidecode(opa)])

