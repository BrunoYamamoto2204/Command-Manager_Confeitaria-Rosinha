import json
def formar_comandas(lista_salg,lista_doce,lista_sobre,lista_bolo,lista_fio_ovos,
                    nome_cliente,num_cel,num_tel,data,dia_semana,hora_pronta,hora_entrega):

    nome_completo = ""
    for nome in nome_cliente.split("_"):
        nome_completo += f"{nome} "

    nomef = f"\033[33mNome:\033[m {nome_completo.title()}"
    dataf = f"\033[33mData:\033[m {data}"
    telf = f'\033[33mTelefone:\033[m {num_tel}'
    semanf = f"\033[33mDia da semana:\033[m {dia_semana}"
    celf = f'\033[33mCelular:\033[m {num_cel}'
    hora_prontaf = f'\033[33mHora(Pronto):\033[m {hora_pronta}'
    hora_entregaf = f'\033[33mHora(Entrega):\033[m{hora_entrega:<40}'

    print("\033[1;36m=\033[m" * 50)  # COLOCAR TUDO ESSAS OPÇÕES LÁ NAS PERGUNTAS DE CRIAR COMANDA
    print(f"\033[1;36m{str(nome_completo.title()):^50}\033[m")
    print("\033[1;36m=\033[m" * 50)
    print(f"{nomef:<40}{dataf}")
    print(f"{telf:<40}{semanf}")
    print(f"{celf:<40}{hora_prontaf}")
    print(f"{hora_entregaf}")
    print("\033[1;36m=\033[m" * 50)

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


def criar_comanda(lista_salg,lista_doce,lista_sobre,lista_bolo,lista_fio_ovos,numero_itens,
                  nome_cliente,num_cel,num_tel,data,dia_semana,hora_pronta,hora_entrega):

    with open("comandas.json","r") as r:
        comanda = json.load(r)

    comanda['comandas'][f"{nome_cliente}"] = {}
    comanda['comandas'][f"{nome_cliente}"]['celular'] = num_cel
    comanda['comandas'][f"{nome_cliente}"]['telefone'] = num_tel
    comanda['comandas'][f"{nome_cliente}"]['data'] = data
    comanda['comandas'][f"{nome_cliente}"]['dia_semana'] = dia_semana
    comanda['comandas'][f"{nome_cliente}"]['hora_pronta'] = hora_pronta
    comanda['comandas'][f"{nome_cliente}"]['hora_entrega'] = hora_entrega
    comanda['comandas'][f"{nome_cliente}"]["num_item"] = numero_itens
    comanda['comandas'][f"{nome_cliente}"]['salgados'] = lista_salg
    comanda['comandas'][f"{nome_cliente}"]['doces'] = lista_doce
    comanda['comandas'][f"{nome_cliente}"]['bolos'] = lista_bolo
    comanda['comandas'][f"{nome_cliente}"]['sobremesas'] = lista_sobre
    comanda['comandas'][f"{nome_cliente}"]['fio_de_ovos'] = lista_fio_ovos
    comanda['comandas'][f"{nome_cliente}"]['ADICIONADO'] = {}

    with open("comandas.json", "w") as w:
        json.dump(comanda, w, indent=4)
def salvar_comandas(lista_salg,lista_doce,lista_sobre,lista_bolo,lista_fio_ovos,numero_itens,nome_cliente):
    with open("comandas.json","r") as r:
        comanda = json.load(r)

    # comanda["comandas"][f"{nome_cliente}"] = {} #Nao sei se da ruim tirar a lista kkk
    comanda["comandas"][f"{nome_cliente}"]['salgados'] = lista_salg
    comanda["comandas"][f"{nome_cliente}"]['doces'] = lista_doce
    comanda["comandas"][f"{nome_cliente}"]['bolos'] = lista_bolo
    comanda["comandas"][f"{nome_cliente}"]['sobremesas'] = lista_sobre
    comanda["comandas"][f"{nome_cliente}"]['fio_de_ovos'] = lista_fio_ovos
    comanda["comandas"][f"{nome_cliente}"]['ADICIONADO'] = {}
    comanda["comandas"][f"{nome_cliente}"]['ADICIONADO']["salgados"] = []
    comanda["comandas"][f"{nome_cliente}"]['ADICIONADO']["doces"] = []
    comanda["comandas"][f"{nome_cliente}"]['ADICIONADO']["bolos"] = []
    comanda["comandas"][f"{nome_cliente}"]['ADICIONADO']["sobremesas"] = []
    comanda["comandas"][f"{nome_cliente}"]['ADICIONADO']["fio_de_ovos"] = []

    comanda['comandas'][f"{nome_cliente}"]["num_item"] = numero_itens
    comanda["num"] += 1

    # print(comanda)
    with open("comandas.json", "w") as w:
        json.dump(comanda, w, indent=4)

