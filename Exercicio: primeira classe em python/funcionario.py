class Funcionario:

    __slots__ = ['_nome','_cpf','_salario']
    def  __init__(self,nome,cpf,salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    @property
    def nome(self):
        return self._nome
    @property
    def cpf(self):
        return self._cpf
    @property
    def salario(self):
        return self._salario


