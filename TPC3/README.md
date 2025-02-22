# Conversor de Markdown para HTML

## TPC3
Este projeto implementa um conversor de Markdown para HTML em Python. O conversor suporta os seguintes elementos:

- **Cabeçalhos** (`#`, `##`, `###`)
- **Negrito** (`**texto**` → `<b>texto</b>`)
- **Itálico** (`*texto*` → `<i>texto</i>`)
- **Listas numeradas** (`1. item` → `<ol><li>item</li></ol>`)
- **Links** (`[texto](url)` → `<a href="url">texto</a>`)
- **Imagens** (`![alt](url)` → `<img src="url" alt="alt">`)

O programa lê um ficheiro Markdown e gera um ficheiro HTML formatado corretamente.

---

## Como Utilizar
1. Coloca o conteúdo Markdown num ficheiro `input.md`.
2. Executa o programa:
   ```sh
   python3 tpc3.py
   ```
3. O output será gerado num ficheiro `output.html`.
4. Abre `output.html` no navegador para visualizar o resultado.

---

## Estrutura do Código

### **1. Leitura do ficheiro Markdown**
O programa lê o conteúdo de `input.md` e processa cada linha para converter os elementos suportados.

### **2. Expressões Regulares Utilizadas**
As expressões regulares são fundamentais para identificar e substituir os elementos Markdown corretamente. Aqui está uma explicação detalhada:

- **Cabeçalhos**: `re.match(r'^(#{1,3})\s*(.+)', line)`
  - Captura `#`, `##` ou `###` seguidos de um espaço e o texto do cabeçalho.
  - `#{1,3}` → Captura entre 1 a 3 `#`.
  - `\s*` → Permite espaços opcionais após os `#`.
  - `(.+)` → Captura o restante da linha como o texto do cabeçalho.

- **Listas numeradas**: `re.match(r'\d+\.\s+(.+)', line)`
  - Captura uma linha que começa com um número seguido de `.` e um espaço.
  - `\d+` → Captura um ou mais dígitos (o número da lista).
  - `\.\s+` → Captura um ponto seguido de pelo menos um espaço.
  - `(.+)` → Captura o restante da linha como o texto do item da lista.

- **Negrito**: `re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)`
  - Substitui texto entre `**` por `<b>...</b>`.
  - `\*\*` → Captura os `**` que indicam negrito.
  - `(.*?)` → Captura qualquer texto dentro do negrito.
  - `\*\*` → Captura os `**` finais.

- **Itálico**: `re.sub(r'\*(.*?)\*', r'<i>\1</i>', line)`
  - Semelhante ao negrito, mas para `*texto*`, substituindo por `<i>texto</i>`.
  
- **Links**: `re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', line)`
  - Captura `[texto](url)` e converte para `<a href="url">texto</a>`.
  - `\[(.*?)\]` → Captura o texto do link entre `[]`.
  - `\((.*?)\)` → Captura a URL entre `()`.

- **Imagens**: `re.sub(r'!\[(.*?)\]\((.*?)\)', r'<p>\1</p> <img src="\2" alt="\1" style="width: 150px; height: auto; display: block; margin-top: 5px;">', line)`
  - Captura `![alt](url)` e converte para `<img src="url" alt="alt">`.
  - O texto alternativo (`alt`) aparece primeiro dentro de `<p>` e depois a imagem é gerada com um tamanho controlado.

---

## Exemplo de Entrada e Saída

### **Entrada (`input.md`)**
```md
# Teste do Conversor de Markdown para HTML

# Exemplo sobre coelhos

## Bold

Este é um **coelho** em negrito.

## Itálico

Este é um *coelho* em itálico.

## Lista Numerada 

1. Os dentes dos coelhos nunca param de crescer!
2. Dão saltos chamados de "binkies" quando estão felizes!
3. Têm um campo de visão de quase 360 graus!

## Link

Como pode ser consultado em [documentário sobre coelhos](https://www.youtube.com/watch?v=U5g7x8SVgE8)

## Imagem

Como se vê na imagem seguinte: ![imagem dum coelho](https://images.pexels.com/photos/326012/pexels-photo-326012.jpeg)
```

### **Saída (`output.html`)**
```html
<h1>Teste do Conversor de Markdown para HTML</h1>

<h1>Exemplo sobre coelhos</h1>

<h2>Bold</h2>

Este é um <b>coelho</b> em negrito.

<h2>Itálico</h2>

Este é um <i>coelho</i> em itálico.

<h2>Lista Numerada</h2>

<ol>
<li>Os dentes dos coelhos nunca param de crescer!</li>
<li>Dão saltos chamados de "binkies" quando estão felizes!</li>
<li>Têm um campo de visão de quase 360 graus!</li>
</ol>

<h2>Link</h2>

Como pode ser consultado em <a href="https://www.youtube.com/watch?v=U5g7x8SVgE8">documentário sobre coelhos</a>

<h2>Imagem</h2>

Como se vê na imagem seguinte: <img src="https://images.pexels.com/photos/326012/pexels-photo-326012.jpeg" alt="imagem dum coelho" style="width: 150px; height: auto; display: block; margin-top: 5px;"> 
```

---

## Identificação
**Nome:** Sara Azevedo Lopes  
**Número de Aluno:** 104179

![Identificação Sara Azevedo Lopes](../fotografia.png)