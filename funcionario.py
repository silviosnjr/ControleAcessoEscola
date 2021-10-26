class Funcionario():
    def __init__(self ,salario, cargo, horario):
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