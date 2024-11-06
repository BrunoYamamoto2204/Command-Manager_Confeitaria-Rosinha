import json
from datetime import datetime,timedelta
def esc_principal():
    while True:
        try:
            escolha = int(input
("""Escolha uma opção: 
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
            print("\033[1;33mEscolha uma opção:\033[m")
            print("\033[33m1 - \033[34mNova Comanda\033[m")
            print("\033[33m2 - \033[34mVer Comanda existente\033[m")
            print("\033[33m3 - \033[34mAdicionar em uma comanda existente\033[m")
            print("\033[33m4 - \033[34mExcluir itens da comanda\033[m")
            print("\033[33m5 - \033[34mSair\033[m")
            print()
            opc = int(input("Escolha: "))
            if opc > 5 or opc < 1:
                print("\033[31mEscolha um número entre 1 e 5 apenas!\033[m\n")
            else:
                break
        except ValueError:
            print("\033[31mEscolha um número entre 1 e 5 apenas!\033[m\n")

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
        except ValueError:
            print("\033[31mEscolha um número entre 1 e 6 apenas!\033[m\n")
        else:
            break

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

def esc_salgado():
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
\033[33m30\033[m- \033[34mEmpadão Camarão  
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
\033[33m15 - \033[34mMorango Nata e suspiro 
\033[33m16 - \033[34mMorango Nata e suspiro   
\033[33m17 - \033[34mTaça Martha Rocha
\033[33m18 - \033[34mTaça Dueto
\033[33m19 - \033[34mTaça Morango Nata e Suspiro\033[m 

Escolha:"""))
            if escolha > 19 or escolha < 1:
                print("\033[31mEscolha um número entre 1 e 19 apenas!\033[m\n")
            else:
                break
        except ValueError:
            print("\033[31mEscolha um número entre 1 e 19 apenas!\033[m\n")

    return escolha
