from datetime import datetime

class Funcionarios:
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = ''
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

    def calcula_idade(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento
    def cadastra(self):
        self.nome = input('digite seu nome: ')
        self.sobrenome= input('digite seu sobrenome: ')
        self.ano_nascimento = input('qual sua data de nascimento: ')

Funcionarios.cadastra()

usuario1 = Funcionarios(nome,sobrenome,ano_nascimento)
usuario2 = Funcionarios('Elena', 'Borges', 2000)
usuario3 = Funcionarios('Elizangela', 'Santos', 2021)






print(Funcionarios.nome_completo(usuario1))

print(Funcionarios.calcula_idade(usuario2))



