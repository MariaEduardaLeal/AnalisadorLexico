import re
from .especificacao import compilar_expressao_regular

expressao_regular = compilar_expressao_regular()

def analisador_lexico(codigo):
    numero_linha = 1
    tokens = []
    contagem_tokens = {}

    for correspondencia in re.finditer(expressao_regular, codigo):
        tipo = correspondencia.lastgroup
        valor = correspondencia.group()

        if tipo == 'IGNORAR':
            continue
        elif tipo == 'INDEVIDO':
            raise RuntimeError(f"Caractere inválido: {valor} na linha {numero_linha}")
        else:
            tokens.append((tipo, valor))
            contagem_tokens[tipo] = contagem_tokens.get(tipo, 0) + 1

        if valor == '\n':
            numero_linha += 1

    return tokens, contagem_tokens
