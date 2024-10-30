import json
import escolha_valida
from comandas import *
def opc_comandas(opc):
    lista_salg = []
    lista_doce = []
    lista_sobre = []
    lista_bolo = []
    lista_fio_ovos=[]

    if opc == 1:
        numero_itens = 1
        criar_comanda(lista_salg,lista_doce,lista_sobre,lista_bolo,lista_fio_ovos,numero_itens)
        with open("comandas.json", "r") as r:
            comanda = json.load(r)
        while True:
            print()
            escolha = escolha_valida.esc_principal()
            print("="*60)
            if escolha == 1:
                salg = escolha_valida.esc_salgado()
                lista_salg.append(escolha_valida.qnd_salg(salg,comanda['num']))
            if escolha == 2:
                doce = escolha_valida.esc_doce()
                lista_doce.append(escolha_valida.qntd_doce(doce,comanda['num']))
            if escolha == 3:
                bolo  = escolha_valida.esc_bolo()
                lista_bolo.append(escolha_valida.qntd_bolo(bolo,comanda['num']))
            if escolha == 4:
                sobremesa = escolha_valida.esc_sobremesa()
                lista_sobre.append(escolha_valida.qntd_sobremesa(sobremesa,comanda['num']))
            if escolha == 5:
                lista_fio_ovos.append(escolha_valida.qntd_fio_de_ovos(comanda['num']))

            numero_itens += 1
            comanda['comandas'][f'comanda{comanda["num"]}']["num_item"] += 1
            with open("comandas.json", "w") as w:
                json.dump(comanda, w, indent=4)


            print("=" * 40)
            cont = input("Mais itens? S/N:").strip().upper()
            print("=" * 40)
            if cont == "N":
                break

        formar_comandas(lista_salg,lista_doce,lista_sobre,lista_bolo,lista_fio_ovos)
        salvar_comandas(lista_salg,lista_doce,lista_sobre,lista_bolo,lista_fio_ovos,numero_itens)

    if opc == 2:
        with open("comandas.json","r") as r:
            comandas = json.load(r)

        esc_comanda = escolha_valida.esc_comandas()
        num_comanda = escolha_valida.num_comanda()
        comanda_geral = comandas["comandas"][f"comanda{num_comanda}"]

        if esc_comanda == 1:
            mostrar_comanda_geral(comanda_geral,num_comanda)
        elif esc_comanda == 2:
            mostrar_comanda_salgados(comanda_geral,num_comanda)
        elif esc_comanda == 3:
            mostrar_comanda_doces(comanda_geral,num_comanda)
        elif esc_comanda == 4:
            mostrar_comanda_bolos(comanda_geral,num_comanda)
        elif esc_comanda == 5:
            mostrar_comanda_sobremesas(comanda_geral,num_comanda)
        elif esc_comanda == 6:
            mostrar_comanda_fio_de_ovos(comanda_geral, num_comanda)


    if opc == 3:

        with open("comandas.json","r") as r:
            comandas = json.load(r)

        num_comanda = escolha_valida.num_comanda()

        lista_salg3 = comandas["comandas"][f"comanda{num_comanda}"]['ADICIONADO']["salgados"]
        lista_doce3 = comandas["comandas"][f"comanda{num_comanda}"]['ADICIONADO']["doces"]
        lista_sobre3 = comandas["comandas"][f"comanda{num_comanda}"]['ADICIONADO']["sobremesas"]
        lista_bolo3 = comandas["comandas"][f"comanda{num_comanda}"]['ADICIONADO']["bolos"]
        lista_fio_ovos3 = comandas["comandas"][f"comanda{num_comanda}"]['ADICIONADO']["fio_de_ovos"]

        print("=" * 40)
        numero_itens = 0
        while True:
            escolha = escolha_valida.esc_principal()
            print("="*60)
            if escolha == 1:
                salg = escolha_valida.esc_salgado()
                qntd_salgado = escolha_valida.qnd_salg(salg,num_comanda)


                lista_salg3.append(qntd_salgado)
            if escolha == 2:
                doce = escolha_valida.esc_doce()
                qntd_doce = escolha_valida.qntd_doce(doce,num_comanda)

                lista_doce3.append(qntd_doce)
            if escolha == 3:
                bolo  = escolha_valida.esc_bolo()
                qntd_bolo = escolha_valida.qntd_bolo(bolo,num_comanda)
                lista_bolo3.append(qntd_bolo)
            if escolha == 4:
                sobremesa = escolha_valida.esc_sobremesa()
                qntd_sobremesa = escolha_valida.qntd_sobremesa(sobremesa,num_comanda)
                lista_sobre3.append(qntd_sobremesa)
            if escolha == 5:
                qntd_fio_ovos = escolha_valida.qntd_fio_de_ovos(num_comanda)
                lista_fio_ovos3.append(qntd_fio_ovos)

            numero_itens += 1
            comandas['comandas'][f'comanda{num_comanda}']["num_item"] += 1
            with open("comandas.json","w") as w:
                json.dump(comandas,w,indent=4)

            print("=" * 40)
            cont = input("Mais itens? S/N:").strip().upper()
            print("=" * 40)
            if cont == "N":
                break

        comanda_salva = salvar_atualizado(lista_salg3,lista_doce3,lista_sobre3,lista_bolo3,lista_fio_ovos3,num_comanda)
        mostrar_comanda_geral(comanda_salva, num_comanda)


    if opc == 4:
        num_comanda = escolha_valida.num_comanda()
        excluir_comanda(num_comanda)

    if opc == 5:
        return 5




