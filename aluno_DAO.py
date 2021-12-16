import csv
from aluno import Aluno

class AlunoDAO():

    def salvar(self, aluno, caminho):
        #print(aluno)
        with open(caminho, mode='a') as arquivo :
            arquivo.write(aluno.__str__())
            arquivo.flush()
        print("Aluno Salvo com cusseso\n")

    def listar(self, caminho, encoding='latin_1'):
        try:
            alunos = []
            with open(caminho, encoding=encoding) as arquivo:
                leitor = csv.reader(arquivo)
                for linha in leitor:
                    aluno = Aluno()
                    aluno.nome, aluno.cpf, aluno.rg, aluno.nascimento, aluno.cgm, aluno.turma, aluno.turno = linha
                    alunos.append(aluno)
            return alunos
        except FileNotFoundError:
            return alunos