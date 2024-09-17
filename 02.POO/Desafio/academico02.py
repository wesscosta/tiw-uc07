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

# Testes com o sistema expandido

# Criação de alunos
aluno1 = Aluno('Alice', '123.456.789-00', '2023001')
aluno2 = Aluno('Bob', '987.654.321-00', '2023002')

# Criação de professores
professor1 = Professor('Carlos', '111.222.333-44', 'Matemática')
professor2 = Professor('Diana', '555.666.777-88', 'Física')

# Criação de cursos
curso1 = Curso('Engenharia')
curso2 = Curso('Ciência da Computação')

# Adicionando alunos e professores aos cursos
curso1.adicionar_aluno(aluno1)
curso1.adicionar_professor(professor1)

curso2.adicionar_aluno(aluno2)
curso2.adicionar_professor(professor2)

# Criação de disciplinas e turmas
disciplina1 = Disciplina('Cálculo I', professor1)
turma1 = Turma('T01')

disciplina2 = Disciplina('Física I', professor2)
turma2 = Turma('T02')

# Adicionando turmas às disciplinas
disciplina1.adicionar_turma(turma1)
disciplina2.adicionar_turma(turma2)

# Adicionando alunos às turmas
turma1.adicionar_aluno(aluno1)
turma2.adicionar_aluno(aluno2)

# Registrando avaliações
avaliacao1 = Avaliacao(9.0, 0.8)
avaliacao2 = Avaliacao(7.5, 1.0)

turma1.registrar_avaliacao(aluno1, avaliacao1)
turma2.registrar_avaliacao(aluno2, avaliacao2)

# Exibindo informações
curso1.exibir_info()
disciplina1.exibir_turmas()
turma1.exibir_avaliacoes()
