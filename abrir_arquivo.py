try:
    arquivo = open('emails.txt', 'w') # Se o arquivo estiver em outra pasta é so passar o caminho
    #arquivo = open('emails.doc')      # w modo de escrita
except FileNotFoundError:                # modo r é de leitura (não precisa expecificar o r no final)
    print('Arquivo não encontrado')      # modo b é modo binario
#except:
    #print('Algum erro ocorreu')
#finally:
    #arquivo.close()     # Fecha o arquivo

#try:
    #with open('emails.txt') as arquivo:    # Usar with com open ( with = com)
        #print(arquivo.readlines())
#except FileNotFoundError:
    #print('Arquivo não existe')


#print(type(arquivo))
#print(arquivo)

#conteudo = arquivo.read()  # Mostra o conteudo do arquivo (.read lé o arquivo e transforma em string)
#print(conteudo)

#conteudo = arquivo.readlines()   # .resdlines transforma o arquivo em uma lista de linhas

#print(conteudo)
#print('Guilherme\nJunqueira')      # \n pula uma linha

#for linha in conteudo:
    #print(linha)
    #print(linha.strip())   # Tira o \n