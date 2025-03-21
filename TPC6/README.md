# Analisador Léxico e Sintático Recursivo Descendente para Expressões Aritméticas Simples

## TPC6
Este trabalho de casa implementa um **analisador léxico** com a biblioteca `PLY` e um **analisador sintático recursivo descendente** em Python, capaz de avaliar expressões aritméticas simples com operações básicas.

As funcionalidades incluídas são:

- **Reconhecimento de números inteiros e operadores** (`+`, `-`, `*`, `/`) através do analisador léxico.
- **Construção de uma árvore sintática** com base nas regras da gramática.
- **Avaliação correta da expressão**, respeitando a precedência dos operadores.
- **Mensagens de erro** claras para erros léxicos e sintáticos.

O **grande destaque** deste TPC é a implementação **manual do analisador sintático**, utilizando a técnica de **análise recursiva descendente**.

---

## Como Utilizar

1. **Executar** o ficheiro principal:
    ```bash
    python3 main.py
    ```
2. Introduzir expressões na consola (ex.: `10 + 2 * 3 - 1`)
3. O programa apresenta os tokens reconhecidos, a árvore gerada e o resultado da expressão.

---

## Estrutura do Código

### **Analisador Léxico (analex.py)**
- Utiliza `ply.lex` para definir tokens:
  - `NUM` → números inteiros positivos
  - `PLUS`, `MINUS`, `TIMES`, `DIVIDE` → operadores aritméticos
- Ignora espaços e tabs
- Emite aviso no caso de símbolo inválido

### **Analisador Sintático (anasin.py)**
- Implementado manualmente com **descida recursiva**
- Segue a gramática:
  ```
  Expr  → Term Expr'
  Expr' → + Term Expr' | - Term Expr' | ε
  Term  → Factor Term'
  Term' → * Factor Term' | / Factor Term' | ε
  Factor → NUM
  ```
- Cada não-terminal é representado por uma função recursiva
- Constrói uma árvore como lista aninhada (`['PLUS', 3, ['TIMES', 2, 4]]`)

### **Avaliador (avaliador.py)**
- Percorre a árvore e calcula o valor final
- Respeita a precedência dos operadores:
  - Multiplicação e divisão antes de adição e subtração

### **Programa Principal (main.py)**
- Lê a expressão do utilizador
- Invoca o analisador léxico e sintático
- Avalia a árvore sintática gerada
- Mostra tokens, árvore e resultado final

---

## Exemplo de Entrada e Saída

```plaintext
Expressão: 5 + 3 * 2
Tokens: [('NUM', 5), ('PLUS', '+'), ('NUM', 3), ('TIMES', '*'), ('NUM', 2)]
AST: ['PLUS', 5, ['TIMES', 3, 2]]
Resultado: 11
```

```plaintext
Expressão: 8 - 6 / 2
Tokens: [('NUM', 8), ('MINUS', '-'), ('NUM', 6), ('DIVIDE', '/'), ('NUM', 2)]
AST: ['MINUS', 8, ['DIVIDE', 6, 2]]
Resultado: 5.0
```

---

## 📁 Estrutura do Projeto

```bash
📂 TPC6
 ├── 📄 analex.py       # Analisador léxico com PLY
 ├── 📄 anasin.py       # Analisador sintático recursivo descendente
 ├── 📄 avaliador.py    # Avaliação da árvore sintática
 ├── 📄 main.py         # Interface principal
 ├── 📄 README.md       # Documentação do trabalho de casa
```

---

## 🎯 Conclusão

Este projeto cumpre o objetivo de construir um analisador léxico com `ply.lex` e um analisador sintático **manual e recursivo**, sendo capaz de:

✅ Interpretar expressões aritméticas simples  
✅ Construir a árvore sintática com base numa gramática LL(1)  
✅ Avaliar expressões respeitando a precedência dos operadores  
✅ Detetar e indicar erros léxicos e sintáticos com clareza  

---

## Identificação
**Nome:** Sara Azevedo Lopes  
**Número de Aluno:** 104179

![Identificação Sara Azevedo Lopes](../fotografia.png)
