#!/usr/bin/env python3

import random

#user chooses
user_choose = int(input("What do you choose? Type 0 for Rock, 1 for Papper or 2 for Scissors: \n"))
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
PRS_list = [rock, paper, scissors]
if user_choose == 0:
   print(PRS_list[0])
elif user_choose == 1:
   print(PRS_list[1])
elif user_choose == 2:
   print(PRS_list[2])
else:
    print("out of range")

print("Computer chose:")

#computer chooses
ran = random.randint(0, len(PRS_list) - 1)
computer_choose = ran
if computer_choose == 0:
   print(PRS_list[0])
elif computer_choose == 1:
   print(PRS_list[1])
elif computer_choose == 2:
   print(PRS_list[2])
else:
    print("out of range")

if user_choose >= 3 or user_choose < 0:
    print("you typed an invalid number you lose!!")
elif user_choose == 0 and computer_choose == 2:
    print("you win")
elif computer_choose == 0 and user_choose == 2:
    print("you lose")
elif computer_choose > user_choose:
    print("you lose")
elif user_choose > computer_choose:
    print("you win")
elif user_choose == computer_choose:
    print("its a draw")
else:
    print("out of range")