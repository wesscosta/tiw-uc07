from ex002 import Quadrado

lado = int(input("Informe o lado do seu quadrado: "))

def novoQuadrado(lado):
  q = Quadrado(lado)
  q.calculoArea()
  
novoQuadrado(lado)
