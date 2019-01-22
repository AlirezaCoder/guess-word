from random import randint
import os


words = ("apple", "orange", "banana", "peach", "zebra", "camel", "rabbit",
         "lion", "sheep", "viper", "table", "pencil", "monitor", "glass")
word = str("")
guessed_letters = []
chance = 10
guessed_letter_count = 0


def get_word():
    word_index = randint(0, len(words)-1)
    return words[word_index]


def get_char_position(_user_input):
    global word
    found_indexes = []
    index = 0
    while index < len(word):
        index = word.find(str(_user_input).lower(), index)
        if index == -1:
            break
        found_indexes.append(index)
        index += 1
    return found_indexes


def check_input(_user_input):
    if not _user_input:
        print("Please Enter A Letter")
        return False
    elif not str(_user_input).isalpha():
        print("Only Letters Are Valid")
        return False
    elif len(str(_user_input)) > 1:
        print("Please Enter Only A Letter")
        return False
    else:
        return True


def print_underline():
    global guessed_letters
    guessed_letters = []
    word_count = len(word)-1
    underline = "_ "
    guessed_letters.append("_")
    while word_count >= 1:
        underline += "_ "
        guessed_letters.append("_")
        word_count -= 1
    print(underline)


def check_renew_game():
    print("Do You Want To Start A New Round Of Game?")
    user_answer = input()
    if user_answer:
        if user_answer.upper() == "Y" or user_answer.upper() == "YES":
            return True
    return False


def print_letters(_indexes, _letter):
    global guessed_letters, guess_count, guessed_letter_count
    index = 0
    while index < len(_indexes):
        if guessed_letters[_indexes[index]] == "_":
            guessed_letters[_indexes[index]] = _letter
            guessed_letter_count += 1
        index += 1
    output = ""
    for i in guessed_letters:
        output += i
        output += " "
    print(output)


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def initiate_game():
    global chance, word, guessed_letter_count
    print("Welcome To Letter Guess Game")
    word = get_word()
    print_underline()
    chance = 10
    guessed_letter_count = 0


initiate_game()
while True:
    print("Please Enter A Letter")
    print("your chance: " + str(chance))
    user_input = input()
    if not check_input(user_input):
        continue
    indexes = get_char_position(user_input)
    if len(indexes) > 0:
        print_letters(indexes, user_input)
        if guessed_letter_count == len(word):
            print("Congratulation! You Won")
            if check_renew_game():
                initiate_game()
            else:
                print("good by.")
                exit()
    else:
        chance -= 1
        if chance == 0:
            print("You Lose!")
            print("The Word Was " + word)
            if check_renew_game():
                initiate_game()
            else:
                print("good by.")
                exit()
        else:
            print_letters(indexes, user_input)
