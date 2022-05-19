'''
try:
    with open('nomes.txt') as arquivo:
        print(arquivo.readlines())
except Exception as error:
    print('Algum erro ocorreu')
    print(error)
'''
'''
try:
    with open('nomes.txt', 'w') as arquivo:
        arquivo.write('João')                     # write = escrever
except Exception as error:
    print('Algum erro ocorreu')
    print(error)
'''

try:
    with open('nomes.txt', 'a') as arquivo:
        arquivo.write('João\n')
except Exception as error:
    print('Algum erro ocorreu')
    print(error)


# 'r' - abre para ler
# 'w' - abre para escrever / arquivo é sobrescrito
# 'a' - abre para escrever / novo conteudo é adicionado ao final do arquivo
# '+' - Ex: 'r+' da a posibilidade de ler e escrever porem se o arquivo não existir ele não vai ser criado
# 'b' - binario
# etc..