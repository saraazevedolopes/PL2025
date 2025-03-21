from anasin import analex_input, parse_expr
from avaliador import avaliar

def main():
    expr = input("Expressão: ")
    try:
        tokens = analex_input(expr)
        print("Tokens:", tokens)
        ast, resto = parse_expr(tokens)
        if resto:
            print("Erro: tokens não consumidos:", resto)
        else:
            print("AST:", ast)
            print("Resultado:", avaliar(ast))
    except Exception as e:
        print("Erro:", e)

if __name__ == "__main__":
    main()