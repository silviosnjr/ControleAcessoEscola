import csv
from funcionario import Funcionario

class FuncionarioDAO():

    def salvar(self, funcionario, caminho):
        #print(funcionario)
        with open(caminho, mode='a') as arquivo :
            arquivo.write(funcionario.__str__())
            arquivo.flush()
        print("Funcionário Salvo com cusseso\n")

    def listar(self, caminho, encoding='latin_1'):
            funcionarios = []
            try :
                with open(caminho, encoding=encoding) as arquivo:
                    leitor = csv.reader(arquivo)
                    for linha in leitor:
                        funcionario = Funcionario()
                        funcionario.nome, funcionario.cpf, funcionario.rg, funcionario.nascimento, funcionario.salario, funcionario.cargo, funcionario.horario = linha
                        funcionarios.append(funcionario)
                return funcionarios
            except FileNotFoundError :
                return funcionarios