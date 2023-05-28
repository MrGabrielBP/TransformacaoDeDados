import tabula
import pandas as pd
import zipfile

# Função para juntar as tabelas em um único DataFrame
def juntar_tabela(lista_tabelas):
    tabela_completa = pd.concat(lista_tabelas, ignore_index=True)
    return tabela_completa

# Caminho do arquivo PDF
caminho = 'Anexo I - Lista completa de procedimentos.pdf'

# Nome do arquivo CSV de destino
nome_do_arquivo_csv_destino = 'Anexo I - Lista completa de procedimentos.csv'

# Nome do arquivo ZIP de destino
nome_do_arquivo_zip_destino = 'Teste_Gabriel_Porto.zip'

# Lendo as tabelas do PDF (elas começam na página 3)
lista_tabelas = tabula.read_pdf(caminho, pages='3-180', lattice=True)

# Juntando as tabelas em um único DataFrame
tabela_completa = juntar_tabela(lista_tabelas)

# Renomeando a coluna "RN\r(alteração)" para remover a quebra de linha
tabela_completa = tabela_completa.rename(columns={"RN\r(alteração)": "RN (alteração)"})

# Alterando as colunas "OD" e "AMB" por suas respectivas legendas
tabela_completa = tabela_completa.rename(columns={"OD": "Seg. Odontológica",
                                                  "AMB": "Seg. Ambulatorial"})

# Substituindo as quebras de linha ('\r') das linhas do DataFrame
tabela_completa = tabela_completa.replace('\r', ' ', regex=True)

# Salvando o DataFrame em um arquivo CSV
tabela_completa.to_csv(nome_do_arquivo_csv_destino, index=False)

# Criando um arquivo ZIP contendo o arquivo CSV
with zipfile.ZipFile(nome_do_arquivo_zip_destino, 'w', zipfile.ZIP_DEFLATED) as arquivozip:
    arquivozip.write(nome_do_arquivo_csv_destino)