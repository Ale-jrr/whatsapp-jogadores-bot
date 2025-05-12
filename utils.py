import re

def extrair_dados_troca(texto):
    padrao = r"eu\s+(.*?)\s+estou trocando\s+(.*?)\s+por\s+(.*?)\s+com\s+(.*)"
    match = re.search(padrao, texto, re.IGNORECASE)
    if match:
        return tuple(m.strip() for m in match.groups())
    return None
