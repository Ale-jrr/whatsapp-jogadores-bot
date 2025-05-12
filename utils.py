import re

def extrair_dados_troca(texto):
    padrao = r"eu (.*?) estou trocando (.*?) por (.*?) com (.*)"
    match = re.search(padrao, texto, re.IGNORECASE)
    if match:
        return match.groups()
    return None