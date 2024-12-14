import json
from datetime import datetime,timedelta
from unidecode import unidecode
import comandas
import excel
def esc_principal():
    while True:
        try:
            escolha = int(input
("""\nEscolha uma opção:\n 
\033[33m1\033[m - \033[34mSalgados\033[m 
\033[33m2\033[m - \033[34mDoces\033[m 
\033[33m3\033[m - \033[34mBolos\033[m 
\033[33m4\033[m - \033[34mSobremesas\033[m 
\033[33m5\033[m - \033[34mFio de Ovos\033[m 

Escolha: """))
            if escolha > 5 or escolha < 1:
                print("\033[31mEscolha um número entre 1 e 5 apenas!\033[m\n")
            else:
                break
        except ValueError:
            print("\033[31mEscolha um número entre 1 e 5 apenas!\033[m\n")

    return escolha

def esc_opcoes():
    while True:
        try:
            print("\033[1;33m\nEscolha uma opção:\033[m")
            print("\033[33m1 - \033[34mNova Comanda\033[m")
            print("\033[33m2 - \033[34mVer Comanda existente\033[m")
            print("\033[33m3 - \033[34mAdicionar em uma comanda existente\033[m")
            print("\033[33m4 - \033[34mExcluir itens da comanda\033[m")
            print("\033[33m5 - \033[34mRelatórios Gerais\033[m")
            print("\033[33m6 - \033[34mRelatórios Diários\033[m")
            print("\033[33m7 - \033[34mExcluir comanda\033[m")
            print("\033[33m8 - \033[34mTabelas Excel\033[m")
            print("\033[33m9 - \033[34mSair\033[m")
            print()
            opc = int(input("Escolha: "))
            if opc > 9 or opc < 1:
                print("\033[31mEscolha um número entre 1 e 9 apenas!\033[m\n")
            else:
                break
        except ValueError:
            print("\033[31mEscolha um número entre 1 e 9 apenas!\033[m\n")

    return opc

def esc_comandas():
    print("=" * 60)
    while True:
        try:
            print("\033[1;33mEscolha uma opção:\033[m\n")
            print("\033[33m1 - \033[34mComanda Geral\033[m")
            print("\033[33m2 - \033[34mComanda Salgados\033[m")
            print("\033[33m3 - \033[34mComanda Doces\033[m")
            print("\033[33m4 - \033[34mComanda Bolos\033[m")
            print("\033[33m5 - \033[34mComanda Sobremesas\033[m")
            print("\033[33m6 - \033[34mComanda Fio de Ovos\033[m")
            print()
            opc = int(input("Escolha: "))
            if opc > 6 or opc < 1:
                print("\033[31mEscolha um número entre 1 e 6 apenas!\033[m\n")
            else:
                break
        except ValueError:
            print("\033[31mEscolha um número entre 1 e 6 apenas!\033[m\n")

    return opc

def nome_comanda():
    with open("comandas.json", "r") as r:
        comandas = json.load(r)

    lista_nomes_clientes = []
    for nomes in comandas['comandas']: #Armazena todos os nomes na lista
        lista_nomes_clientes.append(nomes)

    while True:
        try:
            nome = (input("Nome do cliente referente a comanda: "))
            variavel_nome = ""
            for c in nome.split(): #Converte o nome do clinte no da variável
                variavel_nome += c + "_"

            if variavel_nome.lower() in lista_nomes_clientes: #Confere se tem esse nome na lista
                break
            else: 
                print(f"\033[31mCliente não encontrado!\033[m\n")
        except ValueError:
            print(f"\033[31mCliente não encontrado!\033[m\n")

    return variavel_nome.lower()

def nome_produto(itens_split):

    if len(itens_split) == 6:  # 1 palavra (nome do item)
        produto = (itens_split[5])
        # print(itens_split[5])
    elif len(itens_split) == 7:  # 2 palavras (nome do item)
        produto = (itens_split[5] + " " + itens_split[6])
        # print(itens_split[5] + " " + itens_split[6])
    elif len(itens_split) == 8:  # 3 palavras (nome do item)
        produto = (itens_split[5] + " " + itens_split[6] + " " + itens_split[7])
        # print(itens_split[5] + " " + itens_split[6] + " " + itens_split[7])
    elif len(itens_split) == 9:  # 4 palavras (nome do item)
        produto = (itens_split[5] + " " + itens_split[6] + " " + itens_split[7] + " " + itens_split[8])
        # print(itens_split[5] + " " + itens_split[6] + " " + itens_split[7] + " " + itens_split[8])
    else:  # 5 palavras (nome do item)
        produto = (itens_split[5] + " " + itens_split[6] + " " + itens_split[7] + " " + itens_split[8] + " " + itens_split[9])
        # print(itens_split[5] + " " + itens_split[6] + " " + itens_split[7] + " " + itens_split[8] + " " + itens_split[9])

    return produto

def esc_relatorio():
    while True:
        try:
            print("Escolha uma opção:\n")
            print("\033[33m1 - \033[34mRelatório Geral\033[m")
            print("\033[33m2 - \033[34mRelatório Salgados\033[m")
            print("\033[33m3 - \033[34mRelatório Doces\033[m")
            print("\033[33m4 - \033[34mRelatório Bolos\033[m")
            print("\033[33m5 - \033[34mRelatório Sobremesas\033[m")
            print("\033[33m6 - \033[34mRelatório Fio de Ovos\033[m\n")
            opc = int(input("Escolha: "))

            if opc > 6 or opc < 1:
                print("\033[31mEscolha um número entre 1 e 6 apenas!\033[m\n")
            else:
                break

        except ValueError:
            print("\033[31mEscolha um número entre 1 e 6 apenas!\033[m\n")

    return opc


