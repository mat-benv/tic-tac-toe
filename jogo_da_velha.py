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
checkLinha1 = [celA1, celB1, celC1]
checkLinha2 = [celA2, celB2, celC2]
checkLinha3 = [celA3, celB3, celC3]
checkColunaA = [celA1, celA2, celA3]
checkColunaB = [celB1, celB2, celB3]
checkColunaC = [celC1, celC2, celC3]
checkDiagEsq = [celA1, celB2, celC3]
checkDiagDir = [celC3, celB2, celA1]
listaLinColDiag = [checkLinha1, checkLinha2, checkLinha3, checkColunaA, checkColunaB, checkColunaC, checkDiagDir, checkDiagEsq]

#declarei variáveis para um caralho, esse código ficou longo e ineficiente. Vou tentar fazer ele mais enxuto
#com certeza tem um jeito mais fácil de preencher as células fazendo listas e usando a função for,
#mas eu acho que não ficaria tão bonitinho.

print("Jogo da Velha\nDigite a letra, o número e seu simbolo (nesta ordem) para marcar. (Ex. b2o)")
#coloquei o O minusculo no exemplo para tentar fazer o usuário não usar 0 por acidente

#a ideia é primeiro checar se alguém ganhou e mostrar a mensagem de vitoria caso verdade,
#depois ele vai checar a jogada digitada contra todas as variáveis de celulas pré-definidas e preencher a variável
#com X ou O

#a tabela é inspirada no tabuleiro de xadrez, mas pra ser jogada de xadrez mesmo o X ou O deveria vir antes da célula
#percebi isso bem depois e estou com preguiça de arrumar, talvez arrume mais tarde

while True:
 
    checkLinha1 = [celA1, celB1, celC1]
    checkLinha2 = [celA2, celB2, celC2]
    checkLinha3 = [celA3, celB3, celC3]
    checkColunaA = [celA1, celA2, celA3]
    checkColunaB = [celB1, celB2, celB3]
    checkColunaC = [celC1, celC2, celC3]
    checkDiagEsq = [celA1, celB2, celC3]
    checkDiagDir = [celC1, celB2, celA3]

    listaLinColDiag = [checkLinha1, checkLinha2, checkLinha3, checkColunaA, checkColunaB, checkColunaC, checkDiagDir, checkDiagEsq]
    
    if vitoriaX in listaLinColDiag:
        print(f'\t \t A\t B\tC \n\t1\t{celA1}\t{celB1}\t{celC1}\n\t2\t{celA2}\t{celB2}\t{celC2}\n\t3\t{celA3}\t{celB3}\t{celC3}')
        print('X é o vencedor!')
        break
    elif vitoriaO in listaLinColDiag:
        print(f'\t \t A\t B\tC \n\t1\t{celA1}\t{celB1}\t{celC1}\n\t2\t{celA2}\t{celB2}\t{celC2}\n\t3\t{celA3}\t{celB3}\t{celC3}')
        print('O é o vencedor!')
        break

    else:
        print(f'\t \t A\t B\tC \n\t1\t{celA1}\t{celB1}\t{celC1}\n\t2\t{celA2}\t{celB2}\t{celC2}\n\t3\t{celA3}\t{celB3}\t{celC3}')
        jogada = input("Jogada: ")


        if jogada.upper() == 'A1X':
            celA1 = '|X|'
            continue
        elif jogada.upper() == 'A1O':
            celA1 = '|O|'
            continue
        elif jogada.upper() == 'B1X':
            celB1 = '|X|'
            continue
        elif jogada.upper() == 'B1O':
            celB1 = '|O|'
            continue
        elif jogada.upper() == 'C1X':
            celC1 = '|X|'
            continue
        elif jogada.upper() == 'C1O':
            celC1 = '|O|'
            continue
        elif jogada.upper() == 'A2X':
            celA2 = '|X|'
            continue
        elif jogada.upper() == 'A2O':
            celA2 = '|O|'
            continue
        elif jogada.upper() == 'B2X':
            celB2 = '|X|'
            continue
        elif jogada.upper() == 'B2O':
            celB2 = '|O|'
            continue
        elif jogada.upper() == 'C2X':
            celC2 = '|X|'
            continue
        elif jogada.upper() == 'C2O':
            celC2 = '|O|'
            continue
        elif jogada.upper() == 'A3X':
            celA3 = '|X|'
            continue
        elif jogada.upper() == 'A3O':
            celA3 = '|O|'
            continue
        elif jogada.upper() == 'B3X':
            celB3 = '|X|'
            continue
        elif jogada.upper() == 'B3O':
            celB3 = '|O|'
            continue
        elif jogada.upper() == 'C3X':
            celC3 = '|X|'
            continue
        elif jogada.upper() == 'C3O':
            celC3 = '|O|'
            continue

        else:
            print("Digite uma jogada válida. ")
        #deu um trabalho braçal ridículo com muita chance de erro, com certeza tem um jeito bem melhor da fazer isso