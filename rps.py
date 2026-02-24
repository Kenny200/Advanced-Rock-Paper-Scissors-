import sys
import random


print('')
playerChoice = input('Rock, Paper, or Scissors?\n')
computerChoice = random.choice(['rock', 'paper', 'scissors'])

if playerChoice.lower() != 'rock' and playerChoice.lower() != 'paper' and playerChoice.lower() != 'scissors':
    print('Invalid choice. Please choose Rock, Paper, or Scissors.')
    sys.exit()

print('')
print('You chose: ' + playerChoice)
print('Computer chose: ' + computerChoice)
print('')

if playerChoice.lower() == 'rock' and computerChoice == 'scissors':
    print('🎉You win!')
elif playerChoice.lower() == 'paper' and computerChoice == 'rock':
    print('🎉You win!')
elif playerChoice.lower() == 'scissors' and computerChoice == 'paper':
    print('🎉You win!')
elif playerChoice.lower() == computerChoice:
    print('It\'s a tie!')
else:
    print('💻 Computer wins!')

