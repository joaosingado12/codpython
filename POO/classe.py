class Produto:
    def __init__(self, descricao, preco):
        self.descricao=descricao
        self.preco=preco
    def exibirPreco(self):
        print(f"{self.descricao} Por apenas {self.preco}")


class Pessoa:
    def __init__(self, cpf='', nome='', rg=''):
        self.cpf=cpf
        self.nome=nome
        self.rg=rg
    
    def registro(self):
        self.nome = input("Insira o nome da pessoa: ")
        self.cpf = input("Insira o CPF da pesso: ")
        self.rg = input("Insira o RG da pessoa: ")

    def exibirdados(self):
        print(f"informações da Pessoa:\n{self.nome}\n{self.cpf}\n{self.rg}")
    
class Dog:
    def __init__(self, raca='', peso='', idade=''):
        self.raca=raca
        self.peso=peso
        self.idade=idade

    def info(self):
        self.raca = input('Informe a raça do Cachorro: ')
        self.peso = input('Informe o peso do Cachorro: ')
        self.idade = input('Informe a idade do Cachorro: ')

    def exibirdados(self):
        print(f"Segue as informações do Cachorro:\nRaça: {self.raca}\nPeso: {self.peso}\nIdade: {self.idade}")
