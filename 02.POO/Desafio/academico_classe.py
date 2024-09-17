# Classe Avaliacao
class Avaliacao:
    def __init__(self, nota, peso=1.0):
        self.nota = nota
        self.peso = peso

    def calcular_nota_final(self):
        return self.nota * self.peso

# Classe Turma
class Turma:
    def __init__(self, codigo):
        self.codigo = codigo
        self.alunos = set()
        self.avaliacoes = {}

    def adicionar_aluno(self, aluno):
        self.alunos.add(aluno)

    def remover_aluno(self, aluno):
        self.alunos.discard(aluno)

    def registrar_avaliacao(self, aluno, avaliacao):
        if aluno in self.alunos:
            self.avaliacoes[aluno] = avaliacao
        else:
            print(f'Aluno {aluno.nome} não está matriculado nesta turma.')

    def exibir_alunos(self):
        print(f'Alunos na turma {self.codigo}:')
        for aluno in self.alunos:
            print(aluno)
        print('-' * 30)

    def exibir_avaliacoes(self):
        print(f'Avaliações na turma {self.codigo}:')
        for aluno, avaliacao in self.avaliacoes.items():
            print(f'{aluno.nome}: Nota {avaliacao.nota}, Peso {avaliacao.peso}, Nota Final: {avaliacao.calcular_nota_final()}')
        print('-' * 30)

# Classe Disciplina
class Disciplina:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor
        self.turmas = set()

    def adicionar_turma(self, turma):
        self.turmas.add(turma)

    def exibir_turmas(self):
        print(f'Disciplina: {self.nome}, Professor: {self.professor.nome}')
        for turma in self.turmas:
            turma.exibir_alunos()

# Classe Curso
class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = set()
        self.professores = set()

    def adicionar_aluno(self, aluno):
        self.alunos.add(aluno)

    def remover_aluno(self, aluno):
        self.alunos.discard(aluno)

    def adicionar_professor(self, professor):
        self.professores.add(professor)

    def remover_professor(self, professor):
        self.professores.discard(professor)

    def exibir_info(self):
        print(f'Curso: {self.nome}')
        print('Alunos:')
        for aluno in self.alunos:
            print(aluno)
        print('Professores:')
        for professor in self.professores:
            print(professor)
        print('-' * 30)
