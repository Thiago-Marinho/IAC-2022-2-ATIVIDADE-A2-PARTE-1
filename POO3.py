from FakeDB import FakeDB

Filtro = input("Digite o Sexo do funcionario (M) ou (F): ")

FDB = FakeDB()
cont = 0

print("\nLista de funcionarios conforme consulta:\n")
for listaFunc in FDB.listaFuncionarios():
        if(listaFunc.sexo.lower() == Filtro.lower()):
                print("Nome: " + listaFunc.nome +" "+ listaFunc.sobreNome + " - Sexo: " + listaFunc.sexo)
                cont = cont + 1
if (cont <= 0):
        print("Não á registro com a busca informada")
        exit()