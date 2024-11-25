
class Integrante_IFRN:
    def exibirMensagem(self):
        print("Integrante_IFRN: Seja bem vindo(a) ao IFRN!!!")


class Professor(Integrante_IFRN):
    def exibirMensagem(self):
        print("Professor: Meus alunos são os melhores!!!")

class Aluno(Integrante_IFRN):
    def exibirMensagem(self):
        print("Aluno: Vou estudar pra tirar 100 em POO!!!")

integrante = Integrante_IFRN()
professor = Professor()
aluno = Aluno()

integrante.exibirMensagem()
professor.exibirMensagem()
aluno.exibirMensagem()
