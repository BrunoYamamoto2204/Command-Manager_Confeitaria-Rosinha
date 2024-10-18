import json
def formar_comandas(lista_salg,lista_doce,lista_sobre,lista_bolo,lista_fio_ovos):
    print("\033[1;36m=\033[m" * 40)
    print(f"\033[1;36m{'COMANDA':^40}\033[m")
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

def atualizar_comanda(lista_salg,lista_doce,lista_sobre,lista_bolo,lista_fio_ovos,comanda,num):
    mostrar_comanda_geral(comanda,num)
    print(f"\033[1;33m{'ADICIONADO':^40}\033[m")
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


def salvar_comandas(lista_salg,lista_doce,lista_sobre,lista_bolo,lista_fio_ovos):
    with open("comandas.json","r") as r:
        comanda = json.load(r)

    comanda["comandas"][f"comanda{comanda['num']}"] = {}
    comanda["comandas"][f"comanda{comanda['num']}"]['salgados'] = lista_salg
    comanda["comandas"][f"comanda{comanda['num']}"]['doces'] = lista_doce
    comanda["comandas"][f"comanda{comanda['num']}"]['bolos'] = lista_bolo
    comanda["comandas"][f"comanda{comanda['num']}"]['sobremesas'] = lista_sobre
    comanda["comandas"][f"comanda{comanda['num']}"]['fio_de_ovos'] = lista_fio_ovos

    comanda["num"] += 1

    with open("comandas.json", "w") as w:
        json.dump(comanda, w, indent=4)


def mostrar_comanda_geral(comanda,num):
    print("\033[1;36m=\033[m" * 40)
    print(f"\033[1;36m{'COMANDA'+' '+str(num):^40}\033[m")
    print("\033[1;36m=\033[m" * 40)
    for tipo in comanda:
        if len(comanda[tipo]) > 0:
            printar = f'--||{tipo}||--'.capitalize()
            print(f"\033[34m{printar:^40}\033[m")
            for c in comanda[tipo]:
                print(c)
    print("\033[1;36m=\033[m" * 40)





