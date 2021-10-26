class Aluno():
    def __init__(self, cgm, turma, turno):
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