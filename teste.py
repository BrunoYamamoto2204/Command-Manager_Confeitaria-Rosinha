from datetime import datetime


data = input("||Formato (%dd/%m/%yyyy)||\nData da encomenda: ")
try:
    data_formatada = datetime.strptime(data,"%d/%m/%Y")
    print(f"Formato correto:", datetime.strftime(data_formatada,"%d/%m/%Y"))
except ValueError:
    print("Formato incorreto ")
