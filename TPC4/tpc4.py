import re

def tokenize(code):
    token_specification = [
        ('KEYWORD', r'\b(SELECT|WHERE|LIMIT|FILTER|OPTIONAL|ORDER BY|GROUP BY)\b', re.IGNORECASE),  # Palavras reservadas SPARQL
        ('TYPE',    r'\ba\b'),                # 'a' como rdf:type
        ('VAR',     r'\?\w+'),                # Variáveis SPARQL (ex: ?nome, ?desc)
        ('URI',     r'\b[a-zA-Z_][\w-]*:[\w-]+\b'),  # URIs como dbo:MusicalArtist
        ('LITERAL', r'"[^"]*"(@[a-z]+)?'),    # Literais como "Chuck Berry"@en
        ('NUM',     r'\b\d+\b'),              # Números inteiros isolados (ex: 1000)
        ('OP',      r'[{}.,()]'),             # Operadores/Sinais
        ('SKIP',    r'[ \t]+'),               # Espaços e tabs
        ('NEWLINE', r'\n'),                   # Quebras de linha
        ('ERRO',    r'.'),                    # Qualquer outro não reconhecido
    ]
    
    tok_regex = '|'.join(f'(?P<{id}>{expreg})' for id, expreg, *_ in token_specification)
    reconhecidos = []
    linha = 1

    for m in re.finditer(tok_regex, code, re.MULTILINE | re.IGNORECASE):
        tipo = m.lastgroup
        valor = m.group()
        
        if tipo == 'NUM':
            t = (tipo, int(valor), linha, m.span())
        elif tipo == 'KEYWORD':
            t = (tipo, valor.lower(), linha, m.span())
        elif tipo == 'SKIP':
            continue
        elif tipo == 'NEWLINE':
            linha += 1
            continue
        else:
            t = (tipo, valor, linha, m.span())

        reconhecidos.append(t)

    return reconhecidos

if __name__ == "__main__":
    with open("teste.txt", "r", encoding="utf-8") as f:
        conteudo = f.read()
    
    tokens = tokenize(conteudo)

    with open("resultados.txt", "w", encoding="utf-8") as out_file:
        for tok in tokens:
            out_file.write(str(tok) + "\n")

    print("Resultados em resultados.txt")
