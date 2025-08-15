#importando as bibliotetcas. 

import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import csv
#Variavel para guardar o endereço do site
URL = "http://quotes.toscrape.com"

print("Iniciando o robô scraper...")

#get da biblioteca request para acesar o site. 
resposta = requests.get(URL)

# Agora, criar o Soup. Ele é o resultado de passar o conteúdo da resposta ('resposta.content') para a BeautifulSoup
soup = BeautifulSoup(resposta.content, 'html.parser')

#Usamos o método 'find_all' para encontrar TODOS os elementos.
# encontrar todas as tags <div> que tenham o atributo class="quote".
# O resultado (uma lista de elementos) será guardado na variável 'citacoes'.


citacoes = soup.find_all('div', class_='quote')

# A função len() diz o tamanho de uma lista.
print(f"Verificação: {len(citacoes)} citações encontradas.")
#Transformando em tabela
nome_arquivo = "citacoes.csv"

# O bloco 'with' abre o arquivo e o mantém aberto para tudo que está DENTRO dele
with open(nome_arquivo, 'w', newline='', encoding='utf-8-sig') as arquivo_csv:

    # Cria um "escritor" CSV que sabe como formatar os dados corretamente. delmiter é para reconhecer virgula, ou ponto e virgula.
    escritor = csv.writer(arquivo_csv, delimiter = ';')
    #Escreve o cabeçalho
    escritor.writerow(['Citação', 'Tradução', 'Autor'])
    
    print(f"Gravando dados no arquivo '{nome_arquivo}'...")
    
# Um loop 'for'. Para cada item na  lista 'citacoes'...
    for citacao in citacoes:

        #Procurar a tag span com classe text, usar .text no final para pegar apenas o conteudo do texto
        texto = citacao.find('span', class_='text').text

        #Procurando a tag small com a classe author. 
        autor = citacao.find('small', class_='author').text
        
        try:
            #Fazendo a tradução do texto.
            texto_traduzido = GoogleTranslator(source='auto', target='pt').translate(texto)
        except Exception as e:
            texto_traduzido = "Não foi possível traduzir."
        
        # 3. USO O ESCRITOR PARA SALVAR OS DADOS, NÃO O PRINT
        escritor.writerow([texto, texto_traduzido, autor])

# Esta mensagem só aparece depois que o bloco 'with' termina e o arquivo é salvo.
print(f"Arquivo '{nome_arquivo}' criado com sucesso!")