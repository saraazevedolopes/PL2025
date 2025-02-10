def somador_on_off(texto):
    soma = 0
    ligado = True  # O somador começa ligado por defeito
    resultado = []

    i = 0
    while i < len(texto):
        if texto[i:i+2].lower() == "on":
            ligado = True
            i += 2  # Avança para depois do "on"
        elif texto[i:i+3].lower() == "off":
            ligado = False
            i += 3  # Avança para depois do "off"
        elif texto[i] == "=":
            # Regista o resultado actual sem reiniciar a soma
            resultado.append(soma)
            i += 1
        elif texto[i].isdigit() and ligado:
            # Adiciona o número à soma se o somador estiver ligado
            start = i
            while i < len(texto) and texto[i].isdigit():
                i += 1
            soma += int(texto[start:i])
        else:
            # Avança se o carácter não for relevante
            i += 1

    return resultado


# Ciclo infinito para processar múltiplas entradas até Ctrl+C
try:
    while True:
        texto_utilizador = input("Introduza o texto para processar (Ctrl+C para sair): ")
        resultado = somador_on_off(texto_utilizador)
        print("Resultados:", resultado)
except KeyboardInterrupt:
    print("\nPrograma encerrado pelo utilizador.")
