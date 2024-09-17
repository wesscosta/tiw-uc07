from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, idade, altura, peso):
        self.__nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        
    @abstractmethod
    def calcular_imc(self):
        pass
        
    @abstractmethod
    def fazer_aniversario(self):
        pass
        
    @abstractmethod
    def apresentar(self):
        pass
        
class Homem(Pessoa):
    def __init__(self, nome, idade, altura, peso):
        super().__init__(nome, idade, altura, peso)
        
    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        return imc
        
    def fazer_aniversario(self):
        self.idade += 1
        print(f"Parabéns! {self.nome} agora tem {self.idade} anos.")
        
    def apresentar(self):
        return(f"Olá! Meu nome é {self.nome}, tenho {self.idade} anos, {self.altura}m de altura e peso {self.peso}kg.")
        
class Mulher(Pessoa):
    def __init__(self, nome, idade, altura, peso):
        super().__init__(nome, idade, altura, peso)
        
    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        return imc
        
    def fazer_aniversario(self):
        self.idade += 1
        print(f"Parabéns! {self.nome} agora tem {self.idade} anos.")
        
    def apresentar(self):
        print(f"Olá! Meu nome é {self.nome}, tenho {self.idade} anos, {self.altura}m de altura e peso {self.peso}kg.")