def esc_salgado():
    #ESCOLHA DOS TIPOS DE SALGADOS
    while True:
        try:
            tipo_salg = int(input
("""Escolha o tipo de salgado: 
\033[33m1\033[m - \033[34mFritos\033[m 
\033[33m2 - \033[34mAssados
\033[33m3 - \033[34mEmpadão\033[m 

Escolha:"""))
            if tipo_salg > 3 or tipo_salg < 1:
                print("\033[31mEscolha um número entre 1 e 3 apenas!\033[m\n")
            else:
                break
        except ValueError:
            print("\033[31mEscolha um número entre 1 e 3 apenas!\033[m\n")

    print("="*60)

    #ESCOLHA DOS SALGADOS
    if tipo_salg == 1:
        while True:
            try:
                escolha = int(input
("""Escolha o salgado assado frito: 
\033[33m1 - \033[34mCoxinha\033[m  
\033[33m2 - \033[34mCoxinha c/ Catupiry\033[m 
\033[33m3 - \033[34mKibe\033[m
\033[33m4 - \033[34mKibe Recheado \033[m
\033[33m5 - \033[34mBolinha de Queijo\033[m
\033[33m6 - \033[34mVininha\033[m
\033[33m7 - \033[34mRisoles de Carne\033[m
\033[33m8 - \033[34mRisoles de Queijo e Presunto\033[m
\033[33m9 - \033[34mRisoles de Palmito\033[m 
\033[33m10 - \033[34mRisoles Camarão\033[m 
\033[33m11 - \033[34mMini Pastel Carne\033[m  
\033[33m12 - \033[34mMini Pastel Queijo\033[m
\033[33m13 - \033[34mEspetinho Carne\033[m
\033[33m14 - \033[34mEspetinho Frango\033[m 

Escolha: """))
                if escolha > 14 or escolha < 1:
                    print("\033[31mEscolha um número entre 1 e 14 apenas!\033[m\n")
                else:
                    break
            except ValueError:
                print("\033[31mEscolha um número entre 1 e 14 apenas!\033[m\n")

    if tipo_salg == 2:
        while True:
            try:
                escolha = int(input
("""Escolha o salgado assado:
\033[33m15 - \033[34mEsfiha Carne    
\033[33m16 - \033[34mEsfiha Frango 
\033[33m17 - \033[34mEsfiha Ricota c/ Tomate Seco 
\033[33m18 - \033[34mDoguinho 
\033[33m19 - \033[34mMini Calzone Frango 
\033[33m20 - \033[34mMini Pizza 
\033[33m21 - \033[34mAssado Escarola e Bacon
\033[33m22 - \033[34mEmpadinha Frango
\033[33m23 - \033[34mEmpadinha Palmito
\033[33m24 - \033[34mEmpadinha Camarão
\033[33m25 - \033[34mTrouxinha Camarão  
\033[33m26 - \033[34mFolhado Presunto e Ameixa 
\033[33m27 - \033[34mFolhado Frango /c Catupiry 
\033[33m28 - \033[34mFolhado Presunto e Queijo\033[m
 
Escolha: """))
                if escolha > 28 or escolha < 15:
                    print("\033[31mEscolha um número entre 15 e 28 apenas!\033[m\n")
                else:
                    break
            except ValueError:
                print("\033[31mEscolha um número entre 15 e 28 apenas!\033[m\n")

    if tipo_salg == 3:
        while True:
            try:
                escolha = int(input
("""Escolha o salgado empadão:
\033[33m29\033[m - \033[34mEmpadão Palmito   
\033[33m30\033[m - \033[34mEmpadão Camarão  
\033[33m31\033[m - \033[34mEmpadão Frango\033[m 

Escolha: """))
                if escolha > 31 or escolha < 29:
                    print("\033[31mEscolha um número entre 29 e 31 apenas!\033[m\n")
                else:
                    break
            except ValueError:
                print("\033[31mEscolha um número entre 29 e 31 apenas!\033[m\n")\


    return escolha
def esc_doce():
    while True:
        try:
            tipo_doce = int(input
("""Escolha o tipo de doce: 
\033[33m1\033[m - \033[34mTradicionais/Espelhados\033[m 
\033[33m2 - \033[34mBombom\033[m 

Escolha:"""))
            if tipo_doce > 2 or tipo_doce < 1:
                print("\033[31mEscolha um número entre 1 e 2 apenas!\033[m\n")
            else:
                break
        except ValueError:
            print("\033[31mEscolha um número entre 1 e 2 apenas!\033[m\n")

    print("=" * 60)

    if tipo_doce == 1:
        while True:
            try:
                escolha = int(input
("""Escolha o doce tradicional/espelhado:
\033[33m1\033[m - \033[34mBrigadeiro   
\033[33m2\033[m- \033[34mBrigadeiro Branco
\033[33m3\033[m- \033[34mBeijinho
\033[33m4\033[m- \033[34mOlho de Sogra 
\033[33m5\033[m- \033[34mCajuzinho 
\033[33m6\033[m- \033[34mBrigadeiro Preto c/ Cereal 
\033[33m7\033[m- \033[34mBrigadeiro Branco c/ Cereal 
\033[33m8\033[m- \033[34mDois Amores 
\033[33m9\033[m- \033[34mEspelhado Ouriço 
\033[33m10\033[m- \033[34mEspelhado Dois Amores  
\033[33m11\033[m- \033[34mEspelhado Brigadeiro
\033[33m12\033[m- \033[34mEspelhado Cereja
\033[33m13\033[m- \033[34mEspelhado Nozes
\033[33m14\033[m- \033[34mEspelhado Olho Sogra\033[m  
    
Escolha: """))
                if escolha > 14 or escolha < 1:
                    print("\033[31mEscolha um número entre 1 e 14 apenas!\033[m\n")
                else:
                    break
            except ValueError:
                print("\033[31mEscolha um número entre 1 e 14 apenas!\033[m\n")

    if tipo_doce == 2:
        while True:
            try:
                escolha = int(input
("""Escolha o bombom:
\033[33m15\033[m - \033[34mBomb. Morango   
\033[33m16\033[m - \033[34mBomb. Damasco
\033[33m17\033[m - \033[34mBomb. Uva
\033[33m18\033[m - \033[34mBomb. Cereja 
\033[33m19\033[m - \033[34mBomb. Nozes 
\033[33m20\033[m - \033[34mBomb. Brigadeiro  
\033[33m21\033[m - \033[34mBomb. Côco 
\033[33m22\033[m - \033[34mBomb. Dois Amores 
\033[33m23\033[m - \033[34mBomb. Crocante 
\033[33m24\033[m - \033[34mBomb. Laranjinha  
\033[33m25\033[m - \033[34mBomb. Suspiro
\033[33m26\033[m - \033[34mCamafeu\033[m 

Escolha: """))

                if escolha > 26 or escolha < 14:
                    print("\033[31mEscolha um número entre 15 e 26 apenas!\033[m\n")
                else:
                    break
            except ValueError:
                print("\033[31mEscolha um número entre 15 e 26 apenas!\033[m\n")

    return escolha
