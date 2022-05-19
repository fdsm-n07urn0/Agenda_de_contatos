'''Erros em tempo de copilação'''
#prin('Olá mundo')
#if True
    #print('Olá mundo')

'''Erros em tempo de execução'''
# divisao(a, b):
    #print(a / b)
#divisao(1, 0) # Não é divisivel por zero

'''Erros de lógica'''
#def divisao(a, b):
    #print(a * b) # Ex: Pensa que colocou sinal de divisão
#divisao(1, 2)


#def divisao(a, b):
    #try:
        #print(a / b)
    #except:
    #except Exception as e: # Pega a ecesão
        #print('Divisão inválida')
        #print(e)
#divisao(20, 0)



try:
    a = float(input('Digite o numero A: ')) #ValueError
    b = float(input('Digite o numero B: '))

    print(a/b) # ZeroDivisionError
except ValueError as error:
    print('Input inválido, digite apenas números')
except ZeroDivisionError as error:
    print('Não pode ser feita divisão por zero')
except Exception as error:
    print('Algum erro ocorreu')
    print(error)
finally:
    print('Fim do programa')