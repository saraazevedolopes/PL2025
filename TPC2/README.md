# 🎼 Processamento de Obras Musicais  

## TPC2 - Processamento Manual de CSV  

Este trabalho consiste na **leitura e processamento manual** de um ficheiro CSV contendo informações sobre obras musicais, **sem utilizar o módulo `csv` do Python**.  

O programa extrai e organiza os seguintes dados:  

1. **Lista ordenada alfabeticamente dos compositores musicais.**  
2. **Distribuição das obras por período** (quantidade de obras catalogadas em cada período).  
3. **Dicionário em que a cada período está associada uma lista alfabética dos títulos das obras desse período**.  

Os resultados são guardados no ficheiro **`resultados.txt`**.  

---

## ❌ Restrição Importante  

**De acordo com o enunciado do TPC, é proibido utilizar o módulo `csv` do Python.**  
Portanto, o ficheiro CSV é processado **manualmente**, utilizando **manipulação de strings** e **expressões regulares**.  

---

## Como Utilizar  

1. Certifique-se de que o ficheiro **`obras.csv`** está no mesmo diretório do script.  
2. Execute o programa com:  
   ```bash
   python3 tpc2.py
   ```  
3. Após a execução, os resultados estarão disponíveis no ficheiro **`resultados.txt`**.  
   > Nota: Se o ficheiro `resultados.txt` já existir, os seus dados serão substituídos por novos.  

---

## Estrutura do Ficheiro CSV  

O ficheiro CSV segue a seguinte estrutura:  

```csv
nome;desc;anoCriacao;periodo;compositor;duracao;_id
```

Os campos extraídos são:

- **Nome da obra (`nome`)** → Para organizar alfabeticamente as obras por período.
- **Período histórico (`periodo`)** → Para categorizar as obras.
- **Compositor (`compositor`)** → Para listar alfabeticamente os compositores únicos.  

---

## Implementação e Estratégia  

### 1. Processamento Manual do CSV  
Como o uso do módulo `csv` não é permitido, o ficheiro é tratado como um ficheiro de texto, separando manualmente os campos.  
O código lida com aspas, caracteres especiais e delimitadores inconsistentes para garantir que os dados sejam extraídos corretamente.  

### 2. Extração dos Dados  
A extração dos campos necessários é feita através de **expressões regulares**, armazenando os dados em:

- **`compositores`** → Conjunto (`set`) para armazenar compositores sem repetições.
- **`periodos`** → Contador (`Counter`) para contabilizar o número de obras por período.
- **`obras_por_periodo`** → Dicionário (`defaultdict(list)`) para agrupar os títulos das obras por período.  

🔍 **Expressão Regular Utilizada**  
A extração dos dados do CSV é feita com a seguinte expressão regular (RE):  

```python
regex_extracao = re.compile(r'^([^;]*);(?:[^;]*;){2}([^;]*);([^;]*);')
```

🔹 **Explicação da RE:**  
- `^([^;]*)` → Captura o primeiro campo (nome da obra) antes do primeiro `;`
- `(?:[^;]*;){2}` → Ignora os dois campos seguintes (`desc` e `anoCriacao`)
- `([^;]*)` → Captura o período histórico
- `([^;]*)` → Captura o compositor  

Dessa forma, é possível extrair exatamente os três campos necessários (**Nome, Período e Compositor**) e ignorar os restantes campos do CSV.  

### 3. Escrita dos Resultados  
Os resultados são guardados no ficheiro **`resultados.txt`**, estruturado da seguinte forma:

- Lista ordenada dos compositores.
- Distribuição das obras por período.
- Lista alfabética das obras dentro de cada período.  

---

## 📁 Estrutura do Projeto  

```bash
📂 TPC2
 ├── 📄 tpc2.py             # Código principal
 ├── 📄 obras.csv           # Ficheiro de entrada (dados)
 ├── 📄 resultados.txt      # Ficheiro de saída (resultados)
 ├── 📄 README.md           # Documentação
```

---

## 🎯 Conclusão  

Este projeto demonstra como processar um ficheiro CSV sem utilizar bibliotecas especializadas, manipulando os dados manualmente e garantindo um formato de saída organizado e padronizado.  

✅ **Resumo dos Requisitos Cumpridos:**  
✔️ Não foi utilizado o módulo `csv`  
✔️ Os compositores foram extraídos e ordenados alfabeticamente  
✔️ A quantidade de obras por período foi contabilizada  
✔️ Um dicionário com a lista alfabética das obras por período foi criado  
✔️ Os resultados foram guardados no ficheiro `resultados.txt`  

---

## Identificação  

**Nome:** Sara Azevedo Lopes  
**Número de Aluno:** 104179  

![Identificação Sara Azevedo Lopes](../fotografia.png)

