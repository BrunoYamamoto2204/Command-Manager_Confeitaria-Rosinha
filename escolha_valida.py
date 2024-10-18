import json
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
            print("Escolha uma opção:")
            print("\033[33m1 - \033[34mNova Comanda\033[m")
            print("\033[33m2 - \033[34mVer Comanda existente\033[m")
            print("\033[33m3 - \033[34mAdicionar em uma comanda existente\033[m")
            print("\033[33m4 - \033[34mSair\033[m")
            print()
            opc = int(input("Escolha: "))
            if opc > 4 or opc < 1:
                print("\033[31mEscolha um número entre 1 e 4 apenas!\033[m\n")
            else:
                break
        except ValueError:
            print("\033[31mEscolha um número entre 1 e 4 apenas!\033[m\n")

    return opc

def esc_comandas():
    print("=" * 60)
    while True:
        try:
            print("Escolha uma opção:")
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

def num_comanda():
    with open("comandas.json", "r") as r:
        comandas = json.load(r)
    while True:
        try:
            num = int(input("Escolha o número da comanda: "))
            if num >= comandas["num"] or num < 1:
                print(f"\033[31mSó existem comandas entre 1 e {comandas['num']}!\033[m\n")
            else:
                break
        except KeyError or ValueError:
            print(f"\033[31mSó existem comandas entre 1 e {comandas['num']}!\033[m\n")

    return num

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
\033[33m9\033[m- \033[34mEspelhado Dois Amores  
\033[33m10\033[m- \033[34mEspelhado Brigadeiro
\033[33m11\033[m- \033[34mEspelhado Cereja
\033[33m12\033[m- \033[34mEspelhado Nozes
\033[33m13\033[m- \033[34mEspelhado Olho Sogra\033[m  
    
Escolha: """))
                if escolha > 13 or escolha < 1:
                    print("\033[31mEscolha um número entre 1 e 13 apenas!\033[m\n")
                else:
                    break
            except ValueError:
                print("\033[31mEscolha um número entre 1 e 13 apenas!\033[m\n")

    if tipo_doce == 2:
        while True:
            try:
                escolha = int(input
("""Escolha o bombom:
\033[33m14\033[m - \033[34mBomb. Morango   
\033[33m13\033[m - \033[34mBomb. Damasco
\033[33m15\033[m - \033[34mBomb. Uva
\033[33m16\033[m - \033[34mBomb. Cereja 
\033[33m17\033[m - \033[34mBomb. Nozes 
\033[33m18\033[m - \033[34mBomb. Brigadeiro  
\033[33m19\033[m - \033[34mBomb. Côco 
\033[33m20\033[m - \033[34mBomb. Dois Amores 
\033[33m21\033[m - \033[34mBomb. Crocante 
\033[33m22\033[m - \033[34mBomb. Laranjinha  
\033[33m23\033[m - \033[34mBomb. Suspiro
\033[33m24\033[m - \033[34mCamafeu\033[m 

Escolha: """))
                if escolha > 24 or escolha < 14:
                    print("\033[31mEscolha um número entre 14 e 24 apenas!\033[m\n")
                else:
                    break
            except ValueError:
                print("\033[31mEscolha um número entre 14 e 24 apenas!\033[m\n")

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


def qnd_salg(salg):
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

    if salg < 29:
        return f"\033[1;33m{qntd} UN\033[m - {salgado}"
    else:
        return f"\033[1;33m{qntd} Kg\033[m - {salgado}"

def qntd_doce(doce):
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

    return f"\033[1;33m{qntd} UN\033[m - {doce}"

def qntd_sobremesa(sobre):
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

    if sobre < 7 or sobre > 12:
        return f"\033[1;33m{qntd} Kg\033[m - {sobremesa}"
    else:
        return f"\033[1;33m{qntd} UN\033[m - {sobremesa}"

def qntd_bolo(bolo):
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

    return f"\033[1;33m{qntd} Kg\033[m - {bolos}"

def qntd_fio_de_ovos():
    while True:
        try:
            qntd = (input("Peso do Fio de Ovos(Kg): ").strip().replace(",", "."))
            float(qntd)
        except ValueError:
            print("\033[31m\nDigite uma quantidade válida!\033[m")
        else:
            break

    return f"\033[1;33m{qntd} Kg\033[m - Fio de ovos"

