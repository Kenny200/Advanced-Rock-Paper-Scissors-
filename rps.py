import sys
import random
#from colorama import init, Fore, Back, Style

'''
Todo:
Add color to the banner using colorama
Look for beter data structure for win conditions
'''


ascii_banner = r"""
     _       _                               _   ____  ____  ____  
    / \   __| |_   ____ _ _ __   ___ ___  __| | |  _ \|  _ \/ ___| 
   / _ \ / _` \ \ / / _` | '_ \ / __/ _ \/ _` | | |_) | |_) \___ \ 
  / ___ \ (_| |\ V / (_| | | | | (_|  __/ (_| | |  _ <|  __/ ___) |
 /_/   \_\__,_| \_/ \__,_|_| |_|\___\___|\__,_| |_| \_\_|   |____/ 
                                                                   

"""

hand_gestures = []
classic_mode = ['rock', 'paper', 'scissors']
RPSSL_mode = classic_mode + ['lizard', 'spock']
rps7_mode = classic_mode + ['fire', 'water', 'air', 'sponge']
rps9_mode = rps7_mode + ['gun', 'human']
rps11_mode = rps9_mode + ['devil', 'wolf']
winsCounter = 0
roundCounter = 0
tieCounter = 0

print('')
print(ascii_banner)   
             
def select_game_mode():
    global hand_gestures
    global classic_mode_set
    global BBT_mode_set
    global rps7_mode_set
    while True:
        mode = input('Select mode: ').lower()
        match mode.lower():
            case 'classic':
                hand_gestures = classic_mode
                print('Classic mode selected')
                break
            case 'rpssl':
                hand_gestures = RPSSL_mode
                print('RPSSL mode selected')
                break
            case 'rps7':
                hand_gestures = rps7_mode
                print('RPS7 mode selected')
                break
            case 'rps9':
                hand_gestures = rps9_mode
                print('RPS9 mode selected')
                break
            case 'rps11':
                hand_gestures = rps11_mode
                print('RPS11 mode selected')
                break
            case _:
                print('Invalid choice. Try again.')
                
def get_player_choice():
    hand_gestures
    global roundCounter
    while True:
        choice = input('What will you pick?\n').lower()
        if choice in hand_gestures:
            return choice
        else:
             print('Invalid choice. Try again.') 

while True:
    setgamemode = select_game_mode()
    playerChoice = get_player_choice()
    computerChoice = random.choice(hand_gestures)
    roundCounter += 1

    print('')
    print('You chose: ' + playerChoice)
    print('Computer chose: ' + computerChoice)
    print('')
    
    wins = [
        #classic
        ('rock', 'scissors'),
        ('paper', 'rock'),
        ('scissors', 'paper'),
        #Spock Lizard verison
        ('lizard', 'paper'),
        ('lizard', 'spock'),
        ('spock', 'rock'),
        ('spock', 'scissors'),
        #rps7
        ('rock', 'fire'),
        ('rock', 'sponge'),
        ('fire', 'scissors'),
        ('fire', 'paper'),
        ('fire', 'sponge'),
        ('scissors', 'air'),
        ('scissors', 'sponge'),
        ('sponge', 'paper'),
        ('sponge', 'air'),
        ('sponge', 'water'),
        ('paper', 'air'),
        ('paper', 'water'),
        ('air', 'fire'),
        ('air', 'rock'),
        ('air', 'water'),
        ('water', 'rock'),
        ('water', 'fire'),
        ('water', 'scissors'),
        #rps9
        ('rock', 'human'),
        ('fire', 'human'),
        ('scissors', 'human'),
        ('human', 'sponge'),
        ('human', 'paper'),
        ('human', 'air'),
        ('human', 'water'),
        ('sponge', 'gun'),
        ('paper', 'gun'),
        ('air', 'gun'),
        ('water', 'gun'),
        ('gun', 'rock'),
        ('gun', 'fire'),
        ('gun', 'scissors'),
        ('gun', 'human'),
        # RPS11 additions
        ('wolf', 'sponge'),
        ('wolf', 'paper'),
        ('wolf', 'air'),
        ('wolf', 'water'),
        ('wolf', 'devil'),
        ('rock', 'wolf'),
        ('fire', 'wolf'),
        ('scissors', 'wolf'),
        ('human', 'wolf'),
        ('gun', 'wolf'),
        ('devil', 'rock'),
        ('devil', 'fire'),
        ('devil', 'scissors'),
        ('devil', 'gun'),
        ('devil', 'human'),
        ('paper', 'devil'),
        ('air', 'devil'),
        ('water', 'devil'),
        ('sponge', 'devil')
        
    ]

    if (playerChoice, computerChoice) in wins:
        print('🎉 You win!')
        winsCounter += 1
    elif playerChoice == computerChoice:
        tieCounter += 1
        print('It\'s a tie!')
    else:
        print('💻 Computer wins!')
        
    playerAnswer = input("Try again? (yes/no)\n").lower().strip()
    
    if playerAnswer in ("no", "n"):
        print("Thanks for playing!")
        print(f"Rounds played: {roundCounter}")
        print(f"Rounds won: {winsCounter}")
        print(f"Rounds ties: {tieCounter}")
        sys.exit()
        break
    elif playerAnswer in ("yes", "y"):
        pass
    else:
        print("Enter only yes or no") 
