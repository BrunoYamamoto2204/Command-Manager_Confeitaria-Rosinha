import json
comandas = {"comandas1":{"bolos":["1 - 123","2 - 456"],"salgagos":["1 - 456"]}}
print(comandas)

string = input("Escreva o número: ")
string = string+" -"
for key,value in comandas.items():
    print(f"chave = {key}")
    for k,v in value.items():
        novos_valores = []
        for c in v:
            print(f"valor = {c}")
            if string not in c:
                novos_valores.append(c)  # Adiciona apenas se "1 -" não estiver presente
                # Atualiza a lista original com os novos valores
        print(comandas[key][k])
        comandas[key][k] = novos_valores

print(comandas)

opa = '(4) -> 1 Kg - Torta Choco Morango'.split()
print(opa[0])
