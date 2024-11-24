import json
from datetime import datetime
import escolha_valida


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
    hora_entregaf = f'\033[33mHora(Entrega):\033[m{hora_entrega}'

    print("\033[1;36m=\033[m" * 50)  # COLOCAR TUDO ESSAS OPÇÕES LÁ NAS PERGUNTAS DE CRIAR COMANDA
    print(f"\033[1;36m{str(nome_completo.title()):^50}\033[m")
    print("\033[1;36m=\033[m" * 50)
    print(f"{nomef:<40}{dataf}")
    print(f"{telf:<40}{semanf}")
    print(f"{celf:<40}{hora_prontaf}")
    print(f"{' ':<32}{hora_entregaf}")
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
    print("\033[1;36m=\033[m" * 50)


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
def salvar_relatorio_diario_completo(lista_salg,lista_doce,lista_sobre,lista_bolo,lista_fio_ovos,numero_itens,nome_cliente):
    with open("relatorio_diario_completo.json","r") as r:
        rel_completo = json.load(r)
    with open("comandas.json","r") as r:
        comanda = json.load(r)

    data = comanda['comandas'][nome_cliente]['data']
    horario = comanda['comandas'][nome_cliente]['hora_pronta']

    if data not in rel_completo:
        rel_completo[data] = {}
    if horario not in rel_completo[data]:
        rel_completo[data][horario] = {}

    rel_completo[data][horario][f'{nome_cliente}'] = {}
    rel_completo[data][horario][f"{nome_cliente}"]['salgado'] = lista_salg
    rel_completo[data][horario][f"{nome_cliente}"]['doce'] = lista_doce
    rel_completo[data][horario][f"{nome_cliente}"]['bolo'] = lista_bolo
    rel_completo[data][horario][f"{nome_cliente}"]['sobremesa'] = lista_sobre
    rel_completo[data][horario][f"{nome_cliente}"]['fio_de_ovos'] = lista_fio_ovos
    rel_completo[data][horario][f"{nome_cliente}"]['ADICIONADO'] = {}
    rel_completo[data][horario][f"{nome_cliente}"]['ADICIONADO']["salgado"] = []
    rel_completo[data][horario][f"{nome_cliente}"]['ADICIONADO']["doce"] = []
    rel_completo[data][horario][f"{nome_cliente}"]['ADICIONADO']["bolo"] = []
    rel_completo[data][horario][f"{nome_cliente}"]['ADICIONADO']["sobremesa"] = []
    rel_completo[data][horario][f"{nome_cliente}"]['ADICIONADO']["fio_de_ovos"] = []

    # print(comanda)
    def converter_horario(horario_str):
        return datetime.strptime(horario_str, "%H:%M")

    lista_horarios = []
    for hora in rel_completo[data]:
        lista_horarios.append(hora)

    sorted_keys = sorted(lista_horarios, key=lambda h: datetime.strptime(h, "%H:%M"))

    sorted_data = {}
    sorted_data[data] = {}
    for key in sorted_keys: # keys = hora
        sorted_data[data][key] = rel_completo[data][key]

    rel_completo[data] = sorted_data[data]

    # print(comanda)
    with open("relatorio_diario_completo.json", "w") as w:
        json.dump(rel_completo, w, indent=4)

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
    dataf = f"\033[33mData:\033[m {data}"
    telf = f'\033[33mTelefone:\033[m {num_tel}'
    semanf = f"\033[33mDia da semana:\033[m {dia_semana}"
    celf = f'\033[33mCelular:\033[m {num_cel}'
    hora_prontaf = f'\033[33mHora (Pronto):\033[m {hora_pronta}'
    hora_entregaf = f'\033[33mHora(Entrega):\033[m {hora_entrega}'

    print("\033[1;36m=\033[m" * 50)  # COLOCAR TUDO ESSAS OPÇÕES LÁ NAS PERGUNTAS DE CRIAR COMANDA
    print(f"\033[1;36m{str(nome_completo.title())+'- GERAL':^50}\033[m")
    print("\033[1;36m=\033[m" * 50)
    print(f"{nomef:<40}{dataf}")
    print(f"{telf:<40}{semanf}")
    print(f"{celf:<40}{hora_prontaf}")
    print(f"{' ':<32}{hora_entregaf}")
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
    hora_entregaf = f'\033[33mHora(Entrega):\033[m {hora_entrega}'

    if len(comanda["salgados"]) > 0 or len(comanda["ADICIONADO"]["salgados"]) > 0:
        print("\033[1;36m=\033[m" * 50)  # COLOCAR TUDO ESSAS OPÇÕES LÁ NAS PERGUNTAS DE CRIAR COMANDA
        print(f"\033[1;36m{str(nome_completo.title())+'- SALGADOS':^50}\033[m")
        print("\033[1;36m=\033[m" * 50)
        print(f"{nomef:<40}{dataf}")
        print(f"{telf:<40}{semanf}")
        print(f"{celf:<40}{hora_prontaf}")
        print(f"{' ':<32}{hora_entregaf}")
        print("\033[1;36m=\033[m" * 50)


        for salgado in comanda["salgados"]:
            print(salgado)
        for salgado_add in comanda["ADICIONADO"]["salgados"]:
            print(salgado_add)

        print("\033[1;36m=\033[m" * 40)
        print()

    else:
        print("\033[1;31mSem salgados nesse comanda!\033[m\n")

