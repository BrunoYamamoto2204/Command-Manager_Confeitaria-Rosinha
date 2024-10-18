import json
import escolha_valida
from comandas import *
def add_itens(opc):
    lista_salg = []
    lista_doce = []
    lista_sobre = []
    lista_bolo = []
    lista_fio_ovos=[]

    if opc == 1:
        while True:
            escolha = escolha_valida.esc_principal()
            print("="*60)
            if escolha == 1:
                salg = escolha_valida.esc_salgado()
                lista_salg.append(escolha_valida.qnd_salg(salg))
            if escolha == 2:
                doce = escolha_valida.esc_doce()
                lista_doce.append(escolha_valida.qntd_doce(doce))
            if escolha == 3:
                bolo  = escolha_valida.esc_bolo()
                lista_bolo.append(escolha_valida.qntd_bolo(bolo))
            if escolha == 4:
                sobremesa = escolha_valida.esc_sobremesa()
                lista_sobre.append(escolha_valida.qntd_sobremesa(sobremesa))
            if escolha == 5:
                lista_fio_ovos.append(escolha_valida.qntd_fio_de_ovos())

            print("=" * 40)
            cont = input("Mais itens? S/N:").strip().upper()
            print("=" * 40)
            if cont == "N":
                break

        formar_comandas(lista_salg,lista_doce,lista_sobre,lista_bolo,lista_fio_ovos)
        salvar_comandas(lista_salg,lista_doce,lista_sobre,lista_bolo,lista_fio_ovos)

    if opc == 2:
        with open("comandas.json","r") as r:
            comandas = json.load(r)

        esc_comanda = escolha_valida.esc_comandas()
        num_comanda = escolha_valida.num_comanda()

        if esc_comanda == 1:
            comanda_geral = comandas["comandas"][f"comanda{num_comanda}"]
            mostrar_comanda_geral(comanda_geral,num_comanda)

    if opc == 3:
        lista_salg3 = []
        lista_doce3 = []
        lista_sobre3 = []
        lista_bolo3 = []
        lista_fio_ovos3 = []

        with open("comandas.json","r") as r:
            comandas = json.load(r)

        num_comanda = escolha_valida.num_comanda()
        comanda_atua = comandas["comandas"][f"comanda{num_comanda}"]

        while True:
            escolha = escolha_valida.esc_principal()
            print("="*60)
            if escolha == 1:
                salg = escolha_valida.esc_salgado()
                lista_salg3.append(escolha_valida.qnd_salg(salg))
            if escolha == 2:
                doce = escolha_valida.esc_doce()
                lista_doce3.append(escolha_valida.qntd_doce(doce))
            if escolha == 3:
                bolo  = escolha_valida.esc_bolo()
                lista_bolo3.append(escolha_valida.qntd_bolo(bolo))
            if escolha == 4:
                sobremesa = escolha_valida.esc_sobremesa()
                lista_sobre3.append(escolha_valida.qntd_sobremesa(sobremesa))
            if escolha == 5:
                lista_fio_ovos3.append(escolha_valida.qntd_fio_de_ovos())

            print("=" * 40)
            cont = input("Mais itens? S/N:").strip().upper()
            print("=" * 40)
            if cont == "N":
                break

        atualizar_comanda(lista_salg3,lista_doce3,lista_sobre3,lista_bolo3,lista_fio_ovos3,comanda_atua,num_comanda)


    if opc == 4:
        return 4




