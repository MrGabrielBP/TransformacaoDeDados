# Projeto de Extração de Dados de PDF com Tabula

Este projeto tem como objetivo extrair dados de tabelas presentes em um arquivo PDF utilizando a biblioteca Tabula em Python. Ele é especialmente útil quando há a necessidade de obter dados estruturados a partir de tabelas complexas em um PDF.

## Bibliotecas Utilizadas

O projeto utiliza as seguintes bibliotecas:

- Tabula: Uma biblioteca Python para extração de tabelas de PDFs. Ela permite ler as tabelas em formato tabular e convertê-las em DataFrames do pandas.
- Pandas: Uma biblioteca Python para manipulação e análise de dados. Ela é utilizada para trabalhar com os dados extraídos do PDF, realizar transformações e salvá-los em um arquivo CSV.
- Zipfile: Uma biblioteca Python para manipulação de arquivos ZIP. É usada para compactar o arquivo CSV em um arquivo ZIP no final do processo.

## Instalação das Bibliotecas

Para instalar as bibliotecas necessárias, utilize o gerenciador de pacotes do Python, pip, executando os seguintes comandos:

```bash
pip install tabula-py
```
```bash
pip install pandas
```
```bash
pip install zipfile
```

## Uso da Função `tabula.read_pdf` e o Parâmetro `lattice`

A função `tabula.read_pdf` é utilizada para ler as tabelas presentes no PDF. O parâmetro `lattice` é utilizado para indicar que o PDF segue um padrão de layout de grade. Caso o PDF possua tabelas bem definidas, com células e bordas nítidas, esse parâmetro pode ser definido como `True`. Porém, se as tabelas possuem layout mais complexo, com células mescladas ou bordas indistintas, pode ser necessário usar o parâmetro `lattice=False` para tentar extrair as tabelas de forma adequada. No caso do PDF de exemplo, as tabelas possuem células bem definidas.

Comparando o uso de `lattice=True` e `lattice=False`, é recomendado realizar testes em seu PDF específico para determinar qual opção se ajusta melhor à sua situação.

## Renomeando Colunas e Substituindo Valores

No código do projeto, é realizado o renomeio de algumas colunas específicas. Essas etapas têm o objetivo de melhorar a legibilidade e consistência dos dados extraídos.

No caso do renomeio da coluna "RN\r(alteração)", o motivo é remover a quebra de linha presente no nome original da coluna, facilitando o processamento posterior.

Já a substituição das colunas "OD" e "AMB" por suas respectivas legendas ("Seg. Odontológica" e "Seg. Ambulatorial") é feita para fornecer nomes mais descritivos e compreensíveis às colunas no DataFrame resultante.

## Substituição de Quebras de Linha

No código do projeto, é realizada a substituição dos caracteres de quebra de linha (`\r`) presentes nas linhas do DataFrame. Essa substituição é feita para evitar problemas na leitura do arquivo CSV resultante.

Ao ler o arquivo CSV, alguns programas podem interpretar as quebras de linha como indicadores de novas linhas, o que pode causar erros na leitura dos dados. Portanto, a substituição dos caracteres de quebra de linha garante que as linhas do DataFrame sejam mantidas intactas e que não haja quebras de linha indesejadas durante a leitura do CSV.

## Como Utilizar

Para clonar este projeto e obter uma cópia local em sua máquina, siga os passos abaixo:

1. Abra o terminal ou prompt de comando.
2. Navegue até o diretório onde deseja clonar o projeto.
3. Execute o seguinte comando para clonar o repositório:
```bash
git clone https://github.com/MrGabrielBP/TransformacaoDeDados.git
```
4. Execute o script Python e aguarde a conclusão:
```bash
python codigo.py
```
5. O PDF será lido, convertido para CSV e será salvo na pasta atual. Logo após será zipado com o nome especificado.

Após clonar o projeto, você terá acesso aos arquivos e poderá executar o código em sua própria máquina. Certifique-se de instalar as bibliotecas necessárias antes de executar o projeto.
