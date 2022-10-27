from FakeDB import FakeDB

Filtro = input("Digite a data de aniversario do funcionario: ")

FDB = FakeDB()
cont = 0

print("\nLista de funcionarios conforme consulta:\n")
for listaFunc in FDB.listaFuncionarios():
        if(listaFunc.dataAniversario[6:10] == Filtro):
                print("Nome: " + listaFunc.nome + " " + listaFunc.sobreNome + " - Data de Aniversario:" + listaFunc.dataAniversario)
                cont = cont +1
if (cont <= 0):
        print("Não á registro com a busca informada")
        exit()