def esc_bolo():
    while True:
        try:
            escolha = int(input
("""Escolha o tipo de bolo: 
\033[33m1\033[m - \033[34mAbacaxi /c Côco\033[m 
\033[33m2 - \033[34mAmeixa c/ Côco
\033[33m3 - \033[34mDelícia de Limão e abacaxi
\033[33m4 - \033[34mMartha Rocha 
\033[33m5 - \033[34mPrestígio
\033[33m6 - \033[34mSonho de Valsa
\033[33m7 - \033[34mMorango Nata e Suspiro 
\033[33m8 - \033[34mMorango c/ Chocolate  
\033[33m9 - \033[34mSurpresa de Morango  
\033[33m10 - \033[34mTentação de Morango  
\033[33m11 - \033[34mDueto
\033[33m12 - \033[34mSinfonia de Damasco 
\033[33m13 - \033[34mBolo Trufado 
\033[33m14 - \033[34mFloresta Negra  
\033[33m15 - \033[34mTaça Martha Rocha
\033[33m16 - \033[34mTaça Dueto
\033[33m17 - \033[34mTaça Morango Nata e Suspiro\033[m 

Escolha:"""))
            if escolha > 17 or escolha < 1:
                print("\033[31mEscolha um número entre 1 e 17 apenas!\033[m\n")
            else:
                break
        except ValueError:
            print("\033[31mEscolha um número entre 1 e 17 apenas!\033[m\n")

    return escolha
def esc_sobremesa():
    while True:
        try:
            tipo_sobremesa = int(input
("""Escolha o tipo da sobremesa: 
\033[33m1\033[m - \033[34mTortas/Tortinhas/Quindim\033[m 
\033[33m2 - \033[34mPavês/Profeteroles/Banoff/Mil Folhas\033[m 

Escolha:"""))
            if tipo_sobremesa > 2 or tipo_sobremesa < 1:
                print("\033[31mEscolha um número entre 1 e 2 apenas!\033[m\n")
            else:
                break
        except ValueError:
            print("\033[31mEscolha um número entre 1 e 2 apenas!\033[m\n")

    print("=" * 60)

    if tipo_sobremesa == 1:
        while True:
            try:
                escolha = int(input
("""Escolha a torta:
\033[33m1\033[m - \033[34mTorta Choco Morango  
\033[33m2\033[m - \033[34mTorta Choco Nana 
\033[33m3\033[m - \033[34mTorta Maracujá  
\033[33m4\033[m - \033[34mTorta Limão 
\033[33m5\033[m - \033[34mTorta Morango 
\033[33m6\033[m - \033[34mTorta Alemã
\033[33m7\033[m - \033[34mMini Quindim 
\033[33m8\033[m - \033[34mMini Torta Brigadeiro 
\033[33m9\033[m - \033[34mMini Torta Limão 
\033[33m10\033[m - \033[34mMini Torta Morango   
\033[33m11\033[m - \033[34mMini Torta Strogonoff Nozes
\033[33m12\033[m - \033[34mMini Torta Uva \033[m 

Escolha: """))
                if escolha > 12 or escolha < 1:
                    print("\033[31mEscolha um número entre 1 e 12 apenas!\033[m\n")
                else:
                    break
            except ValueError:
                print("\033[31mEscolha um número entre 1 e 12 apenas!\033[m\n")
    if tipo_sobremesa ==2:
        while True:
            try:
                escolha = int(input
("""Escolha a torta:
\033[33m13\033[m - \033[34mMil Folhas
\033[33m14\033[m - \033[34mMil Folhas c / Morango
\033[33m15\033[m - \033[34mMil Folhas c / Frutas
\033[33m16\033[m - \033[34mPavê Frutas Tropicais
\033[33m17\033[m - \033[34mPavê Morango
\033[33m18\033[m - \033[34mPavê Pêssego
\033[33m19\033[m - \033[34mPavê Abacaxi
\033[33m20\033[m - \033[34mProfeteroles
\033[33m21\033[m - \033[34mBanoff\033[m

Escolha: """))
                if escolha > 21 or escolha < 13:
                    print("\033[31mEscolha um número entre 13 e 21 apenas!\033[m\n")
                else:
                    break
            except ValueError:
                print("\033[31mEscolha um número entre 13 e 21 apenas!\033[m\n")
    return escolha


