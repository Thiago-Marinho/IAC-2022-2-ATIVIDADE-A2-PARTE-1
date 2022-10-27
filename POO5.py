from FakeDB import FakeDB

Filtro = input("Digite as três primeiras letras do sobrenome do funcionario: ")

FDB = FakeDB()
cont = 0

for listaFunc in FDB.listaFuncionarios():
        if(listaFunc.sobreNome[0:3].lower() == Filtro.lower()):
                print(listaFunc.nome + listaFunc.sobreNome)
                cont = cont + 1
if (cont <= 0):
        print("Não á registro com a busca informada")
        exit()