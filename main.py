import add_itens
import escolha_valida

while True:
    opc = escolha_valida.esc_opcoes()
    resp = add_itens.opc_comandas(opc)
    if resp == 7:
        break

# SEPARAR OS RELATORIOS DIARIO COMPLETO POR HORARIO
# EXCLUIR NA PARTE DE RELATORIO COMPLETO
# ESPECIFICAR OS DIAS NO RELATORIO DIARIO COMPLETO
# CONFIRMAR/VOLTAR NA HORA DE INCLUIR NA COMANDA
# OPCAO DE SEPRAR COMANDAS DIARIAS COMPLETAS POR SETOR
# ARRUMAR FORMATACAO SE NAO FOR PARA ENTREGA
# FORMATAR HORARIO NA COMANDA

                    ## RESUMO DOS JSONs ##
# COMANDAS - SALVAS APÓS TERMINAR DE REGISTRAR A COMANDA
# RLATORIO DIARIO SIMPLES - LOGO APÓS DIGITAR O ITEM
# RLATORIO DIARIO COMPLETO - SALVA APÓS TERMINAR DE REGISTRAR A COMANDA
# DADOS - LOGO APÓS DIGITAR O ITEM