def esc_sobremesa():
    while True:
        try:
            tipo_sobremesa = int(input
("""Escolha o tipo da sobremesa: 
\033[33m1\033[m - \033[34mTortas/Tortinhas\033[m 
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
    with open("comandas.json", "r") as r:
         comanda = json.load(r)

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
                qntd = (input("Peso do Empadão(Kg): ").strip().replace(",","."))
                float(qntd)
        except ValueError:
            print("\033[31m\nDigite uma quantidade válida!\033[m")
        else:
            break

    num_item = comanda['comandas'][nome]["num_item"]
    if salg < 29:
        return f"({num_item}) -> {qntd} UN - {salgado}"
    else:
        return f"({num_item}) -> {qntd} Kg - {salgado}"

def qntd_doce(doce,nome):
    with open("comandas.json", "r") as r:
         comanda = json.load(r)
    lista_doce = ["Brigadeiro", "Brigadeiro Branco", "Beijinho", "Olho de Sogra", "Cajuzinho",
                   "Brigadeiro Preto c/ Cereal", "Brigadeiro Branco c/ Cereal", "Dois Amores", "Espelhado Ouriço",
                   "Espelhado Dois Amores", "Espelhado Brigadeiro", "Espelhado Cereja", "Espelhado Nozes",
                   "Espelhado Olho Sogra", "Bomb. Morango", "Bomb. Damasco", "Bomb. Uva", "Bomb. Cereja", "Bomb. Nozes",
                   "Bomb. Brigadeiro", "Bomb. Côco", "Bomb. Dois Amores", "Bomb. Crocante", "Bomb. Laranjinha",
                   "Bomb. Suspiro", "Camafeu"]

    doce = lista_doce[doce - 1]

    while True:
        try:
            qntd = int(input("Quantidade de Doces(UN): ").strip())
        except ValueError:
            print("\033[31m\nDigite uma quantidade válida!\033[m")
        else:
            break

    num_item = comanda['comandas'][nome]["num_item"]
    return f"({num_item}) -> {qntd} UN - {doce}"

def qntd_sobremesa(sobre,nome):
    with open("comandas.json", "r") as r:
         comanda = json.load(r)
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

    num_item = comanda['comandas'][nome]["num_item"]
    if sobre < 7 or sobre > 12:
        return f"({num_item}) -> {qntd} KG - {sobremesa}"
    else:
        return f"({num_item}) -> {qntd} UN - {sobremesa}"

def qntd_bolo(bolo,nome):
    with open("comandas.json", "r") as r:
         comanda = json.load(r)
    lista_bolos = ["Abacaxi c/ Côco", "Ameixa c/ Côco", "Delícia de Limão e Abacaxi", "Martha Rocha", "Prestígio",
                   "Sonho de Valsa", "Morango Nata e Suspiro", "Morango c/ Chocolate", "Surpresa de Morango",
                   "Tentação de Morango", "Dueto", "Sinfonia de Damasco", "Bolo Trufado", "Floresta Negra",
                   "Morango Nata e Suspiro", "Morango Nata e Suspiro", "Taça Martha Rocha", "Taça Dueto",
                   "Taça Morango Nata e Suspiro"]

    bolos = lista_bolos[bolo - 1]

    while True:
        try:
            qntd = (input("Peso do bolo(Kg): ").strip().replace(",", "."))
            float(qntd)
        except ValueError:
            print("\033[31m\nDigite uma quantidade válida!\033[m")
        else:
            break

    num_item = comanda['comandas'][nome]["num_item"]
    return f"({num_item}) -> {qntd} Kg - {bolos}"

def qntd_fio_de_ovos(nome):
    with open("comandas.json", "r") as r:
         comanda = json.load(r)
    while True:
        try:
            qntd = (input("Peso do Fio de Ovos(Kg): ").strip().replace(",", "."))
            float(qntd)
        except ValueError:
            print("\033[31m\nDigite uma quantidade válida!\033[m")
        else:
            break

    num_item = comanda['comandas'][nome]["num_item"]
    return f"({num_item}) -> {qntd} Kg - Fio de ovos"


def nome_cliente():

    while True:

        while True:
            nome = input("\033[33mNome do cliente:\033[m ").strip()
            print("\nNome está correto? Caso não \033[33mdigite\033[m qualquer tecla")
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
                num_cel = input("\033[36m|| Formato (91234-5678) ||\033[m\nmNúmero de celular: ").strip()

                for c in num_cel:
                    if c.isnumeric():
                        numerico += 1
                    elif c == "-":
                        traco += 1
                if numerico == 9 and traco == 1:
                    break
                else:
                    print("\033[31mNúmero de celular inválido\033[m\n")
            except:
                print("\033[mNúmero celular inválido!\033[m")

        num_tel = '0'


    if esc_cel_tel == 2:
        # TELEFONE
        while True:
            try:
                numerico = 0
                traco = 0
                num_tel = input("\033[36m|| Formato (1234-5678) ||\033[m\nNúmero de telefone: ").strip()

                for c in num_tel:
                    if c.isnumeric():
                        numerico += 1
                    elif c == "-":
                        traco += 1
                if numerico == 8 and traco == 1:
                    break
                else:
                    print("\033[31mNúmero de telefone inválido\033[m\n")
            except:
                print("\033[mNúmero telefone inválido!\033[m")

        num_cel = '0'

    if esc_cel_tel == 3:
        # TELEFONE
        while True:
            try:
                numerico = 0
                traco = 0
                num_tel = input("\033[36m|| Formato (1234-5678) ||\033[m\nNúmero de telefone: ").strip()

                for c in num_tel:
                    if c.isnumeric():
                        numerico += 1
                    elif c == "-":
                        traco += 1
                if numerico == 8 and traco == 1:
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
                num_cel = input("\033[36m|| Formato (91234-5678) ||\033[m\nmNúmero de celular: ").strip()

                for c in num_cel:
                    if c.isnumeric():
                        numerico += 1
                    elif c == "-":
                        traco += 1
                if numerico == 9 and traco == 1:
                    break
                else:
                    print("\033[31mNúmero de celular inválido\033[m\n")
            except:
                print("\033[mNúmero celular inválido!\033[m")

    return [num_cel,num_tel]

def dia_data():
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
    #DIA DA SEMANA
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

    return [data_formatada,dia_semana]

def horario_comanda():
    while True:
        encomenda = input("\nA comanda é para \033[33mencomenda?\033[m S/N:").strip().upper()
        if encomenda  == "S" or encomenda == "N":
            break
        else:
            print("\033[31mResposta inválida! Responda S/N\033[m")

    if encomenda == "S":
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
        while True:
            try:
                horario_pronto = input("||Formato (00:00)||\nHorário da encomenda: ")
                horario_formatado = datetime.strptime(horario_pronto,"%H:%M")
            except ValueError:
                print("\033[31mHorário Inválido!\033[m")
            else:
                horario_pronto = datetime.strftime(horario_formatado, "%H:%M")
                horario_entrega = 0
                break

    return [horario_pronto,horario_entrega]