from validate_docbr import CPF

class Documento:

    @staticmethod
    def cria_documento(documento):
        if (len(documento) == 11):
            return DocCpf(documento)
        else :
            raise ("Quantidade de dígitos está incorreta!")

class DocCpf:
    def __init__(self, documento):
        if (self.valida(documento)) :
            self.cpf = documento
        else :
            return false;
            raise ValueError("Cpf inválido")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)