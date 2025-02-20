import re
from collections import Counter, defaultdict

def normalizar_csv(input_file):
    registros = []
    buffer = []
    dentro_de_aspas = False  

    with open(input_file, encoding="utf-8") as csvfile:
        linhas = csvfile.readlines()
        for line in linhas[1:]:  
            line = line.strip()
            nova_linha = []
            
            for char in line:
                if char == '"':
                    dentro_de_aspas = not dentro_de_aspas  
                if dentro_de_aspas and char == ';':
                    nova_linha.append(',')  
                else:
                    nova_linha.append(char)
            
            buffer.append("".join(nova_linha))
            
            if not dentro_de_aspas:
                registros.append(" ".join(buffer))  
                buffer = []

    return registros

def escrever_resultados(compositores, periodos, obras_por_periodo):
    with open("resultados.txt", "w", encoding="utf-8") as f:
        f.write("\n📜 Lista ordenada alfabeticamente dos compositores musicais:\n\n")
        for compositor in sorted(compositores):
            f.write(f"  - {compositor}\n")

        f.write("\n📊 Distribuição das obras por período:\n\n")
        for periodo in sorted(periodos):
            f.write(f"  - {periodo}: {periodos[periodo]} obras\n")

        f.write("\n📚 Lista alfabética das obras por período:\n\n")
        for periodo in sorted(obras_por_periodo):
            f.write(f"🎼 {periodo}:\n")
            for titulo in sorted(obras_por_periodo[periodo]):
                f.write(f"  - {titulo}\n")
            f.write("\n")  

    print("✅ Os resultados foram guardados em 'resultados.txt'.")

def process_csv(input_file):
    regex_extracao = re.compile(r'^([^;]*);(?:[^;]*;){2}([^;]*);([^;]*);')  

    registros = normalizar_csv(input_file)
    compositores = set()
    periodos = Counter()
    obras_por_periodo = defaultdict(list)  

    for registo in registros:
        match = regex_extracao.search(registo)
        
        if match:
            nome, periodo, compositor = match.groups()
            nome = nome.strip()
            periodo = periodo.strip()
            compositor = compositor.strip()
            
            compositores.add(compositor)
            periodos[periodo] += 1
            obras_por_periodo[periodo].append(nome)

    escrever_resultados(compositores, periodos, obras_por_periodo)

if __name__ == "__main__":
    process_csv("obras.csv")
