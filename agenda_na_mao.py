# Dicionario dentro de dicionario
agenda = {
    "guilherme": {
        "tel": "99999-1010",
        "email": "contato@solyd.com.br",
        "endereço": "av. 1"
    },
    "maria": {
        "tel": "99229-2020",
        "email": "maria@solyd.com.br",
        "endereço": "av. 2"
    },
    "joao": {
        "tel": "96267-1660",
        "email": "joao@solyd.com.br",
        "endereço": "av. 3"
    },
}

agenda["guilherme"]["endereço"] = "Rua das nações"     # Troca o endereço da pessoa

# Adiciona uma nova pessoa
agenda["lucas"] = {
    "tel": "98882-2189",
    "email": "lucas@solyd.com.br",
    "endereço": "av. josé bonifacio",
}

agenda.pop("guilherme")       # Remove uma pessoa

for contato in agenda:
    print(contato)

print(agenda["lucas"])
#print(agenda["guilherme"]["endereço"])