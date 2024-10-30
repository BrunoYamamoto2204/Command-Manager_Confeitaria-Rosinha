import json
def formar_comandas(lista_salg,lista_doce,lista_sobre,lista_bolo,lista_fio_ovos):
    with open("comandas.json", "r") as r:
        comanda = json.load(r)

    print("\033[1;36m=\033[m" * 40)
    print(f"\033[1;36m{'COMANDA'+' '+str(comanda['num']):^40}\033[m")
    print("\033[1;36m=\033[m" * 40)
    if len(lista_salg) > 0:
        print(f"\033[34m{'--||Salgados||--':^40}\033[m")
        for c in lista_salg:
            print(c)
    if len(lista_doce) > 0:
        print(f"\033[34m{'--||Doces||--':^40}\033[m")
        for c in lista_doce:
            print(c)
    if len(lista_sobre) > 0:
        print(f"\033[34m{'--||Sobremesas||--':^40}\033[m")
        for c in lista_sobre:
            print(c)
    if len(lista_bolo) > 0:
        print(f"\033[34m{'--||Bolos||--':^40}\033[m")
        for c in lista_bolo:
            print(c)
    if len(lista_fio_ovos) > 0:
        print(f"\033[34m{'--||Fio de Ovos||--':^40}\033[m")
        for c in lista_fio_ovos:
            print(c)
    print("\033[1;36m=\033[m" * 40)


def criar_comanda(lista_salg,lista_doce,lista_sobre,lista_bolo,lista_fio_ovos,numero_itens):
    with open("comandas.json","r") as r:
        comanda = json.load(r)

    comanda["comandas"][f"comanda{comanda['num']}"] = {}
    comanda['comandas'][f'comanda{comanda["num"]}']["num_item"] = numero_itens
    comanda["comandas"][f"comanda{comanda['num']}"]['salgados'] = lista_salg
    comanda["comandas"][f"comanda{comanda['num']}"]['doces'] = lista_doce
    comanda["comandas"][f"comanda{comanda['num']}"]['bolos'] = lista_bolo
    comanda["comandas"][f"comanda{comanda['num']}"]['sobremesas'] = lista_sobre
    comanda["comandas"][f"comanda{comanda['num']}"]['fio_de_ovos'] = lista_fio_ovos
    comanda["comandas"][f"comanda{comanda['num']}"]['ADICIONADO'] = {}

    with open("comandas.json", "w") as w:
        json.dump(comanda, w, indent=4)
def salvar_comandas(lista_salg,lista_doce,lista_sobre,lista_bolo,lista_fio_ovos,numero_itens):
    with open("comandas.json","r") as r:
        comanda = json.load(r)

    comanda["comandas"][f"comanda{comanda['num']}"] = {} #Nao sei se da ruim tirar a lista kkk
    comanda["comandas"][f"comanda{comanda['num']}"]['salgados'] = lista_salg
    comanda["comandas"][f"comanda{comanda['num']}"]['doces'] = lista_doce
    comanda["comandas"][f"comanda{comanda['num']}"]['bolos'] = lista_bolo
    comanda["comandas"][f"comanda{comanda['num']}"]['sobremesas'] = lista_sobre
    comanda["comandas"][f"comanda{comanda['num']}"]['fio_de_ovos'] = lista_fio_ovos
    comanda["comandas"][f"comanda{comanda['num']}"]['ADICIONADO'] = {}
    comanda["comandas"][f"comanda{comanda['num']}"]['ADICIONADO']["salgados"] = []
    comanda["comandas"][f"comanda{comanda['num']}"]['ADICIONADO']["doces"] = []
    comanda["comandas"][f"comanda{comanda['num']}"]['ADICIONADO']["bolos"] = []
    comanda["comandas"][f"comanda{comanda['num']}"]['ADICIONADO']["sobremesas"] = []
    comanda["comandas"][f"comanda{comanda['num']}"]['ADICIONADO']["fio_de_ovos"] = []

    comanda['comandas'][f'comanda{comanda["num"]}']["num_item"] = numero_itens
    comanda["num"] += 1

    # print(comanda)
    with open("comandas.json", "w") as w:
        json.dump(comanda, w, indent=4)

