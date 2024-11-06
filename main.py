import add_itens
import escolha_valida

while True:
    opc = escolha_valida.esc_opcoes()
    resp = add_itens.opc_comandas(opc)
    if resp == 5:
        break

# CONFERIR COMO FICOU A FORMATAÇÃO E A ORGANIZAÇÃO DE TUDO
# COLCAR AS FORMATAÇÃO NOVA EM TODOS OS LUGARES QUE MOSTRAM AS COMANDAS


