
from FakeDB import FakeDB

FDB = FakeDB()
for list in FDB.listaFuncionarios():
    print(list.nome + list.sobreNome + list.sexo )
