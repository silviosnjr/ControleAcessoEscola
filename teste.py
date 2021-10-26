from pessoa_fisica import PessoaFisica
from funcionario import Funcionario
from aluno import Aluno
from professor import Professor

pessoa_silvio = PessoaFisica("Silvio", "111.111.111-22", "4.444.444-4", "01/02/1987")
print("PESSOA Nome: {} - CPF: {}".format(pessoa_silvio.nome, pessoa_silvio.cpf))

funcionario_fulano = Funcionario("1.000,00", "zelador", "08:00 as 17:00")
print("Funcionário Salário: {} - horário de trabalho: {}".format(funcionario_fulano.salario, funcionario_fulano.horario))

aluno_beltrano = Aluno("111-1", "1º ano", "noite")
print("Aluno CGM: {} - Ano: {}".format(aluno_beltrano.cgm, aluno_beltrano.turma))

professor_ciclano = Professor("3.000,00", "geografia", "temporário")
print("Professor Salário: {} - Formação: {}".format(professor_ciclano.salario, professor_ciclano.formacao))
