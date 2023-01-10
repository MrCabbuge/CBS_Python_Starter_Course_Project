import pyjokes
import randfacts
import random
from words import words
import string


# Function for a number guessing game
def number_guesser():
    print('Welcome to the "number guesser!"'.center(50, ' '))
    print('Think of a number between 1 and 10!'.center(50, ' '))
    print('The bot will try to guess the number in the range!'.center(50, ' '))
    low = 1
    high = 10
    user_feedback = ''
    while user_feedback != 'c':
        if low != high:
            computer_guess = random.randint(low, high)
        else:
            computer_guess = low
        user_feedback = input(f'Is {computer_guess} too high (H), too low (L), or correct (C)?? ').lower()
        if user_feedback == 'h':
            high = computer_guess - 1
        elif user_feedback == 'l':
            low = computer_guess + 1
    print(f'Yay! The computer guessed your number, {computer_guess}, correctly!')
    while True:
        print('Would you like another round?')
        user_input = input('Input (y/n): ')
        match user_input:
            case 'y':
                number_guesser()
            case 'n':
                break


# Function for random facts sharing
def random_facts():
    x = randfacts.get_fact()
    print(x)
    while True:
        print('Would you like another interesting fact?')
        user_input = input('Input (y/n): ')
        match user_input:
            case 'y':
                x = randfacts.get_fact()
                print(x)
            case 'n':
                break


# Function Hangman game
def hangman():
    def get_valid_word(words):
        chosen_word = random.choice(words)  # randomly chooses something from the list
        while '-' in chosen_word or ' ' in chosen_word:
            chosen_word = random.choice(words)
        return chosen_word.upper()

    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed
    lives = 7
    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')
        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')
        else:
            print('\nThat is not a valid letter.')
    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')
    while True:
        print('Would you like another round?')
        user_input = input('Input (y/n): ')
        match user_input:
            case 'y':
                hangman()
            case 'n':
                break


# Function for recommending music
def music_choice():
    heavy_metal = ['Metallica - Enter Sandman', 'Asking Alexandria - Inside the fire', 'Slipknot - Duality']
    hip_hop = ['Lady Gaga - Poker Face', 'Nicki Minaj - Anaconda', 'Dax - JOKER']
    rock = ['Rise Against - Make it stop', 'Hot Water Music - Drag my body', 'Godsmack - Good day to die']
    print('Recommending some music. Pick a genre:')
    print('\n\t1. Heavy Metal\n\t2. Hip-Hop\n\t3. Rock')
    movie_rec = input('Your choice: ')
    match movie_rec:
        case '1':
            print(random.choice(heavy_metal))
        case '2':
            print(random.choice(hip_hop))
        case '3':
            print(random.choice(rock))


# Function for recommending movies
def movie_choice():
    comedy = ['The Big Lebowski', 'Superbad', 'Zoolander']
    horror = ['The conjuring', 'Paranormal Activity', 'Hellraiser']
    adventures = ['The Lord of the Rings', 'Matrix', 'Avatar']
    print('Recommending a movie. Pick a genre:')
    print('\n\t1. Comedy\n\t2. Horror\n\t3. Adventures')
    movie_rec = input('Your choice: ')
    match movie_rec:
        case '1':
            print(random.choice(comedy))
        case '2':
            print(random.choice(horror))
        case '3':
            print(random.choice(adventures))


# Function for recommending games
def game_choice():
    shooters = ['Halo', 'Battlefield 1', 'DOOM']
    sandbox = ['Minecraft', 'Project Zomboid', 'Rimworld']
    strategy = ['Stellaris', 'Age of Empires', 'Civilization VI']
    print('Recommending some PC games. Pick a genre:')
    print('\n\t1. Shooters\n\t2. Sandbox\n\t3. Strategy')
    game_rec = input('Your choice: ')
    match game_rec:
        case '1':
            print(random.choice(shooters))
        case '2':
            print(random.choice(sandbox))
        case '3':
            print(random.choice(strategy))


# Function for palying games
def user_games():
    print('Pick a game of your liking:')
    print('\n\t1. Computer\'s guessing numbers\n\t2. Hangman')
    user_game_rec = input('Your choice: ')
    match user_game_rec:
        case '1':
            number_guesser()
        case '2':
            hangman()


# Function for jokes and facts sharing
def extra():
    print('Pick a game of your liking:')
    print('\n\t1. Get a joke\n\t2. Get a random fact')
    extra_rec = input('Your choice: ')
    match extra_rec:
        case '1':
            print(pyjokes.get_joke())
            while True:
                print('Would you like another joke?')
                user_input = input('Input (y/n): ')
                match user_input:
                    case 'y':
                        print(pyjokes.get_joke())
                    case 'n':
                        break
        case '2':
            random_facts()


# Function for main menu integration
def main_menu():
    while True:
        print('Welcome my simple chat-bot!'.center(50, '*'))
        print('Select one of available options: '.center(50, ' '))
        print('\n1. Recommend a movie\n2. Recommend some music\n3. '
              'Recommend PC game\n4. Play a game\n5. Extra')
        user_choice = input('Your choice: ')
        match user_choice:
            case "1":
                movie_choice()
            case "2":
                music_choice()
            case "3":
                game_choice()
            case "4":
                user_games()
            case "5":
                extra()
            case _:
                print('Invalid choice, try again')
        new_calc = input('Type Enter to continue. Type Off to exit ')
        if new_calc == 'Off':
            break


def main():
    main_menu()


if __name__ == '__main__':
    main()
