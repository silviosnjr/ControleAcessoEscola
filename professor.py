from pessoa_fisica import PessoaFisica

class Professor(PessoaFisica):
    def __init__(self, nome, cpf, rg, nascimento, salario, formacao, vinculo):
        super().__init__(nome, cpf, rg, nascimento)
        self.__salario = salario
        self.__formacao = formacao
        self.__vinculo = vinculo

    @property
    def salario(self):
        return self.__salario

    @property
    def formacao(self):
        return self.__formacao

    @property
    def vinculo(self):
        return self.__formacao

    def __str__(self):
        return "PROFESSOR - Nome: {} - CPF: {} - RG: {} - Nascimento: {} - " \
               "Salário: {} - Formação: {} - Vínculo: {}".format(
            super().nome, super().cpf, super().rg, super().dataNascimento,
            self.__salario, self.__formacao, self.__vinculo)

    def acessarEscola(self, codigoAcesso):
        if(codigoAcesso == super().cpf):
            print("Boa aula professor(a), {}".format(super().nome))
            return True
        else:
            return False