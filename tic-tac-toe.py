#These are the strings that build the board and check for victory. The "cel" ones chance as the game goes on,
#the "vitoria" ones are constante.
celA1 = '| |'
celA2 = '| |'
celA3 = '| |'
celB1 = '| |'
celB2 = '| |'
celB3 = '| |'
celC1 = '| |'
celC2 = '| |'
celC3 = '| |'
vitoriaX = ['|X|', '|X|', '|X|']
vitoriaO = ['|O|', '|O|', '|O|']

print('Jogo da Velha\nDigite seu símbolo (X ou O), a letra (coluna) e o número (linha) para marcar no tabuleiro. (Ex. ob2, xa3)\nDigite "SAIR" para sair.')

while True:

    #Updating the board.
    tabuleiro = f'\t   A\t B\t C\n\t1 {celA1}\t{celB1}\t{celC1}\n\n\t2 {celA2}\t{celB2}\t{celC2}\n\n\t3 {celA3}\t{celB3}\t{celC3}'

    #Updantint lists of cells. These are read for a victory check.
    checkLinha1 = [celA1, celB1, celC1]
    checkLinha2 = [celA2, celB2, celC2]
    checkLinha3 = [celA3, celB3, celC3]
    checkColunaA = [celA1, celA2, celA3]
    checkColunaB = [celB1, celB2, celB3]
    checkColunaC = [celC1, celC2, celC3]
    checkDiagEsq = [celA1, celB2, celC3]
    checkDiagDir = [celC1, celB2, celA3]

#Updating lists of victory conditions and cells.
    listaLinColDiag = [checkLinha1, checkLinha2, checkLinha3, checkColunaA, checkColunaB, checkColunaC, checkDiagDir, checkDiagEsq]
    allCels = [celA1, celA2, celA3, celB1, celB2, celB3, celC1, celC2, celC3]

#Checking for victory.
    if vitoriaX in listaLinColDiag:
        print(tabuleiro)
        print('X é o vencedor!')
        a = input("Jogar de novo?(s/n) ").lower()
        if a == 's':
            celA1 = celA2 = celA3 = celB1 = celB2 = celB3 = celC1 = celC2 = celC3 = '| |'
            continue
        else:
            break

    elif vitoriaO in listaLinColDiag:
        print(tabuleiro)
        print('O é o vencedor!')
        a = input("Jogar de novo?(s/n) ").lower()
        if a == 's':
            celA1 = celA2 = celA3 = celB1 = celB2 = celB3 = celC1 = celC2 = celC3 = '| |'
            continue
        else:
            break

    #Checking for a full board.
    elif '| |' not in allCels: 
        print(tabuleiro)
        print('Deu velha! :(')
        a = input("Jogar de novo?(s/n) ").lower()
        if a == 's':
            celA1 = celA2 = celA3 = celB1 = celB2 = celB3 = celC1 = celC2 = celC3 = '| |'
            continue
        else:
            break
#After each game, the user is prompted to play again, if "yes", the board is wiped and the while loop continues.

    else:
        print(tabuleiro)
        jogada = input("Jogada: ").upper()

#Checking for each possible play. Very ineffient, but it's my first project and I didn't know any better.
        if jogada == 'XA1' and celA1 == '| |':
            celA1 = '|X|'
        elif jogada == 'OA1' and celA1 == '| |':
            celA1 = '|O|'
        elif jogada == 'XB1' and celB1 == '| |':
            celB1 = '|X|'
        elif jogada == 'OB1' and celB1 == '| |':
            celB1 = '|O|'
        elif jogada == 'XC1' and celC1 == '| |':
            celC1 = '|X|'
        elif jogada == 'OC1' and celC1 == '| |':
            celC1 = '|O|'
        elif jogada == 'XA2' and celA2 == '| |':
            celA2 = '|X|'
        elif jogada == 'OA2' and celA2 == '| |':
            celA2 = '|O|'
        elif jogada == 'XB2' and celB2 == '| |':
            celB2 = '|X|'
        elif jogada == 'OB2' and celB2 == '| |':
            celB2 = '|O|'
        elif jogada == 'XC2' and celC2 == '| |':
            celC2 = '|X|'
        elif jogada == 'OC2' and celC2 == '| |':
            celC2 = '|O|'
        elif jogada == 'XA3' and celA3 == '| |':
            celA3 = '|X|'
        elif jogada == 'OA3' and celA3 == '| |':
            celA3 = '|O|'
        elif jogada == 'XB3' and celB3 == '| |':
            celB3 = '|X|'
        elif jogada == 'OB3' and celB3 == '| |':
            celB3 = '|O|'
        elif jogada == 'XC3' and celC3 == '| |':
            celC3 = '|X|'
        elif jogada == 'OC3' and celC3 == '| |':
            celC3 = '|O|'
        elif jogada == 'SAIR':
            break

        #For invalid input.
        else:
            print('Digite uma jogada válida. Seu símbolo, letra e depois número (nesta ordem. Ex: ob2).\nO espaço deve estar vazio.\nDigite "SAIR" para sair.')

input("Obrigado por jogar! ") #End message.
