def avaliar(ast):
    if isinstance(ast, int):
        return ast
    if isinstance(ast, list):
        op, esq, dir = ast
        ve = avaliar(esq)
        vd = avaliar(dir)
        if op == 'PLUS':
            return ve + vd
        elif op == 'MINUS':
            return ve - vd
        elif op == 'TIMES':
            return ve * vd
        elif op == 'DIVIDE':
            return ve / vd
    raise ValueError("Expressão inválida")