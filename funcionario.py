from pessoa_fisica import PessoaFisica

class Funcionario(PessoaFisica):
    def __init__(self, nome, cpf, rg, nascimento, salario, cargo, horario):
        super().__init__(nome, cpf, rg, nascimento)
        self.__salario = salario
        self.__cargo = cargo
        self.__horario = horario

    @property
    def salario(self):
        return self.__salario

    @property
    def cargo(self):
        return self.__cargo

    @property
    def horario(self):
        return self.__horario

    def __str__(self):
        return "FUNCIONÁRIO - Nome: {} - CPF: {} - RG: {} - Nascimento: {} - " \
               "Salário: {} - Carga: {} - Horario: {}".format(
            super().nome, super().cpf, super().rg, super().dataNascimento,
            self.__salario, self.__cargo, self.__horario)

    def acessarEscola(self, codigoAcesso):
        if (codigoAcesso == super().cpf):
            print("Bom trabalho, {}".format(super().nome))
            return True
        else :
            return False