#  Nome: Gabriel Gomes Dos Santos 
#   Codigo feito para a prova pratica realizada no dia 27/09/2023 das 14:00 as 17:15 
#   Nessa prova tivemos que criar um programa para manipular dados de um inventario 
#   de produto(carros) em uma empresa que procurava dizitalizar seus estoque para 
#   facilitar suas buscas, tal programa guarda informações dos veiculos como:
#   placa, marca, modelo, valor, Km rodados, limite de uso 
#   e suas funções são:
#   Adicionar um novo carro para o inventario, remover um carro do inventario, calcular valor total dos carros no inventario,
#   listar carros no inventario que devem ser ventido, buscar um carro apartir de uma placa.
#   Esse programa funciona em forma de loop, que so sera parado quando o usuario selecionar a opção 0 no menu.

import os
inventario = [
{"placa": 1111, "marca": "Fiat", "modelo": "Argo Drive 1.3", "valor": 130000, "km_rodado": 25000, "limite_de_uso":20000},
{"placa": 2222, "marca": "Honda", "modelo": "FIT EX 1.4", "valor": 100000, "km_rodado": 15000, "limite_de_uso":20000},
{"placa": 3333, "marca": "Toyota", "modelo": "Corolla XEI 2.0", "valor": 150000, "km_rodado": 35000,"limite_de_uso":20000}
            ]
placas = {}
tamanho = len(inventario)
valortotal = 0
def cls():
    os.system('cls')
    
def menu():
    cls()
    print("============================================================================")
    print("                       Bem-Vindo ao nosso estoque                         \n")
    print("1 - Adicionar um novo veículo ao estoque") #Feito
    print("2 - Remover um veículo do estoque a partir de uma placa" )
    print("3 - Calcular o valor total em estoque") #Feito
    print("4 - Listar todos os veículos que precisam ser colocados à venda por desgaste") #Feito
    print("5 - Buscar Veiculo a partir de sua placa") #Feito
    print("0 - Sair")
    print("")
    print("============================================================================")
    opc = int(input("Qual o sua opção:"))
    return(opc)

def adicionar(): #1
    cls()
    cadastro = True
    new_placa = int(input("Digite o Número da placa:"))
    for i in range(0, len(inventario)):
        if new_placa == inventario[i]['placa']:
            cadastro = False
            break
    
    if cadastro:
        
        new_marca = input("Digite a Marca:")
        new_modelo = input("Digite o Modelo:")
        new_valor = int(input("Digite o valor:"))
        new_km = int(input("Digite a Kilometragem:"))
        new_limite = int(input("Digite o limite:"))
        dados = {"placa": new_placa, "marca": new_marca, "modelo": new_modelo, "valor": new_valor, "km_rodado": new_km, "limite_de_uso":new_limite}
        inventario.append(dados)  

        input("Dados Adicionados com sucesso\nPrecione qualquer teclad para seguir...")
        
    else:
        print("Placa ja cadastrada.")
        input("Presione qualquer tecla para voltar para o menu...")
        

def remover(): #2
    cls()
    remove = False
    rvm_placa = int(input("Digite a placa do veiculo de deseja remover: "))
    for placa in range(0, len(inventario)):
        if rvm_placa == inventario[placa]["placa"]:
            remove = True
            valor = placa

    if remove:
        inventario.pop(valor)
        input("Carro Removido com sucesso!\nPrecione qualquer tecla para continuar...")
    else: 
        print("Placa ou carro nao encontrados\nPrecione qualquer tecla para continuar....")

def cal(): #3
    global valortotal
    cls()
    for i in range(0, len(inventario)):
        a = inventario[i]['valor']
        valortotal = a+valortotal
    print("O Valor total é:",valortotal)    
    input("Presione qualquer tecla para voltar para o menu...")

def lista():#4
    tamanho = len(inventario)
    vendidos = False
    cls()
    print("Devem ser colocados a vendo os caros:\n")
    for i in range(0, tamanho):
        km = inventario[i]['km_rodado']
        limite = inventario[i]['limite_de_uso']
        modelo = inventario[i]['modelo']
        marca = inventario[i]['marca']
        placa = inventario[i]['placa']
        if km > limite: 
            print("Carro:",marca,modelo,"Placa:",placa)
            vendidos = True
    if vendidos:        
        input("\nPresione qualquer tecla para voltar para o menu...")
    else:
         input("Sem carros a serem vendido, presione qualquer tecla para voltar para o menu...")

def busca(): #5
    cls()
    buscar = True
    tamanho = len(inventario)
    busca = int(input("Digite qual a placa do veiculo procurado:"))            
    for i in range(0, tamanho):
        a = inventario[i]['placa']
        if busca == a:
            buscar = True
            i1 = i
            break
        else:
            buscar = False    
            
    if buscar:
        print("Placa Encontrada.")
        input("Presione qualquer tecla para exibir as informações...")
        cls()
        print("Placa:",inventario[i1]['placa'])
        print("marca:",inventario[i1]['marca'])
        print("Modelo:",inventario[i1]['modelo'])
        print("Valor:",inventario[i1]['valor'])
        print("Km Rodados:",inventario[i1]['km_rodado'])
        print("Limite de Uso:",inventario[i1]['limite_de_uso'])
        input("Preciose qualquer tecla para voltar para o menu...")        

    else:
        print("Placa nao encontrada....")
        input("Preciose qualquer tecla para voltar para o menu...")

while True:
    
    opc = menu()
    
    match opc:
        
        case 1:
            adicionar()
        
        case 2:
            remover()    
        
        case 3:
            cal()
            
        case 4:
            lista()    
            
        case 5:
            busca()
        
        case 0:
            cls()
            print("Programa Encerrado!")
            break