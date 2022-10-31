   
import openpyxl
import random

#Criacao de uma planilha
tabela = openpyxl.Workbook()
tabela.create_sheet('bdArvores')
bdarvores_page = tabela['bdArvores']

#Adicionando dados na tabela
bdarvores_page.append(['arvore', 'NomePopular', 'dap', 'altura'])
arvore = arvoresParaFor = 0

while True:
    nome = str(input('Qual o nome da especie: '))

    arvoresDoLaco = quantidadeArvores = int(input('Quantas arvores temos dessa especie: '))

    dapmin = float(input('Digite o DAP minimo da arvore: '))
    dapmax = float(input('Digite o DAP maximo da arvore: '))
    if dapmin > dapmax:
        print('=======VALORES DIGITADOS INCORRETAMENTE=======')
        dapmin = float(input('Digite o DAP minimo da arvore: '))
        dapmax = float(input('Digite o DAP maximo da arvore: '))
    

    print('--------------------------------------------------------------------------')

    hmin = float(input('Digite a altura minima da arvore: '))
    hmax = float(input('Digite a altura maxima da arvore: '))
    if hmin > hmax:
        print('=======VALORES DIGITADOS INCORRETAMENTE=======')
        dapmin = float(input('Digite o DAP minimo da arvore: '))
        dapmax = float(input('Digite o DAP maximo da arvore: '))
    

    print('--------------------------------------------------------------------------')

    quantidadeArvores += quantidadeArvores
    

    for AdicionandoTabela in range(arvoresParaFor, arvoresDoLaco):
        h = random.randint(hmin, hmax)
        dap = random.randint(dapmin, dapmax)
        arvore += 1
        bdarvores_page.append([arvore, nome, dap, h])
    tabela.save(filename= 'geracaoTabelaComArvores/BDinfoArvores.xlsx')
    opcao = str(input('Deseja continuar[S/N]: ')).upper()
    if opcao == 'N':
        continue