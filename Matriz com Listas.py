#Crie um programa que declare uma matriz de dimensão 5×5 e preencha com valores lidos pelo teclado. No final, mostre a
#matriz na tela, com a formatação correta.
matriz = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
for linha in range(0,5):
    for coluna in range(0,5):
        while True:
            try:
                matriz[linha][coluna] = int(input("número:"))
                break
            except Exception as Er:
                print(f"Erro.Digite um número inteiro.\nSegue, oficialmente o tipo do ERRO->{Er}.{ValueError}.\nContinue preenchendo sua Matriz.")
for linha in range(0,5):
    print("|",end=(''))
    for coluna in range(0,5):
        print(f'{matriz[linha][coluna]:^8}|',end=('')) #os parâmetros do 'for' fazem o fatiamento correto, e o nome das variáveis do 'for' são 'linhas' e 'colunas'
    print() #sem esse print vazio, com uma identação atrás, ele não formata corretamente, isto é, não faz uma quebra de linha
