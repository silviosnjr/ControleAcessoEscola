from abc import ABCMeta, abstractmethod

class PessoaFisica(metaclass = ABCMeta) :
    def __init__(self):
        self.__nome = None
        self.__cpf = None
        self.__rg = None
        self.__nascimento = None

    def __str__(self):
        return "{},{},{},{}".format(self.__nome, self.__cpf, self.__rg, self.__nascimento)

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def rg(self):
        return self.__rg

    @property
    def nascimento(self):
        return self.__nascimento

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @rg.setter
    def rg(self, rg):
        self.__rg = rg

    @nascimento.setter
    def nascimento(self, nascimento):
        self.__nascimento = nascimento

    @abstractmethod
    def acessarEscola(self, cpf):
        pass