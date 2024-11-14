import json
import escolha_valida
from comandas import *
def opc_comandas(opc):
    lista_salg = []
    lista_doce = []
    lista_sobre = []
    lista_bolo = []
    lista_fio_ovos=[]

    if opc == 1: #CRIAR COMANDA
        numero_itens = 1
        nome = escolha_valida.nome_cliente()
        numeros = escolha_valida.numero_cliente() # [Celular,telefone]
        data_e_dia = escolha_valida.dia_data() # [Data, dia_semana]
        horario = escolha_valida.horario_comanda() # [Pronto,Entrega]

        celular = numeros[0]
        telefone = numeros[1]
        data = data_e_dia[0]
        dia_semana = data_e_dia[1] #ARRUMAR, DIA DA SEMANA ESTÁ EM NÚMERO KAKAKAKAK
        hora_pronta = horario[0]
        hora_entrega = horario[1]

        criar_comanda(lista_salg,lista_doce,lista_sobre,lista_bolo,lista_fio_ovos,numero_itens,
                      nome,celular,telefone,data,dia_semana,hora_pronta,hora_entrega)

        with open("comandas.json", "r") as r:
            comanda = json.load(r)

        while True:
            print()
            escolha = escolha_valida.esc_principal()
            print("="*60)
            if escolha == 1:
                salg = escolha_valida.esc_salgado()
                lista_salg.append(escolha_valida.qnd_salg(salg,nome))
            if escolha == 2:
                doce = escolha_valida.esc_doce()
                lista_doce.append(escolha_valida.qntd_doce(doce,nome))
            if escolha == 3:
                bolo  = escolha_valida.esc_bolo()
                lista_bolo.append(escolha_valida.qntd_bolo(bolo,nome))
            if escolha == 4:
                sobremesa = escolha_valida.esc_sobremesa()
                lista_sobre.append(escolha_valida.qntd_sobremesa(sobremesa,nome))
            if escolha == 5:
                lista_fio_ovos.append(escolha_valida.qntd_fio_de_ovos(nome))

            numero_itens += 1

            comanda['comandas'][str(nome)]["num_item"] += 1

            with open("comandas.json", "w") as w:
                json.dump(comanda, w, indent=4)


            print("=" * 40)
            cont = input("Mais itens? S/N:").strip().upper()
            print("=" * 40)
            if cont == "N":
                break

        formar_comandas(lista_salg,lista_doce,lista_sobre,lista_bolo,lista_fio_ovos,nome,celular,telefone,data,dia_semana,hora_pronta,hora_entrega)
        salvar_comandas(lista_salg,lista_doce,lista_sobre,lista_bolo,lista_fio_ovos,numero_itens,nome)

    if opc == 2: #VER COMANDAS
        with open("comandas.json","r") as r:
            comandas = json.load(r)

        esc_comanda = escolha_valida.esc_comandas()
        nome_comanda = escolha_valida.nome_comanda()
        comanda_geral = comandas["comandas"][nome_comanda]

        if esc_comanda == 1:
            mostrar_comanda_geral(comanda_geral,nome_comanda)
        elif esc_comanda == 2:
            mostrar_comanda_salgados(comanda_geral,nome_comanda)
        elif esc_comanda == 3:
            mostrar_comanda_doces(comanda_geral,nome_comanda)
        elif esc_comanda == 4:
            mostrar_comanda_bolos(comanda_geral,nome_comanda)
        elif esc_comanda == 5:
            mostrar_comanda_sobremesas(comanda_geral,nome_comanda)
        elif esc_comanda == 6:
            mostrar_comanda_fio_de_ovos(comanda_geral, nome_comanda)

    if opc == 3: # ADICIONAR NA COMANDA

        with open("comandas.json","r") as r:
            comandas = json.load(r)

        nome_comanda = escolha_valida.nome_comanda()

        lista_salg3 = comandas["comandas"][f"{nome_comanda}"]['ADICIONADO']["salgados"]
        lista_doce3 = comandas["comandas"][f"{nome_comanda}"]['ADICIONADO']["doces"]
        lista_sobre3 = comandas["comandas"][f"{nome_comanda}"]['ADICIONADO']["sobremesas"]
        lista_bolo3 = comandas["comandas"][f"{nome_comanda}"]['ADICIONADO']["bolos"]
        lista_fio_ovos3 = comandas["comandas"][f"{nome_comanda}"]['ADICIONADO']["fio_de_ovos"]

        print("=" * 40)
        while True:
            escolha = escolha_valida.esc_principal()
            print("="*60)
            if escolha == 1:
                salg = escolha_valida.esc_salgado()
                qntd_salgado = escolha_valida.qnd_salg(salg,nome_comanda)
                lista_salg3.append(qntd_salgado)
            if escolha == 2:
                doce = escolha_valida.esc_doce()
                qntd_doce = escolha_valida.qntd_doce(doce,nome_comanda)
                lista_doce3.append(qntd_doce)
            if escolha == 3:
                bolo  = escolha_valida.esc_bolo()
                qntd_bolo = escolha_valida.qntd_bolo(bolo,nome_comanda)
                lista_bolo3.append(qntd_bolo)
            if escolha == 4:
                sobremesa = escolha_valida.esc_sobremesa()
                qntd_sobremesa = escolha_valida.qntd_sobremesa(sobremesa,nome_comanda)
                lista_sobre3.append(qntd_sobremesa)
            if escolha == 5:
                qntd_fio_ovos = escolha_valida.qntd_fio_de_ovos(nome_comanda)
                lista_fio_ovos3.append(qntd_fio_ovos)

            comandas['comandas'][f'{nome_comanda}']["num_item"] += 1
            with open("comandas.json","w") as w:
                json.dump(comandas,w,indent=4)

            print("=" * 40)
            cont = input("Mais itens? S/N:").strip().upper()
            print("=" * 40)
            if cont == "N":
                break

        mostrar_comanda_geral(comandas["comandas"][f"{nome_comanda}"], nome_comanda)


    if opc == 4: # EXCLUIR DA COMANDA
        nome_comanda = escolha_valida.nome_comanda()
        excluir_comanda(nome_comanda)

    if opc == 5: #RELATORIOS GERAIS
        relatorio = escolha_valida.esc_relatorio()
        if relatorio == 1:
            relatorio_geral()
        elif relatorio == 2:
            relatorio_salgados()
        elif relatorio == 3:
            relatorio_doces()
        elif relatorio == 4:
            relatorio_bolos()
        elif relatorio == 5:
            relatorio_sobremesas()
        elif relatorio == 6:
            relatorio_fio_ovos()

    if opc == 6: #SAIR
        return 6