def qnd_salg(salg,nome):
    with open("comandas.json", "r", encoding="utf-8") as r:
         comanda = json.load(r)
    with open("dados.json", "r") as r:
        dados = json.load(r)

    lista_salg = ["Coxinha", "Coxinha c/ Catupiry", "Kibe", "Kibe Recheado", "Bolinha de Queijo", "Vininha",
                  "Risoles de Carne", "Risoles de Queijo e Presunto", "Risoles de Palmito", "Risoles Camarão",
                  "Mini Pastel Carne", "Mini Pastel Queijo", "Espetinho Carne", "Espetinho Frango", "Esfiha Carne",
                  "Esfiha Frango", "Esfiha Ricota c/ Tomate Seco", "Doguinho", "Mini Calzone Frango", "Mini Pizza",
                  "Assado Escarola e Bacon", "Empadinha Frango", "Empadinha Palmito", "Empadinha Camarão",
                  "Trouxinha Camarão", "Folhado Presunto e Ameixa", "Folhado Frango c/ Catupiry",
                  "Folhado Presunto e Queijo", "Empadão Palmito", "Empadão Camarão", "Empadão Frango",""]

    salgado = lista_salg[salg - 1]

    while True:
        try:
            if salg < 29:
                qntd = int(input("Quantidade de Salgados(UN): ").strip())
            else:
                qntd = float(input("Peso do Empadão(Kg): ").strip().replace(",","."))
                float(qntd)
        except ValueError:
            print("\033[31m\nDigite uma quantidade válida!\033[m")
        else:
            break

    #ADICIONAR EM DADOS
    if salg >= 1 and salg <= 14: #FRITOS
        dados_salgado = dados['salgado']['fritos'][unidecode(salgado)] + qntd
        dados['salgado']['fritos'][unidecode(salgado)] = dados_salgado
    if salg >=15 and salg <= 28: #ASSADOS
        dados_salgado = dados['salgado']['assados'][unidecode(salgado)] + qntd
        dados['salgado']['assados'][unidecode(salgado)] = dados_salgado
    if salg >=29 and salg <= 31: #ASSADOS
        dados_salgado = dados['salgado']['empadao'][unidecode(salgado)] + float(qntd)
        dados['salgado']['empadao'][unidecode(salgado)] = dados_salgado

    with open("dados.json", "w") as w:
        json.dump(dados, w, indent=4, ensure_ascii=False)

    #ADICIONAR EM RELATORIO DIARIO SIMPLES
    with open("relatorio_diario_simples.json", "r") as r:
        data = json.load(r)

    data_simples = comanda['comandas'][nome]["data"] #DATA A SER ADD NO RELATORIO SIMPLES
    if unidecode(salgado) in data[data_simples]['salgado']: #CONFERE SE TEM ESSE PRODUTO, E ADICIONA SE TIVER
        qntd_simples = data[data_simples]['salgado'][unidecode(salgado)] + float(qntd)
        data[data_simples]['salgado'][unidecode(salgado)] = qntd_simples
    else:                                                    #CASO NAO TENHA, CRIA
        data[data_simples]['salgado'][unidecode(salgado)] = float(qntd)

    with open("relatorio_diario_simples.json", "w") as w:
        json.dump(data, w, indent=4)

    #ADICIONAR EM COMANDAS
    num_item = comanda['comandas'][nome]["num_item"]
    if salg < 29:
        return f"({num_item}) -> {qntd} UN - {salgado}"
    else:
        return f"({num_item}) -> {qntd} Kg - {salgado}"

def qntd_doce(doces,nome):
    with open("comandas.json", "r", encoding="utf-8") as r:
         comanda = json.load(r)
    with open("dados.json", "r") as r:
        dados = json.load(r)

    lista_doce = ["Brigadeiro", "Brigadeiro Branco", "Beijinho", "Olho de Sogra", "Cajuzinho",
                   "Brigadeiro Preto c/ Cereal", "Brigadeiro Branco c/ Cereal", "Dois Amores", "Espelhado Ouriço",
                   "Espelhado Dois Amores", "Espelhado Brigadeiro", "Espelhado Cereja", "Espelhado Nozes",
                   "Espelhado Olho Sogra", "Bomb. Morango", "Bomb. Damasco", "Bomb. Uva", "Bomb. Cereja", "Bomb. Nozes",
                   "Bomb. Brigadeiro", "Bomb. Côco", "Bomb. Dois Amores", "Bomb. Crocante", "Bomb. Laranjinha",
                   "Bomb. Suspiro", "Camafeu"]

    doce = lista_doce[doces - 1]

    while True:
        try:
            qntd = int(input("Quantidade de Doces(UN): ").strip())
        except ValueError:
            print("\033[31m\nDigite uma quantidade válida!\033[m")
        else:
            break

    # ADICIONAR EM DADOS
    if doces >= 1 and doces <= 14:
        dados_doce = dados['doce']['tradicional/espelhado'][unidecode(doce)] + qntd
        dados['doce']['tradicional/espelhado'][unidecode(doce)] = dados_doce
    if doces >= 15 and doces <= 26:
        dados_doce = dados['doce']['bombom'][unidecode(doce)] + qntd
        dados['doce']['bombom'][unidecode(doce)] = dados_doce

    with open("dados.json", "w") as w:
        json.dump(dados, w, indent=4, ensure_ascii=False)

    # ADICIONAR EM RELATORIO DIARIO SIMPLES
    with open("relatorio_diario_simples.json", "r") as r:
        data = json.load(r)

    data_simples = comanda['comandas'][nome]["data"]  # DATA A SER ADD NO RELATORIO SIMPLES
    if unidecode(doce) in data[data_simples]['doce']:  # CONFERE SE TEM ESSE PRODUTO, E ADICIONA SE TIVER
        qntd_simples = data[data_simples]['doce'][unidecode(doce)] + float(qntd)
        data[data_simples]['doce'][unidecode(doce)] = qntd_simples
    else:                                               # CASO NAO TENHA, CRIA
        data[data_simples]['doce'][unidecode(doce)] = float(qntd)

    with open("relatorio_diario_simples.json", "w") as w:
        json.dump(data, w, indent=4)

    #ADICIONAR EM COMANDAS
    num_item = comanda['comandas'][nome]["num_item"]
    return f"({num_item}) -> {qntd} UN - {doce}"