def mostrar_comanda_doces(comanda,nome):
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
    hora_entregaf = f'\033[33mHora(Entrega):\033[m {hora_entrega}'


    if len(comanda["doces"]) > 0 or len(comanda["ADICIONADO"]["doces"]) > 0:
        print("\033[1;36m=\033[m" * 50)  # COLOCAR TUDO ESSAS OPÇÕES LÁ NAS PERGUNTAS DE CRIAR COMANDA
        print(f"\033[1;36m{str(nome_completo.title())+'- DOCES':^50}\033[m")
        print("\033[1;36m=\033[m" * 50)
        print(f"{nomef:<40}{dataf}")
        print(f"{telf:<40}{semanf}")
        print(f"{celf:<40}{hora_prontaf}")
        print(f"{' ':<32}{hora_entregaf}")
        print("\033[1;36m=\033[m" * 50)


        for doce in comanda["doces"]:
            print(doce)
        for doce_add in comanda["ADICIONADO"]["doces"]:
            print(doce_add)

        print("\033[1;36m=\033[m" * 50)
        print()

    else:
        print("\033[1;31mSem doces nesse comanda!\033[m\n")


def mostrar_comanda_bolos(comanda,nome):
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
    hora_entregaf = f'\033[33mHora(Entrega):\033[m {hora_entrega}'

    if len(comanda["bolos"]) > 0 or len(comanda["ADICIONADO"]["bolos"]) > 0:
        print("\033[1;36m=\033[m" * 50)  # COLOCAR TUDO ESSAS OPÇÕES LÁ NAS PERGUNTAS DE CRIAR COMANDA
        print(f"\033[1;36m{str(nome_completo.title())+'- BOLOS':^50}\033[m")
        print("\033[1;36m=\033[m" * 50)
        print(f"{nomef:<40}{dataf}")
        print(f"{telf:<40}{semanf}")
        print(f"{celf:<40}{hora_prontaf}")
        print(f"{' ':<32}{hora_entregaf}")
        print("\033[1;36m=\033[m" * 50)

        for bolo in comanda["bolos"]:
            print(bolo)
        for bolo_add in comanda["ADICIONADO"]["bolos"]:
            print(bolo_add)

        print("\033[1;36m=\033[m" * 50)
        print()

    else:
        print("\033[1;31mSem bolos nesse comanda!\033[m\n")

