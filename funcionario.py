from pessoa_fisica import PessoaFisica

class Funcionario(PessoaFisica):
    def __init__(self):
        self.__salario = None
        self.__cargo = None
        self.__horario = None

    @property
    def salario(self):
        return self.__salario

    @property
    def cargo(self):
        return self.__cargo

    @property
    def horario(self):
        return self.__horario

    @salario.setter
    def salario(self, salario):
        self.__salario = salario

    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo

    @horario.setter
    def horario(self, horario):
        self.__horario = horario

    def __str__(self):
        return "{},{},{},{}\n".format(super().__str__(), self.__salario, self.__cargo, self.__horario)

    def acessarEscola(self, cpf):
        if (cpf == super().cpf):
            print("Bom trabalho ", super().nome)
            return True
        else:
            return False