import add_itens
import escolha_valida

while True:
    opc = escolha_valida.esc_opcoes()
    resp = add_itens.opc_comandas(opc)
    if resp == 6:
        break

# FAZER A PARTE DE MOSTRAR O RELATORIO DIARIO SIMPLES
# FAZER RELATORIO DIARIO COMPLETO