def mostrar_comanda_sobremesas(comanda,nome):
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
    hora_entregaf = f'\033[33mHora(Entrega):\033[m {hora_entrega}'

    if len(comanda["sobremesas"]) > 0 or len(comanda["ADICIONADO"]["sobremesas"]) > 0:
        print("\033[1;36m=\033[m" * 50)  # COLOCAR TUDO ESSAS OPÇÕES LÁ NAS PERGUNTAS DE CRIAR COMANDA
        print(f"\033[1;36m{str(nome_completo.title())+'- SOBREMESAS':^50}\033[m")
        print("\033[1;36m=\033[m" * 50)
        print(f"{nomef:<40}{dataf}")
        print(f"{telf:<40}{semanf}")
        print(f"{celf:<40}{hora_prontaf}")
        print(f"{' ':<32}{hora_entregaf}")
        print("\033[1;36m=\033[m" * 50)

        for sobremesa in comanda["sobremesas"]:
            print(sobremesa)
        for sobremesa_add in comanda["ADICIONADO"]["sobremesas"]:
            print(sobremesa_add)

        print("\033[1;36m=\033[m" * 50)
        print()

    else:
        print("\033[1;31mSem sobremesas nesse comanda!\033[m\n")

def mostrar_comanda_fio_de_ovos(comanda,nome):
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
    hora_entregaf = f'\033[33mHora(Entrega):\033[m{hora_entrega}'

    if len(comanda["fio_de_ovos"]) > 0 or len(comanda["ADICIONADO"]["fio_de_ovos"]) > 0:
        print("\033[1;36m=\033[m" * 50)  # COLOCAR TUDO ESSAS OPÇÕES LÁ NAS PERGUNTAS DE CRIAR COMANDA
        print(f"\033[1;36m{str(nome_completo.title())+'- FIO DE OVOS':^50}\033[m")
        print("\033[1;36m=\033[m" * 50)
        print(f"{nomef:<40}{dataf}")
        print(f"{telf:<40}{semanf}")
        print(f"{celf:<40}{hora_prontaf}")
        print(f"{' ':<32}{hora_entregaf}")
        print("\033[1;36m=\033[m" * 50)

        for fio_de_ovos in comanda["fio_de_ovos"]:
            print(fio_de_ovos)
        for fio_de_ovo_add in comanda["ADICIONADO"]["fio_de_ovos"]:
            print(fio_de_ovo_add)

        print("\033[1;36m=\033[m" * 50)
        print()

    else:
        print("\033[1;31mSem Fio de ovos nesse comanda!\033[m\n")
