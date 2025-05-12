import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credenciais.json", scope)
client = gspread.authorize(creds)
sheet = client.open("LISTA DE TIMES").sheet1

def realizar_troca(nome1, jogador1, jogador2, nome2):
    dados = sheet.get_all_values()
    colunas = list(zip(*dados))
    colunas_sem_nulos = [list(filter(None, col)) for col in colunas]
    try:
        idx1, idx2 = None, None
        for i, col in enumerate(colunas_sem_nulos):
            if nome1 in col[0]:
                idx1 = i
            if nome2 in col[0]:
                idx2 = i
        if idx1 is None or idx2 is None:
            return False, "❌ Dono não encontrado na planilha."

        col1 = colunas_sem_nulos[idx1]
        col2 = colunas_sem_nulos[idx2]

        if jogador1 not in col1 or jogador2 not in col2:
            return False, "❌ Jogador não encontrado no time informado."

        row1 = col1.index(jogador1)
        row2 = col2.index(jogador2)

        sheet.update_cell(row1 + 1, idx1 + 1, jogador2)
        sheet.update_cell(row2 + 1, idx2 + 1, jogador1)
        return True, f"✅ Troca realizada com sucesso entre {nome1} e {nome2}: {jogador1} ⇄ {jogador2}"
    except Exception as e:
        return False, f"Erro ao processar a troca: {e}"