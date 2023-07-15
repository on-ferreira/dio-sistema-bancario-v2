class Account():
    def __init__(self):
        self.saldo = 0.00
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3
        self.log = []
    
    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.log.append("Depósito R$ " + str(valor))

    def saque(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
        elif self.numero_saques >= self.LIMITE_SAQUES:
            print("Limite de saques atingido")
        elif valor > 500:
            print("O limite por saque é de R$500.00")
        else:
            self.numero_saques += 1
            self.saldo -= valor
            self.log.append("Saque R$ " + str(valor))

    def extrato(self):
        print("Saldo R$ " + str(self.saldo))
        if len(self.log) == 0:
            print("Não foram realizadas movimentações.")
        else:
            print("Log de Operações")
            for op in self.log:
                print(op)

class Client():
    def __init__(self, nome):
        self.contas = []
        self.nome = nome
    
    def criar_conta(self):
        conta = Conta()
        self.contas.append(conta)

    def menu(self):
        op = 0
        while op != 5:
            print('''
--- Digite a operação que deseja realizar ---

1 - Depósito
2 - Saque
3 - Extrato
4 - Cadastrar nova conta
5 - Sair
---------------------------------------------
            ''')
            op = int(input())

            if op == 1:
                valor = int(input('Digite o valor do depósito: '))
                if valor > 0:
                    conta = self.selecionar_conta()
                    if conta:
                        conta.deposito(valor)

            elif op == 2:
                valor = int(input('Digite o valor do saque: '))
                conta = self.selecionar_conta()
                if conta:
                    conta.saque(valor)

            elif op == 3:
                conta = self.selecionar_conta()
                if conta:
                    conta.extrato()

            elif op == 4:
                conta = Account()
                self.contas.append(conta)
                print("Nova conta criada com sucesso")

            elif op == 5:
                pass

    def selecionar_conta(self):
        if len(self.contas) == 0:
            print("Nenhuma conta cadastrada.")
            return None

        print("Selecione a conta:")
        for i, conta in enumerate(self.contas):
            print(f"{i+1} - Conta {i+1}")

        op = int(input())
        if op < 1 or op > len(self.contas):
            print("Opção inválida.")
            return None

        return self.contas[op - 1]


class Banco():
    def __init__(self):
        self.clientes = []

    def cadastrar_cliente(self, nome):
        cliente = Client(nome)
        self.clientes.append(cliente)

    def menu_principal(self):
        while True:
            print('''
--- Digite a operação que deseja realizar ---

1 - Cadastrar cliente
2 - Acessar cliente
3 - Sair
---------------------------------------------
            ''')
            op = int(input())

            if op == 1:
                nome = input('Digite o nome do cliente: ')
                self.cadastrar_cliente(nome)

            elif op == 2:
                cliente = self.selecionar_cliente()
                if cliente:
                    cliente.menu()

            elif op == 3:
                exit()

    def selecionar_cliente(self):
        if len(self.clientes) == 0:
            print("Nenhum cliente cadastrado.")
            return None

        print("Selecione o cliente:")
        for i, cliente in enumerate(self.clientes):
            print(f"{i+1} - {cliente.nome}")

        op = int(input())
        if op < 1 or op > len(self.clientes):
            print("Opção inválida.")
            return None

        return self.clientes[op - 1]



banco = Banco()
banco.menu_principal()