def excluir_comanda(nome):
    with open("comandas.json","r") as r:
        comandas = json.load(r)
    with open("dados.json", "r") as r:
        dados = json.load(r)
    with open("relatorio_diario_completo.json","r") as r:
        relatorio = json.load(r)

    comanda = comandas['comandas'][f'{nome}']
    data = comanda['data']
    hora = comanda['hora_pronta']
    rel_completo = relatorio[data][hora][f'{nome}']

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
    hora_entregaf = f'\033[33mHora(Entrega):\033[m{hora_entrega}'

    print("\033[1;36m=\033[m" * 50)  # COLOCAR TUDO ESSAS OPÇÕES LÁ NAS PERGUNTAS DE CRIAR COMANDA
    print(f"\033[1;36m{str(nome_completo.title()):^50}\033[m")
    print("\033[1;36m=\033[m" * 50)
    print(f"{nomef:<40}{dataf}")
    print(f"{telf:<40}{semanf}")
    print(f"{celf:<40}{hora_prontaf}")
    print(f"{hora_entregaf:>56}")
    print("\033[1;36m=\033[m" * 50)

    data_encomenda = comanda['data']

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

    print("\033[1;36m=\033[m" * 50)

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
                    #EXCLUIR EM COMANDAS
                    if num_excluir not in itens_split[0]: #SE O NÃO FOR O ITEM, É ADICIONADO NA LISTA
                        lista_adicionados.append(itens)

                    #EXCLUIR EM DADOS
                    else:                                 #SE FOR O ITEM
                        escolha_valida.validar_exclusao(itens_split,itens_split[2],data_encomenda) #(Produto, quantidade)

                comanda[tipo][tipos_add] = lista_adicionados

        else:
            lista_itens = []
            for itens in comanda[tipo]:
                itens_split = str(itens).split()
                # EXCLUIR EM COMANDAS
                if num_excluir not in itens_split[0]: #SE O NÃO FOR O ITEM, É ADICIONADO NA LISTA
                    lista_itens.append(itens)
                # EXCLUIR EM DADOS
                else:                                   #SE FOR O ITEM
                    escolha_valida.validar_exclusao(itens_split,itens_split[2],data_encomenda)  #(Produto, quantidade)
            comanda[tipo] = lista_itens

    # RELATORIO DIARIO COMPLETO
    for tipo in rel_completo:

        if tipo == "ADICIONADO":
            for tipos_add in rel_completo[tipo]:
                lista_adicionados_relatorio = []
                for itens in rel_completo[tipo][tipos_add]:
                    itens_split = str(itens).split()
                    # EXCLUIR EM RELATORIO DIARIO COMPLETO
                    if num_excluir not in itens_split[0]: #SE O NÃO FOR O ITEM, É ADICIONADO NA LISTA
                        lista_adicionados_relatorio.append(itens)

                rel_completo[tipo][tipos_add] = lista_adicionados_relatorio
        else:
            lista_adicionados_relatorio = []
            for itens in rel_completo[tipo]:
                itens_split = str(itens).split()
                # EXCLUIR EM RELATORIO DIARIO COMPLETO
                if num_excluir not in itens_split[0]: #SE O NÃO FOR O ITEM, É ADICIONADO NA LISTA
                    lista_adicionados_relatorio.append(itens)

            rel_completo[tipo] = lista_adicionados_relatorio

    with open("comandas.json", "w") as w:
        json.dump(comandas, w, indent=4)
    with open("relatorio_diario_completo.json", "w") as wr:
        json.dump(relatorio, wr, indent=4)

    print(f"\033[32mItem {num_excluir} excluído com sucesso\033[m")
    print()

def relatorio_geral():
    with open("dados.json", "r") as r:
        dados = json.load(r)

    print(f"\n \033[1;34m{'-'*20}{'||Geral||'}{'-'*20}\033[m")

    #DOCES
    print("\033[33m|| Doces || \033[m")

    tradicionais = dados['doce']['tradicional/espelhado']
    print("\033[4;34m(Tradicionais)\033[m")
    for doces in sorted(tradicionais):
        print(f"\033[36m{doces} = \033[33m{tradicionais[doces]}\033[m")

    bombom = dados['doce']['bombom']
    print("\n\033[4;34m(Bombom)\033[m")
    for doces in sorted(bombom):
        print(f"\033[36m{doces} = \033[33m{bombom[doces]}\033[m")

    #SALGADOS
    print("\n\033[33m|| Salgados || \033[m")

    fritos = dados['salgado']['fritos']
    print("\n\033[4;34m(Fritos)\033[m")
    for salgados in sorted(fritos):
        print(f"\033[36m{salgados} = \033[33m{fritos[salgados]}\033[m")

    assados = dados['salgado']['assados']
    print("\n\033[4;34m(Assados)\033[m")
    for salgados in sorted(assados):
        print(f"\033[36m{salgados} = \033[33m{assados[salgados]}\033[m")

    empadao = dados['salgado']['empadao']
    print("\n\033[4;34m(Empadào)\033[m")
    for salgados in sorted(empadao):
        print(f"\033[36m{salgados} = \033[33m{empadao[salgados]}\033[m")

    #BOLO
    print("\n\033[33m|| Bolos || \033[m")

    bolos = dados['bolo']
    for bolo in sorted(bolos):
        print(f"\033[36m{bolo} = \033[33m{bolos[bolo]}")

    #SOBREMESAS
    print("\n\033[33m|| Sobremesas || \033[m")

    tortas = dados['sobremesa']['tortas']
    print("\n\033[4;34m(Tortas)\033[m")
    for sobremesa in sorted(tortas):
        print(f"\033[36m{sobremesa} = \033[33m{tortas[sobremesa]}\033[m")

    outras = dados['sobremesa']['Paves/Profiteroles/Banoff/Mil Folhas']
    print("\n\033[4;34m(Paves/Profiteroles/Banoff/Mil Folhas)\033[m")
    for sobremesa in sorted(outras):
        print(f"\033[36m{sobremesa} = \033[33m{outras[sobremesa]}\033[m")

    #Fio de ovos
    print("\n\033[33m|| Fio de Ovos || \033[m")
    fio_ovos = dados['fio_de_ovos']
    for fio in fio_ovos:
        print(f"\033[36m{str(fio).capitalize()} = \033[33m{fio_ovos[fio]}\033[m")


    print("-"*45)
    print()

