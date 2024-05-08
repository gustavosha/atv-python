frase = "cada carro tem o seu motor seu motorista e sua gasolina"
palavras = frase.split()

frequencia = {}
for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1

print(frequencia)