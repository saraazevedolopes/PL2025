#!/usr/bin/env python3

import re
import ply.lex as lex

tokens = [
    'KEYWORD',
    'TYPE',
    'VAR',
    'URI',
    'LITERAL',
    'NUM',
    'OP',
]

# Palavras reservadas SPARQL (maiúsculas/minúsculas)
def t_KEYWORD(t):
    r'(?i)\b(SELECT|WHERE|LIMIT|FILTER|OPTIONAL|ORDER BY|GROUP BY)\b'
    t.value = (t.type, t.value.lower(), t.lineno, (t.lexpos, t.lexpos + len(t.value)))
    return t

# O `a` como atalho para `rdf:type`
def t_TYPE(t):
    r'\ba\b'
    t.value = (t.type, t.value, t.lineno, (t.lexpos, t.lexpos + len(t.value)))
    return t

# Variáveis SPARQL (ex: `?nome`, `?desc`)
def t_VAR(t):
    r'\?\w+'
    t.value = (t.type, t.value, t.lineno, (t.lexpos, t.lexpos + len(t.value)))
    return t

# URIs (ex: `dbo:MusicalArtist`, `foaf:name`)
def t_URI(t):
    r'\b[a-zA-Z_][\w-]*:[\w-]+\b'
    t.value = (t.type, t.value, t.lineno, (t.lexpos, t.lexpos + len(t.value)))
    return t

# Literais de string (ex: `"Chuck Berry"@en`)
def t_LITERAL(t):
    r'"[^"]*"(@[a-z]+)?'
    t.value = (t.type, t.value, t.lineno, (t.lexpos, t.lexpos + len(t.value)))
    return t

# Números inteiros isolados (ex: `1000`)
def t_NUM(t):
    r'\b\d+\b'
    t.value = (t.type, int(t.value), t.lineno, (t.lexpos, t.lexpos + len(t.value)))
    return t

# Operadores/Sinais (`{ } . , ( )`)
def t_OP(t):
    r'[{}.,()]'
    t.value = (t.type, t.value, t.lineno, (t.lexpos, t.lexpos + len(t.value)))
    return t

# Ignorar espaços e tabs
t_ignore = ' \t'

# Contar novas linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Tratamento de erro
def t_error(t):
    print(f'Inválido: "{t.value[0]}"', file=sys.stderr)
    t.lexer.skip(1)

lexer = lex.lex()

if __name__ == '__main__':
    with open("teste.txt", "r", encoding="utf-8") as f:
        data = f.read()
    
    lexer.input(data)

    with open("LEXresultados.txt", "w", encoding="utf-8") as out_file:
        for token in lexer:
            out_file.write(str(token.value) + "\n")  

    print("Resultados em LEXresultados.txt")
