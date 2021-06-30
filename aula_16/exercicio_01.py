#Se a pessoa tiver mais que 30 anos, as calorias de comer são em dobro
#Se a pesssoa tiver menos que 30 anos, as calorias de malhar são em dobro
class Pessoa:
    def __init__(self, nome, idade, peso):
        self.nomePessoa = nome
        self.idadePessoa = idade
        self.pesoPessoa = peso
    def comer(self, calorias):
        if self.idadePessoa >= 30:
            calorias = calorias*2
            self.pesoPessoa += calorias
        else:
            self.pesoPessoa += calorias
    def malhar(self, calorias):
        if self.idadePessoa <= 30:
            calorias = calorias*2
            self.pesoPessoa -= calorias
        else:
            self.pesoPessoa -= calorias
    def mostrarDados(self):
        return f'''
        Os dados salvos são:
        Nome: {self.nomePessoa}
        Idade: {self.idadePessoa}
        Peso: {self.pesoPessoa}'''

#Programa Principal
pessoa1 = Pessoa(str(input('Informe o nome da pessoa 1: ').strip().capitalize()), 
            int(input('Informe a idade da pessoa 1: ')), 
            float(input('Informe o peso da pessoa 1: ')))
print(pessoa1.mostrarDados())
pessoa1.comer(10)
print(pessoa1.mostrarDados())