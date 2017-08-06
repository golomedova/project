import random
from copy import deepcopy
from collections import defaultdict

#invalid chars
invChrs = 'ьъы'

# returns last valid char from input string
def GetLastChr(inputStr):
    i = 1
    while inputStr[-i] in invChrs and i < inputStr.__len__():
        i = i + 1
    lastChr = inputStr[-i]
    if lastChr in invChrs:
        lastChr = None
    return lastChr


# returns first char for non-empty string
def GetFirstChr(inputstr):
    if inputstr.__len__() != 0:
        firstchr = inputstr[0]
    else:
        firstchr = ""
    return firstchr

# importing txt file and making a dictionary
with open('wg.txt') as slova:
    words = defaultdict(list)
    lines = [line.strip() for line in slova]
    for word in lines:
        words[word[0]].append(word)
    print("words in dict \n")

# try count
count = 0

# copy of a dictionary
wordsСopy = deepcopy(words)

# bot new turn
def BotTurn(player_word):
    first_char = GetFirstChr(player_word)
    if player_word in wordsСopy[first_char]:
        del wordsСopy[first_char][wordsСopy[first_char].index(player_word)]

    first_bot_letter = GetLastChr(player_word)
    print("So, my first letter is: ", first_bot_letter)
    available_words_count = len(wordsСopy[first_bot_letter])
    if available_words_count == 0:
        return "Error"
    bot_choice_index = random.randrange(0, available_words_count)
    available_words = wordsСopy[first_bot_letter]
    bot_choice = available_words[bot_choice_index]

    del wordsСopy[first_bot_letter][bot_choice_index]
    print("My new word is: ", bot_choice)
    print("Your first letter is: ", GetLastChr(bot_choice))
    return GetLastChr(bot_choice)

firstTurn = True

# player's turn
def PlayerTurn(required_first_char):
    global firstTurn
    while True:
        print("Print a word: ")
        player_word = str(input()).lower()
        if firstTurn:
            required_first_char =  GetFirstChr(player_word)
        if ((player_word in wordsСopy[required_first_char]) or player_word == "stop"):
            break
        else:
            print("Invalid first char or already used word, try another word: ")
    firstTurn = False
    return player_word

first_required_char = ""
print("Welcome here! To stop print \"stop\". Enjoy this game!")
while True:
    new_player_word = PlayerTurn(first_required_char)
    count+=1
    if (new_player_word != "stop"):
        first_required_char = BotTurn(new_player_word)
        if first_required_char == "Error":
            print("You're winner! Your result is ", count, " words!")
            break
    else:
        print("You're looser! Your result is ", count, " words!")
        break