def qntd_sobremesa(sobre,nome):
    with open("comandas.json", "r", encoding="utf-8") as r:
         comanda = json.load(r)
    with open("dados.json", "r") as r:
        dados = json.load(r)

    lista_sobremesa = ["Torta Choco Morango", "Torta Choco Nana", "Torta Maracujá", "Torta Limão", "Torta Morango",
                        "Torta Alemã", "Mini Quindim", "Mini Torta Brigadeiro", "Mini Torta Limão",
                        "Mini Torta Morango", "Mini Torta Strogonoff Nozes", "Mini Torta Uva", "Mil Folhas",
                        "Mil Folhas c/ Morango", "Mil Folhas c/ Frutas", "Pavê Frutas Tropicais", "Pavê Morango",
                        "Pavê Pêssego", "Pavê Abacaxi", "Profiteroles", "Banoff"]

    sobremesa = lista_sobremesa[sobre - 1]

    while True:
        try:
            if sobre < 7 or sobre > 12:
                qntd = (input("Peso da Sobremesa(Kg): ").strip().replace(",", "."))
                float(qntd)
            else:
                qntd = int(input("Quantidade do Sobremesas(UN): ").strip())
        except ValueError:
            print("\033[31m\nDigite uma quantidade válida!\033[m")
        else:
            break

    # ADICIONAR EM DADOS
    if sobre >= 1 and sobre <= 12:
        dados_sobremesa = dados['sobremesa']['tortas'][unidecode(sobremesa)] + float(qntd)
        dados['sobremesa']['tortas'][unidecode(sobremesa)] = dados_sobremesa
    if sobre >= 13 and sobre <= 21:
        dados_sobremesa = dados['sobremesa']['Paves/Profiteroles/Banoff/Mil Folhas'][unidecode(sobremesa)] + float(qntd)
        dados['sobremesa']['Paves/Profiteroles/Banoff/Mil Folhas'][unidecode(sobremesa)] = dados_sobremesa

    with open("dados.json", "w") as w:
        json.dump(dados, w, indent=4, ensure_ascii=False)

    # ADICIONAR EM RELATORIO DIARIO SIMPLES
    with open("relatorio_diario_simples.json", "r") as r:
        data = json.load(r)

    data_simples = comanda['comandas'][nome]["data"]  # DATA A SER ADD NO RELATORIO SIMPLES
    if unidecode(sobremesa) in data[data_simples]['sobremesa']:  # CONFERE SE TEM ESSE PRODUTO, E ADICIONA SE TIVER
        qntd_simples = data[data_simples]['sobremesa'][unidecode(sobremesa)] + float(qntd)
        data[data_simples]['sobremesa'][unidecode(sobremesa)] = qntd_simples
    else:                                               # CASO NAO TENHA, CRIA
        data[data_simples]['sobremesa'][unidecode(sobremesa)] = float(qntd)

    with open("relatorio_diario_simples.json", "w") as w:
        json.dump(data, w, indent=4)

    #ADICIONAR EM COMANDAS
    num_item = comanda['comandas'][nome]["num_item"]
    if sobre < 7 or sobre > 12:
        return f"({num_item}) -> {qntd} KG - {sobremesa}"
    else:
        return f"({num_item}) -> {qntd} UN - {sobremesa}"

def qntd_bolo(bolo,nome):
    with open("comandas.json", "r", encoding="utf-8") as r:
         comanda = json.load(r)
    with open("dados.json", "r") as r:
        dados = json.load(r)

    lista_bolos = ["Abacaxi c/ Côco", "Ameixa c/ Côco", "Delícia de Limão e Abacaxi", "Martha Rocha", "Prestígio",
                   "Sonho de Valsa", "Morango Nata e Suspiro", "Morango c/ Chocolate", "Surpresa de Morango",
                   "Tentação de Morango", "Dueto", "Sinfonia de Damasco", "Bolo Trufado", "Floresta Negra",
                   "Taça Martha Rocha", "Taça Dueto", "Taça Morango Nata e Suspiro"]

    bolos = lista_bolos[bolo - 1]

    while True:
        try:
            qntd = (input("Peso do bolo(Kg): ").strip().replace(",", "."))
            float(qntd)
        except ValueError:
            print("\033[31m\nDigite uma quantidade válida!\033[m")
        else:
            break

    # ADICIONAR EM DADOS

    dados_bolos = dados['bolo'][unidecode(bolos)] + float(qntd)
    dados['bolo'][unidecode(bolos)] = dados_bolos

    with open("dados.json", "w") as w:
        json.dump(dados, w, indent=4, ensure_ascii=False)

    # ADICIONAR EM RELATORIO DIARIO SIMPLES
    with open("relatorio_diario_simples.json", "r") as r:
        data = json.load(r)

    data_simples = comanda['comandas'][nome]["data"]  # DATA A SER ADD NO RELATORIO SIMPLES
    if unidecode(bolos) in data[data_simples]['bolo']:  # CONFERE SE TEM ESSE PRODUTO, E ADICIONA SE TIVER
        qntd_simples = data[data_simples]['bolo'][unidecode(bolos)] + float(qntd)
        data[data_simples]['bolo'][unidecode(bolos)] = qntd_simples
    else:                                               # CASO NAO TENHA, CRIA
        data[data_simples]['bolo'][unidecode(bolos)] = float(qntd)

    with open("relatorio_diario_simples.json", "w") as w:
        json.dump(data, w, indent=4)

    #ADICIONAR EM COMANDAS
    num_item = comanda['comandas'][nome]["num_item"]
    return f"({num_item}) -> {qntd} Kg - {bolos}"

