celA1 = '|X|'
celA2 = '|X|'
celA3 = '|X|'
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

print(checkColunaA == vitoriaX)