# Criador         : Brayan vieira 
# função          : Um sistema para E-comerce
# versão          : 1.0
# data da criação : 26/2/2024

import requests
import os
import platform
#-------------------------------------------------------------------------
#                           Variaveis padrões do programa 
roupas = ["Camisa polo Gear","Camisa do Lula","Camisa do bolsonaro"]
preco_roupas = [40,15,15]
solicitar_enter = " \n insira Qualquer tecla para continuar : " 
barras = 20 * "-"
conta_total = 0
ERRO_PADRAO = " \n você inseriu um caracter invalido \n "
#-------------------------------------------------------------------------
#                   Menu do programa 
menu_de_compras = '''

     ███╗░░░███╗██╗░░░██╗███████╗██████╗░
     ████╗░████║██║░░░██║██╔════╝██╔══██╗
     ██╔████╔██║██║░░░██║█████╗░░██████╔╝
     ██║╚██╔╝██║██║░░░██║██╔══╝░░██╔══██╗
     ██║░╚═╝░██║╚██████╔╝██║░░░░░██║░░██║
     ╚═╝░░░░░╚═╝░╚═════╝░╚═╝░░░░░╚═╝░░╚═╝
     
        Bem-vindo a melhor Loja de Roupas

        Selecione uma seção para continuar :

       
        | 1. Camisetas  |


Insira uma seção : '''
#-------------------------------------------------------------------------
#                           função limpar tela 
def limpador():
    sistema_operacional = platform.system()
    if sistema_operacional == "Windows":
        limpador = "cls"
    elif sistema_operacional == "Linux" or sistema_operacional == "Mac":
        limpador = "clear"
    return os.system(limpador)
#-------------------------------------------------------------------------
#                       capturando erros com try
try:
    limpador()
    escolha_de_produtos = int(input(menu_de_compras))
except ValueError:
      limpador()
      print(ERRO_PADRAO)
      input(solicitar_enter)
      exit()
#-------------------------------------------------------------------------
#                           Mostrando o estoque 
limpador()
print(" \n Nosso estoque de Camisetas : \n \n ")
#-------------------------------------------------------------------------
#                       percorrendo a lista de roupas e mostrando 
for i in range(len(roupas)):
    print(f"{roupas[i]}")
    print(f" Preço = {preco_roupas[i]} \n ID = {i} \n {barras}")
#-------------------------------------------------------------------------
#                           capturando erro de id inexistente 
try:
    escolha_de_camisa = int(input(" \n Insira o id do produto que deseja \n \n Insira : "))
    limpador()
except ValueError:
        print(ERRO_PADRAO)
        exit()
#-------------------------------------------------------------------------
#                       escolhendo as camisas e salvando 
match escolha_de_camisa:
     case 0:
          conta_total += 40
          itens_adquiridos = roupas[0]
     case 1:
          conta_total += 15
          itens_adquiridos = roupas[1]
     case 2:
          conta_total += 15
          itens_adquiridos = roupas[2]
     case _:
#-------------------------------------------------------------------------
#                                      Saida de erros 
          limpador()
          print("ERRO \n \n ID inexistente ")
          exit()
#-------------------------------------------------------------------------
#                       calculando as compras totais 
qtd_pecas = int(input("quantas peças você deseja adiquirir ? \n Ex : 10 peças \n \n Insira : "))
compras_totais = conta_total * qtd_pecas
#-------------------------------------------------------------------------
#                       Menu de informações 
nome_completo = '''
 ___________________________________________________
|                  Menu de compras                  |
|___________________________________________________|
|                                                   |
| Iremos pedir alguns dados para finalizar a compra |
|                                                   |
|___________________________________________________|                                                  



Insira o seu nome completo para continuar :  '''
ADD_CARTAO = '''
****************************************************
*                                                  *
*           ADICIONAR CARTÃO DE CRÉDITO           *
*                                                  *
*        Garantimos a segurança dos seus dados     *
*            durante todo o processo.              *
*                                                  *
****************************************************


Insira os numeros do seu cartão : '''
limpador()
#-------------------------------------------------------------------------
#                           Entrada de dados 
nome_completo = input(nome_completo)
testando_nome = len(nome_completo)
#-------------------------------------------------------------------------
#                               testando se o nome é valido 
if testando_nome < 2:
     limpador()
     print(" \n \n Nome invalido \n \n insira o nome completo \n \n ")
     exit()
limpador()
#-------------------------------------------------------------------------
#                                   inserindo e testando se o cpf e valido 
cpf = int(input("Insira seu cpf sem . ou / para finalizar sua compra \n \n \n Insira : "))
if cpf < 11:
    limpador()
    print("\n O cpf inserido é invalido \n ")
limpador()
try:
#-------------------------------------------------------------------------
#                   inserindo o cartão e capturando erros de valor 
    cartao = int(input(ADD_CARTAO))
except ValueError:
    limpador()
    print("\n você inseriu um caracter invalido \n ")
    exit()
limpador()
#-------------------------------------------------------------------------
#                           Inserindo informções do cartão 
data_do_cartao = int(input(" \n Insira a data do seu cartão \n \n  sem caracteres especiais \n \n Ex : 111230 \n \n Insira : "))
codigo_seguranca = int(input(" \n \n Insira O codigo de segurança do cartão \n \n Insira : "))
#-------------------------------------------------------------------------
#                           pegando os primeiros digitos para verificar 
convertendo_str = str(cartao)
cartao_completo = convertendo_str[:6]
#-------------------------------------------------------------------------
#                           criando uma requisição para a api testar o cartão
requisicao = f"https://api.bincodes.com/bin/json/269dd6d8ba361c16ee83a68067df9b67/{cartao_completo}"
dados_da_Requisicao = requests.get(requisicao)
#-------------------------------------------------------------------------
#                           convertendo a requisição para um objeto 
total = dados_da_Requisicao.json()
#-------------------------------------------------------------------------
#                   validando a resposta da requisição 
if total["valid"] == "false":
    limpador()
    print(" Erro na compra \n \n O cartão inserido é invalido\n ")
#-------------------------------------------------------------------------
#                   menu para confirmar informações 
menu_de_confirme_dados = f'''

            Confirme os dados inseridos 

    Nome completo         : {nome_completo} 
    CPF                   : {cpf}
    Numero do cartão      : {cartao}
    data do cartão        : {data_do_cartao}
    codigo de segurança   : {codigo_seguranca}
    Itens adquiridos      : {itens_adquiridos}
    preço total da compra : {compras_totais:.2f}
    
Os dados acima estão corretos ? \n \n [S] sim | [N] não \n \n Insira : '''
limpador()
#-------------------------------------------------------------------------
#                       entrada de dados do menu 
confirmar_dados = input(menu_de_confirme_dados).lower().startswith("s")
#-------------------------------------------------------------------------
#                       verificando a confirmação 
if confirmar_dados:
    limpador()
    print("Dados confirmados com sucesso \n ")
    input(solicitar_enter)
    limpador()
    print("     Compra realizada com sucesso \n \n ")
    exit()
print("\n \n informações não confirmadas \n \n saindo do programa......")