def qntd_fio_de_ovos(nome):
    with open("comandas.json", "r", encoding="utf-8") as r:
         comanda = json.load(r)
    with open("dados.json", "r") as r:
        dados = json.load(r)

    while True:
        try:
            qntd = (input("Peso do Fio de Ovos(Kg): ").strip().replace(",", "."))
        except ValueError:
            print("\033[31m\nDigite uma quantidade válida!\033[m")
        else:
            break

    # ADICIONAR EM DADOS
    dados_foi_de_ovos = dados['fio_de_ovos']["Fio de ovos"] + float(qntd)
    dados['fio_de_ovos']["Fio de ovos"] = dados_foi_de_ovos

    with open("dados.json", "w") as w:
        json.dump(dados, w, indent=4, ensure_ascii=False)

    # ADICIONAR EM RELATORIO DIARIO SIMPLES
    with open("relatorio_diario_simples.json", "r") as r:
        data = json.load(r)

    data_simples = comanda['comandas'][nome]["data"]  # DATA A SER ADD NO RELATORIO SIMPLES
    if 'Fio de ovos' in data[data_simples]['fio_de_ovos']:  # CONFERE SE TEM ESSE PRODUTO, E ADICIONA SE TIVER
        qntd_simples = data[data_simples]['fio_de_ovos']['Fio de ovos'] + float(qntd)
        data[data_simples]['fio_de_ovos']['Fio de ovos'] = qntd_simples
    else:                                               # CASO NAO TENHA, CRIA
        data[data_simples]['fio_de_ovos']['Fio de ovos'] = float(qntd)

    with open("relatorio_diario_simples.json", "w") as w:
        json.dump(data, w, indent=4)

    #ADICIONAR EM COMANDAS
    num_item = comanda['comandas'][nome]["num_item"]
    return f"({num_item}) -> {qntd} Kg - Fio de ovos"


def nome_cliente():

    while True:

        while True:
            nome = input("\033[33mNome do cliente:\033[m ").strip()
            print("\nNome está correto? Caso contrário, \033[33mdigite\033[m qualquer tecla")
            confirmar = input("Se não, pressione \033[33mENTER\033[m para continuar... ")
            print()
            if confirmar == "":
                break
            else:
                continue
        if nome == "":
            print("\033[31mNome inválido\033[m")
        else:
            break

    variavel_nome = ""
    for c in nome.split():
        variavel_nome+=c+"_"

    return variavel_nome.lower()

def numero_cliente():
    with open("comandas.json", "r") as r:
        comandas = json.load(r)

    while True:
        try:
            print("\033[1;33mEscolha uma das opções:\033[m ")
            print("(1) - Apenas Celular ")
            print("(2) - Apenas Telefone ")
            print("(3) - Telefone e Celular\n")
            esc_cel_tel = int(input("Escolha: "))
            if esc_cel_tel < 1 or esc_cel_tel >3:
                print("\033[mApenas números entre 1 e 3\033[m")
            else:
                break
        except:
            print("\033[mApenas números entre 1 e 3\033[m")

    print()
    if esc_cel_tel == 1:
        # CELULAR
        while True:
            try:
                numerico = 0
                traco = 0
                num_cel = input("\033[36m|| Formato (41 91234-5678) ||\033[m\nNúmero de celular: ").strip()

                for c in num_cel:
                    if c.isnumeric():
                        numerico += 1
                    elif c == "-":
                        traco += 1
                if numerico == 11 and traco == 1:
                    break
                else:
                    print("\033[31mNúmero de celular inválido\033[m\n")
            except:
                print("\033[mNúmero celular inválido!\033[m")

        num_tel = ''


    if esc_cel_tel == 2:
        # TELEFONE
        while True:
            try:
                numerico = 0
                traco = 0
                num_tel = input("\033[36m|| Formato (41 1234-5678) ||\033[m\nNúmero de telefone: ").strip()

                for c in num_tel:
                    if c.isnumeric():
                        numerico += 1
                    elif c == "-":
                        traco += 1
                if numerico == 10 and traco == 1:
                    break
                else:
                    print("\033[31mNúmero de telefone inválido\033[m\n")
            except:
                print("\033[mNúmero telefone inválido!\033[m")

        num_cel = ''

    if esc_cel_tel == 3:
        # TELEFONE
        while True:
            try:
                numerico = 0
                traco = 0
                num_tel = input("\033[36m|| Formato (41 1234-5678) ||\033[m\nNúmero de telefone: ").strip()

                for c in num_tel:
                    if c.isnumeric():
                        numerico += 1
                    elif c == "-":
                        traco += 1
                if numerico == 10 and traco == 1:
                    break
                else:
                    print("\033[31mNúmero de telefone inválido\033[m\n")
            except:
                print("\033[mNúmero telefone inválido!\033[m")

        print()

        # CELULAR
        while True:
            try:
                numerico = 0
                traco = 0
                num_cel = input("\033[36m|| Formato (41 91234-5678) ||\033[m\nNúmero de celular: ").strip()

                for c in num_cel:
                    if c.isnumeric():
                        numerico += 1
                    elif c == "-":
                        traco += 1
                if numerico == 11 and traco == 1:
                    break
                else:
                    print("\033[31mNúmero de celular inválido\033[m\n")
            except:
                print("\033[mNúmero celular inválido!\033[m")

    return [num_cel,num_tel]

def dia_data(nome):
    #DATA
    while True:
        try:
            data = input("\n\033[36m|| Formato (%dd/%m/%yyyy) ||\033[m\nData da encomenda: ")
            data_formatada = datetime.strptime(data, "%d/%m/%Y")
        except ValueError:
            print("\033[31mData inválida!\033[m")
        else:
            data_formatada = datetime.strftime(data_formatada,"%d/%m/%Y")
            break

    print()

    #ADICIONAR DATA NO RELATORIO_DIARIO
    with open("relatorio_diario_simples.json", "r") as r:
        data = json.load(r)
    with open("relatorio_diario_completo.json", "r") as r:
        data_completa = json.load(r)

    if data_formatada not in data:  #SÓ VAI SER CRIADO SE AINDA NÃO EXISTIR A DATA
        data[data_formatada] = {"doce":{},"salgado":{},"bolo":{},"sobremesa":{},"fio_de_ovos":{}}
        data_completa[data_formatada] = {}

    def converter_data(data_str):
        return datetime.strptime(data_str, "%d/%m/%Y")

    sorted_keys = sorted(data.keys(), key=converter_data)
    sorted_keys_completa = sorted(data_completa.keys(), key=converter_data)

    sorted_data = {} #DIARIO SIMPLES
    for key in sorted_keys:
        sorted_data[key] = data[key]

    sorted_data_completa = {} #DIARIO COMPLETO
    for key in sorted_keys_completa:
        sorted_data_completa[key] = data_completa[key]

    with open("relatorio_diario_simples.json", "w") as w:
        json.dump(sorted_data, w, indent=4)

    with open("relatorio_diario_completo.json", "w") as w:
        json.dump(sorted_data_completa, w, indent=4)

    #DIA DA SEMANA
    dias_da_semana=["","Segunda-Feira","Terça-Feira","Quarta-Feira","Quinta-Feira","Sexta-Feira","Sábado","Domingo"]

    while True:
        print("\033[1;33mEscolha o dia da semana:\033[m ")
        print("\033[33m(1)\033[m Segunda-Feira ")
        print("\033[33m(2)\033[m Terça-Feira ")
        print("\033[33m(3)\033[m Quarta-Feira ")
        print("\033[33m(4)\033[m Quinta-Feira ")
        print("\033[33m(5)\033[m Sexta-Feira ")
        print("\033[33m(6)\033[m Sábado ")
        print("\033[33m(7)\033[m Domingo ")

        try:
            dia_semana = int(input("\nEscolha uma o dia: "))
            if dia_semana < 1 or dia_semana > 7:
                print("\033[31mDigite apenas valores de 1 a 7\033[m")
            else:
                break
        except ValueError:
            print("\033[31mDigite apenas valores de 1 a 7\033[m")

    return [data_formatada,dias_da_semana[dia_semana]]

