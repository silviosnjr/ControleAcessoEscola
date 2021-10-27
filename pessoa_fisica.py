from abc import ABCMeta, abstractmethod

class PessoaFisica(metaclass=ABCMeta):
    def __init__(self, nome, cpf, rg, nascimento):
        self.__nome = nome
        self.__cpf = cpf
        self.__rg = rg
        self.__dataNascimento = nascimento

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
    def dataNascimento(self):
        return self.__dataNascimento

    @abstractmethod
    def acessarEscola(self, codigoAcesso):
        pass
