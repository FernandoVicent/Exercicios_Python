from datetime import datetime

class Funcionarios:
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

    def calcula_idade(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento


usuario1 = Funcionarios('Silvia', 'Cabral', 2009)
usuario2 = Funcionarios('Elena', 'Borges', 2000)
usuario3 = Funcionarios('Elizangela', 'Santos', 2021)



print(Funcionarios.nome_completo(usuario1))

print(Funcionarios.calcula_idade(usuario2))



