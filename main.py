import add_itens
import escolha_valida

while True:
    opc = escolha_valida.esc_opcoes()
    resp = add_itens.add_itens(opc)
    if resp == 4:
        break