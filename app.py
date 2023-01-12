import random;

choices = ["pedra","papel","tesoura"]

def computerChoice():
   computerChoiceReturn = random.choice(choices)
   return computerChoiceReturn

def selectChoice(str):
     playerChoice = choices[str]
     return playerChoice;
     
def play():
     selected = input("Faça sua escolha [1 para pedra] - [2 para papel] - [3 para tesoura]: ")
     toInt = int(selected)
     normalize = toInt-1

     move = selectChoice(normalize);
     cpu = computerChoice();
     print("Escolha do jogador: " + move+" "+" Escolha do computador: "+cpu)

     if move == "pedra" and cpu == "tesoura":
          print("você ganhou!")
     elif move == "papel" and cpu == "pedra":
          print("você ganhou!")
     elif move == "teroura" and cpu =="papel":
          print("você ganhou!")
     elif move == cpu:
          print("O jogo empatou!")    
     else:
          print("Voce perdeu!")
play();