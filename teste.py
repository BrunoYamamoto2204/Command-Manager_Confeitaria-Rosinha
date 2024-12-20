import json
import escolha_valida
from unidecode import unidecode
import comandas
from datetime import datetime
import pandas as pd
import os
from openpyxl.styles import Font, PatternFill, Alignment
import openpyxl

# itens_adicionados = escolha_valida.validar_igualdade('jonson_silva_','salgado','22/04/2024','11:30')
#
# with open("relatorio_diario_completo.json", "r") as r:
#     rel_completo = json.load(r)
#
#
# rel_completo['22/04/2024']['11:30']['jonson_silva_']["ADICIONADO"]['salgado'] = itens_adicionados
#
#
# with open("relatorio_diario_completo.json", "w") as w:
#     json.dump(rel_completo, w, indent=4)

def remover_copias(lista):
    lista_formatada = []
    seen = []
    for item in lista:
        if item not in seen:
            lista_formatada.append(item)
            seen.append(item)

    return lista_formatada