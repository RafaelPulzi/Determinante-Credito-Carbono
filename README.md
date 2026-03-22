# 🌿 Determinante de Crédito de Carbono

[![Licença](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-%3E%3D2.0-black.svg)](https://flask.palletsprojects.com/)
[![Status do Projeto](https://img.shields.io/badge/status-em%20desenvolvimento-yellow.svg)]()
[![Contribuições](https://img.shields.io/badge/contribui%C3%A7%C3%B5es-bem%20vindas-brightgreen.svg)](CONTRIBUTING.md)

## 📌 Sobre o Projeto

Este projeto serve como um facilitador para determinar quantos créditos de carbono uma empresa pode emitir. Ele considera dois cenários:

- **Empresas com florestas próprias**: calcula os créditos com base na área florestal existente.
- **Empresas sem florestas**: realiza o cálculo do custo para plantar uma floresta, permitindo que a empresa obtenha créditos de carbono como um passivo ambiental.

A ferramenta foi desenvolvida para auxiliar na gestão ambiental corporativa, tornando mais acessível a estimativa de compensação de emissões.

## ✨ Funcionalidades

- Cálculo automatizado de créditos de carbono
- Análise de cenários com e sem vegetação nativa
- Estimativa de custos para reflorestamento
- Interface web amigável (Flask)
- Geração de tabelas comparativas

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+** – Linguagem principal
- **Flask** – Framework web
- **Pandas** – Manipulação de dados e análise
- **HTML/CSS** – Interface do usuário

## 📁 Estrutura do Projeto

```
Determinante-Credito-Carbono/
├── .venv/                 # Ambiente virtual
├── css/                   # Estilos da aplicação
├── geracaoTabelaComArvores/ # Scripts para geração de tabelas
├── img/                   # Imagens do projeto
├── templates/             # Templates HTML (Jinja2)
├── app.py                 # Aplicação principal Flask
├── analise.py             # Lógica de análise e cálculos
├── dados.csv              # Base de dados utilizada
├── fonts.txt              # Configuração de fontes
├── requirements.txt       # Dependências do projeto
└── README.md              # Documentação
```

## 🚀 Como Executar o Projeto

### Pré-requisitos

- Python 3.10 ou superior
- pip (gerenciador de pacotes Python)

### Passos

1. **Clone o repositório**
   ```bash
   git clone https://github.com/RafaelPulzi/Determinante-Credito-Carbono.git
   cd Determinante-Credito-Carbono
   ```

2. **Crie e ative um ambiente virtual (recomendado)**
   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Linux/Mac
   .venv\Scripts\activate         # Windows
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação**
   ```bash
   python app.py
   ```

5. **Acesse no navegador**
   ```
   http://127.0.0.1:5000
   ```

## 📊 Como Usar

1. Na interface web, informe os dados da empresa (área de vegetação, emissões, etc.)
2. O sistema calculará automaticamente:
   - Total de créditos de carbono disponíveis
   - Custo estimado para reflorestamento (se necessário)
   - Quantidade de árvores a serem plantadas
3. Visualize os resultados e faça o download das tabelas geradas

## 🤝 Contribuindo

Contribuições são muito bem-vindas! Sinta-se à vontade para:

- Abrir **issues** para relatar bugs ou sugerir melhorias
- Enviar **pull requests** com correções ou novas funcionalidades

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais informações.
