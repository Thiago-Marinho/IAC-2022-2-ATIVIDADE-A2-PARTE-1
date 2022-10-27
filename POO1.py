from FakeDB import FakeDB

Filtro = input("Digite as três primeiras letras do nome do funcionario: ")

FDB = FakeDB()
cont = 0

print("\nLista de funcionarios conforme consulta:\n")
for listaFunc in FDB.listaFuncionarios():
        if(listaFunc.nome[0:3].lower() == Filtro.lower()):
                print("Nome: " + listaFunc.nome + " "+ listaFunc.sobreNome)
                cont = cont + 1
if (cont <= 0):
        print("Não á registro com a busca informada")
        exit()