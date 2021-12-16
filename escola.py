from pessoa_fisica import PessoaFisica
from aluno import Aluno
from professor import Professor
from funcionario import Funcionario
from aluno_DAO import AlunoDAO
from professor_DAO import ProfessorDAO
from funcionario_DAO import FuncionarioDAO
from validate_docbr import CPF

class Escola():
    def __init__(self):
        self.__nome = "Escola Estadual Programadores do Futuro"
        self.menu()

    def __getitem__(self, item):
        return self.__pessoas[item]

    def __len__(self):
        return len(self.__pessoas)

    def solicitarAcesso(self) :
        print("\nSolicitando ACESSO À ESCOLA")
        codigo_acesso = input("Qual o seu código de acesso: ")
        pessoas = self.carregaPessoas()
        for pessoa in pessoas:
            if(pessoa.acessarEscola(codigo_acesso)):
                print() #para qubrar uma linha
                self.menu()
        print ("Acesso negado!")
        print()  # para qubrar uma linha
        self.menu()

    def menu(self):
        print("MENU - O que você deseja fazer ?")
        print("Digite 1 para adicionar um NOVO ALUNO ?")
        print("Digite 2 para adicionar um NOVO PROFESSOR ?")
        print("Digite 3 para adicionar um NOVO FUNCIONÁRIO ?")
        print("Digite 4 para LISTAR TODOS")
        print("Digite 5 para ACESSAR ESCOLA")
        print("Digite 6 para SAIR")

        resposta = input("Digite o número da sua respostas: ")

        if(resposta == "1"):
            self.adicionarAluno()
        elif(resposta == "2"):
            self.adicionarProfessor()
        elif(resposta == "3"):
            self.adicionarFuncionario()
        elif(resposta == "4"):
            self.listarTodos()
        elif (resposta == "5"):
            self.solicitarAcesso()
        elif(resposta == "6"):
            pass

    def adicionarPessoaFisica(self, pessoa):
        pessoa.nome = input("Nome: ")
        cpf_valido = False
        validador = CPF()
        while(cpf_valido):
            cpf = input("CPF: ")
            cpf.replace(".", "")
            cpf.replace("-", "")
            cpf_valido = validador.validate(cpf)
            if (not cpf_valido) : print("CPF Inválido, digite novamente!")
        pessoa.cpf = validador.mask(input("CPF: "))
        pessoa.rg = input("RG: ")
        pessoa.nascimento = input("Data de Nascimento: ")

    def adicionarAluno(self):
        aluno = Aluno()
        print("\nAdicionando um NOVO ALUNO(A)")
        self.adicionarPessoaFisica(aluno)
        aluno.cgm = input("Número CGM do aluno:")
        aluno.turma = input("Turma do aluno:")
        aluno.turno = input("Turno do aluno (manhã, tarde ou noite):")
        dao_aluno = AlunoDAO()
        dao_aluno.salvar(aluno, "dados/alunos.csv")
        self.menu()

    def adicionarProfessor(self):
        professor = Professor()
        print("\nAdicionando um NOVO PROFESSOR(A)")
        self.adicionarPessoaFisica(professor)
        professor.salario = input("Salário do aluno:")
        professor.formacao = input("Formação do aluno:")
        professor.vinculo = input("Vínculo do professor (permanente, temporário):")
        dao_professor = ProfessorDAO()
        dao_professor.salvar(professor, "dados/professores.csv")
        self.menu()

    def adicionarFuncionario(self):
        funcionario = Funcionario()
        print("\nAdicionando um NOVO FUNCIONÁRIO(A)")
        self.adicionarPessoaFisica(funcionario)
        funcionario.salario = input("Salário do aluno:")
        funcionario.cargo = input("Cargo:")
        funcionario.horario = input("Horário de trabalho:")
        dao_funcionario = FuncionarioDAO()
        dao_funcionario.salvar(funcionario, "dados/funcionarios.csv")
        self.menu()

    def listarTodos(self):
        print("\nLISTA DE CADASTROS")
        pessoas = self.carregaPessoas()
        for pessoa in pessoas:
            print(pessoa, end="")
        print()  #para qubrar uma linha
        self.menu()

    def carregaPessoas(self):
        dao_aluno = AlunoDAO()
        dao_professor = ProfessorDAO()
        dao_funcionario = FuncionarioDAO()

        pessoas = []
        pessoas = dao_aluno.listar("dados/alunos.csv")
        pessoas += dao_professor.listar("dados/professores.csv")
        pessoas += dao_funcionario.listar("dados/funcionarios.csv")

        return pessoas