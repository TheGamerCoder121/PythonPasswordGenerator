"""
Password Generator:
= - - - - - =
1) Import needed libraries and things needed for orginization
2) Create vars.
3) Welcome user to program
4) Have the user type in a phrase 
5) Remove punctuation and invalid characters that might break the program
6) Grades phrase by ammount of characters
7) Create a fancy animation to play
8) Generates password from a dictionary and replaces letters with values from dictionary
9) Joins generated password string from list 
10) Displays password 
"""

#! Python libraries
from pyfiglet import Figlet  # Fancy Text XD
import time  # Python time module
import random
import operator
import sys  # Help with system commands
import os  # Deals with OS related commands ect
from termcolor import colored  # Fancy colored text ;)
from time import sleep
from tqdm import tqdm  # Loading bar :)
from tqdm import trange

# Vars

f = Figlet(font='larry3d')  #! Defines Figlet rendering engine text font

#! Ignore - Misc stuff for future implementation
websites = {
    "name": [
        "Google", "Amazon", 'Snapchat', "Facebook", "LinkedIn",
        "Bank Of America"
    ],
    "year": [1998, 1994, 2011, 2004, 2002, 1998]
}

errorResponces = [
    "HEY! I am not very smart, ok. Tell me something I can understand please ;(",
    "uhhhh, what?", "I dont understand what you mean",
    "Excuse me, but what did you just say?", "What? o.0",
    "Try again, I don't know what you are saying"
]

# Dict. for letters to replace
rep_letters = {
    'a': '@',
    'b': 'B',
    'c': '<',
    'd': 'D',
    'e': '3',
    'f': 'f',
    'g': '&',
    'h': '-',
    'i': '*',
    'j': '}',
    'k': 'k',
    'l': '1',
    'm': '^',
    'n': 'N',
    'o': '0',
    'p': '6',
    'q': '9',
    'r': '4',
    's': 'S',
    't': 't',
    " ": "",
    'u': 'U',
    'v': '|',
    'w': 'W',
    'x': '#',
    'y': 'Y',
    'z': "-",
    '1': 'a',
    '2': 'Z',
    '3': 's',
    '4': 'R',
    '5': 't',
    '6': 'y',
    '7': 'u',
    '8': 'i',
    '9': 'o',
    '0': 'p',
    '/': '\\',
    '\\': '/',
    '-': '_',
    '_': '-',
    '(': ')',
    ')': '(',
    '|': ']',
    '}': '{',
    '{': '}',
}

# punctuation and invalled chars.
punctuation = [
    ".", ",", "?", "\'", "\"", "`", "~", "!", "*", '&', '^', '%', '$', '#',
    '@', ":", ";"
]

# Allows clearing of the teminal / console
clear = lambda: os.system('clear')

#  End of Vars
#! =========== !
# Main program

# Welcome User
print("Welcome to")
welcome = lambda: print(colored(f.renderText('Password Generator'), 'green'))
welcome()
sleep(3)
# ---


def fancyanimation(string):
    # # Plays fancy animation
    """
    Ignore below

    # animation = "|/-\\"

    # print("\nGenerating your password...")

    # for i in range(20):
    #     time.sleep(0.1)
    #     sys.stdout.write("\r" + animation[i % len(animation)])
    #     sys.stdout.flush()
    # clear()
    """
    us = list(string)
    for i in trange(len(us)):
        sleep(0.3)


def cipher_encrypt(plain_text, key):

    encrypted = ""

    for c in plain_text:

        if c.isupper():  #check if it's an uppercase character

            c_index = ord(c) - ord('A')

            # shift the current character by key positions
            c_shifted = (c_index + key) % 26 + ord('A')

            c_new = chr(c_shifted)

            encrypted += c_new

        elif c.islower():  #check if its a lowecase character

            # subtract the unicode of 'a' to get index in [0-25) range
            c_index = ord(c) - ord('a')

            c_shifted = (c_index + key) % 26 + ord('a')

            c_new = chr(c_shifted)

            encrypted += c_new

        elif c.isdigit():

            # if it's a number,shift its actual value
            c_new = (int(c) + key) % 10

            encrypted += str(c_new)

        else:

            # if its neither alphabetical nor a number, just leave it like that
            encrypted += c

    return encrypted


#Random fuction
#Yes, I am too lazy to create a dictionary manually lmao
def createdict():
    n = int(input("enter a n value:"))
    d = {}

    for i in range(n):
        keys = input()  # here i have taken keys as strings
        values = input()  # here i have taken values as integers
        d[keys] = values
    print(d)


