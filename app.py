from flask import Flask, request
from google_sheets import realizar_troca
from utils import extrair_dados_troca
import os

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.form
    mensagem = data.get("Body", "").strip()
    resposta = "Formato inválido. Envie no padrão: EU João estou trocando Neymar por Messi com Lucas."

    if mensagem.lower().startswith("eu"):
        dados = extrair_dados_troca(mensagem)
        if dados:
            sucesso, resposta = realizar_troca(*dados)
    return resposta, 200

if __name__ == "__main__":
    app.run(debug=True)