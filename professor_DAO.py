import csv
from professor import Professor

class ProfessorDAO():

    def salvar(self, professor, caminho):
        #print(professor)
        with open(caminho, mode='a') as arquivo :
            arquivo.write(professor.__str__())
            arquivo.flush()
        print("Professor Salvo com cusseso\n")

    def listar(self, caminho, encoding='latin_1'):
            professores = []
            try :
                with open(caminho, encoding=encoding) as arquivo:
                    leitor = csv.reader(arquivo)
                    for linha in leitor:
                        professor = Professor()
                        professor.nome, professor.cpf, professor.rg, professor.nascimento, professor.salario, professor.formacao, professor.vinculo = linha
                        professores.append(professor)
                return professores
            except FileNotFoundError :
                return professores