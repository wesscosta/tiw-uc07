# Classe Retangulo: Crie uma classe que modele um retangulo:

# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

class RetanguloClass:
  def __init__(self, comprimento, largura):
    self.comprimento = comprimento
    self.largura = largura
    
  def mudarLados(self, novoComprimento, novaLargura):
    self.comprimento = novoComprimento
    self.largura = novaLargura
    print("Os lados mudaram!")
    
  def retornarLados(self):
    return self.comprimento, self.largura
    
  def calcularArea(self):
     return self.comprimento * self.largura
  
  def calularPerimetro(self):
     return 2* (self.comprimento + self.largura)
   
class Main:
  comprimento = int(input('Digite um valor'))
  largura = int(input('Digite um valor'))
  
  meuRetangulo = RetanguloClass(comprimento, largura)
  print (f'Os lados: {meuRetangulo.retornarLados()}')
  
if __name__ == '__main__':
  Main
