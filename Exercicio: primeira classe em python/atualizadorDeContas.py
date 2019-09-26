class AtualizadorDeContas:
    def __init__(self, selic, saldo_total=0):
        self._selic = selic
        self._saldo_total = saldo_total

    def roda (self, conta, taxa):
        print(conta.saldo)
        conta.atualiza(taxa)
        self._saldo_total += conta.saldo