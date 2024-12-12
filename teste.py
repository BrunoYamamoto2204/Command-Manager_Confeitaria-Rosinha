import json
import escolha_valida
from unidecode import unidecode
import comandas
from datetime import datetime

with open("relatorio_diario_completo.json","r") as r:
    rel_completo = json.load(r)
relatorio = rel_completo["22/04/2024"]

for hora in relatorio:
    for cliente in relatorio[hora]:
        valores = relatorio[hora][cliente]["doce"]
        dado = {}

        # NOMES
        cliente_split = str(cliente).split("_")
        nome = ""
        for p in cliente_split:
            nome += " " + p
        dado["Nome"] = nome.title().strip()

        # HORÁRIOS
        dado["Horário"] = hora

        # ITENS
        for e,v in enumerate(valores):
            valores = []
            v_split = str(v).split()
            del v_split[:2]

            v_format = ""
            for p in v_split:
                v_format += " " + p

            valores.append(v_format.strip())
            dado[f"Item {e+1}"] = valores

        valores_add = relatorio[hora][cliente]["ADICIONADO"]["doce"]
        for e,v in enumerate(valores_add):
            valores = []
            v_split = str(v).split()
            del v_split[:2]

            v_format = ""
            for p in v_split:
                v_format += " " + p

            valores.append(v_format.strip())
            dado[f"Item {len(dado)-1}"] = valores


        print(dado)