def relatorio_salgados():
    with open("dados.json", "r") as r:
        dados = json.load(r)

    print("\n\033[33m|| Salgados || \033[m")

    fritos = dados['salgado']['fritos']
    print("\n\033[4;34m(Fritos)\033[m")
    for salgados in sorted(fritos):
        print(f"\033[36m{salgados} = \033[33m{fritos[salgados]}\033[m")

    assados = dados['salgado']['assados']
    print("\n\033[4;34m(Assados)\033[m")
    for salgados in sorted(assados):
        print(f"\033[36m{salgados} = \033[33m{assados[salgados]}\033[m")

    empadao = dados['salgado']['empadao']
    print("\n\033[4;34m(Empadào)\033[m")
    for salgados in sorted(empadao):
        print(f"\033[36m{salgados} = \033[33m{empadao[salgados]}\033[m")


    print("-" * 45)
    print()

def relatorio_doces():
    with open("dados.json", "r") as r:
        dados = json.load(r)

    print("\033[33m|| Doces || \033[m")

    tradicionais = dados['doce']['tradicional/espelhado']
    print("\033[4;34m(Tradicionais)\033[m")
    for doces in sorted(tradicionais):
        print(f"\033[36m{doces} = \033[33m{tradicionais[doces]}\033[m")

    bombom = dados['doce']['bombom']
    print("\n\033[4;34m(Bombom)\033[m")
    for doces in sorted(bombom):
        print(f"\033[36m{doces} = \033[33m{bombom[doces]}\033[m")


    print("-" * 45)
    print()

def relatorio_bolos():
    with open("dados.json", "r") as r:
        dados = json.load(r)

    print("\n\033[33m|| Bolos || \033[m")

    bolos = dados['bolo']
    for bolo in sorted(bolos):
        print(f"\033[36m{bolo} = \033[33m{bolos[bolo]}")


    print("-" * 45)
    print()

def relatorio_sobremesas():
    with open("dados.json", "r") as r:
        dados = json.load(r)

    print("\n\033[33m|| Sobremesas || \033[m")

    tortas = dados['sobremesa']['tortas']
    print("\n\033[4;34m(Tortas)\033[m")
    for sobremesa in sorted(tortas):
        print(f"\033[36m{sobremesa} = \033[33m{tortas[sobremesa]}\033[m")

    outras = dados['sobremesa']['Paves/Profiteroles/Banoff/Mil Folhas']
    print("\n\033[4;34m(Paves/Profiteroles/Banoff/Mil Folhas)\033[m")
    for sobremesa in sorted(outras):
        print(f"\033[36m{sobremesa} = \033[33m{outras[sobremesa]}\033[m")

    # # Fio de ovos
    # print("\n\033[33m|| Fio de Ovos || \033[m")
    # fio_ovos = dados['fio_de_ovos']
    # for fio in fio_ovos:
    #     print(f"\033[36m{str(fio).capitalize()} = \033[33m{fio_ovos[fio]}\033[m")
    #
    # print("-" * 45)
    # print()

