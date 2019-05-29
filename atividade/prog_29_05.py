class PI:
    def __init__ (self, titulo, ano, alunos, professores):
        self.titulo = titulo
        self.ano = ano
        self.alunos = alunos
        self.professores = professores

class Aluno:

    def __init__(self,turma,curso,nome):
        self.turma = turma
        self.curso = curso
        self.nome = nome

class Professor:

    def __init__(self, areas, nome):
        self.areas = []
        self.nome = nome

class Area:

    def __init__ (self,nome, periodicos, eventos):
        self.nome = nome
        self.periodicos = []
        self.eventos = []

class Periodico:

    def __init__ (self, editora, ISSN):
        self.editora = editora
        self.ISSN = float(8)

class Evento:

    def __init__ (self, nome, ano, local):
        self.nome = nome
        self.ano = ano
        self.local = local

if __name__ == "__main__":

    evento_1 = Evento ("MICTI", 2019, "Brusque")
    periodico_1 = Periodico ("IFC", 20463920)
    area_1 = Area ("banco de dados", periodico_1, evento_1)
    area_2 = Area ("geografia", periodico_1, evento_1)
    professor_1 = Professor (area_1, "Aldelir Luiz")
    professor_2 = Professor (area_2, "Cloves Castro")
    aluno_1 = Aluno ( 301, "Informática", "Gustavo Kistner")
    aluno_2 = Aluno ( 301, "Informática", "Vinicius Franke")
    pi_1 = PI ("Portal de Oportunidades", 2019, [aluno_1, aluno_2], [professor_1, professor_2])

    print("Projeto integrador: ", pi_1.titulo, "\n", "Ano: ", pi_1.ano, "\n", "Aluno(s):", end=" ")
    for i in pi_1.alunos:
       print(i.nome, end=", ")
    print("\n" , "Professores: ", end="")
    for i in pi_1.professores:
       print(i.nome, end=", ")
    

    