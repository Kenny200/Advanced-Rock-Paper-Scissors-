import sys
import random
#from colorama import init, Fore, Back, Style

hand_gestures = ['rock', 'paper', 'scissors', 'lizard', 'spock']

ascii_banner = r"""
     _       _                               _   ____  ____  ____  
    / \   __| |_   ____ _ _ __   ___ ___  __| | |  _ \|  _ \/ ___| 
   / _ \ / _` \ \ / / _` | '_ \ / __/ _ \/ _` | | |_) | |_) \___ \ 
  / ___ \ (_| |\ V / (_| | | | | (_|  __/ (_| | |  _ <|  __/ ___) |
 /_/   \_\__,_| \_/ \__,_|_| |_|\___\___|\__,_| |_| \_\_|   |____/ 
                                                                   

"""
print('')
print(ascii_banner)



"""
--------------------------------------------------------------------------
This code was AI-generated on 2026-03-22
Claude link: https://claude.ai/share/6468d72f-5933-4119-aad9-c6c4b570ed23
---------------------------------------------------------------------------
"""
while True:
    playerChoice = input('Rock, Paper, or Scissors?\n').lower()
    if playerChoice in (hand_gestures):
        break
    else:
        print('Invalid choice. Try again.')

computerChoice = random.choice(hand_gestures)

'''
if playerChoice.lower() != 'rock' and playerChoice.lower() != 'paper' and playerChoice.lower() != 'scissors' and playerChoice.lower() != 'lizard' and playerChoice.lower() != 'spock':
    print('Invalid choice. Try again.')
    sys.exit()
'''

print('')
print('You chose: ' + playerChoice)
print('Computer chose: ' + computerChoice)
print('')

if playerChoice.lower() == 'rock'.lower() and computerChoice == 'scissors':
    print('🎉You win!')
elif playerChoice.lower() == 'paper'.lower() and computerChoice == 'rock':
    print('🎉You win!')
elif playerChoice.lower() == 'scissors'.lower() and computerChoice == 'paper':
    print('🎉You win!')
elif playerChoice.lower() == 'lizard'.lower() and computerChoice == 'paper':
    print('🎉You win!')
elif playerChoice.lower() == 'lizard'.lower() and computerChoice == 'spock':
    print('🎉You win!')
elif playerChoice.lower() == 'spock'.lower() and computerChoice == 'rock':
    print('🎉You win!')
elif playerChoice.lower() == 'spock'.lower() and computerChoice == 'scissors':
    print('🎉You win!')
elif playerChoice.lower() == computerChoice:
    print('It\'s a tie!')
else:
    print('💻 Computer wins!')