def horario_comanda():
    while True:
        encomenda = input("\nA comanda é para \033[33mentrega?\033[m S/N:").strip().upper()
        if encomenda  == "S" or encomenda == "N":
            break
        else:
            print("\033[31mResposta inválida! Responda S/N\033[m")

    if encomenda == "S":
        local = local_de_entrega()

        while True:
            try:
                horario_entrega = input("\n\033[36m|| Formato (00:00) ||\033[m\nHorário da entrega: ")
                horario_formatado = datetime.strptime(horario_entrega,"%H:%M")
            except ValueError:
                print("\033[31mHorário Inválido!\033[m")
            else:
                horario_pronto = horario_formatado - timedelta(hours=1)
                horario_entrega = datetime.strftime(horario_formatado, "%H:%M")
                horario_pronto = datetime.strftime(horario_pronto, "%H:%M")
                break

    elif encomenda == "N":
        local = "-"

        while True:
            try:
                horario_pronto = input("\n\033[36m||Formato (00:00)||\033[m\nHorário da encomenda: ")
                horario_formatado = datetime.strptime(horario_pronto,"%H:%M")
            except ValueError:
                print("\033[31mHorário Inválido!\033[m")
            else:
                horario_pronto = datetime.strftime(horario_formatado, "%H:%M")
                horario_entrega = 0
                break

    return [horario_pronto,horario_entrega,local]

def obs(nome_cliente):
    with open('comandas.json','r') as r:
        comandas = json.load(r)

    while True:
        s_n = input("\nObservação? S/N: ").strip().upper()
        if s_n == "S":
            while True:
                observacao = input("\033[33mObs:\033[m ").strip()
                print("\nObservação está correto? Caso contrário, \033[33mdigite\033[m qualquer tecla")
                confirmar = input("Se não, pressione \033[33mENTER\033[m para continuar... ")
                print()
                if confirmar == "":
                    break
                else:
                    continue
            if s_n == "":
                print("\033[31mObservação vazia!\033[m")
            else:
                break

        elif s_n == "N":
            observacao = ""
            break
        else:
            print("\033[31mResposta Inválida! Responda S ou N\033[m")

    comandas['comandas'][nome_cliente]['obs'] = observacao

    with open("comandas.json",'w') as w:
        json.dump(comandas, w, indent=4)

    return observacao

def local_de_entrega():
    while True:

        while True:
            local = input("\033[33mEndereço da entrega:\033[m ").strip()
            print("\nEndereço está correto? Caso contrário, \033[33mdigite\033[m qualquer tecla")
            confirmar = input("Se não, pressione \033[33mENTER\033[m para continuar... ")
            print()
            if confirmar == "":
                break
            else:
                continue
        if local == "":
            print("\033[31mEndereço inválido\033[m")
        else:
            break

    return local

def validar_exclusao(itens_split,qntd,data):
    with open("dados.json", "r") as r:
        dados = json.load(r)
    with open('relatorio_diario_simples.json','r') as r:
        rel_simples =json.load(r)

    produto = nome_produto(itens_split)

    #SALGADOS
    if unidecode(produto) in dados['salgado']['fritos']:
        dados['salgado']['fritos'][unidecode(produto)] -= float(qntd)
    elif unidecode(produto) in dados['salgado']['assados']:
        dados['salgado']['assados'][unidecode(produto)] -= float(qntd)
    elif unidecode(produto) in dados['salgado']['empadao']:
        dados['salgado']['empadao'][unidecode(produto)] -= float(qntd)

    if unidecode(produto) in rel_simples[data]['salgado']:
        rel_simples[data]['salgado'][unidecode(produto)] -= float(qntd)

    #DOCES
    if unidecode(produto) in dados['doce']['tradicional/espelhado']:
        dados['doce']['tradicional/espelhado'][unidecode(produto)] -= float(qntd)
    elif unidecode(produto) in dados['doce']['bombom']:
        dados['doce']['bombom'][unidecode(produto)] -= float(qntd)

    if unidecode(produto) in rel_simples[data]['doce']:
        rel_simples[data]['doce'][unidecode(produto)] -= float(qntd)

    #BOLOS
    if unidecode(produto) in dados['bolo']:
        dados['bolo'][unidecode(produto)] -= float(qntd)

    if unidecode(produto) in rel_simples[data]['bolo']:
        rel_simples[data]['bolo'][unidecode(produto)] -= float(qntd)

    #SOBREMESAS
    if unidecode(produto) in dados['sobremesa']['tortas']:
        dados['sobremesa']['tortas'][unidecode(produto)] -= float(qntd)
    if unidecode(produto) in dados['sobremesa']['Paves/Profiteroles/Banoff/Mil Folhas']:
        dados['sobremesa']['Paves/Profiteroles/Banoff/Mil Folhas'][unidecode(produto)] -= float(qntd)

    if unidecode(produto) in rel_simples[data]['sobremesa']:
        rel_simples[data]['sobremesa'][unidecode(produto)] -= float(qntd)

    #FIO DE OVOS
    if unidecode(produto) in dados['fio_de_ovos']:
        dados['fio_de_ovos']["Fio de ovos"] -= float(qntd)

    if unidecode(produto) in rel_simples[data]['fio_de_ovos']:
        rel_simples[data]['fio_de_ovos'][unidecode(produto)] -= float(qntd)

    with open("dados.json", "w") as w:
        json.dump(dados, w, indent=4)
    with open("relatorio_diario_simples.json", "w") as w2:
        json.dump(rel_simples, w2, indent=4)


