# Classe Quadrado: Crie uma classe que modele um quadrado:

# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
  def __init__(self, lado):
    self.lado = lado
    
  def mudarLado(self, lado):
    self.lado = lado
    
  def calculoArea(self):
    area = self.lado**2
    print(f"Lado do quadrado: {self.lado}")
    print(f"Área do quadrado: {area} m2")

    
