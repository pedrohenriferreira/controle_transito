# Alex Cardoso, Gustavo Biasso, Pedro Ferreira

def infracao(vel_permitida, vel_registrada):  # função para verificar a infração
      excesso = vel_registrada - vel_permitida # comparação entre os valores
      if excesso <= 0: # se a diferença entre os valores for menor ou igual a 0
        multa = 0
        pontos = 0
        return  "Nenhuma infração", multa, pontos  # retorna string da infração, valor da multa e pontos 
      elif excesso <= 0.2 * vel_permitida: # se a diferença for menor ou igual a 20%
        multa = 130.16
        pontos = 0
        return "Infração leve", multa, pontos # retorna string da infração, valor da multa e pontos 
      elif excesso <= 0.5 * vel_permitida: # se a diferença for menor ou igual a 50%
        multa = 195.23
        pontos = 5
        return "Infração grave", multa, pontos   # retorna string da infração, valor da multa e pontos 
      else: # se a diferença for maior que 50%
        multa = 880.41
        pontos = 7
        return "Infração gravíssima", multa, pontos # retorna string da infração, valor da multa e pontos 
    
def ver_reincidencia(multa, reincidente): # função para verificar se o motorista é reincidente 
      if reincidente == 's': 
        return multa * 2
      else:
         return multa 

def desconto(multa, pagar): # Aplica o desconto 
    if pagar == 's':
      return multa * 0.8  

def principal(): # função feita para armazenar os valores em variaveis 
   print('Sistema de controle de transito')
   placa = input("Informe a placa do veiculo: ").upper()
   nome_motorista = input("Informe o nome do condutor: ").upper()
   vel_registrada = float(input("Informe a velocidade registrada: "))
   vel_permitida = float(input("Informe a velocidade permitida na via: "))
   reincidente = input("O motorista ja foi multado anteriormente? (s/n): ").lower() 
   

   classificacao, multa, pontos = infracao(vel_permitida, vel_registrada) # variavel classificação, multa e ponto recebe a função infração
   ver_multa = ver_reincidencia(multa, reincidente) # a variavel multa recebe a função para verificar reincidente 
   
   print(f'\n Infração: { classificacao }')
   print(f'Multa: { ver_multa }')
   print(f'Pontos: { pontos }')

   if classificacao == 'Infração gravíssima': # se a infração for gravissima o motorista é informado que deve realizar o curso
      print("O condutor deve realizar o curso de reciclagem no Detran.")

   pagar = input("Deseja pagar agora? (s/n): ").lower() 
   valor_final = desconto(multa, pagar)

   if pagar == 's':
      print(f'A multa com desconto ficou no total de { valor_final:.2f}')
   else:
      return "Voce possui uma multa pendente."

print(f'{principal()}')
    



        