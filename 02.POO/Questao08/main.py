# Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?

class MacacoClass :
  def __init__(self,nome):
    self.nome = nome 
    self.bucho = []
    
  def comer(self,comida):
    self.bucho.append(comida)
    
  def verBucho(self):
    return (self.bucho)
  
  def digerir(self):
    del self.bucho[0]
    
    
  def __str__(self) -> str:
   return verBucho()
 
class Main :
  macaco1 = MacacoClass("macaco")
  macaco1.comer("banana")
  macaco1.comer("limão")
  macaco1.comer("lima")
  
  macaco2 = MacacoClass("macaco2")
  macaco2.comer("laranja")
  macaco2.comer("tanja")
  macaco2.comer("arroz")
  
  print(macaco1.verBucho())
  print(macaco2.verBucho())
  
  macaco2.digerir()
  print(macaco2.verBucho())
  macaco1.comer(macaco2)
  
  print(macaco1.verBucho())
  
    
    
    
  