def salvar_atualizado(lista_salg,lista_doce,lista_sobre,lista_bolo,lista_fio_ovos,num):
    with open("comandas.json","r") as r:
        comanda = json.load(r)

    comanda["comandas"][f"comanda{num}"]['ADICIONADO']['salgados'] = lista_salg
    comanda["comandas"][f"comanda{num}"]['ADICIONADO']['doces'] = lista_doce
    comanda["comandas"][f"comanda{num}"]['ADICIONADO']['bolos'] = lista_bolo
    comanda["comandas"][f"comanda{num}"]['ADICIONADO']['sobremesas'] = lista_sobre
    comanda["comandas"][f"comanda{num}"]['ADICIONADO']['fio_de_ovos'] = lista_fio_ovos

    with open("comandas.json", "w") as w:
        json.dump(comanda, w, indent=4) #Perguntar pro GPT o porque ele está retornando 1 em vez do dicionario ao escpolher a opcao 3
    return comanda['comandas'][f'comanda{num}']

def mostrar_comanda_geral(comanda,num):
    print("\033[1;36m=\033[m" * 40)
    print(f"\033[1;36m{'COMANDA'+' '+str(num):^40}\033[m")
    print("\033[1;36m=\033[m" * 40)
    # print(comanda)
    for tipo in comanda:
        # print(tipo)
        if tipo == 'num_item':
            continue
        if len(comanda[tipo]) > 0:
            if str(tipo) == "ADICIONADO":
                print("-"*40)
                printar = f'--||{str(tipo).capitalize()}||--'
                print(f"\033[33m{printar:^40}\033[m")
                for cat_add in comanda[tipo]:
                    for item in comanda[tipo][cat_add]:
                        print(item)
            else:
                printar = f'--||{str(tipo).capitalize()}||--'
                print(f"\033[34m{printar:^40}\033[m")
                for c in comanda[tipo]:
                    print(c)
    print("\033[1;36m=\033[m" * 40)

def mostrar_comanda_salgados(comanda,num):
    print("\033[1;36m=\033[m" * 40)
    print(f"\033[1;36m{'COMANDA' + ' ' + str(num) + '- SALGADOS':^40}\033[m")
    print("\033[1;36m=\033[m" * 40)
    try:
        try:
            for salgado in comanda["salgados"]:
                print(salgado)
        except:
            print("Sem salgados ")
        try:
            for salgado_add in comanda["ADICIONADO"]["salgados"]:
                print(salgado_add)
        except KeyError:
            a="sopra ter algo"
    except:
        print("erro")
    print("\033[1;36m=\033[m" * 40)

def mostrar_comanda_doces(comanda,num):
    print("\033[1;36m=\033[m" * 40)
    print(f"\033[1;36m{'COMANDA' + ' ' + str(num) + '- DOCES':^40}\033[m")
    print("\033[1;36m=\033[m" * 40)
    try:
        try:
            for doce in comanda["doces"]:
                print(doce)
        except:
            print("Sem doces ")
        try:
            for doce_add in comanda["ADICIONADO"]["doces"]:
                print(doce_add)
        except KeyError:
            a = "sopra ter algo"
    except:
        print("erro")
    print("\033[1;36m=\033[m" * 40)

def mostrar_comanda_bolos(comanda,num):
    print("\033[1;36m=\033[m" * 40)
    print(f"\033[1;36m{'COMANDA' + ' ' + str(num) + '- BOLOS':^40}\033[m")
    print("\033[1;36m=\033[m" * 40)
    try:
        try:
            for bolo in comanda["bolos"]:
                print(bolo)
        except:
            print("Sem bolos ")
        try:
            for bolo_add in comanda["ADICIONADO"]["bolos"]:
                print(bolo_add)
        except KeyError:
            a = "sopra ter algo"
    except:
        print("erro")
    print("\033[1;36m=\033[m" * 40)

