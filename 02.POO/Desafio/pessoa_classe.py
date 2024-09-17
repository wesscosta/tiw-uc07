# Classe Pessoa (superclasse)
class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return f'Nome: {self.nome}, CPF: {self.cpf}'

# Classe Aluno (subclasse de Pessoa)
class Aluno(Pessoa):
    def __init__(self, nome, cpf, matricula):
        super().__init__(nome, cpf)
        self.matricula = matricula

    def __str__(self):
        return f'{super().__str__()}, Matrícula: {self.matricula}'

# Classe Professor (subclasse de Pessoa)
class Professor(Pessoa):
    def __init__(self, nome, cpf, disciplina):
        super().__init__(nome, cpf)
        self.disciplina = disciplina

    def __str__(self):
        return f'{super().__str__()}, Disciplina: {self.disciplina}'
