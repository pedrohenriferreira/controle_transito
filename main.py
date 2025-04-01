# Alex Cardoso, Gustavo Biasso, Pedro Ferreira

def infracao(vel_permitida, vel_registrada):
      excesso = vel_registrada - vel_permitida
      if excesso <= 0:
        return "Nenhuma infração", 0, 0
      elif excesso <= 0.2 * vel_permitida:
        return "Infração leve", 130.16, 0
      elif excesso <= 0.5 * vel_permitida:
        return "Infração grave", 195.23, 5
      else:
        return "Infração gravíssima", 880.41, 7
    
def ver_reincidencia(multa, reincidente):
      return multa * 2 if reincidente else multa

def desconto(multa, pagar):
   return multa * 0.8 if pagar else multa

def principal():
   print('Sistema de controle de transito')
   placa = input("Informe a placa do veiculo: ").upper()
   nome_motorista = input("Informe o nome do condutor: ").upper()
   vel_registrada = float(input("Informe a velocidade registrada: "))
   vel_permitida = float(input("Informe a velocidade permitida na via: "))
   reincidente = input("O motorista ja foi multado anteriormente? (s/n): ").lower() == 's'
   

   classificacao, multa, pontos = infracao(vel_permitida, vel_registrada)
   multa = ver_reincidencia(multa, reincidente)
   
   print(f'\n Infracao: { classificacao }')
   print(f'Multa: { multa }')
   print(f'Pontos: { pontos }')

   if classificacao == 'infracao gravissima':
      print("O condutor deve realizar o curso de reciclagem no Detran.")

   pagar = input("Deseja pagar agora? (s/n): ").lower() == 's'
   valor_final = desconto(multa, pagar)

   if pagar:
      print(f'A multa com desconto ficou no total de { valor_final:.2f}')

principal()
    



        