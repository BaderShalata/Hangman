# from Bio import SeqIO
#
# # Specify the path to your FASTQ file
# file_path = '/Users/badershalata/Downloads/1_control_18S_2019_minq7 - Copy.fastq'
#
# # Open the file and read the sequences
# sequences = SeqIO.parse(file_path, 'fastq')
#
# # Iterate over the sequences and print each record
# for record in sequences:
#     print("Sequence ID:", record.id)
#     print("Sequence:", record.seq)
#     print()
# x = 'str'
# y = x
# y += '5'
# print(y)
# print(x)
# l1 = [1,2,3,4]
# l1[0] = 'C'
# print(f"String: L1 List: {l1}")
#

# def guess(x):
#     random_Num = random.randint(1, x)
#     guess = 0
#     while guess != random_Num:
#         guess = (int(input(f"Guess a number between 1 and {x}")))
#         if guess < random_Num:
#             print("Try again, HINT: Your guess was LOWER than X")
#         elif guess > random_Num:
#             print("Try Again, HINT: Your guess was HIGHER than X")
#         else:
#             print(f"CONGRATS! X was {random_Num}")
#
# #
# def computerGuess(x):
#     low = 1
#     high = x
#     feedback = ""
#     while feedback != 'c':
#         guess = random.randint(low, high)
#         print(guess)
#         feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?").lower()
#         if feedback == "h":
#             high = guess - 1
#         elif feedback == "l":
#             low = guess + 1
#     print("GOOD JOB YOU GUESSED THE NUMBER")
#
#
# def rps():
#     beats = {
#         "rock": "scissors",
#         "scissors": "paper",
#         "paper": "rock"
#     }
#     compTurn = random.choice(['rock', 'paper', 'scissors'])
#     playerTurn = input("Your turn: ")
#     if beats[compTurn] == playerTurn:
#         print("COMPUTER WINS!")
#     elif beats[playerTurn] == compTurn:
#         print("PLAYER WINS!!")
#     else:
#         print("DRAW")
import random
from Transposing import wording
word_list = ["words"]
def words():
    lives = 5
    word = random.choice(wording)
    display = []
    for letter in range(0, len(word)):
        display += "_"
    print(display)
    while lives>=1:
        print(word)
        guess = input("GUESS A LETTER: ")
        for index,letter in enumerate(word):
            if guess == letter:
                display[index] = guess
        if len(guess) > 1 or len(guess) == 0:
            print("Invalid input")
        if guess not in word:
         lives = lives-1
        print(display)
        if "_" not in display:
            print("Good job!")
            break
    else:
        print("YOU SUCK!")
words()