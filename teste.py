remove = False
inventario = [
{"placa": 1111, "marca": "Fiat", "modelo": "Argo Drive 1.3", "valor": 130000, "km_rodado": 25000, "limite_de_uso":20000},
{"placa": 2222, "marca": "Honda", "modelo": "FIT EX 1.4", "valor": 100000, "km_rodado": 15000, "limite_de_uso":20000},
{"placa": 3333, "marca": "Toyota", "modelo": "Corolla XEI 2.0", "valor": 150000, "km_rodado": 35000,"limite_de_uso":20000}
            ]

rvm_placa = int(input("Digite a placa do veiculo de deseja remover: "))
for placa in range(0, len(inventario)):
    if rvm_placa == inventario[placa]["placa"]:
        remove = True
        valor = placa


if remove:
    inventario.pop(valor)

print(inventario)