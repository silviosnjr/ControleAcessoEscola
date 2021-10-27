from pessoa_fisica import PessoaFisica

class Aluno(PessoaFisica):
    def __init__(self, nome, cpf, rg, nascimento, cgm, turma, turno):
        super().__init__(nome, cpf, rg, nascimento)
        self.__cgm = cgm
        self.__turma = turma
        self.__turno = turno

    @property
    def cgm(self):
        return self.__cgm

    @property
    def turma(self):
        return self.__turma

    @property
    def turno(self):
        return self.__turno

    def __str__(self):
        return "ALUNO - Nome: {} - CPF: {} - RG: {} - Nascimento: {} - " \
               "CGM: {} - Turma: {} - Turno: {}".format(
            super().nome, super().cpf, super().rg, super().dataNascimento,
            self.__cgm, self.__turma, self.__turno)

    def acessarEscola(self, codigoAcesso):
        if (codigoAcesso == self.__cgm):
            print("Boa aula aluno(a), {}".format(super().nome))
            return True
        else:
            return False





