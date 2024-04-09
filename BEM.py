def menu():
  """Exibe as opções do caixa eletrônico."""
  print("""
  [d] Depositar
  [s] Sacar
  [e] Extrato
  [q] Sair

  => """)

def deposito(saldo):
  """Realiza um depósito na conta."""
  valor = float(input("Informe o valor do depósito: "))
  if valor > 0:
    saldo += valor
    print("Depósito realizado com sucesso!")
    return saldo
  else:
    print("Operação falhou! O valor informado é inválido.")
    return saldo

def saque(saldo, limite, numero_saques, limite_saques):
  """Realiza um saque na conta."""
  valor = float(input("Informe o valor do saque: "))
  excedeu_saldo = valor > saldo
  excedeu_limite = valor > limite
  excedeu_saques = numero_saques >= limite_saques

  if excedeu_saldo:
    print("Operação falhou! Você não tem saldo suficiente.")
  elif excedeu_limite:
    print("Operação falhou! O valor do saque excede o limite.")
  elif excedeu_saques:
    print("Operação falhou! Número máximo de saques excedido.")
  elif valor > 0:
    saldo -= valor
    print("Saque realizado com sucesso!")
    return saldo, numero_saques + 1
  else:
    print("Operação falhou! O valor informado é inválido.")
    return saldo, numero_saques

def extrato(saldo, extrato):
  """Exibe o extrato da conta."""
  print("\n================ EXTRATO ================")
  print("Não foram realizadas movimentações." if not extrato else extrato)
  print(f"\nSaldo: R$ {saldo:.2f}")
  print("==========================================")

def main():
  """Função principal do caixa eletrônico."""
  saldo = 0
  limite = 500
  extrato = ""
  numero_saques = 0
  limite_saques = 3

  while True:
    menu()
    opcao = input()

    if opcao == "d":
      saldo = deposito(saldo)
    elif opcao == "s":
      saldo, numero_saques = saque(saldo, limite, numero_saques, limite_saques)
    elif opcao == "e":
      extrato(saldo, extrato)
    elif opcao == "q":
      break
    else:
      print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
  main()
