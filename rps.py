import sys
import random
#from colorama import init, Fore, Back, Style

@TODO: Add color to the text using colorama
@TODO: Difficulty modes

ascii_banner = r"""
     _       _                               _   ____  ____  ____  
    / \   __| |_   ____ _ _ __   ___ ___  __| | |  _ \|  _ \/ ___| 
   / _ \ / _` \ \ / / _` | '_ \ / __/ _ \/ _` | | |_) | |_) \___ \ 
  / ___ \ (_| |\ V / (_| | | | | (_|  __/ (_| | |  _ <|  __/ ___) |
 /_/   \_\__,_| \_/ \__,_|_| |_|\___\___|\__,_| |_| \_\_|   |____/ 
                                                                   

"""

hand_gestures = []
classic_mode_list = ['rock', 'paper', 'scissors']  
BBT_mode_list = ['rock', 'paper', 'scissors', 'lizard', 'spock']
rps7_mode_list = ['rock', 'paper', 'scissors', 'fire', 'water', 'air', 'sponge']
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
            return choice
        else:
             print('Invalid choice. Try again.')    
             
def select_game_mode():
    global hand_gestures
    global classic_mode_list
    global BBT_mode_list
    global rps7_mode_list
    while True:
        mode =input('Select difficulty: ').lower()
        match mode:
            case 'classic':
                hand_gestures = classic_mode_list
                print('Classic mode selected')
                break
            case 'bigger better than':
                hand_gestures = BBT_mode_list
                print('Bigger Better Than mode selected')
                break
            case 'rps7':
                hand_gestures = rps7_mode_list
                print('RPS7 mode selected')
                break
            case _:
                print('Invalid choice. Try again.')



while True:
    playerChoice = get_player_choice()
    computerChoice = random.choice(hand_gestures)
    roundCounter += 1

    print('')
    print('You chose: ' + playerChoice)
    print('Computer chose: ' + computerChoice)
    print('')
    
    wins = [
        ('rock', 'scissors'),
        ('paper', 'rock'),
        ('scissors', 'paper'),
        ('lizard', 'paper'),
        ('lizard', 'spock'),
        ('spock', 'rock'),
        ('spock', 'scissors'),
    ]

    if (playerChoice, computerChoice) in wins:
        print('🎉 You win!')
        winsCounter += 1
    elif playerChoice == computerChoice:
        print('It\'s a tie!')
    else:
        print('💻 Computer wins!')
        
    select.game.mode()

    while True:
        playerChoice = get_player_choice()
        playerAnswer = input("Try again? (yes/no)\n").lower().strip()
        if playerAnswer in ("no", "n"):
            print("Thanks for playing!")
            print(f"Rounds played: {roundCounter}")
            print(f"Rounds won: {winsCounter}")
            sys.exit()
            break
        elif playerAnswer in ("yes", "y"):
            break
        else:
            print("Enter only yes or no")        
