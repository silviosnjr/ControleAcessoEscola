from pessoa_fisica import PessoaFisica

class Professor(PessoaFisica) :
    def __init__(self):
        self.__salario = None
        self.__formacao = None
        self.__vinculo = None

    @property
    def salario(self):
        return self.__salario

    @property
    def formacao(self):
        return self.__formacao

    @property
    def vinculo(self):
        return self.__vinculo

    @formacao.setter
    def formacao(self, formacao):
        self.__formacao = formacao

    @salario.setter
    def salario(self, salario):
        self.__salario = salario

    @vinculo.setter
    def vinculo(self, vinculo):
        self.__vinculo = vinculo

    def __str__(self):
        return "{},{},{},{}\n".format(super().__str__(), self.__salario, self.__formacao, self.__vinculo)

    def acessarEscola(self, cpf):
        if (cpf == super().cpf):
            print("Boa aula professor(a)", super().nome)
            return True
        else:
            return False