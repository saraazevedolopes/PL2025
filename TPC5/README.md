# Analisador Léxico para Máquina de Vending  

## TPC5
Este trabalho de casa implementa uma **máquina de vending simulada** em Python, oferecendo funcionalidades para:

- **Listar** produtos, apresentando código, nome, quantidade e preço.  
- **Selecionar** um produto, reduzindo o stock conforme o saldo do utilizador.  
- **Adicionar** ou **remover** produtos, atualizando o inventário existente.  
- **Inserir moedas**, somando ao saldo disponível para efetuar compras.  
- **Terminar** a sessão, devolvendo o troco remanescente.

O **grande destaque** em relação ao trabalho anterior é a **introdução de estados** no lexer, nomeadamente o estado `insertcoins`, que gere especificamente a introdução de moedas antes de regressar ao estado padrão dos comandos gerais.

---

## Como Utilizar
1. **Alterar o conteúdo do ficheiro `stock.json`** caso se pretenda ajustar o inventário de produtos ou **utilizar o já existente** com dados predefinidos.
2. **Executar** o comando:
    ```sh
    python3 maquina_vending.py
    ```
3. Introduzir os comandos na consola (ex.: LISTAR, MOEDA 1e, 50c., SELECIONAR X2, etc.).
A aplicação apresenta as respostas de acordo com as operações realizadas.

---

## Estrutura do Código

### **Leitura de Input**
A aplicação lê cada linha introduzida pelo utilizador (através da consola) e processa-a para identificar os tokens. Após o reconhecimento dos tokens, as operações da máquina de vending são executadas.

### **Expressões Regulares e Estados**
As **expressões regulares** definidas no código servem para identificar vários tipos de tokens, tais como:

- **Comandos**  
    ```python
  r'(?i)\b(LISTAR|SELECIONAR|SAIR|ADICIONAR|REMOVER)\b'
  ```
Reconhece comandos (insensível a maiúsculas/minúsculas), p. ex. LISTAR, selecionar.

- **Moeda** 
    ```python
  r'(?i)((?:1|5|10|20|50)c|(?:1|2)e)(\s*,\s*((?:1|5|10|20|50)c|(?:1|2)e))*\s*\.'
  ```
Identifica sequências de moedas (p. ex. 1e, 50c.) exclusivamente no estado insertcoins.

- **Código de Produto** 
    ```python
  r'\b[A-Z]\d{1,2}\b'
  ```
Reconhece um código composto por uma letra maiúscula e 1 a 2 dígitos (ex.: X1, A10).

- **Inteiros** 
    ```python
  r'\b\d+\b'
  ```
Captura inteiros isolados, p. ex. para quantidade ou preço.

- **Floats** 
    ```python
  r'\b\d+\.\d+\b'
  ```
Reconhece números decimais (ex.: 0.5), p. ex. para preço.

### **Estados**
Além das expressões regulares, existe o uso de dois **estados**:

1. **INITIAL**: estado padrão, em que são reconhecidos comandos, códigos de produto, inteiros, floats, etc.
2. **insertcoins**: é ativado quando se lê o comando MOEDA; neste estado, apenas se interpretam sequências de moedas até ao ponto final (.), regressando depois a INITIAL.
Desta forma, o código permanece organizado e legível, isolando a lógica de inserção de moedas num estado dedicado a isso.

O uso deste estado permite diferenciar os momentos em que a máquina está a processar **comandos gerais** dos momentos em que está a receber **valores monetários**. Sem um estado dedicado a isto, seria mais difícil validar corretamente a entrada de moedas, podendo causar erros no reconhecimento dos tokens ou dificultar a gestão do saldo.  

Desta forma, o código permanece **organizado e legível**, isolando a lógica de inserção de moedas num estado dedicado.  

### Atualização de Stock
Sempre que o utilizador **adiciona** ou **remove** produtos, o ficheiro `stock.json` é **imediatamente atualizado**, reflectindo as alterações feitas ao inventário. Isto assegura que o estado do stock se mantém consistente ao longo de toda a execução do programa.