def mostrar_comanda_geral(comanda,nome):
    nome_completo = ""
    for nome in nome.split("_"):
        nome_completo += f"{nome} "
    data = comanda['data']
    num_tel = comanda['telefone']
    num_cel = comanda['celular']
    dia_semana = comanda['dia_semana']
    hora_pronta = comanda['hora_pronta']
    hora_entrega = comanda['hora_entrega']

    nomef = f"\033[33mNome:\033[m {nome_completo.title()}"
    data = f"\033[33mData:\033[m {data}"
    telf = f'\033[33mTelefone:\033[m {num_tel}'
    semanf = f"\033[33mDia da semana:\033[m {dia_semana}"
    celf = f'\033[33mCelular:\033[m {num_cel}'
    hora_prontaf = f'\033[33mHora (Pronto):\033[m {hora_pronta}'
    hora_entregaf = f'\033[33mHora(Entrega):\033[m {hora_entrega:<40}'



    print("\033[1;36m=\033[m" * 50)  # COLOCAR TUDO ESSAS OPÇÕES LÁ NAS PERGUNTAS DE CRIAR COMANDA
    print(f"\033[1;36m{str(nome_completo.title()):^50}\033[m")
    print("\033[1;36m=\033[m" * 50)
    print(f"{nomef:<40}{data}")
    print(f"{telf:<40}{semanf}")
    print(f"{celf:<40}{hora_prontaf}")
    print(f"{hora_entregaf}")
    print("\033[1;36m=\033[m" * 50)

    for tipo in comanda:
        # print(tipo)
        if isinstance(comanda[tipo], int) or isinstance(comanda[tipo], str):
            continue
        if len(comanda[tipo]) > 0:
            if str(tipo) == "ADICIONADO":
                print("-"*40)
                printar = f'--||{str(tipo).capitalize()}||--'
                print(f"\033[33m{printar:^50}\033[m")
                for cat_add in comanda[tipo]:
                    for item in comanda[tipo][cat_add]:
                        print(item)
            else:
                printar = f'--||{str(tipo).capitalize()}||--'
                print(f"\033[34m{printar:^50}\033[m")
                for c in comanda[tipo]:
                    print(c)
    print("\033[1;36m=\033[m" * 50)

def mostrar_comanda_salgados(comanda,nome):
    nome_completo = ""
    for nome in nome.split("_"):
        nome_completo += f"{nome} "
    data = comanda['data']
    num_tel = comanda['telefone']
    num_cel = comanda['celular']
    dia_semana = comanda['dia_semana']
    hora_pronta = comanda['hora_pronta']
    hora_entrega = comanda['hora_entrega']

    nomef = f"\033[33mNome:\033[m {nome_completo.title()}"
    dataf = f"\033[33mData:\033[m {data}"
    telf = f'\033[33mTelefone:\033[m {num_tel}'
    semanf = f"\033[33mDia da semana:\033[m {dia_semana}"
    celf = f'\033[33mCelular:\033[m {num_cel}'
    hora_prontaf = f'\033[33mHora(Pronto):\033[m {hora_pronta}'
    hora_entregaf = f'\033[33mHora(Entrega):\033[m {hora_entrega:<40}'

    if len(comanda['salgados']) != 0:
        print("\033[1;36m=\033[m" * 50)  # COLOCAR TUDO ESSAS OPÇÕES LÁ NAS PERGUNTAS DE CRIAR COMANDA
        print(f"\033[1;36m{str(nome_completo.title() + '- SALGADOS'):^50}\033[m")
        print("\033[1;36m=\033[m" * 50)
        print(f"{nomef:<40}{dataf}")
        print(f"{telf:<40}{semanf}")
        print(f"{celf:<40}{hora_prontaf}")
        print(f"{hora_entregaf}")
        print("\033[1;36m=\033[m" * 50)

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
        print()

    else:
        print("\033[1;31mSem salgados nesse comanda!\033[m\n")

