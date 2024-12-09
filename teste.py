import json
import escolha_valida
from unidecode import unidecode
import comandas
from datetime import datetime

with open("comandas.json", 'r') as r:
    comanda = json.load(r)
with open("relatorio_diario_completo.json", 'r') as r:
    rel_completo = json.load(r)

nome = "aaaaaa_"
cliente = comanda['comandas'][nome]
data = cliente['data']
hora = cliente['hora_pronta']
relatorio = rel_completo[data][hora][nome]

# COMANDAS, REL.SIMPLES, DADOS
for categoria in cliente:

    if isinstance(cliente[categoria],list) or isinstance(cliente[categoria], dict):

        if categoria == "ADICIONADO":
            for cat_add in cliente[categoria]:

                for produtos_add in cliente[categoria][cat_add]:
                    produtos_split = produtos_add.split()
                    print(produtos_split)
                    escolha_valida.validar_exclusao(produtos_split,produtos_split[2], data)

                cliente[categoria][cat_add] = []
        else:
            for produtos in cliente[categoria]:
                produtos_split = produtos.split()
                print(produtos_split)
                escolha_valida.validar_exclusao(produtos_split, produtos_split[2], data)

            cliente[categoria] = []

# REL.COMPLETO
for categoria in relatorio:
    if categoria == "ADICIONADO":
        for cat_add in relatorio[categoria]:
            relatorio[categoria][cat_add] = []
    else:
        relatorio[categoria] = []

# APAGA EM COMANDAS
if nome in comanda['comandas']:
    del comanda['comandas'][nome]
    print(f"Comanda de {nome} removida com sucesso.")
else:
    print(f"Comanda de {nome}' não existe.")

# APAGA EM REL.COMPLETO
del rel_completo[data][hora][nome]


with open("comandas.json", 'w') as w:
    json.dump(comanda, w, indent=4)

with open("relatorio_diario_completo.json", 'w') as w:
    json.dump(rel_completo, w, indent=4)



