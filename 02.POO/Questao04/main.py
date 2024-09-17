class PessoaClass:
  def __init__(self, nome, idade, peso, altura):
    self.nome = nome
    self.idade = idade
    self.peso = peso
    self.altura = altura
  
  def envelhecer(self, newIdade):
    print('você está ficando velho')
    if self.idade < 21:
      difIdade = newIdade - self.idade
      self.altura += difIdade * 0.5
      print(f'Você agora tem {self.altura}')
    self.idade = newIdade
  
  def engordar(self, gordo):
    self.peso = gordo
    print('você ganhou peso')
    
  def emagrecer(self, magro):
    self.peso = magro
    print('você perdeu peso')
    
  def crescer(self, newAltura):
    self.altura = newAltura
    print('Você cresceu')

class Main:
  pessoa = PessoaClass('Filipi', 19, 65, 181)
  print(f'nome: {pessoa.nome}, idade: {pessoa.idade}, peso: {pessoa.peso}')
  pessoa.envelhecer(23)
  print(f'nova idade: {pessoa.idade}')
  pessoa.engordar(70)
  print(pessoa.peso)
  pessoa.emagrecer(60)
  print(pessoa.peso)
  # pessoa.crescer(184)
  print(f'nova altura {pessoa.altura}')

Main()