def relatorios_diarios():
    with open("relatorio_diario_completo.json", "r") as r:
        rel_completo = json.load(r)

    while True:
        try:
            print("\n\033[1;33mEscolha o tipo de relatório diário:\033[m")
            print("\033[33m1 - \033[34mRelatório Diário Simples\033[m")
            print("\033[33m2 - \033[34mRelatório Diário Completo\033[m\n")
            escolha = int(input("Escolha: "))
        except:
            print("\033[31mEscolha um número entre 1 e 2 apenas!\033[m\n")
        else:
            if escolha == 1 or escolha == 2:
                break
            else:
                print("\033[31mEscolha um número entre 1 e 2 apenas!\033[m\n")

    while True:
        try:
            data = input("\n\033[36m|| Formato (%dd/%m/%yyyy) ||\033[m\nData da encomenda: ")
            data_formatada = datetime.strptime(data, "%d/%m/%Y")
        except ValueError:
            print("\033[31mData inválida!\033[m")
        else:
            data_formatada = datetime.strftime(data_formatada, "%d/%m/%Y")
            if data_formatada in rel_completo:  # TANTO FAZ COMPLETO OU SIMPLES, ABOS VÃO TER AS MESMAS DATAS
                break
            else:
                print("\033[33mNada cadastrado nesta data!\033[m")

    if escolha == 1:
        comandas.relatorio_diario_simples(data_formatada)

    if escolha == 2:
        comandas.relatorio_diario_completo(data_formatada)

def tabelas_excel():
    with open("relatorio_diario_completo.json", "r") as r:
        rel_completo = json.load(r)

    while True:
        try:
            print("\n\033[1;33mEscolha o tipo de tabela:\033[m")
            print("\033[33m1 - \033[34mTabela Geral (Salgados, Doces, Bolos, Sobremesas, Fio de Ovos)\033[m")
            print("\033[33m2 - \033[34mTabela de Encomendas\033[m\n")
            escolha = int(input("Escolha: "))
        except:
            print("\033[31mEscolha um número entre 1 e 2 apenas!\033[m\n")
        else:
            if escolha == 1 or escolha == 2:
                break
            else:
                print("\033[31mEscolha um número entre 1 e 2 apenas!\033[m\n")

    while True:
        try:
            data = input("\n\033[36m|| Formato (%dd/%m/%yyyy) ||\033[m\nData da encomenda: ")
            data_formatada = datetime.strptime(data, "%d/%m/%Y")
        except ValueError:
            print("\033[31mData inválida!\033[m")
        else:
            data_formatada = datetime.strftime(data_formatada, "%d/%m/%Y")
            if data_formatada in rel_completo:  # TANTO FAZ COMPLETO OU SIMPLES, ABOS VÃO TER AS MESMAS DATAS
                break
            else:
                print("\033[33mNada cadastrado nesta data!\033[m")

    if escolha == 1:
        excel.tabela_encomendas(data_formatada)
    if escolha == 2:
        excel.tabela_entregas(data_formatada)

def validar_igualdade(nome,categoria,dia,hora):
    with open("relatorio_diario_completo.json", "r") as r:
        rel_completo = json.load(r)

    relatorio = rel_completo[dia][hora][nome]
    itens_cat = relatorio[categoria]

    tirar_repetidos = []

    if len(relatorio[categoria]) > 0:
        nomes_categoria = []
        for item in itens_cat: # Junta apenas os nomes do item.split()
            split = item.split()
            nome = nome_produto(split)

            split = (split[:5])
            split.append(nome)

            nomes_categoria.append(split)

        nomes_categoria_add_atualizado = []
        nomes_categoria_atualizado = []

        for item in nomes_categoria: # Passa por todos os itens da categoria
            qntd_item = float(item[2])
            qntd_total = qntd_item

            for item_add in relatorio["ADICIONADO"][categoria]: # Dentro de cada item, procura se não tem um igual no ADD
                split_add = str(item_add).split()
                nome_add = nome_produto(split_add)

                if nome_add in item[5]: # Se tiver o mesmo item no na categiria e no ADD

                    qntd_item_add = float(split_add[2])
                    qntd_total += qntd_item_add

                else:
                    tirar_repetidos.append(item[5]) # Registra os itens que tem na categoria
                    nomes_categoria_add_atualizado.append(item_add)

            item[2] = qntd_total

            juntar_nome = ""
            for p in item:
                juntar_nome += " " + str(p)

            nomes_categoria_atualizado.append(juntar_nome.strip())


        relatorio[categoria] = nomes_categoria_atualizado

        with open("relatorio_diario_completo.json","w") as w:
            json.dump(rel_completo,w,indent=4)

        itens_nao_repetidos = []
        for item in nomes_categoria_add_atualizado:
            item_split = str(item).split()
            nome = nome_produto(item_split)

            if nome not in tirar_repetidos:
                # print(tirar_repetidos)
                tirar_repetidos.append(nome) # Vai adicionando os itens aos que já formam para não repetir no add
                itens_nao_repetidos.append(item) # Só adiciona se ainda nao tiver o nome no add

        return itens_nao_repetidos

    else:
        return relatorio["ADICIONADO"][categoria]