---

## Exemplo de Entrada e Saída

```plaintext
maq: Stock carregado, Estado atualizado.
maq: Bom dia. Estou disponível para atender o seu pedido.
>> LISTAR
maq:
cod | nome | quantidade | preço
---------------------------------
A23 água 0.5L 8 0.7
B12 sumo laranja 5 1.2
C34 batata frita 10 1.5
D56 chocolate 3 1.0
E78 café 15 0.8
>> MOEDA 1e, 5c.
maq: Saldo = 1e5c
>> SELECIONAR X1 
maq: Produto inexistente.
>> SELECIONAR B12
maq: Saldo insuficiente para satisfazer o seu pedido
maq: Saldo = 1e5c; Pedido = 120c
>> SELECIONAR A23
maq: Pode retirar o produto dispensado "água 0.5L"
maq: Saldo = 0e35c
>> ADICIONAR X3 10 1.2
maq: Produto novo detectado! Introduza o nome para X3: folhado misto
maq: Produto "folhado misto" adicionado com 10 unidades a 1.2 euros.
>> REMOVER X3
maq: Produto "folhado misto" removido do stock.
>> SAIR
maq: Pode retirar o troco: 1e 20c, 1e 10c, 1e 5c.
maq: Até à próxima
 ```

### Explicação das Operações
1. **LISTAR**: Mostra a lista de produtos disponíveis na máquina.
2. **MOEDA 1e, 5c**: Atualizando o saldo.
3. **SELECIONAR X1**: Retorna erro, pois o produto não existe.
4. **SELECIONAR B12**: Retorna erro de saldo insuficiente.
5. **SELECIONAR A23**: Compra o produto "água 0.5L", atualizando o saldo.
6. **ADICIONAR X3 10 1.2**: Adiciona um novo produto e pede um nome para ele.
7. **REMOVER X3**: Remove o produto adicionado anteriormente.
8. **SAIR**: Devolve o troco e encerra a interação.

---

## 📁 Estrutura do Projeto  

```bash
📂 TPC5
 ├── 📄 tpc5.py         # Implementação do analisador léxico com `ply.lex`
 ├── 📄 stock.json      # Ficheiro JSON contendo o stock da máquina
 ├── 📄 README.md       # Documentação do projeto
```
---

## 🎯 Conclusão  

Este projeto implementa um analisador léxico para uma **máquina de vending**, permitindo a simulação da interação com a máquina através de comandos textuais.

✅ **Resumo dos Objetivos Cumpridos:**  

✔️ **Implementação de um lexer utilizando PLY (Python Lex-Yacc)** para interpretar comandos inseridos pelo utilizador.  
✔️ **Introdução de estados no lexer**, incluindo `insertcoins`, que gere especificamente a inserção de moedas.  
✔️ **Identificação e tratamento de tokens específicos**, incluindo:  
- **Comandos** (`LISTAR`, `SELECIONAR`, `MOEDA`, `ADICIONAR`, `REMOVER`, `SAIR`).  
- **Valores Monetários** (euros e cêntimos) com suporte a múltiplos valores por comando.  
- **Códigos de Produto**, garantindo que apenas produtos válidos sejam processados.  

✔️ **Gestão do stock da máquina**, sendo armazenado num ficheiro JSON (`stock.json`), com suporte para listagem, adição e remoção de produtos.  
✔️ **Implementação de verificações de saldo e devolução de troco**, garantindo que o utilizador recebe troco adequado no final da interação.  
✔️ **Mensagens de erro detalhadas** para ajudar o utilizador a corrigir entradas inválidas e a compreender o funcionamento da máquina.  

---

## Identificação
**Nome:** Sara Azevedo Lopes  
**Número de Aluno:** 104179

![Identificação Sara Azevedo Lopes](../fotografia.png)