# Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.

class TV:
  def __init__(self, canal, volume):
    self.canal = canal
    self.volume = volume
    
  def mudar(self, newCanal):
    self.canal = newCanal
    return(f'Canal alterado para {self.canal}')
  
  def mais(self):
    self.volume += 1
    return(f'Volume aumentado para {self.volume}')
  
  def menos(self):
    self.volume -= 1
    return(f'Volume reduzido para {self.volume}')
  
  
  def __str__(self):
    return(f'Canal {self.canal}, volume {self.volume}')
  
class Main:
  newTv = TV(10, 20)
  newTv.mudar(4)
  print(newTv.mudar(7))
  
  newTv.mais()
  newTv.mais()
  newTv.mais()
  newTv.mais()
  newTv.menos()
  print(newTv)
  
if __name__ == '__main__':
    Main
    
