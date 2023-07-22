import random, os, time

#color codes
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"

#hard: 
#list of words to pick from
hardWords = ["ferocious", "clandestine", "insurmountable", "centerfold", "reveler", "calamitous", "unmoored", "incandescent", "vigilante", "gauche", "glistened", "coax", "illicit", "ricochet", "wisteria", "contrarian", "eulogize", "hindsight", "wonderstruck", "escapism", "pedigree", "marvelous"]

listOfWords = ["peace", "epiphany", "mirrorball", "dynasty", "summer", "emma", "haunted", "american", "castle", "gorgeous", "august", "cardigan", "enchanted", "december", "lavender", "karma", "paris", "snow", "willow", "invisible", "champagne"]

key = """
  ooo,    .---.
 o`  o   /    |\________________
o`   'oooo()  | ________   _   _)
`oo   o` \    |/        | | | |
  `ooo'   `---'         "-" |_|
                                hjw"""


score = ['■ ■ ■ ■ ■ ■','■ ■ ■ ■ ■ □','■ ■ ■ ■ □ □','■ ■ ■ □ □ □','■ ■ □ □ □ □','■ □ □ □ □ □']
failed = "□ □ □ □ □ □"

#ASCII art
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def gameRules():
  SKIP = input("Press enter to continue or S to skip how to play  ").strip().lower()
  if SKIP == "s":
    print()
  else:
    time.sleep(1)
    print(""" 
                   T~~
                   |
                  /"\
          T~~     |'| T~~
      T~~ |    T~ WWWW|
      |  /"\   |  |  |/\T~~
     /"\ WWW  /"\ |' |WW|
    WWWWW/\| /   \|'/\|/"\
    |   /__\/]WWW[\/__\WWWW
    |"  WWWW'|I_I|'WWWW'  |
    |   |' |/  -  \|' |'  |
    |'  |  |LI=H=LI|' |   |
    |   |' | |[_]| |  |'  |
    |   |  |_|###|_|  |   |
    '---'--'-/___\-'--'---'
    """)
    time.sleep(2)
    print()
    print(RED, "\"SOMEBODY HELP!!!!....\"", RESET)
    print("")
    time.sleep(3)
    os.system("clear")
    time.sleep(1)
    print("Once upon a time... Taylor was kidnapped by word thieves.")
    print()
    time.sleep(2)
    print("You are the word police, and only you can save Taylor.")
    time.sleep(2)
    print()
    print("Guess the 4 different rounds of password these evil word thieves used to kidnap Taylor.")
    print()
    print(f"Be careful, you only get {RED}6 wrong guesses per round{RESET}.")
    time.sleep(2)
    print()
    print()
    print(f"{RED}HINT: these are words you can find in Taylor's music. As soon as you know the password, type it out to save Taylor.{RESET}")
    time.sleep(6)
    print()
    print()
    
