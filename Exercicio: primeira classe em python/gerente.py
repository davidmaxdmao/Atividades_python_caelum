import funcionario
class Gerente(funcionario.Funcionario):

    __slots__ = ['_nome', '_cpf', '_salario','_senha','_qtd_funcionarios']

    def __init__(self, nome, cpf, salario, senha, qtd_funcionarios):
        super().__init__(nome,cpf,salario)
        self._senha = senha
        self._qtd_funcionarios = qtd_funcionarios


    @property
    def senha(self):
        return(self._senha)

    @property
    def qtd_funcionarios(self):
        return self._qtd_funcionarios


    def autentica(self, senha):
        if self._senha == senha:
            print("acesso permitido")
            return True
        else:
            print("acesso negado")
            return False


