# Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

# Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.


class Bichinho:
  def __init__ (self, nome, fome, saude, idade):
    self.nome = nome
    self.fome = fome
    self.saude = saude
    self.idade = idade
    
  def humor (self):
    humor = (self.fome + self.saude)/2
    return humor
    
  def alterarNome (self, newNome):
    self.nome = newNome
    
  def alterarFome (self, newFome):
    self.fome = newFome
    
  def alterarSaude (self, newSaude):
    self.saude = newSaude
  
  def alterarIdade (self, newIdade):
    self.idade = newIdade
    
  def __str__(self) -> str:
    return(f'nome:{self.nome} \n fome:{self.fome} \n saude:{self.saude} \n idade:{self.idade} \n humor:{self.humor()}')
  
class Main:
  tobias = Bichinho("tobias", 7, 10, 5)
  print(tobias)
  
  tobias.alterarSaude (6)
  tobias.alterarNome ("Tonhão")
  tobias.alterarIdade (50)
  tobias.alterarFome (0)
  
  print(tobias)
