import random

fichas = 10;

while 1:
  print('Número de fichas:', fichas)
  if fichas == 0:
    print('Suas fichas acabaram.\nGAME OVER!')
    break
  cartas = ['A♤','2♤','3♤','4♤','5♤','6♤','7♤','8♤','9♤','10♤','J♤','Q♤','K♤','A♧','2♧','3♧','4♧','5♧','6♧','7♧','8♧','9♧','10♧','J♧','Q♧','K♧','A♥','2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','10♥','J♥','Q♥','K♥','A♢','2♢','3♢','4♢','5♢','6♢','7♢','8♢','9♢','10♢','J♢','Q♢','K♢']
  pontos = 0
  Hpontos = 0
  aposta = int(input('Valor da aposta: '))
  if aposta > fichas:
    print('Você não possui essa quantidade de fichas para apostar!')
    continue
  carta1 = random.choice(cartas)
  cartas.remove(carta1)
  carta2 = random.choice(cartas)
  cartas.remove(carta2)

  print(carta1 , carta2)

  if carta1[:-1] == 'A':
    if carta2[:-1] == '10' or carta2[:-1] == 'J' or carta2[:-1] == 'Q' or carta2[:-1] == 'K':
      pontos += 11
    else: pontos += 1
    
  elif carta1[:-1] == '2':
    pontos += 2
  elif carta1[:-1] == '3':
    pontos += 3
  elif carta1[:-1] == '4':
    pontos += 4
  elif carta1[:-1] == '5':
    pontos += 5
  elif carta1[:-1] == '6':
    pontos += 6
  elif carta1[:-1] == '7':
    pontos += 7
  elif carta1[:-1] == '8':
    pontos += 8
  elif carta1[:-1] == '9':
    pontos += 9
  elif carta1[:-1] == '10' or 'J' or 'Q' or 'K':
    pontos += 10

  if carta2[:-1] == 'A':
    if carta1[:-1] == '10' or carta1[:-1] == 'J' or carta1[:-1] == 'Q' or carta1[:-1] == 'K':
      pontos += 11
    else: pontos += 1
    
  elif carta2[:-1] == '2':
    pontos += 2
  elif carta2[:-1] == '3':
    pontos += 3
  elif carta2[:-1] == '4':
    pontos += 4
  elif carta2[:-1] == '5':
    pontos += 5
  elif carta2[:-1] == '6':
    pontos += 6
  elif carta2[:-1] == '7':
    pontos += 7
  elif carta2[:-1] == '8':
    pontos += 8
  elif carta2[:-1] == '9':
    pontos += 9
  elif carta2[:-1] == '10' or 'J' or 'Q' or 'K':
    pontos += 10

  print('sua pontuação :' , pontos)
  if pontos == 21:
    fichas += aposta
    print("BLACK JACK!!!\nVocê ganhou a rodada!")
    continue

  
  print("1 - Stand(parar)\n2 - Hit(pegar mais uma carta)\n3 - Surrender(rendição)")
  x = int(input("Qual jogada você deseja fazer?"))

  if(x == 1):
    Hcarta1 = random.choice(cartas)
    cartas.remove(Hcarta1)
    Hcarta2 = random.choice(cartas)
    cartas.remove(Hcarta2)

    print(Hcarta1 , Hcarta2)

    if Hcarta1[:-1] == 'A':
      if Hcarta2[:-1] == '10' or Hcarta2[:-1] == 'J' or Hcarta2[:-1] == 'Q' or Hcarta2[:-1] == 'K':
        Hpontos += 11
      else: Hpontos += 1
    
    elif Hcarta1[:-1] == '2':
      Hpontos += 2
    elif Hcarta1[:-1] == '3':
      Hpontos += 3
    elif Hcarta1[:-1] == '4':
      Hpontos += 4
    elif Hcarta1[:-1] == '5':
      Hpontos += 5
    elif Hcarta1[:-1] == '6':
      Hpontos += 6
    elif Hcarta1[:-1] == '7':
      Hpontos += 7
    elif Hcarta1[:-1] == '8':
      Hpontos += 8
    elif Hcarta1[:-1] == '9':
      Hpontos += 9
    elif Hcarta1[:-1] == '10' or 'J' or 'Q' or 'K':
      Hpontos += 10

    if Hcarta2[:-1] == 'A':
      if Hcarta1[:-1] == '10' or Hcarta1[:-1] == 'J' or Hcarta1[:-1] == 'Q' or Hcarta1[:-1] == 'K':
        Hpontos += 11
      else: Hpontos += 1
    
    elif Hcarta2[:-1] == '2':
      Hpontos += 2
    elif Hcarta2[:-1] == '3':
      Hpontos += 3
    elif Hcarta2[:-1] == '4':
      Hpontos += 4
    elif Hcarta2[:-1] == '5':
      Hpontos += 5
    elif Hcarta2[:-1] == '6':
      Hpontos += 6
    elif Hcarta2[:-1] == '7':
      Hpontos += 7
    elif Hcarta2[:-1] == '8':
      Hpontos += 8
    elif Hcarta2[:-1] == '9':
      Hpontos += 9
    elif Hcarta2[:-1] == '10' or 'J' or 'Q' or 'K':
      Hpontos += 10

    print('pontuação da casa :' , Hpontos)

    if Hpontos < pontos:
      Hcarta3 = random.choice(cartas)
      cartas.remove(Hcarta3)

      print(Hcarta1 , Hcarta2, Hcarta3)

      if Hcarta3[:-1] == 'A':
        if Hpontos >= 12:
          Hpontos += 10
      elif Hcarta3[:-1] == '2':
        Hpontos += 2
      elif Hcarta3[:-1] == '3':
        Hpontos += 3
      elif Hcarta3[:-1] == '4':
        Hpontos += 4
      elif Hcarta3[:-1] == '5':
        Hpontos += 5
      elif Hcarta3[:-1] == '6':
        Hpontos += 6
      elif Hcarta3[:-1] == '7':
        Hpontos += 7
      elif Hcarta3[:-1] == '8':
        Hpontos += 8
      elif Hcarta3[:-1] == '9':
        Hpontos += 9
      elif Hcarta3[:-1] == '10' or 'J' or 'Q' or 'K':
        if Hcarta1[:-1] == 'A' or Hcarta2[:-1] == 'A':
          Hpontos += 20
        elif Hcarta1[:-1] == 'A' and Hcarta2[:-1] == 'A':
          Hpontos += 30
        else:
          Hpontos += 10

      print('Pontuação da casa:' , Hpontos)

    

      if Hpontos > 21:
        print("A casa excedeu o limite de pontos")
        fichas += aposta
        continue

  elif(x == 3):
    if aposta % 2 != 0:
      aposta += 1
    fichas -= aposta/2
    print("Rodada abandonada!")
    continue

  elif(x == 2): 
    carta3 = random.choice(cartas)
    cartas.remove(carta3)

    print(carta1 , carta2, carta3)

    if carta3[:-1] == 'A':
      if pontos >= 12:
        pontos += 11
      
      else: pontos += 1
    
    elif carta3[:-1] == '2':
      pontos += 2
    elif carta3[:-1] == '3':
      pontos += 3
    elif carta3[:-1] == '4':
      pontos += 4
    elif carta3[:-1] == '5':
      pontos += 5
    elif carta3[:-1] == '6':
      pontos += 6
    elif carta3[:-1] == '7':
      pontos += 7
    elif carta3[:-1] == '8':
      pontos += 8
    elif carta3[:-1] == '9':
      pontos += 9
    elif carta3[:-1] == '10' or 'J' or 'Q' or 'K':
      if carta1[:-1] == 'A' or carta2[:-1] == 'A':
        pontos += 20
      elif carta1[:-1] == 'A' and carta2[:-1] == 'A':
        pontos += 30
      else:
        pontos += 10

    print('sua pontuação :' , pontos)

    if pontos == 21:
     fichas += aposta
     print("BLACK JACK!!!\nVocê ganhou a rodada!")
     continue

    elif pontos > 21:
      print("Você excedeu o limite de pontos")
      fichas -= aposta
      continue

    Hcarta1 = random.choice(cartas)
    cartas.remove(Hcarta1)
    Hcarta2 = random.choice(cartas)
    cartas.remove(Hcarta2)

    print(Hcarta1 , Hcarta2)

    if Hcarta1[:-1] == 'A':
      if Hcarta2[:-1] == '10' or Hcarta2[:-1] == 'J' or Hcarta2[:-1] == 'Q' or Hcarta2[:-1] == 'K':
        Hpontos += 11
      else: Hpontos += 1
    
    elif Hcarta1[:-1] == '2':
      Hpontos += 2
    elif Hcarta1[:-1] == '3':
      Hpontos += 3
    elif Hcarta1[:-1] == '4':
      Hpontos += 4
    elif Hcarta1[:-1] == '5':
      Hpontos += 5
    elif Hcarta1[:-1] == '6':
      Hpontos += 6
    elif Hcarta1[:-1] == '7':
      Hpontos += 7
    elif Hcarta1[:-1] == '8':
      Hpontos += 8
    elif Hcarta1[:-1] == '9':
      Hpontos += 9
    elif Hcarta1[:-1] == '10' or Hcarta1[:-1] == 'J' or Hcarta1[:-1] == 'Q' or Hcarta1[:-1] == 'K':
      Hpontos += 10

    if Hcarta2[:-1] == 'A':
      if Hcarta1[:-1] == '10' or Hcarta1[:-1] == 'J' or Hcarta1[:-1] == 'Q' or Hcarta1[:-1] == 'K':
        Hpontos += 11
      else: Hpontos += 1
    
    elif Hcarta2[:-1] == '2':
      Hpontos += 2
    elif Hcarta2[:-1] == '3':
      Hpontos += 3
    elif Hcarta2[:-1] == '4':
      Hpontos += 4
    elif Hcarta2[:-1] == '5':
      Hpontos += 5
    elif Hcarta2[:-1] == '6':
      Hpontos += 6
    elif Hcarta2[:-1] == '7':
      Hpontos += 7
    elif Hcarta2[:-1] == '8':
      Hpontos += 8
    elif Hcarta2[:-1] == '9':
      Hpontos += 9
    elif Hcarta2[:-1] == '10' or Hcarta2[:-1] ==  'J' or Hcarta2[:-1] == 'Q' or Hcarta2[:-1] == 'K':
      Hpontos += 10

    print('pontuação da casa :' , Hpontos)

    if Hpontos < pontos:
      Hcarta3 = random.choice(cartas)
      cartas.remove(Hcarta3)

      print(Hcarta1 , Hcarta2, Hcarta3)

      if Hcarta3[:-1] == 'A':
        if Hpontos >= 12:
          Hpontos += 11
      elif Hcarta3[:-1] == '2':
        Hpontos += 2
      elif Hcarta3[:-1] == '3':
        Hpontos += 3
      elif Hcarta3[:-1] == '4':
        Hpontos += 4
      elif Hcarta3[:-1] == '5':
        Hpontos += 5
      elif Hcarta3[:-1] == '6':
        Hpontos += 6
      elif Hcarta3[:-1] == '7':
        Hpontos += 7
      elif Hcarta3[:-1] == '8':
        Hpontos += 8
      elif Hcarta3[:-1] == '9':
        Hpontos += 9
      elif Hcarta3[:-1] == '10' or 'J' or 'Q' or 'K':
        if Hcarta1[:-1] == 'A' or Hcarta2[:-1] == 'A':
          Hpontos += 20
        elif Hcarta1[:-1] == 'A' and Hcarta2[:-1] == 'A':
          Hpontos += 30
        else:
          Hpontos += 10

      print('Pontuação da casa:' , Hpontos)

    

      if Hpontos > 21:
        print("A casa excedeu o limite de pontos")
        fichas += aposta
        continue
      
  
  if pontos > Hpontos:
    fichas += aposta
    print("Você ganhou a rodada!")

  elif pontos < Hpontos:
    fichas -= aposta
    print("Você perdeu a rodada!")
  else: print("Rodada empatada!")
    
    