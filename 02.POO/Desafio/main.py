from pessoa_classe import Aluno,Professor
from academico_classe import Avaliacao,Curso,Disciplina, Turma



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
