import pandas as pd
# ##Para rodar um questao comente as outras.
#
#
# ##QUESTAO 1
#
#
# qntdMaior = []
# qtd = 0
# id = 0
# Dados2021 = pd.read_excel(r"/Users/cliente/Desktop/Dados2021.xlsx", 'Vendas')
#
# Dados2021 = Dados2021[['ID Cliente', 'Quantidade']]
# Dados2021 = Dados2021.groupby(["ID Cliente"], as_index=False).sum()
# Dados2021 = Dados2021.sort_values(["Quantidade"], ascending=False)
#
# for items in range(len(Dados2021['Quantidade'])):
#     qntdMaior.append(float(Dados2021['Quantidade'][items]))
#     if qntdMaior[items - 1] > qtd:
#          id = items
#          qtd = qntdMaior[items-1]
#
# print(f"Id do cliente que mais comprou = {id} \n Quantidade = {qtd}")
#
#
# ##QUESTAO 2
#
#
# margemAbsoluta = []
# margemAbsolutaInt = []
# cont = 0
# maior = 0
# Dados2021 = pd.read_excel(r"/Users/cliente/Desktop/Dados2021.xlsx", 'Vendas')
# DadosProdutos = pd.read_excel(r"/Users/cliente/Desktop/DadosProdutos.xlsx", 'TbProduto')
#
# Dados2021 = Dados2021[['ID Produto', 'Total', 'custo_tot']]
# Dados2021 = Dados2021.groupby(["ID Produto"], as_index=False).sum()
# Dados2021['custo_tot'] = Dados2021['custo_tot'].astype(int)
#
# Dados2021.rename(columns={'Total': 'Receita', 'custo_tot': 'Custo_total'}, inplace=True)
#
# DadosProdutos = DadosProdutos[['ID Produto', 'Imposto']]
#
# for values in range(len(Dados2021['ID Produto'])):
#         auxiliar = 0
#         auxiliar = Dados2021['Receita'][values] - (Dados2021['Receita'][values] * DadosProdutos['Imposto'][values]) - Dados2021['Custo_total'][values]
#         margemAbsoluta.append("{:.2f}".format(auxiliar))
#
# for items in margemAbsoluta:
#    margemAbsolutaInt.append(float(items))
#
# for nums in range(len(margemAbsoluta)):
#      if margemAbsolutaInt[nums] > maior:
#          cont = nums
#          maior = margemAbsolutaInt[nums]
#
# print(f'O produto {cont + 1} tem a maior margem total de {maior}')
#
#
# ##QUESTAO 3
#
#
# margemPercentual=[]
# margemPercentualInt=[]
# cont = 0
# maior = 0
# Dados2021 = pd.read_excel(r"/Users/cliente/Desktop/Dados2021.xlsx", 'Vendas')
# DadosProdutos = pd.read_excel(r"/Users/cliente/Desktop/DadosProdutos.xlsx", 'TbProduto')
#
# Dados2021 = Dados2021[['ID Produto', 'Total', 'margem']]
# Dados2021 = Dados2021.groupby(["ID Produto"], as_index=False).sum()
# Dados2021['margem'] = Dados2021['margem'].astype(int)
# Dados2021.rename(columns={'Total': 'preco_total', 'margem': 'margem_absoluta'}, inplace=True)
#
# DadosProdutos = DadosProdutos[['ID Produto', 'Imposto']]
#
# for values in Dados2021['ID Produto']:
#     auxiliar = 0
#     auxiliar = Dados2021['margem_absoluta'][values-1]/(Dados2021['preco_total'][values-1]*(1-DadosProdutos['Imposto'][values-1]))
#     margemPercentual.append("{:.2f}".format(auxiliar))
#
# for items in margemPercentual:
#     margemPercentualInt.append(float(items))
#
# for nums in range(len(margemPercentual)):
#     if margemPercentualInt[nums] > maior:
#         cont = nums
#         maior = margemPercentualInt[nums]
#
# print(f'O produto {cont + 1} tem a maior margem percentual de {maior}')
#
#
# ##QUESTAO 4
#
#
# auxiliar = 0
# auxiliar2 = 0
# ValoresTotal = []
# ValoresMeta = []
# resultados = []
#
# dataframeDados2021 = pd.read_excel(r"/Users/cliente/Desktop/Dados2021.xlsx", 'Vendas')
# dataframeDadosProdutos = pd.read_excel(r"/Users/cliente/Desktop/DadosProdutos.xlsx", 'TbMeta')
#
# dataframeDados2021 = dataframeDados2021[['Data','ID Produto','Total']]
# dataframeDados2021['Data'] = dataframeDados2021['Data'].astype(str)
#
# for values in dataframeDados2021['Data']:
#     if "2021-05" not in values:
#         dataframeDados2021.drop(index=[auxiliar], inplace=True)
#     auxiliar = auxiliar + 1
#
# Dados2021Grouped = dataframeDados2021.groupby(['ID Produto'],  as_index=False).sum()
#
# dataframeDadosProdutos = dataframeDadosProdutos[['Data','Produto','Meta']]
# DadosProdutosMaio2021 = dataframeDadosProdutos.loc[dataframeDadosProdutos['Data'] == 'maio-2021']
#
# DadosProdutosMaio2021['Meta'] = DadosProdutosMaio2021['Meta'].astype(int)
# Dados2021Grouped['Total'] = Dados2021Grouped['Total'].astype(int)
#
# for total in Dados2021Grouped['Total']:
#     ValoresTotal.append(total)
#
# for meta in DadosProdutosMaio2021['Meta']:
#     ValoresMeta.append(meta)
#
# for nums in ValoresTotal:
#     if ValoresTotal[auxiliar2] >= ValoresMeta[auxiliar2]:
#         resultados.append(f' A Meta do produto {auxiliar2+1} foi batida')
#     else:
#         resultados.append(f' A Meta do produto {auxiliar2+1} nao foi batida')
#     auxiliar2 = auxiliar2 + 1
#     print(resultados[auxiliar2-1])
#