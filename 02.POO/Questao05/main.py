class ContaCorrente:
  def __init__(self, num, nome, saldo):
      self.num = num
      self.nome = nome
      self.saldo = saldo
      
  def alterar_nome(self, novo_nome):
    self.nome = novo_nome
    return self.nome
    
  def depositar(self, valor):
    self.saldo += max(valor, 0)
    
  def saque(self, valor):
    self.saldo -= min(valor,self.saldo) if valor > 0 else 0
  
  def __str__(self):
    return (f"Na conta {self.num} Do titular {self.nome} tem o saldo {self.saldo}")
    
    
    
conta = ContaCorrente(6892, "Ruan", 1000)
conta.saque(500)
conta.depositar(200)

print(conta)
