# Somador On/Off

## TPC1
Este projecto implementa um somador on/off em Python. O somador processa uma sequência de caracteres e realiza as seguintes operações:
1. Soma as sequências de dígitos presentes no texto quando o somador está ligado (`on`).
2. Ignora as sequências de dígitos quando o somador está desligado (`off`).
3. Sempre que encontra o carácter `=`, regista o resultado da soma acumulada.
4. Ignora os caracteres irrelevantes no processamento.

O programa demonstra o uso de lógica condicional e manipulação de sequências de caracteres em Python.

---

## Como Utilizar
1. Execute o programa num terminal ou ambiente Python.
2. Introduza uma sequência de caracteres que contenha números, `on`, `off` e `=`. Existem 3 exemplos na pasta `resultados`.
3. O programa processa a sequência e apresenta os resultados.
4. Pode introduzir várias sequências seguidas sem necessidade de reiniciar o programa.
5. **Para sair do programa, pressione `Ctrl+C` no terminal.**  

**Nota:** Se `Ctrl+C` (`^C`) aparecer dentro da sequência de entrada, o programa simplesmente ignora esse carácter e continua a execução normalmente.

---

## Proposta de Resolução

O programa **Somador On/Off** foi implementado em Python e segue uma abordagem baseada em análise léxica e sintática para interpretar e processar o texto de entrada.

### **1. Analisador Léxico**
A análise léxica identifica e interpreta os elementos relevantes (ou tokens) na sequência de entrada. Neste caso, os tokens são:
- **Inteiros**: Sequências consecutivas de dígitos (`0-9`).
- **Comandos**: Palavras-chave como `on`, `off` e o carácter `=`.
- **Caracteres irrelevantes**: Todos os outros caracteres que não afectam o funcionamento do somador.

No código, esta análise é feita com a função `isdigit()` para identificar inteiros e com verificações específicas para os comandos `on`, `off` e `=`.

---

### **2. Analisador Sintático**
A análise sintática define o comportamento do programa com base na sequência de tokens identificados. A lógica segue as seguintes regras:
1. Quando encontra o comando `on`, o somador passa para o estado ligado.
2. Quando encontra o comando `off`, o somador passa para o estado desligado.
3. Se encontra um número e o somador está ligado, adiciona o número à soma.
4. Quando encontra o carácter `=`, regista o valor acumulado, sem reiniciar a soma.

Esta lógica é implementada através de um ciclo que percorre o texto e avalia cada elemento com base no estado actual (`ligado` ou `desligado`).

---

### **3. Implementação e Estratégia**
O código usa:
- Um acumulador (`soma`) para guardar o valor total.
- Uma variável de estado (`ligado`) que indica se o somador está activado ou desactivado.
- Um ciclo para percorrer os caracteres da sequência, aplicando as regras definidas.

Inclui também verificações para ignorar caracteres irrelevantes e para tratar múltiplos dígitos consecutivos como um único número.

---

### **4. Justificação do Método**
Este método é eficaz porque:
- Processa a sequência de forma linear, garantindo eficiência.
- Implementa conceitos fundamentais de análise léxica e sintática, úteis em linguagens de programação e compiladores.
- Produz resultados corretos, mesmo com a presença de caracteres aleatórios ou comandos em ordem imprevisível.

---

## Resultados

Abaixo estão três testes de exemplo, disponíveis na pasta `resultados`, com as respetivas entradas e saídas esperadas.

📌 **[Resultado 1](../resultados/resultado1.txt)**  
**Entrada:** `"on10off20on30=on40="`  
**Saída esperada:** `[40, 80]`  
➡️ Explicação:
- `on10` → somador ligado, soma `10`
- `off20` → somador desligado, `20` ignorado
- `on30` → somador ligado novamente, soma `30` (**40** acumulado)
- `=` → regista **40**
- `on40` → somador ligado, soma `40` (**80** acumulado)
- `=` → regista **80**

---

📌 **[Resultado 2](../resultados/resultado2.txt)**  
**Entrada:** `"xxon10!!off??30#on50=tfdwgyqshjon10gddbdof2hwbuwbdonoied6="`  
**Saída esperada:** `[60, 78]`  
➡️ Explicação:
- Ignora caracteres irrelevantes (`xx`, `!!`, `??`, `#`, `tfdwgyqshj`, etc.)
- `on10` → somador ligado, soma `10`
- `off30` → somador desligado, `30` ignorado
- `on50` → somador ligado, soma `50` (**60** acumulado)
- `=` → regista **60**
- `on10` → somador ligado, soma `10` (**70** acumulado)
- `2` → somador ainda ligado, soma `2` 
- `on6` → somador ligado, soma `6` (**78** acumulado)
- `=` → regista **78**

---

📌 **[Resultado 3](../resultados/resultado3.txt)**  
**Entrada:** `"off10on50=off30on20=^Con123s1212="`  
**Saída esperada:** `[50, 70, 1405]`  

**Nota sobre `^C`:**  
Neste teste, a sequência contém `^C`, que representa `Ctrl+C`, mas surge **dentro do texto**, sendo simplesmente ignorado pelo programa, que continua a execução normalmente. **O programa só é interrompido se `Ctrl+C` for pressionado diretamente no terminal sem qualquer outra entrada.**

➡️ **Explicação:**
- `off10` → somador desligado, `10` ignorado.
- `on50` → somador ligado, soma `50`
- `=` → regista **50**
- `off30` → somador desligado, `30` ignorado.
- `on20` → somador ligado, soma `20` (**70** acumulado).
- `=` → regista **70**
- `^C` → ignorado.
- `on123` → somador ligado, soma `123`.
- `on1212` → somador ligado, soma `1212` (**1405** acumulado).
- `=` → regista **1405**

---

## Lista de Resultados dos Exemplos Anteriores
Os ficheiros de saída encontram-se na pasta `resultados`:

- [Resultado 1](Resultados/resultado1.txt) – Teste básico com `on` e `off`.
- [Resultado 2](Resultados/resultado2.txt) – Teste com caracteres irrelevantes.
- [Resultado 3](Resultados/resultado3.txt) – Teste com `^C` dentro da sequência.

---

## Identificação

**Nome:** Sara Azevedo Lopes  
**Número de Aluno:** 104179  

![Identificação Sara Azevedo Lopes](../fotografia.png)
