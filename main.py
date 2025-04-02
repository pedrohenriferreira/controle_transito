# Alex Cardoso, Gustavo Biasso, Pedro Ferreira

def infracao(vel_permitida, vel_registrada):  # função para verificar a infração
      excesso = vel_registrada - vel_permitida # comparação entre os valores
      if excesso <= 0: # se a diferença entre os valores for menor ou igual a 0
        return "Nenhuma infração", 0, 0  # retorna string da infração, valor da multa e pontos 
      elif excesso <= 0.2 * vel_permitida: # se a diferença for menor ou igual a 20%
        return "Infração leve", 130.16, 0 # retorna string da infração, valor da multa e pontos 
      elif excesso <= 0.5 * vel_permitida: # se a diferença for menor ou igual a 50%
        return "Infração grave", 195.23, 5 # retorna string da infração, valor da multa e pontos 
      else: # se a diferença for maior que 50%
        return "Infração gravíssima", 880.41, 7 # retorna string da infração, valor da multa e pontos 
    
def ver_reincidencia(multa, reincidente): # função para verificar se o motorista é reincidente 
      return multa * 2 if reincidente else multa # retorna o valor da multa e se caso for reincidente multiplica o valor por 2 e aplica

def desconto(multa, pagar): # Aplica o desconto 
   return multa * 0.8 if pagar else multa # multiplica o valor da multa por 8% e aplica o desconto

def principal(): # função feita para armazenar os valores em variaveis 
   print('Sistema de controle de transito')
   placa = input("Informe a placa do veiculo: ").upper()
   nome_motorista = input("Informe o nome do condutor: ").upper()
   vel_registrada = float(input("Informe a velocidade registrada: "))
   vel_permitida = float(input("Informe a velocidade permitida na via: "))
   reincidente = input("O motorista ja foi multado anteriormente? (s/n): ").lower() == 's'
   

   classificacao, multa, pontos = infracao(vel_permitida, vel_registrada) # variavel classificação, multa e ponto recebe a função infração
   multa = ver_reincidencia(multa, reincidente) # a variavel multa recebe a função para verificar reincidente 
   
   print(f'\n Infracao: { classificacao }')
   print(f'Multa: { multa }')
   print(f'Pontos: { pontos }')

   if classificacao == 'Infração gravíssima': # se a infração for gravissima o motorista é informado que deve realizar o curso
      print("O condutor deve realizar o curso de reciclagem no Detran.")

   pagar = input("Deseja pagar agora? (s/n): ").lower() == 's'
   valor_final = desconto(multa, pagar)

   if pagar:
      print(f'A multa com desconto ficou no total de { valor_final:.2f}')

principal()
    



        