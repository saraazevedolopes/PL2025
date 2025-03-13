import json
import re
import ply.lex as lex
import sys

states = (
    ("insertcoins", "exclusive"),
)

tokens = [
    'COMMAND',
    'MOEDA',
    'COINS',
    'PRODUCT_CODE',
    'INT',
    'FLOAT'
]

def t_COMMAND(t):
    r'(?i)\b(LISTAR|SELECIONAR|SAIR|ADICIONAR|REMOVER)\b'
    t.value = t.value.upper()
    return t

def t_MOEDA(t):
    r'(?i)\bMOEDA\b'
    t.lexer.begin("insertcoins")
    t.value = t.value.upper()
    return t

def t_PRODUCT_CODE(t):
    r'\b[A-Z]\d{1,2}\b'
    return t

def t_FLOAT(t):
    r'\b\d+\.\d+\b'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\b\d+\b'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f'Erro: Entrada inválida "{t.value}"', file=sys.stderr)
    t.lexer.skip(len(t.value))

def t_insertcoins_COINS(t):
    r'(?i)((?:1|5|10|20|50)c|(?:1|2)e)(\s*,\s*((?:1|5|10|20|50)c|(?:1|2)e))*\s*\.'
    t.lexer.begin("INITIAL")
    vals = re.findall(r'(?i)((?:1|5|10|20|50)c|(?:1|2)e)', t.value)
    lista = []
    for v in vals:
        coin = v.lower()
        if coin.endswith('c'):
            lista.append((int(coin[:-1]), 'c'))
        else:
            lista.append((int(coin[:-1]), 'e'))
    t.value = lista
    return t

def t_insertcoins_error(t):
    leftover = t.lexer.lexdata[t.lexer.lexpos:]
    print(f'Erro (moedas): input inválido "{leftover.strip()}"')
    t.lexer.skip(len(leftover))
    t.lexer.begin("INITIAL")

t_insertcoins_ignore = ' \t'

lexer = lex.lex()

def carregar_stock():
    try:
        with open("stock.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def guardar_stock(stock):
    with open("stock.json", "w", encoding="utf-8") as f:
        json.dump(stock, f, indent=4)

def maquina_vending():
    stock = carregar_stock()
    saldo = 0
    print("maq: Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")
    while True:
        entrada = input(">> ")
        if not entrada.strip():
            continue

        lexer.input(entrada)
        tokens_lidos = list(lexer)

        if not tokens_lidos:
            continue

        cmd = tokens_lidos[0]
        if cmd.type == "COMMAND":
            if cmd.value == "LISTAR":
                print("maq:")
                print("cod | nome | quantidade | preço")
                print("---------------------------------")
                for item in stock:
                    print(f"{item['cod']} {item['nome']} {item['quant']} {item['preco']}")
            elif cmd.value == "SELECIONAR":
                if len(tokens_lidos) < 2 or tokens_lidos[1].type != "PRODUCT_CODE":
                    print("maq: Código de produto inválido.")
                    continue
                codigo = tokens_lidos[1].value
                produto = next((p for p in stock if p["cod"] == codigo), None)
                if not produto:
                    print("maq: Produto inexistente.")
                elif produto["quant"] == 0:
                    print("maq: Produto esgotado.")
                else:
                    preco_cents = int(produto["preco"] * 100)
                    if saldo < preco_cents:
                        print("maq: Saldo insuficiente para satisfazer o seu pedido")
                        print(f"maq: Saldo = {saldo // 100}e{saldo % 100}c; Pedido = {preco_cents}c")
                    else:
                        saldo -= preco_cents
                        produto["quant"] -= 1
                        print(f"maq: Pode retirar o produto dispensado \"{produto['nome']}\"")
                        print(f"maq: Saldo = {saldo // 100}e{saldo % 100}c")
            elif cmd.value == "ADICIONAR":
                if len(tokens_lidos) < 3 or tokens_lidos[1].type != "PRODUCT_CODE" or tokens_lidos[2].type != "INT":
                    print("maq: Comando inválido. Use: ADICIONAR <CÓDIGO> <QUANTIDADE> [PREÇO]")
                    continue
                codigo = tokens_lidos[1].value
                quantidade = tokens_lidos[2].value
                produto = next((p for p in stock if p["cod"] == codigo), None)
                if produto:
                    if len(tokens_lidos) > 3:
                        print(f"maq: Produto já existe. Use apenas: ADICIONAR {codigo} <QUANTIDADE>")
                        continue
                    produto["quant"] += quantidade
                    print(f"maq: Adicionados {quantidade} unidades ao stock de \"{produto['nome']}\". Preço mantido: {produto['preco']} euros.")
                else:
                    if len(tokens_lidos) != 4 or tokens_lidos[3].type not in ["FLOAT", "INT"]:
                        print("maq: Produto novo! Precisa indicar o preço. Use: ADICIONAR <CÓDIGO> <QUANTIDADE> <PREÇO>")
                        continue
                    preco = float(tokens_lidos[3].value)
                    nome = input(f"maq: Produto novo detectado! Introduza o nome para {codigo}: ")
                    stock.append({"cod": codigo, "nome": nome, "quant": quantidade, "preco": preco})
                    print(f"maq: Produto \"{nome}\" adicionado com {quantidade} unidades a {preco} euros.")
                guardar_stock(stock)
            elif cmd.value == "REMOVER":
                if len(tokens_lidos) < 2 or tokens_lidos[1].type != "PRODUCT_CODE":
                    print("maq: Comando inválido. Use: REMOVER <CÓDIGO>")
                    continue
                codigo = tokens_lidos[1].value
                produto = next((p for p in stock if p["cod"] == codigo), None)
                if not produto:
                    print("maq: Produto inexistente.")
                else:
                    stock.remove(produto)
                    print(f"maq: Produto \"{produto['nome']}\" removido do stock.")
                guardar_stock(stock)
            elif cmd.value == "SAIR":
                troco = saldo
                moedas = [50, 20, 10, 5, 2, 1]
                troco_distribuido = {}
                for moeda in moedas:
                    qtd = troco // moeda
                    if qtd > 0:
                        troco_distribuido[moeda] = qtd
                    troco %= moeda
                if troco_distribuido:
                    troco_formatado = ", ".join([f"{qtd}e {m}c" for m, qtd in troco_distribuido.items()])
                    print(f"maq: Pode retirar o troco: {troco_formatado}.")
                print("maq: Até à próxima")
                guardar_stock(stock)
                sys.exit()
            else:
                print("maq: Comando não reconhecido.")
        elif cmd.type == "MOEDA":
            for tk in tokens_lidos[1:]:
                if tk.type == "COINS":
                    soma = 0
                    for (valor, tipo) in tk.value:
                        if tipo == 'e':
                            soma += valor * 100
                        else:
                            soma += valor
                    saldo += soma
                    print(f"maq: Saldo = {saldo // 100}e{saldo % 100}c")
        else:
            print("maq: Comando ou entrada não reconhecida.")

if __name__ == "__main__":
    maquina_vending()
