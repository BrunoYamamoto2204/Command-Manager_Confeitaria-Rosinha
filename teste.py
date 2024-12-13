import json
import escolha_valida
from unidecode import unidecode
import comandas
from datetime import datetime
import pandas as pd
import os
from openpyxl.styles import Font, PatternFill, Alignment
import openpyxl




def itens_entregas(cliente,hora,endereco,dia):
    with open("relatorio_diario_completo.json", "r") as r:
        rel_completo = json.load(r)
    relatorio = rel_completo[dia]

    categorias = ['salgado', 'doce', 'bolo', 'sobremesa', 'fio_de_ovos']
    dado = {}
    item = 0

    for c in categorias:
        valores = relatorio[hora][cliente][c]

        # NOMES
        cliente_split = str(cliente).split("_")
        nome = ""
        for p in cliente_split:
            nome += " " + p
        dado["Nome"] = nome.title().strip()

        # HORÁRIOS
        dado["Horário"] = hora

        # ENDEREÇO
        dado["Endereço"] = endereco

        # ITENS
        for v in (valores):
            item += 1
            v_split = str(v).split()
            del v_split[:2]

            v_format = ""
            for p in v_split:
                v_format += " " + p

            dado[f"Item {item}"] = v_format

        valores_add = relatorio[hora][cliente]["ADICIONADO"][c]
        for v in (valores_add):
            item += 1
            v_split = str(v).split()
            del v_split[:2]

            v_format = ""
            for p in v_split:
                v_format += " " + p

            dado[f"Item {item}"] = v_format

    return dado

def tabela_entregas(dia):
    with open("relatorio_diario_completo.json", "r") as r:
        rel_completo = json.load(r)
    relatorio = rel_completo[dia]

    ## ---------------------------- TABELA ----------------------------#

    nome_arquivo = "Entregas.xlsx"

    current_directory = os.getcwd()

    file_path = os.path.join(current_directory,nome_arquivo)

    tabela = pd.DataFrame(columns=["Nome", "Horário","Endereço"] + [f"Item {i + 1}" for i in range(30)])

    for hora in relatorio:
        for cliente in relatorio[hora]:

            endereco = relatorio[hora][cliente]['entrega']

            if endereco != "-":
                dados = itens_entregas(cliente, hora,endereco,dia)

                for i in range(1, 31):
                    dados.setdefault(f"Item {i}", "")

                add = pd.DataFrame([dados])
                tabela = pd.concat([tabela, add], ignore_index=True)

    with pd.ExcelWriter(nome_arquivo) as w:
        tabela.to_excel(w, sheet_name='Encomendas', index=False)

    ## ---------------------------- PERSONALIZAÇÃO ----------------------------#
    wb = openpyxl.load_workbook(nome_arquivo)
    sheet = wb.active

    # Fonte
    fonte = Font(name='Arial', size=12, bold=True)
    # Cor da célula
    fill_header = PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid")
    # Alinhar
    alignment = Alignment(horizontal="center", vertical="center")

    # Altura das células
    for row in sheet.iter_rows():
        for cell in row:
            cell.font = fonte
            cell.alignment = alignment
            sheet.row_dimensions[row[0].row].height = 100

    # Colorir o cabeçalho
    for cell in sheet[1]:
        cell.fill = fill_header

    # Largura das células
    for col in sheet.columns:
        column = col[0].column_letter
        sheet.column_dimensions[column].width = 50

    wb.save(nome_arquivo)
