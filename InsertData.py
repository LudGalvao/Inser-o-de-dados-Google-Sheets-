import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

#id da Tabela do Google Sheets
ESCOPES = ["https://www.googleapis.com/auth/spreadsheets"] 

ID_PLANILHA_DE_EXEMPLO = "id da planilha"

def obter_entrada(mensagem):
    valor = input(mensagem + ": ")
    return valor.strip()

def main():
    credenciais = None

    if os.path.exists("token.json"):
        credenciais = Credentials.from_authorized_user_file("token.json", ESCOPES)

    if not credenciais or not credenciais.valid:
        if credenciais and credenciais.expired and credenciais.refresh_token:
            credenciais.refresh(Request())
        else:
            fluxo = InstalledAppFlow.from_client_secrets_file(
                "client_secret.json", ESCOPES
            )
            credenciais = fluxo.run_local_server(port=0)
        # Salvar as credenciais para a próxima execução
        with open("token.json", "w") as token:
            token.write(credenciais.to_json())
    
    servico = build("sheets", "v4", credentials=credenciais)
    planilha = servico.spreadsheets()

    # Obter dados de entrada do usuário
    competicao = obter_entrada("Competição")
    fase = obter_entrada("Fase")
    rodada = obter_entrada("Rodada")
    ano = obter_entrada("Ano")
    mandante = obter_entrada("Mandante")
    visitante = obter_entrada("Visitante")
    gols_m = obter_entrada("Gols Mandante")
    gols_v = obter_entrada("Gols Visitante")
    chutes_m = obter_entrada("Chutes Mandante")
    chutes_v = obter_entrada("Chutes Visitante")
    chutes_no_gol_m = obter_entrada("Chutes no Gol Mandante")
    chutes_no_gol_v = obter_entrada("Chutes no Gol Visitante")
    posse_m = obter_entrada("Posse Mandante")
    posse_v = obter_entrada("Posse Visitante")
    passes_m = obter_entrada("Passes Mandante")
    passes_v = obter_entrada("Passes Visitante")
    impedimentos_m = obter_entrada("Impedimentos Mandante")
    impedimentos_v = obter_entrada("Impedimentos Visitante")

    # Preparar a linha para inserção
    valores = [
        competicao, fase, rodada, ano, mandante, visitante,
        gols_m, gols_v, chutes_m, chutes_v, chutes_no_gol_m, chutes_no_gol_v,
        posse_m, posse_v, passes_m, passes_v, impedimentos_m, impedimentos_v,
    ]
    
    # Chamar a API do Sheets para adicionar os dados
    resultado = planilha.values().append(
        spreadsheetId=ID_PLANILHA_DE_EXEMPLO,
        range="Sul-Americana 2020!A1",  # Intervalo de células corrigido
        valueInputOption="RAW",
        body={"values": [valores]},
    ).execute()

    print("Dados adicionados com sucesso.")

if __name__ == "__main__":
    main()
