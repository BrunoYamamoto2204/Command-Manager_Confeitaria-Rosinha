import json
import escolha_valida
from unidecode import unidecode

with open("comandas.json","r") as r:
    dados = json.load(r)

#
str = 'Kibe'
#
#
# if str in dados['salgado']['fritos']:
#     print('Está em fritos ')
#
# elif str in dados['salgado']['empadao']:
#     print('Está em empadao ')


# itens_split = dados['comandas']['jonson_silva_']['ADICIONADO']['bolos'][4].split()
# if len(itens_split) == 6: #1
#     print(itens_split[5])
# elif len(itens_split) == 7:  # 2
#     print(itens_split[5] + " " + itens_split[6])
# elif len(itens_split) == 8:  # 3
#     print(itens_split[5] + " " + itens_split[6] + " " + itens_split[7])
# elif len(itens_split) == 9:  # 4
#     print(itens_split[5] + " " + itens_split[6] + " " + itens_split[7] + " " + itens_split[8])
# else:  # 5
#     print(itens_split[5] + " " + itens_split[6] + " " + itens_split[7] + " " + itens_split[8] + " "+itens_split[9])

validar = "(19) -> 1.0 Kg - Empadão Frango".split()
escolha_valida.validar_exclusao(validar,validar[2])