def relatorio_fio_ovos():
    with open("dados.json", "r") as r:
        dados = json.load(r)

    print("\n\033[33m|| Fio de Ovos || \033[m")
    fio_ovos = dados['fio_de_ovos']
    for fio in fio_ovos:
        print(f"\033[36m{str(fio).capitalize()} = \033[33m{fio_ovos[fio]}\033[m")

    print("-" * 45)
    print()

def relatorio_diario_simples(data_formatada):
    with open("relatorio_diario_simples.json", "r") as r:
        rel_simples = json.load(r)

    print()
    print("_"*80)
    print(f"Tipo: Relatório Diário Simples")
    print(f"Data: \033[1;33m({data_formatada})\033[m")
    print("-"*80)
    for categorias in rel_simples[data_formatada]:
        print_categoria = f" \033[34m-- || {categorias.upper()} || --\033[m "
        print(f"{print_categoria:^80}")

        for produtos in rel_simples[data_formatada][categorias]:
            print_produtos = f" \033[33m>>\033[m {produtos} : {rel_simples[data_formatada][categorias][produtos]} \033[33m<<\033[m "
            print(f"{print_produtos:^90}")
    print("-"*80)
    print()

def relatorio_diario_completo(data_formatada):
    with open("relatorio_diario_completo.json", "r") as r:
        rel_completo = json.load(r)

    while True:
        try:
            print("\nEscolha uma opção:\n")
            print("\033[33m1 - \033[34mRelatório Geral\033[m")
            print("\033[33m2 - \033[34mRelatório Salgados\033[m")
            print("\033[33m3 - \033[34mRelatório Doces\033[m")
            print("\033[33m4 - \033[34mRelatório Bolos\033[m")
            print("\033[33m5 - \033[34mRelatório Sobremesas\033[m")
            print("\033[33m6 - \033[34mRelatório Fio de Ovos\033[m\n")
            esc_relatorio = int(input("Escolha: "))

            if esc_relatorio > 6 or esc_relatorio < 1:
                print("\033[31mEscolha um número entre 1 e 6 apenas!\033[m\n")
            else:
                break
        except ValueError:
            print("\033[31mEscolha um número entre 1 e 6 apenas!\033[m\n")

    print()
    print("_" * 80)
    print(f"Tipo: Relatório Diário Completo")
    print(f"Categoria: {rel_completo}")
    print(f"Data: \033[1;33m({data_formatada})\033[m")
    print("-" * 80)

    if esc_relatorio == 1:
        for dia in rel_completo:

            if dia == data_formatada:
                for hora in rel_completo[dia]:

                    printar_hora = f"█   {hora:>20}{'█':>20}"
                    print(f'{"━"*43:^80}')
                    print(f"{printar_hora:^80}")
                    print(f'{"━"*43:^80}')

                    for cliente in rel_completo[dia][hora]:
                        nome_completo = ""
                        for nome in cliente.split("_"):
                            nome_completo += f"{nome} "

                        print(f"\033[33m{'='*40:^80}\033[m")
                        print(f"\033[33m{nome_completo.title():^80}\033[m")
                        print(f"\033[33m{'=' * 40:^80}\033[m")

                        for categoria in rel_completo[dia][hora][cliente]:
                            print_categoria = f" \033[34m-- || {categoria.upper()} || --\033[m "
                            print(f"{print_categoria:^85}")

                            if categoria == "ADICIONADO":
                                for cat_add in rel_completo[dia][hora][cliente][categoria]:
                                    for item in rel_completo[dia][hora][cliente][categoria][cat_add]:
                                        print_produtos = f" \033[33m>>\033[m {item}  \033[33m<<\033[m "
                                        print(f"{print_produtos:^95}")
                            else:
                                for item in rel_completo[dia][hora][cliente][categoria]:
                                    print_produtos = f" \033[33m>>\033[m {item} \033[33m<<\033[m "
                                    print(f"{print_produtos:^95}")
    elif esc_relatorio == 2:
        for dia in rel_completo:

            if dia == data_formatada:
                for hora in rel_completo[dia]:

                    printar_hora = f"█   {hora:>20}{'█':>20}"
                    print(f'{"━"*43:^80}')
                    print(f"{printar_hora:^80}")
                    print(f'{"━"*43:^80}')

                    for cliente in rel_completo[dia][hora]:
                        nome_completo = ""

                        if len(rel_completo[dia][hora][cliente]['salgado']) > 0 or len(rel_completo[dia][hora][cliente]["ADICIONADO"]['salgado']) > 0: # Só mostra de o cliente tiver a categoria
                            for nome in cliente.split("_"):
                                nome_completo += f"{nome} "

                            print(f"\033[33m{'='*40:^80}\033[m")
                            print(f"\033[33m{nome_completo.title():^80}\033[m")
                            print(f"\033[33m{'=' * 40:^80}\033[m")
                            print_categoria = f" \033[34m-- || SALGADOS || --\033[m "
                            print(f"{print_categoria:^85}")

                            for item in rel_completo[dia][hora][cliente]['salgado']:

                                print_produtos = f" \033[33m>>\033[m {item}  \033[33m<<\033[m "
                                print(f"{print_produtos:^95}")

                            for item in rel_completo[dia][hora][cliente]["ADICIONADO"]["salgado"]:
                                print_produtos = f" \033[33m>>\033[m {item}  \033[33m<<\033[m "
                                print(f"{print_produtos:^95}")

    elif esc_relatorio == 3:
        for dia in rel_completo:

            if dia == data_formatada:
                for hora in rel_completo[dia]:

                    printar_hora = f"█   {hora:>20}{'█':>20}"
                    print(f'{"━"*43:^80}')
                    print(f"{printar_hora:^80}")
                    print(f'{"━"*43:^80}')

                    for cliente in rel_completo[dia][hora]:
                        nome_completo = ""

                        if len(rel_completo[dia][hora][cliente]['doce']) > 0 or len(rel_completo[dia][hora][cliente]["ADICIONADO"]['doce']) > 0: # Só mostra de o cliente tiver a categoria
                            for nome in cliente.split("_"):
                                nome_completo += f"{nome} "

                            print(f"\033[33m{'='*40:^80}\033[m")
                            print(f"\033[33m{nome_completo.title():^80}\033[m")
                            print(f"\033[33m{'=' * 40:^80}\033[m")
                            print_categoria = f" \033[34m-- || DOCES || --\033[m "
                            print(f"{print_categoria:^85}")

                            for item in rel_completo[dia][hora][cliente]['doce']:

                                print_produtos = f" \033[33m>>\033[m {item}  \033[33m<<\033[m "
                                print(f"{print_produtos:^95}")

                            for item in rel_completo[dia][hora][cliente]["ADICIONADO"]["doce"]:
                                print_produtos = f" \033[33m>>\033[m {item}  \033[33m<<\033[m "
                                print(f"{print_produtos:^95}")

    elif esc_relatorio == 4:
        for dia in rel_completo:

            if dia == data_formatada:
                for hora in rel_completo[dia]:

                    printar_hora = f"█   {hora:>20}{'█':>20}"
                    print(f'{"━"*43:^80}')
                    print(f"{printar_hora:^80}")
                    print(f'{"━"*43:^80}')

                    for cliente in rel_completo[dia][hora]:
                        nome_completo = ""

                        if len(rel_completo[dia][hora][cliente]['bolo']) > 0 or len(rel_completo[dia][hora][cliente]["ADICIONADO"]['bolo']) > 0: # Só mostra de o cliente tiver a categoria
                            for nome in cliente.split("_"):
                                nome_completo += f"{nome} "

                            print(f"\033[33m{'='*40:^80}\033[m")
                            print(f"\033[33m{nome_completo.title():^80}\033[m")
                            print(f"\033[33m{'=' * 40:^80}\033[m")
                            print_categoria = f" \033[34m-- || BOLO || --\033[m "
                            print(f"{print_categoria:^85}")

                            for item in rel_completo[dia][hora][cliente]['bolo']:

                                print_produtos = f" \033[33m>>\033[m {item}  \033[33m<<\033[m "
                                print(f"{print_produtos:^95}")

                            for item in rel_completo[dia][hora][cliente]["ADICIONADO"]["bolo"]:
                                print_produtos = f" \033[33m>>\033[m {item}  \033[33m<<\033[m "
                                print(f"{print_produtos:^95}")

    elif esc_relatorio == 5:
        for dia in rel_completo:

            if dia == data_formatada:
                for hora in rel_completo[dia]:

                    printar_hora = f"█   {hora:>20}{'█':>20}"
                    print(f'{"━"*43:^80}')
                    print(f"{printar_hora:^80}")
                    print(f'{"━"*43:^80}')

                    for cliente in rel_completo[dia][hora]:
                        nome_completo = ""

                        if len(rel_completo[dia][hora][cliente]['sobremesa']) > 0 or len(rel_completo[dia][hora][cliente]["ADICIONADO"]['sobremesa']) > 0: # Só mostra de o cliente tiver a categoria
                            for nome in cliente.split("_"):
                                nome_completo += f"{nome} "

                            print(f"\033[33m{'='*40:^80}\033[m")
                            print(f"\033[33m{nome_completo.title():^80}\033[m")
                            print(f"\033[33m{'=' * 40:^80}\033[m")
                            print_categoria = f" \033[34m-- || SOBREMESA || --\033[m "
                            print(f"{print_categoria:^85}")

                            for item in rel_completo[dia][hora][cliente]['sobremesa']:

                                print_produtos = f" \033[33m>>\033[m {item}  \033[33m<<\033[m "
                                print(f"{print_produtos:^95}")

                            for item in rel_completo[dia][hora][cliente]["ADICIONADO"]["sobremesa"]:
                                print_produtos = f" \033[33m>>\033[m {item}  \033[33m<<\033[m "
                                print(f"{print_produtos:^95}")

    elif esc_relatorio == 6:
        for dia in rel_completo:

            if dia == data_formatada:
                for hora in rel_completo[dia]:

                    printar_hora = f"█   {hora:>20}{'█':>20}"
                    print(f'{"━"*43:^80}')
                    print(f"{printar_hora:^80}")
                    print(f'{"━"*43:^80}')

                    for cliente in rel_completo[dia][hora]:
                        nome_completo = ""

                        if len(rel_completo[dia][hora][cliente]['fio_de_ovos']) > 0 or len(rel_completo[dia][hora][cliente]["ADICIONADO"]['fio_de_ovos']) > 0: # Só mostra de o cliente tiver a categoria
                            for nome in cliente.split("_"):
                                nome_completo += f"{nome} "

                            print(f"\033[33m{'='*40:^80}\033[m")
                            print(f"\033[33m{nome_completo.title():^80}\033[m")
                            print(f"\033[33m{'=' * 40:^80}\033[m")
                            print_categoria = f" \033[34m-- || FIO DE OVOS || --\033[m "
                            print(f"{print_categoria:^85}")

                            for item in rel_completo[dia][hora][cliente]['fio_de_ovos']:

                                print_produtos = f" \033[33m>>\033[m {item}  \033[33m<<\033[m "
                                print(f"{print_produtos:^95}")

                            for item in rel_completo[dia][hora][cliente]["ADICIONADO"]["fio_de_ovos"]:
                                print_produtos = f" \033[33m>>\033[m {item} \033[33m<<\033[m "
                                print(f"{print_produtos:^95}")

    print("-" * 80)
    print()