def mostrar_comanda_doces(comanda,nome):
    nome_completo = ""
    for nome in nome.split("_"):
        nome_completo += f"{nome} "
    dataf = comanda['data']
    num_tel = comanda['telefone']
    num_cel = comanda['celular']
    dia_semana = comanda['dia_semana']
    hora_pronta = comanda['hora_pronta']
    hora_entrega = comanda['hora_entrega']

    nomef = f"\033[33mNome:\033[m {nome_completo.title()}"
    data = f"\033[33mData:\033[m {dataf}"
    telf = f'\033[33mTelefone:\033[m {num_tel}'
    semanf = f"\033[33mDia da semana:\033[m {dia_semana}"
    celf = f'\033[33mCelular:\033[m {num_cel}'
    hora_prontaf = f'\033[33mHora(Pronto):\033[m {hora_pronta}'
    hora_entregaf = f'\033[33mHora(Entrega):\033[m {hora_entrega:<40}'


    if len(comanda['doces']) != 0:
        print("\033[1;36m=\033[m" * 50)  # COLOCAR TUDO ESSAS OPÇÕES LÁ NAS PERGUNTAS DE CRIAR COMANDA
        print(f"\033[1;36m{str(nome_completo.title() + '- DOCES'):^50}\033[m")
        print("\033[1;36m=\033[m" * 50)
        print(f"{nomef:<40}{data}")
        print(f"{telf:<40}{semanf}")
        print(f"{celf:<40}{hora_prontaf}")
        print(f"{hora_entregaf}")
        print("\033[1;36m=\033[m" * 50)

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
        print("\033[1;36m=\033[m" * 50)
        print()

    else:
        print("\033[1;31mSem doces nesse comanda!\033[m\n")


def mostrar_comanda_bolos(comanda,nome):
    nome_completo = ""
    for nome in nome.split("_"):
        nome_completo += f"{nome} "
    dataf = comanda['data']
    num_tel = comanda['telefone']
    num_cel = comanda['celular']
    dia_semana = comanda['dia_semana']
    hora_pronta = comanda['hora_pronta']
    hora_entrega = comanda['hora_entrega']

    nomef = f"\033[33mNome:\033[m {nome_completo.title()}"
    data = f"\033[33mData:\033[m {dataf}"
    telf = f'\033[33mTelefone:\033[m {num_tel}'
    semanf = f"\033[33mDia da semana:\033[m {dia_semana}"
    celf = f'\033[33mCelular:\033[m {num_cel}'
    hora_prontaf = f'\033[33mHora(Pronto):\033[m {hora_pronta}'
    hora_entregaf = f'\033[33mHora(Entrega):\033[m {hora_entrega:<40}'

    if len(comanda['bolos']) != 0:
        print("\033[1;36m=\033[m" * 50)  # COLOCAR TUDO ESSAS OPÇÕES LÁ NAS PERGUNTAS DE CRIAR COMANDA
        print(f"\033[1;36m{str(nome_completo.title() + '- BOLOS'):^50} - BOLOS\033[m")
        print("\033[1;36m=\033[m" * 50)
        print(f"{nomef:<40}{data}")
        print(f"{telf:<40}{semanf}")
        print(f"{celf:<40}{hora_prontaf}")
        print(f"{hora_entregaf}")
        print("\033[1;36m=\033[m" * 50)

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
        print("\033[1;36m=\033[m" * 50)
        print()
    else:
        print("\033[1;31mSem bolos nesse comanda!\033[m\n")

def mostrar_comanda_sobremesas(comanda,nome):
    nome_completo = ""
    for nome in nome.split("_"):
        nome_completo += f"{nome} "
    dataf = comanda['data']
    num_tel = comanda['telefone']
    num_cel = comanda['celular']
    dia_semana = comanda['dia_semana']
    hora_pronta = comanda['hora_pronta']
    hora_entrega = comanda['hora_entrega']

    nomef = f"\033[33mNome:\033[m {nome_completo.title()}"
    data = f"\033[33mData:\033[m {dataf}"
    telf = f'\033[33mTelefone:\033[m {num_tel}'
    semanf = f"\033[33mDia da semana:\033[m {dia_semana}"
    celf = f'\033[33mCelular:\033[m {num_cel}'
    hora_prontaf = f'\033[33mHora(Pronto):\033[m {hora_pronta}'
    hora_entregaf = f'\033[33mHora(Entrega):\033[m {hora_entrega:<40}'

    if len(comanda['sobremesas']) != 0:
        print("\033[1;36m=\033[m" * 50)  # COLOCAR TUDO ESSAS OPÇÕES LÁ NAS PERGUNTAS DE CRIAR COMANDA
        print(f"\033[1;36m{str(nome_completo.title() + '- SOBREMESAS'):^50} - SOBREMESAS\033[m")
        print("\033[1;36m=\033[m" * 50)
        print(f"{nomef:<40}{data}")
        print(f"{telf:<40}{semanf}")
        print(f"{celf:<40}{hora_prontaf}")
        print(f"{hora_entregaf}")
        print("\033[1;36m=\033[m" * 50)

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
        print("\033[1;36m=\033[m" * 50)
        print()

    else:
        print("\033[1;31mSem sobremesas nesse comanda!\033[m\n")

