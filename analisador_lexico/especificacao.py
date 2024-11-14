def obter_especificacao_tokens():
    return [
        ('PALAVRAS_CHAVE', r'\blet\b|\bif\b|\belse\b|\bwhile\b|\btry\b|\bcatch\b|\bconst\b|\bbreak\b|\bswitch\b|\bcase\b'),
        ('NUMEROS', r'\b\d+\b'),
        ('IDENTIFICADORES', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
        ('OPERADORES', r'[+\-*/=<>!&|^%]'),
        ('STRING', r'"([^"\\]*(\\.[^"\\]*)*)"|\'([^\'\\]*(\\.[^\'\\]*)*)\''),  # Suporte a aspas duplas e simples
        ('DELIMITADORES', r'[(){};,.]'),
        ('IGNORAR', r'[ \t\n]+'),
        ('INDEVIDO', r'.'),
    ]

def compilar_expressao_regular():
    especificacao_tokens = obter_especificacao_tokens()
    return '|'.join(f'(?P<{nome}>{regex})' for nome, regex in especificacao_tokens)
