 #!/usr/bin/env python3
import random
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

user_cards = []
computer_cards = []

def blackjack_detector_user(user_cards):
    blackjack_detector_user = 0
    for i in user_cards:
        blackjack_detector_user += i
    if blackjack_detector_user == 21:
        return True
    else:
        return "Not detected"
    
def blackjack_detector_computer(computer_cards):
    blackjack_detector_computer = 0
    for i in computer_cards:
        blackjack_detector_computer += i
    if blackjack_detector_computer == 21:
        return True
    else:
        return "Not detected"

def calculator_user(user_cards):
    user_total = 0
    for cards in user_cards:
        user_total += cards
    return user_total

def calculator_computer(computer_cards):
    computer_total = 0
    for cards in computer_cards:
        computer_total += cards
    return computer_total

def ace_checker_user(user_cards):
    for cards in user_cards:
        if cards == 11:
            return cards
        else:
            return "ace not there"

def ace_checker_computer(computer_cards):
    for cards in computer_cards:
        if cards == 11:
            return cards
        else:
            return "ace not there"

def append_user():
    random.shuffle(cards)
    for i in range(0, 1):
        get_cards_for_user = random.choice(cards)
        append_to_list = user_cards.append(get_cards_for_user)

def append_computer():
    random.shuffle(cards)
    for i in range(0, 1):
        get_cards_for_computer = random.choice(cards)
        append_to_computer_list = computer_cards.append(get_cards_for_computer)


random.shuffle(cards)
print(cards)
# shuffled = str(cards)
for i in range(0, 2):
    get_cards_for_user = random.choice(cards)
    append_to_list = user_cards.append(get_cards_for_user)
    get_cards_for_computer = random.choice(cards)
    append_to_computer_list = computer_cards.append(get_cards_for_computer)

print(user_cards)
print(computer_cards)

calculated_user = calculator_user(user_cards)
print(calculated_user)
calculated_computer = calculator_computer(computer_cards)
print(calculated_computer)

blackjack_detected_user = blackjack_detector_user(user_cards)
print(blackjack_detected_user)
blackjack_detected_computer = blackjack_detector_computer(computer_cards)
print(blackjack_detected_computer)

if blackjack_detected_user == True and blackjack_detected_computer == True:
    print("you lose")
elif blackjack_detected_computer == True:
    print("You lose")
elif blackjack_detected_user == True:
    print("you win")

ace_checked_user = ace_checker_user(user_cards)
print(ace_checked_user)
ace_checked_computer = ace_checker_computer(computer_cards)
print(ace_checked_computer)

if calculated_user > 21:
    if ace_checked_user == 11:
        ace_checked_user = 1
    if ace_checked_user == 1 and calculated_user > 21:
        print("you lose")
    else:
        pass 
else:
    print("you lose")

get_another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

if get_another_card == 'y':
    append_user()
    total_user = calculator_user(user_cards)
    print(total_user)
    total_computer = calculator_computer(computer_cards)
    print(total_computer)
elif get_another_card == 'n':
    append_computer()
    total_computer = calculator_computer(computer_cards)
    print(total_computer)

print(user_cards)
print(computer_cards)



























#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

