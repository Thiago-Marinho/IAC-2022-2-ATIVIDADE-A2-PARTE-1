import random

from FakeDB import FakeDB

FDB = FakeDB()
numRandom = []
listTemp = FDB.listaFuncionarios()
x = random.randint(1, 49)
cont = 0


numTest = (random.randrange(1, 50))
numRandom.append(numTest)
numTest = (random.randrange(1, 50))

for i in range(x):
        #for j in numRandom:
        if(numRandom.__contains__(numTest)):
                numTest = (random.randrange(1, 50))

        else:
                numRandom.append(numTest)
                numTest = (random.randrange(1, 50))


cont = 0
for listaFunc in FDB.listaFuncionarios():

        if (listaFunc.codigo == numRandom[cont]):
                print(listaFunc.nome + listaFunc.sobreNome + listaFunc.sexo)
                cont = cont + 1

if (cont <= 0):
        print("Não á registro com a busca informada")
        exit()

