#dicionario = {"tijolo": "objeto para montar muros"}       # O dicionário possui chave e valor
#print(dicionario)                                         # Dicioário não é ordenado não possui indice
#print(dicionario["tijolo"])        # Exibi o valor da chave (tijolo)

#dicionario = {
    #"tijolo": "objeto para montar muros",
    #"constituição": "lei máxima do Brasil}

#print(dicionario["constituição"])

#idades = {
    #"guilherme": 19,
    #"maria": 17,
    #"joão": 22}

#print(idades["guilherme"])

pessoas = {
    "guilherme": 19,
    "maria": 17,
    "joão": 22
}

#for pessoa in pessoas:
    #print(pessoa)             # Vai printar as chaves

#for pessoa in pessoas.values():    # Printa os valores
    #print(pessoa)

for pessoa in pessoas:    # Printa os valores
    print(pessoas[pessoa])
