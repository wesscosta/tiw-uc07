#Classe Bola: Crie uma classe que modele uma bola:
#Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor


class BolaClass:
  def __init__(self, cor, circunferencia,material):
    self.material = material
    self.circunferencia = circunferencia
    self.cor = cor
    
  def set_cor(self, newCor):
    self.cor = newCor
    print('A cor foi alterada com sucesso!!')
    
  def get_cor(self):
    return self.cor
