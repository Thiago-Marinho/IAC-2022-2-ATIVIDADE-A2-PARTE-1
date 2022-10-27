from datetime import datetime

class Funcionario:

    def __init__(self, codigo: int, nome: str, sobreNome: str, sexo: str, dataAniversario: datetime):
        self.codigo = codigo
        self.nome = nome
        self.sobreNome = sobreNome
        self.sexo = sexo
        self.dataAniversario = dataAniversario

