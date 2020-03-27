# Simple Morse code encode and decoding
# Based on info found on Geeks for Geeks
# DVG : 03/03/2020
# This program requiires the following files :
#   di.mp3
#   da.mp3
#   nos.mp3

import subprocess
from time import sleep

# Dictionary representing the morse coded chart
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


# Compose a morse sequence
def encrypt(message):
    cipher = ' '
    for letter in message:
        if letter != ' ':
            try:
              cipher += MORSE_CODE_DICT[letter] + ' '
            except:
              cipher +="E"
        else:
            # One space indicates new letter, two means new word
            cipher += ' '
    return cipher


def tone(message, speed = 0.05):
    for morse in message:
        if morse == '.':
            subprocess.call(["mpg123", "-q", "di.mp3"])
        elif morse == '-':
            subprocess.call(["mpg123", "-q", "da.mp3"])
        elif morse == ' ':
            subprocess.call(["mpg123", "-q", "nos.mp3"])

        sleep(speed)


def main():
    # while True:
    message = input("What should I convert? : ")
    result = encrypt(message.upper())
    print(result)
    tone(result)


if __name__ == '__main__':
    main()