def mostrar_comanda_fio_de_ovos(comanda,nome):
    nome_completo = ""
    for nome in nome.split("_"):
        nome_completo += f"{nome} "
    dataf = comanda['data']
    num_tel = comanda['telefone']
    num_cel = comanda['celular']
    dia_semana = comanda['dia_semana']
    hora_pronta = comanda['hora_pronta']
    hora_entrega = comanda['hora_entrega']

    nomef = f"\033[33mNome:\033[m {nome_completo.title()}"
    data = f"\033[33mData:\033[m {dataf}"
    telf = f'\033[33mTelefone:\033[m {num_tel}'
    semanf = f"\033[33mDia da semana:\033[m {dia_semana}"
    celf = f'\033[33mCelular:\033[m {num_cel}'
    hora_prontaf = f'\033[33mHora(Pronto):\033[m {hora_pronta}'
    hora_entregaf = f'\033[33mHora(Entrega):\033[m{hora_entrega:<40}'

    if len(comanda['fio_de_ovos']) != 0:
        print("\033[1;36m=\033[m" * 50)  # COLOCAR TUDO ESSAS OPÇÕES LÁ NAS PERGUNTAS DE CRIAR COMANDA
        print(f"\033[1;36m{str(nome_completo.title() + '- FIO DE OVOS'):^50} - FIO DE OVOS\033[m")
        print("\033[1;36m=\033[m" * 50)
        print(f"{nomef:<40}{data}")
        print(f"{telf:<40}{semanf}")
        print(f"{celf:<40}{hora_prontaf}")
        print(f"{hora_entregaf}")
        print("\033[1;36m=\033[m" * 50)

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
        print("\033[1;36m=\033[m" * 50)
        print()

    else:
        print("\033[1;31mSem Fio de ovos nesse comanda!\033[m\n")
def excluir_comanda(nome):
    with open("comandas.json","r") as r:
        comandas = json.load(r)

    comanda = comandas['comandas'][f'{nome}']

    nome_completo = ""
    for nome in nome.split("_"):
        nome_completo += f"{nome} "

    dataf = comanda['data']
    num_tel = comanda['telefone']
    num_cel = comanda['celular']
    dia_semana = comanda['dia_semana']
    hora_pronta = comanda['hora_pronta']
    hora_entrega = comanda['hora_entrega']

    nomef = f"\033[33mNome:\033[m {nome_completo.title()}"
    dataf = f"\033[33mData:\033[m {dataf}"
    telf = f'\033[33mTelefone:\033[m {num_tel}'
    semanf = f"\033[33mDia da semana:\033[m {dia_semana}"
    celf = f'\033[33mCelular:\033[m {num_cel}'
    hora_prontaf = f'\033[33mHora(Pronto):\033[m {hora_pronta}'
    hora_entregaf = f'\033[33mHora(Entrega):\033[m{hora_entrega:<40}'

    print("\033[1;36m=\033[m" * 50)  # COLOCAR TUDO ESSAS OPÇÕES LÁ NAS PERGUNTAS DE CRIAR COMANDA
    print(f"\033[1;36m{str(nome_completo.capitalize()).capitalize():^50}\033[m")
    print("\033[1;36m=\033[m" * 50)
    print(f"{nomef:<40}{dataf}")
    print(f"{telf:<40}{semanf}")
    print(f"{celf:<40}{hora_prontaf}")
    print(f"{hora_entregaf}")
    print("\033[1;36m=\033[m" * 50)

    for tipo in comanda:
        if isinstance(comanda[tipo], int) or isinstance(comanda[tipo], str):
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
        if isinstance(comanda[tipo], int) or isinstance(comanda[tipo], str):
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






















