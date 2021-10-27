from aluno import Aluno
from funcionario import Funcionario
from professor import Professor

class Escola():

    def __init__(self):
        self.__nome = "Escola dos Programadores do Futuro"
        aluno1 = Aluno("Beltrano", "111.222.333-44", "8.888.888-8", "01/02/1990", "111-1", "1º ano", "noite")
        professor1 = Professor("Ciclano", "444.555.666-77", "0.000.000-0", "30/05/1988", "3.000,00", "geografia", "temporário")
        funcionario1 = Funcionario("Fulano", "222.333.444-55", "9.999.999-9", "21/05/1989", "1.000,00", "zelador", "08:00 as 17:00")
        aluno2 = Aluno("João", "999.222.333-44", "8.889.888-8", "10/03/1990", "333-1", "2º ano", "tarde")
        professor2 = Professor("José", "888.555.666-77", "0.555.000-0", "20/05/1987", "3.000,00", "matemática", "permanente")
        funcionario2 = Funcionario("Maria", "555.333.444-55", "9.000.999-9", "20/05/1980", "1.000,00", "zelador", "17:00 as 22:00")
        self.__pessoas = [aluno1, professor1, funcionario1, aluno2, professor2, funcionario2]

    def __getitem__(self, item) :
        return self.__pessoas[item]

    def __len__(self):
        return len(self.__pessoas)

    def solicitaAcessa(self):
        codigo_acesso = input("Qual o seu código de acesso: ")
        for pessoa in self.__pessoas :
            if(pessoa.acessarEscola(codigo_acesso)):
                return True
        print("Acesso negado!")
        return False




