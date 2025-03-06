# Analisador Léxico para SPARQL

## TPC4
Este trabalho de casa implementa um **analisador léxico para consultas SPARQL** em Python.  
O analisador reconhece os seguintes elementos da linguagem:

- **Palavras reservadas** (`SELECT`, `WHERE`, `LIMIT`, `FILTER`, `OPTIONAL`, `ORDER BY`, `GROUP BY`)
- **Variáveis** (ex: `?nome`, `?desc`)
- **URIs** (ex: `dbo:MusicalArtist`, `foaf:name`)
- **Literais** (ex: `"Chuck Berry"@en`)
- **Números** (ex: `1000`)
- **Operadores** (`{}`, `.`, `,`, `()`)

O programa lê um ficheiro SPARQL e gera um ficheiro de saída contendo a lista de tokens reconhecidos.

---

## Como Utilizar
### **Executar o Analisador Léxico**
1. Colocar a consulta SPARQL no ficheiro `teste.txt` ou utilizar a que já está presente neste.
2. Executar o analisador léxico:
   ```sh
   python3 LEXtpc4.py
   ```
3. O output será gerado no ficheiro `LEXresultados.txt`, contendo os tokens reconhecidos.

### **Alternativa com Expressões Regulares**
Para testar a versão alternativa, que utiliza apenas expressões regulares:
```sh
python3 tpc4.py
```
O output será gerado no ficheiro `resultados.txt`.

---

## Estrutura do Código

### **Leitura do Ficheiro de Entrada**
O programa lê o conteúdo de `teste.txt` e processa cada linha para identificar os tokens.

### **Expressões Regulares Utilizadas**
As expressões regulares são usadas para identificar os diferentes tipos de tokens:

- **Palavras reservadas**:
  ```python
  r'\b(SELECT|WHERE|LIMIT|FILTER|OPTIONAL|ORDER BY|GROUP BY)\b'
  ```
Reconhece palavras reservadas SPARQL em maiúsculas ou minúsculas.

- **Variáveis**:
  ```python
  r'\?\w+'
  ```
Captura variáveis SPARQL que começam com ?.

- **URIs**:
  ```python
  r'\b[a-zA-Z_][\w-]*:[\w-]+\b'
  ```
Reconhece URIs como dbo:MusicalArtist.

- **Literais**:
  ```python
  r'"[^"]*"(@[a-z]+)?'
  ```
Captura literais de texto, como "Chuck Berry"@en.

- **Números**:
  ```python
  r'\b\d+\b'
  ```
Reconhece números inteiros isolados.

- **Operadores**:
  ```python
  r'[{}.,()]''
  ```
Reconhece {}, ., ,, ().

---

## Exemplo de Entrada e Saída
### Entrada (teste.txt)
  ```sparql
  # DBPedia: obras de Chuck Berry
    SELECT ?nome ?desc WHERE {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
  } LIMIT 1000
  ```

### Saída (LEXresultados.txt ou resultados.txt)
  ```plaintext
  ('KEYWORD', 'select', 1, (0, 6))
  ('VAR', '?nome', 1, (7, 12))
  ('VAR', '?desc', 1, (13, 18))
  ('KEYWORD', 'where', 1, (19, 24))
  ('OP', '{', 1, (25, 26))
  ('VAR', '?s', 2, (27, 29))
  ('TYPE', 'a', 2, (30, 31))
  ('URI', 'dbo:MusicalArtist', 2, (32, 49))
  ('OP', '.', 2, (49, 50))
  ('VAR', '?s', 3, (51, 53))
  ('URI', 'foaf:name', 3, (54, 63)) 
  ('LITERAL', '"Chuck Berry"@en', 3, (64, 80))
  ('OP', '.', 3, (81, 82))
  ('VAR', '?w', 4, (83, 85))
  ('URI', 'dbo:artist', 4, (86, 96))
  ('VAR', '?s', 4, (97, 99))
  ('OP', '.', 4, (99, 100))
  ('VAR', '?w', 5, (101, 103))
  ('URI', 'foaf:name', 5, (104, 113))
  ('VAR', '?nome', 5, (114, 119))
  ('OP', '.', 5, (119, 120))
  ('VAR', '?w', 6, (121, 123))
  ('URI', 'dbo:abstract', 6, (124, 136))
  ('VAR', '?desc', 6, (137, 142))
  ('OP', '}', 7, (143, 144))
  ('KEYWORD', 'limit', 7, (145, 150))
  ('NUM', 1000, 7, (151, 155))
  ```

---

## Diferenças entre `LEXtpc4.py` e `tpc4.py`
O trabalho de casa tem **duas versões** do analisador léxico:

| Versão      | Implementação        | Output |
|------------|---------------------|--------|
| `tpc4.py`  | **Baseada em `re`** (expressões regulares) | `resultados.txt` |
| `LEXtpc4.py` | **Baseada em `ply.lex`** (biblioteca de análise léxica) | `LEXresultados.txt` |

Ambas as versões fazem a mesma análise, mas `LEXtpc4.py` usa um **analisador léxico estruturado**, enquanto `tpc4.py` usa apenas **expressões regulares**.

---

## 📁 Estrutura do Projeto  

```bash
📂 TPC4
 ├── 📄 LEXtpc4.py         # Versão do analisador léxico com `ply.lex`
 ├── 📄 tpc4.py            # Versão do analisador léxico baseada em expressões regulares
 ├── 📄 teste.txt          # Ficheiro de entrada com a consulta SPARQL
 ├── 📄 LEXresultados.txt  # Saída da versão `LEXtpc4.py`
 ├── 📄 resultados.txt     # Saída da versão `tpc4.py`
 ├── 📄 README.md          # Documentação do projeto
```
---

## 🎯 Conclusão  

Este projeto implementa um **analisador léxico para SPARQL**, permitindo identificar e classificar corretamente os tokens presentes em consultas SPARQL. 

✅ **Resumo dos Objetivos Cumpridos:**  
✔️ Identificação de **palavras-chave** (constantes do tipo string), como `SELECT`, `WHERE`, `LIMIT`, `FILTER`, `OPTIONAL`, `ORDER BY`, `GROUP BY`.  
✔️ Identificação de **sinais** (constituídos apenas por 1 carácter), como `{`, `}`, `.`, `,`, `(`, `)`.  
✔️ Identificação de **símbolos terminais variáveis**:  
  **Variáveis**: tokens do tipo `?nome`, `?desc`.  
  **Números**: tokens que representam números inteiros, como `1000`.  
  **URIs**: tokens que representam URIs, como `dbo:MusicalArtist` ou `foaf:name`.  
  **Literais**: tokens que representam literais de texto, como `"Chuck Berry"@en`.  
✔️ Uso de duas abordagens: **expressões regulares (`re`)** e **biblioteca `ply.lex`**.  
✔️ Ficheiros de saída com os tokens analisados (`LEXresultados.txt` e `resultados.txt`).  

---

## Identificação
**Nome:** Sara Azevedo Lopes  
**Número de Aluno:** 104179

![Identificação Sara Azevedo Lopes](../fotografia.png)
