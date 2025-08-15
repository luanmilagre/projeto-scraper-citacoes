# 🤖 Scraper de Citações com Tradução Automática

![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![GitHub issues](https://img.shields.io/github/issues/SEU-USUARIO/SEU-REPOSITORIO)
![GitHub forks](https://img.shields.io/github/forks/SEU-USUARIO/SEU-REPOSITORIO)

> Projeto de web scraping criado como parte do meu portfólio de Desenvolvedor Python / Engenheiro de Dados.

## 📖 Sobre o Projeto

Este projeto consiste em um robô (web scraper) desenvolvido em Python que automatiza o processo de extração de dados de um site. Ele navega até a página "Quotes to Scrape", coleta todas as citações famosas, seus respectivos autores e, em seguida, utiliza uma API para traduzir cada citação para o português.

Ao final do processo, todos os dados coletados e traduzidos são salvos de forma organizada em um arquivo **`citacoes.csv`**, pronto para ser utilizado em planilhas ou para outras análises de dados.

## 🛠️ Tecnologias Utilizadas

Este projeto foi construído utilizando as seguintes tecnologias e bibliotecas:

* **Python 3:** Linguagem de programação principal.
* **Requests:** Para realizar as requisições HTTP e obter o conteúdo da página web.
* **BeautifulSoup4:** Para analisar (parse) o HTML da página e encontrar os elementos desejados.
* **Deep-Translator:** Para realizar a tradução automática das citações de inglês para português.
* **Git & GitHub:** Para versionamento e hospedagem do código.

## 🚀 Como Rodar o Projeto

Siga os passos abaixo para executar o projeto localmente em sua máquina.

### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
* [Git](https://git-scm.com)
* [Python 3](https://www.python.org)

### Rodando o Script

```bash
# 1. Clone este repositório para sua máquina local
git clone [https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git](https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git)

# 2. Navegue até o diretório do projeto
cd projeto-scraper-citacoes

# 3. Crie um ambiente virtual para o projeto
python -m venv .venv

# 4. Ative o ambiente virtual
# No Windows:
.venv\Scripts\activate
# No Linux ou macOS:
# source .venv/bin/activate

# 5. Instale todas as dependências listadas no requirements.txt
pip install -r requirements.txt

# 6. Execute o script principal
python scraper.py


👨‍💻 Autor
Luan Milagre

LinkedIn: www.linkedin.com/in/devluanmilagre

GitHub: @luanmilagre