
import random

print("===================")
print("Rock Paper Scissors")
print("===================")

print("1. Rock ✊")
print("2. Paper ✋")
print("3. Scissors ✌️")

player = int(input("Choisisez un nombre entre 1 et 3 : "))

if player==1:
  print("Vous avez choisi: ✊")
elif player==2:
  print("Vous avez choisi: ✋")
elif player==3:
  print("Vous avez choisi: ✌️")
else:
  print("Choisissez un nombre entre 1 et 3.")

computer = random.randint(1, 3)

if computer==1:
    print("CPU chose: ✊")
elif computer==2:
    print("CPU chose: ✋")
elif computer==3:
    print("CPU chose: ✌️")
else:
    print("Please pick a number 1-3.")

if player==1 and computer==3:
    print("La pierre bat les ciseaux donc le joueur gagne!")
elif player==3 and computer==1:
    print("Les ciseaux bat la pierre donc l'ordinateur gagne!")
elif player==3 and computer==2:
    print("Les ciseaux bat le papier donc le joueur gagne!")
elif player==2 and computer==3:
    print("Le papier bat les ciseaux donc l'ordinateur gagne!")
elif player==2 and computer==1:
    print("Le papier bat la pierre donc le joueur gagne!")
elif player==1 and computer==2:
    print("La pierre bat le papier donc l'ordinateur gagne!")
elif player==2 and computer==2:
    print("EGALITE!")
elif player==1 and computer==1:
    print("EGALITE!")
elif player==3 and computer==3:
    print("EGALITE!")
else:
    print("Try again.")

