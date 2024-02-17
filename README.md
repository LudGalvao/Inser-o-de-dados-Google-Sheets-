# PySheetsInsert

PySheetsInsert é uma ferramenta em Python para inserir dados em planilhas do Google Sheets.

## Ferramentas Utilizadas

- **google-auth**: Biblioteca para autenticação com as APIs do Google.
- **google-auth-oauthlib**: Biblioteca para fluxos de autenticação OAuth2 com o Google.
- **googleapiclient**: Biblioteca para interagir com as APIs do Google.

## Pré-requisitos

Certifique-se de ter o pip do Google e a versão correta do Python instalados.

### Instalação do pip do Google

```
pip install google-auth google-auth-oauthlib google-api-python-client
```


## Configuração

Antes de começar, é necessário configurar as credenciais de autenticação com o Google.

1. Crie um projeto no [Google Cloud Console](https://console.cloud.google.com/).
2. Ative a API do Google Sheets para o seu projeto.
3. Crie um arquivo de credenciais JSON para o tipo de autenticação que deseja utilizar (por exemplo, OAuth2).
4. Renomeie o arquivo de credenciais para `credentials.json` e coloque-o no diretório raiz do projeto.

## Uso

Execute o script `main.py` para inserir dados na planilha do Google Sheets.

```bash
python main.py