def mostrar_comanda_sobremesas(comanda,num):
    print("\033[1;36m=\033[m" * 40)
    print(f"\033[1;36m{'COMANDA' + ' ' + str(num) + '- SOBREMESAS':^40}\033[m")
    print("\033[1;36m=\033[m" * 40)
    try:
        try:
            for sobremesa in comanda["sobremesas"]:
                print(sobremesa)
        except:
            print("Sem sobremesas ")
        try:
            for sobremesa_add in comanda["ADICIONADO"]["sobremesas"]:
                print(sobremesa_add)
        except KeyError:
            a = "sopra ter algo"
    except:
        print("erro")
    print("\033[1;36m=\033[m" * 40)

def mostrar_comanda_fio_de_ovos(comanda,num):
    print("\033[1;36m=\033[m" * 40)
    print(f"\033[1;36m{'COMANDA' + ' ' + str(num) + '- FIO DE OVOS':^40}\033[m")
    print("\033[1;36m=\033[m" * 40)
    try:
        try:
            for fio_de_ovos in comanda["fio_de_ovos"]:
                print(fio_de_ovos)
        except:
            print("Sem doces ")
        try:
            for fio_de_ovo_add in comanda["ADICIONADO"]["fio_de_ovos"]:
                print(fio_de_ovo_add)
        except KeyError:
            a = "sopra ter algo"
    except:
        print("erro")
    print("\033[1;36m=\033[m" * 40)

def excluir_comanda(num):
    with open("comandas.json","r") as r:
        comandas = json.load(r)

    print("\033[1;36m=\033[m" * 40)
    print(f"\033[1;36m{'COMANDA'+' '+str(num):^40}\033[m")
    print("\033[1;36m=\033[m" * 40)

    comanda = comandas['comandas'][f'comanda{num}']

    for tipo in comanda:
        if isinstance(comanda[tipo],int): #como o primeiro valor é o num dos itens é necessário pular
            continue
        if len(comanda[tipo]) > 0:
            if str(tipo) == "ADICIONADO":
                print("-"*40)
                printar = f'--||{str(tipo).capitalize()}||--'
                print(f"\033[33m{printar:^40}\033[m")
                for cat_add in comanda[tipo]:
                    for item in comanda[tipo][cat_add]:
                        item = str(item).split()
                        for caracteres in item: # Esse for é só para deixar o número entre parênteses em amarelo
                            if caracteres == item[0]:
                                print(f"\033[1;33m{caracteres}\033[m",end=" ")
                            else:
                                print(caracteres,end=' ')
                        print()

            else:
                printar = f'--||{str(tipo).capitalize()}||--'
                print(f"\033[34m{printar:^40}\033[m")
                for item in comanda[tipo]:
                    item = str(item).split()
                    for caracteres in item: # Esse for é só para deixar o número entre parênteses em amarelo
                        if caracteres == item[0]:
                            print(f"\033[1;33m{caracteres}\033[m", end=" ")
                        else:
                            print(caracteres, end=' ')
                    print()

    print("\033[1;36m=\033[m" * 40)

    while True:
        try:
            num_excluir = int(input("Escolha o número entre \033[1;33m(parênteses)\033[m do item para excluir: "))
            if num_excluir >= comanda['num_item'] or num_excluir < 1:
                print(f"\033[31mEscolha um número entre 1 e {comanda['num_item']-1} apenas!\033[m\n") #Como no json está o num do próximo item, -1 para desconsidera-lo
            else:
                break
        except ValueError:
            print(f"\033[31mEscolha um número entre 1 e {comanda['num_item']-1} apenas!\033[m\n")

    num_excluir = "("+str(num_excluir)+")"

    for tipo in comanda:
        if isinstance(comanda[tipo],int):
            continue
        if tipo == "ADICIONADO":
            for tipos_add in comanda[tipo]:
                lista_adicionados = []
                for itens in comanda[tipo][tipos_add]:
                    itens_split = str(itens).split()
                    if num_excluir not in itens_split[0]:
                        lista_adicionados.append(itens)
                comanda[tipo][tipos_add] = lista_adicionados
        else:
            lista_itens = []
            for itens in comanda[tipo]:
                itens_split = str(itens).split()
                if num_excluir not in itens_split[0]:
                    lista_itens.append(itens)
            comanda[tipo] = lista_itens

    with open("comandas.json", "w") as w:
        json.dump(comandas, w, indent=4)

    print(f"\033[32mItem {num_excluir} excluído com sucesso\033[m")
    print()









