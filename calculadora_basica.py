while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite um operador (+-/*): ')
    numeros_validos = None # aqui é uma flag (bandeirinha)
    num_1_float = 0 # adicionamos fora p/ evitar erros
    num_2_float = 0
    try: # tente, em caso de excessão, p/ o programa ñ parar de funcionar
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True # após tentar try, se não gerar erro então aqui é True
    except: # exceto, no caso desta excessão
        numeros_validos = None # garante que continue sendo None, caso gere algum erro na linha anterior
    if numeros_validos is None: # checando se é None, então print
        print('Um ou mais números digitados são inválidos')
        continue # p/ impedir que o código pare aqui, vai levar p/ o topo do laço
    operadores_permitidos = '+-/*'
    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue
    if len(operador) > 1:
        print('Digite apenas um operador')
        continue    
    print('Efetuando conta. Confira o resultado abaixo: ')
    if operador == '+':
        print(num_1_float + num_2_float)
    elif operador == '-':
        print(num_1_float - num_2_float)
    elif operador == '/':
        print(num_1_float / num_2_float)
    elif operador == '*':
        print(num_1_float * num_2_float)
    else:
        print('Não deveria ter chegado aqui.')
    sair = input('Quer sair? [s]air: ').lower().startswith('s') # única "sair"
    print(sair)
    if sair is True: # se sair for booleano, ou "s"
        break # se digitar qualquer outra coisa, vai entrar em loop