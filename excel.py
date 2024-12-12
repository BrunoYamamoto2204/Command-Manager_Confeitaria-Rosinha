import os
import pandas as pd
from openpyxl.styles import Font, PatternFill, Alignment
import openpyxl
import json

with open("relatorio_diario_completo.json","r") as r:
    rel_completo = json.load(r)
relatorio = rel_completo["22/04/2024"]

def itens_clientes(cliente,hora,cat):
    valores = relatorio[hora][cliente][cat]
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
    for e, v in enumerate(valores):
        v_split = str(v).split()
        del v_split[:2]

        v_format = ""
        for p in v_split:
            v_format += " " + p

        dado[f"Item {e + 1}"] = v_format

    valores_add = relatorio[hora][cliente]["ADICIONADO"][cat]
    for e, v in enumerate(valores_add):
        v_split = str(v).split()
        del v_split[:2]

        v_format = ""
        for p in v_split:
            v_format += " " + p

        dado[f"Item {len(dado)-1}"] = v_format

    return dado

## ---------------------------- PERSONALIZAÇÃO ----------------------------#
# def css(categoria):
#     wb = openpyxl.load_workbook(nome_arquivo)
#     sheet = wb[categoria]
#
#     # Fonte
#     fonte = Font(name='Arial', size=12, bold=True)
#     # Cor da célula
#     fill_header = PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid")
#     # Alinhar
#     alignment = Alignment(horizontal="center", vertical="center")
#
#     # Altura das células
#     for row in sheet.iter_rows():
#         for cell in row:
#             cell.font = fonte
#             cell.alignment = alignment
#             sheet.row_dimensions[str(row[0].row)].height = 100
#
#
#     # Colorir o cabeçalho
#     for cell in sheet[1]:
#         cell.fill = fill_header
#
#     # Largura das células
#     for col in sheet.columns:
#         column = col[0].column_letter
#         sheet.column_dimensions[column].width = 50
#
#     wb.save(nome_arquivo)

## ---------------------------- TABELA ----------------------------#

nome_arquivo = "Relatorio_completo.xlsx"

current_directory = os.getcwd()

file_path = os.path.join(current_directory,nome_arquivo)

if os.path.exists(file_path):
    print("Relatório já criado")
else:
    categorias = ['doce', 'salgado', 'bolo', 'sobremesa', 'fio_de_ovos']

    with pd.ExcelWriter(nome_arquivo) as writer:
        for categoria in categorias:
            tabela_categoria = pd.DataFrame(columns=["Nome", "Horário"] + [f"Item {i + 1}" for i in range(30)])

            for hora in relatorio:
                for nome in relatorio[hora]:

                    # Define os dados de cada categoria
                    dados_categoria = itens_clientes(nome, hora, categoria)

                    # Garantir que todos os itens tenham valor
                    for i in range(1, 31):
                        dados_categoria.setdefault(f"Item {i}", "")

                    add = pd.DataFrame([dados_categoria])
                    tabela_categoria = pd.concat([tabela_categoria, add],ignore_index=True)

            tabela_categoria.to_excel(writer, sheet_name=categoria.capitalize(), index=False)

## ---------------------------- PERSONALIZAÇÃO ----------------------------#

wb = openpyxl.load_workbook(nome_arquivo)

for categoria in wb.sheetnames:
    # try:
    sheet = wb[categoria]

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
            sheet.row_dimensions[(row[0].row)].height = 100

    # Colorir o cabeçalho
    for cell in sheet[1]:
        cell.fill = fill_header

    # Largura das células
    for col in sheet.columns:
        column = col[0].column_letter
        sheet.column_dimensions[column].width = 50

    # except Exception as e:
    #     print(f"Erro na planilha {categoria}: {e}")

wb.save(nome_arquivo)