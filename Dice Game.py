#Dice Rolling Game

import random
min=1
max=6
again="yes"
while again=="yes" or again=="y":
    print("Dice is rolling..")
    x=random.randint(min,max)
    print(x)
    again="no"
    again=input("play again y/n\n")