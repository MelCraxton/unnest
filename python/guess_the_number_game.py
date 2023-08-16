
import random

def game():
    computer_guess = random.randint(0,100)
    print(computer_guess)

    level = input('Please select a difficulty level, E for easy, M for medium or H for hard: ')
    lives = 0

    if level.lower() == 'e':
        lives += 10
    elif level.lower() == 'm':
        lives += 8
    else:
        lives += 5

    continue_game = True

    while continue_game and lives > 0:
        human_guess = int(input('What do you think the computer guessed? '))

        if human_guess > computer_guess:        
            lives = lives - 1
            print(f'Too high, you have {lives} lives remaining!')        
        elif human_guess < computer_guess:        
            lives = lives - 1
            print(f'Too low, you have {lives} lives remaining!')
        else:        
            continue_game = False
            print(f'Bang on! You won with {lives} lives remaining!')
    play_again = input('Would you like to play again, if yes type Y else type N: ')
    if play_again.lower() == 'y':
        game()
    else:
        print('Adios amigos')
        
game()