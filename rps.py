import sys
import random
#from colorama import init, Fore, Back, Style

ascii_banner = r"""
     _       _                               _   ____  ____  ____  
    / \   __| |_   ____ _ _ __   ___ ___  __| | |  _ \|  _ \/ ___| 
   / _ \ / _` \ \ / / _` | '_ \ / __/ _ \/ _` | | |_) | |_) \___ \ 
  / ___ \ (_| |\ V / (_| | | | | (_|  __/ (_| | |  _ <|  __/ ___) |
 /_/   \_\__,_| \_/ \__,_|_| |_|\___\___|\__,_| |_| \_\_|   |____/ 
                                                                   

"""

hand_gestures = ['rock', 'paper', 'scissors', 'lizard', 'spock']
winsCounter = 0
roundCounter = 0

print('')
print(ascii_banner)

def get_player_choice():
    global hand_gestures
    global roundCounter
    while True:
        choice = input('What will you pick?\n').lower()
        if choice in hand_gestures:
            roundCounter += 1
            return choice
        else:
             print('Invalid choice. Try again.')    

computerChoice = random.choice(hand_gestures)

print('')
print('You chose: ' + playerChoice)
print('Computer chose: ' + computerChoice)
print('')

if playerChoice.lower() == 'rock'.lower() and computerChoice == 'scissors':
    print('🎉You win!')
    winsCounter += 1
elif playerChoice.lower() == 'paper'.lower() and computerChoice == 'rock':
    print('🎉You win!')
    winsCounter += 1
elif playerChoice.lower() == 'scissors'.lower() and computerChoice == 'paper':
    print('🎉You win!')
    winsCounter += 1
elif playerChoice.lower() == 'lizard'.lower() and computerChoice == 'paper':
    print('🎉You win!')
    winsCounter += 1
elif playerChoice.lower() == 'lizard'.lower() and computerChoice == 'spock':
    print('🎉You win!')
    winsCounter += 1
elif playerChoice.lower() == 'spock'.lower() and computerChoice == 'rock':
    print('🎉You win!')
    winsCounter += 1
elif playerChoice.lower() == 'spock'.lower() and computerChoice == 'scissors':
    print('🎉You win!')
    winsCounter += 1
elif playerChoice.lower() == computerChoice:
    print('It\'s a tie!')
else:
    print('💻 Computer wins!')

while True:
    playerAnswer = input("Try again? (yes/no)\n").lower().strip()
    if playerAnswer == "no".lower() or playerAnswer == "n".lower():
        print("Thanks for playing!")
        print(f"Rounds played: {roundCounter}")
        print(f"Rounds won: {winsCounter}")
        break
    elif playerAnswer == "yes".lower() or playerAnswer == "y".lower():
        break
    else:
        print("Enter only yes or no")        
