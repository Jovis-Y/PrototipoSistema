from abc import ABC, abstractclassmethod, abstractproperty
from tempo import get_timestamp
from terminalFuncs import log

ListaClientes = []
idTemp = 0

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    _agencia = "0001"
    def __init__(self, idConta, cliente):
        self._saldo = 0
        self._idConta = idConta
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def criar_conta(cls, cliente, idConta):
        return cls(idConta, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def idConta(self):
        return self._idConta

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo

        if valor > saldo:
            log("amarelo", "Saldo Insuficiente")

        elif valor > 0:
            self._saldo -= valor
            log("verde", "DEPÓSITO REALIZADO COM SUCESSO: saldo -> {self._saldo}")
            return True

        else:
            log("amarelo", "SAQUE NÃO REALIZADO")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            log("verde", f"DEPÓSITO REALIZADO COM SUCESSO: saldo -> {self._saldo}")
        else:
            log("amarelo", "DEPÓSITO NÃO REALIZADO")
            return False

        return True


class ContaCorrente(Conta):
    limite=500
    limite_saques=3
    def __init__(self, idConta, cliente):
        super().__init__(idConta, cliente)

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        if valor > self.limite:
            print("Saldo Insuficiente")

        elif numero_saques >= self.limite_saques:
            print("3 saques já foram realizados hoje")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.idConta}
            Titular:\t{self.cliente.nome}
        """

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "data": get_timestamp(),
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                
            }
        )


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


def estaCadastrado(CPF):
    if len(ListaClientes) == 0:
        return False
    
    for cliente in ListaClientes:
        if cliente.cpf == CPF:
            return True
    
    return False

def returnCliente(CPF):    
    for cliente in ListaClientes:
        if cliente.cpf == CPF:
            return cliente

def getInstaceConta(idconta) -> ContaCorrente or None:
    if len(ListaClientes) == 0:
        return None
    
    for cliente in ListaClientes:
        for conta in cliente.contas:
            if conta.idConta == idconta:
                return conta
    
    return None

def extrato(conta:ContaCorrente):
    for transacao in conta.historico.transacoes:
        for value in transacao.values():
            if value == "Saque":
                print(f"{value}   ", end=" ")
            print(value, end=" ")
        print()
