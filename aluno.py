from pessoa_fisica import PessoaFisica

class Aluno(PessoaFisica) :
    def __init__(self):
        self.__cgm = None
        self.__turma = None
        self.__turno = None

    @property
    def cgm(self):
        return self.__cgm

    @property
    def turma(self):
        return self.__cpf

    @property
    def turno(self):
        return self.__turno

    @cgm.setter
    def cgm(self, cgm):
        self.__cgm = cgm

    @turma.setter
    def turma(self, turma):
        self.__turma = turma

    @turno.setter
    def turno(self, turno):
        self.__turno = turno

    def __str__(self):
        return "{},{},{},{}\n".format(super().__str__(), self.__cgm, self.__turma, self.__turno)

    def acessarEscola(self, cgm):
        if (cgm == self.__cgm):
            print("Boa aula aluno(a)", super().nome)
            return True
        else:
            return False