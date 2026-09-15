import re


def validar_email(email):
    """Retorna True quando o e-mail possui um formato válido."""
    padrao = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
    return bool(re.match(padrao, email))


def validar_telefone(telefone):
    """Retorna True quando o telefone contém entre 10 e 11 dígitos."""
    numeros = re.sub(r"\D", "", telefone)
    return len(numeros) in (10, 11)
