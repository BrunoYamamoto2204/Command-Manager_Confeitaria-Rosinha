import add_itens
import escolha_valida

while True:
    opc = escolha_valida.esc_opcoes()
    resp = add_itens.opc_comandas(opc)
    if resp == 8:
        break

# IMPRESSÃO NO EXCEL

                    ## RESUMO DOS JSONs ##
# COMANDAS - SALVAS APÓS TERMINAR DE REGISTRAR A COMANDA
# RLATORIO DIARIO SIMPLES - LOGO APÓS DIGITAR O ITEM
# RLATORIO DIARIO COMPLETO - SALVA APÓS TERMINAR DE REGISTRAR A COMANDA
# DADOS - LOGO APÓS DIGITAR O ITEM


