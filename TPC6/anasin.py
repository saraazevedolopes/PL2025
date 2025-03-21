from analex import lexer

def analex_input(expr):
    lexer.input(expr)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append((tok.type, tok.value))
    return tokens

def parse_expr(tokens):
    node, tokens = parse_term(tokens)
    while tokens and tokens[0][0] in ('PLUS', 'MINUS'):
        op, _ = tokens.pop(0)
        right, tokens = parse_term(tokens)
        node = [op, node, right]
    return node, tokens

def parse_term(tokens):
    node, tokens = parse_factor(tokens)
    while tokens and tokens[0][0] in ('TIMES', 'DIVIDE'):
        op, _ = tokens.pop(0)
        right, tokens = parse_factor(tokens)
        node = [op, node, right]
    return node, tokens

def parse_factor(tokens):
    if not tokens or tokens[0][0] != 'NUM':
        raise ValueError("Esperava-se um número")
    value = tokens.pop(0)[1]
    return value, tokens