def company():
    #Welcomes user to this part of the program and takes a input from user
    print(
        "Hello! Please enter in a company url / name / phrase. If you enter in a url, remember that adding .com or https:// or both will have an effect on how your password is generated!\n"
    )
    userinput = input("> ")

    # Calls the 'cipher_encrypt' function using the users input as the 'plain text' and 3 as the numbers of chars. to shift each value
    companypassword = cipher_encrypt(userinput, 3)

    companypassword = companypassword.replace(" ", "")

    testpass = list(companypassword)

    if testpass[0] != testpass[0].upper():
        testpass[0] = testpass[0].upper()

    listToStr = ' '.join(map(str, testpass))
    listToStr = listToStr.replace(" ", "")
    while len(listToStr) < 8:
        listToStr = listToStr + listToStr

    if listToStr[-4:] == ".com":
        listToStr += "@"
    elif listToStr[0:4] == "http":
        listToStr += "%"
    elif listToStr[0:4] == "http" and listToStr[-4:] == ".com":
        listToStr += "&"
    else:
        listToStr += "*"

    gen_password = colored(listToStr, 'red')

    fancyanimation(listToStr)
    clear()
    # https://google.com becomes Kwwsv://jrrjoh.frp*
    print(
        f'\nYour generated password is {gen_password} \nRun your generated password though howsecureismypassword.net to see how secure your password is!\n\n'
    )
    input("Press enter to continue")


# Asks for input from user and prossess text
def otherPassword():
    print(
        "Please enter in a phrase / company name / company URL. The longer the phrase / company name / company URL the more complex your generated password will be!"
    )
    userinput = input("> ")

    for i in punctuation:
        userinput = userinput.replace(i, "")

    userinput = userinput.lower()
    userinput = list(userinput)

    if len(userinput) < 6:
        print(
            "\nThats a short phrase, try to make it a bit longer so it will be harder for computers to crack!"
        )
        print(
            colored(
                "I have made this program so your password generated will be a minumum of 8 characters.",
                'green'))
    elif len(userinput) < 8:
        print(
            "\nThat is a good phrase, it will get past most password requirements"
        )
    elif len(userinput) >= 8 and len(userinput) < 16:
        print(
            f"\nDang! Thats one long phrase! {len(userinput)} characters long to be exact."
        )
    elif len(userinput) > 8:
        print(
            f"\nOh WOW. Your phrase is {len(userinput)} characters long. I hope that you have a password manager beacuse this is going to be one long and complex password!"
        )

    # ======

    time.sleep(6)

    fancyanimation(''.join(map(str, userinput)))

    # Generates and outputs password
    listindex = 0
    for i in userinput:
        if userinput[listindex] in userinput[listindex]:
            userinput[listindex] = userinput[listindex].replace(
                userinput[listindex], rep_letters[i])
            listindex += 1
        else:
            print()

    clear()

    listToStr = ' '.join(map(str, userinput))
    listToStr = listToStr.replace(" ", "")

    while len(listToStr) < 8:
        listToStr = listToStr + listToStr
        print(listToStr)

    gen_password = colored(listToStr, 'red')

    # https://google.com becomes -tt6S\\&00&13<0^
    print(
        f'\nYour generated password is {gen_password} \nRun your generated password though howsecureismypassword.net to see how secure your password is!\n\n'
    )
    input("Press ENTER to continue")


def demo():
    enter = lambda: input("Press ENTER or RETURN to continue")
    separator = lambda text: print(colored("\n" + text, "white", "on_green"))
    color = lambda text: colored(text, "red")
    enter()
    print(
        "Hello there! Welcome to the demo and explanation of this program!\n ")
    enter()
    separator("Start of program")
    print(
        "\n During the begining of the program, the user is welcomed to the program though the console.\n Behind the scenes,I import internal and external python modules to assist with making this program"
    )
    enter()
    print(
        "\nFirst I import the module, Figlet. Figlet is used for creating the fancy text you see when you are welcomed to the program. Like this:"
    )
    enter()
    print(f.renderText("Hi!"))
    enter()
    print(
        "Next I import python's time module. The Python time module provides many ways of representing time in code, such as objects, numbers, and strings. In my case, I use it to pause and make my program appear smoother and easier to use."
    )
    sleep(10)
    print(
        "Like I just did, I waited 10 seconds then continued to print this message into the console"
    )
    enter()
    print(
        "Now I am not going to explain all of the modules as that would take to long. But some ther modules i used are: sys, os, tqtm and termcolor"
    )
    enter()
    separator("Main program")
    print(
        "\nSo now that all of the modules have imported and variables been declared. Its time for the main chunk of the program!"
    )
    enter()
    print(f"\nFirst, the program runs through a while loop and a function to get user input.\nBased on the user input {color('(either 1, 2, or the easter egg phrase XD)')} it calls the correct function that relates to the users input. ")
    enter()
    print()
    enter()

def firstInput():
    clear()
    print(
        "Would you like to generate a password with a Caesar Cipher (1) or custom dictionary and algorithm (2)\nType exit to exit"
    )

    choice = input("> ")

    return choice


isActive = True

while isActive == True:
    choice = firstInput()
    if choice == "1":
        company()
    elif choice == "2":
        otherPassword()
    elif choice == "red":
        print(colored(f.renderText('RED SUS!!!'), "red"))
        time.sleep(5)
    elif choice.lower == "exit":
        isActive = False
    elif choice.lower() == "demo":
        print(colored("STOP", "red"))
        sleep(2)
        print("Its demo time :)")
        sleep(2)
        demo()
    else:
        print(errorResponces[random.randrange(len(errorResponces))])
        time.sleep(3)
