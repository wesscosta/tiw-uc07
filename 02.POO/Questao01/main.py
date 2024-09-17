from bola_classe import BolaClass

class Main:
  def executar():
    bola01 = BolaClass('Preta',7,'Plastico')
    print(bola01.cor)
    bola01.set_cor('azul')
    print(bola01.cor)

if __name__ == "__main__":
  Main.executar()
