import random, os, time, modules

#game title
time.sleep(1)
print("====== SAVE TAYLOR! ======")
print()
USERNAME = input("What's your name?  ").upper()
print()
modules.gameRules()
print(f"Lets hope Taylor is saved by you, {USERNAME}!")
time.sleep(2)
os.system("clear")

#show users what they guessed
def displayGuess():
  print()
  if guessList != []:
    print(f"You guessed: {guessList}")
  else:
    print()

round = 0  
previousWords = []
userScore = []
failed = "□ □ □ □ □ □"

#pick level
level = input("Pick your level: \nNormal or extra hard? :").strip().lower()
if level == "normal":
  level = modules.listOfWords
else:
  level = modules.hardWords

#=========== game begins here ============
while True:
  #generate word, guess list and lives
  myWord = random.choice(level)
  guessList = []
  dead = 0
  round +=1
  if round == 1:
    print()
  else:
    print(f"Round {round} of 4 ~~~~~~~~~~~~~~~~~~~~~~~")
  #------------- rounds begins here -------------
  while True:
    displayGuess()
    print()
    print()
    #user input
    userGuess = input("Guess a letter \nor the full password:  ").lower()
    print()
    if userGuess in guessList:
      print(f"you already guessed {modules.RED}{userGuess}{modules.RESET}!")
      time.sleep(1.5)
      os.system("clear")
      print()
      continue
    elif userGuess == " ":
      os.system("clear")
      continue
  
    else:
      guessList.append(userGuess)
  
    #------ processing user input
    #user guesses word
    if userGuess.lower() == myWord:
      previousWords.append(myWord)
      modules.listOfWords.remove(myWord)
      time.sleep(1)
      print(f"{modules.GREEN}{USERNAME}, one more password unlocked, amazing job.{modules.RESET}")
      print("")
      time.sleep(1)
      print("===================")
      print("Your Taylor Score:")
      time.sleep(1)
      roundScore = modules.score[dead]
      userScore.append(roundScore)
      print(roundScore)
      print("===================")
      print()
      time.sleep(3)
      os.system("clear")
      break
  
    #user guess wrong letter
    if userGuess not in myWord:
      dead = dead + 1
      print("oh no...")
      print(f"{dead} out of 6 wrong guesses.")
      print(modules.HANGMANPICS[dead])
      time.sleep(1.5)
      if dead == 6:
        print()
        
        userScore.append(failed)
        print(f"the password was: {modules.BLUE}{myWord}{modules.RESET}")
        previousWords.append(myWord)
        modules.listOfWords.remove(myWord)
        break
  
    #user guess right
    if userGuess in myWord:
      print(f"You're one step closer!")
  
    print()
    print()
    
    #printing for user to see how they did 
    for letter in myWord:
      if letter in guessList:
        print(letter, end="")
      else:
        letter = "_"
        print(letter, end="")
    
    time.sleep(1)
    os.system("clear")
  
    print()
    print()
  print()

  #end of game / if user gets to the 4th round
  if round == 4:
    os.system("clear")
    print(f"Here are all the passwords you guessed: {previousWords}")
    print()
    print("===================")
    print("Your Final Taylor Score")
    for round in userScore:
      print(round)
    print("===================")
    print()

    if failed in userScore:
      time.sleep(1)
      print("!!!!!BANG!!!!!")
      time.sleep(1)
      print(f"{modules.RED}{USERNAME} you were too late... Taylor can't be saved anymore... {modules.RESET}")
      print()
      time.sleep(1)
      print("No worries, there's another Taylor on a different multiverse you can save.")
      time.sleep(1)
      print("Refresh the page to try again")
    else:
      time.sleep(1)
      print("You take a deep breath, the passwords have been entered.")
      time.sleep(1)
      print("You hear a click...")
      print()
      time.sleep(2)
      print("\033[95m" + "\"Hello?....\"" + "\033[0m")
      time.sleep(1.5)
      print(f"{modules.GREEN}{USERNAME} you did it! You saved Taylor!")
      time.sleep(1)
      print(modules.key)
      time.sleep(2)
      print()
      print(f"You unlocked the key to Taylor's vault.{modules.RESET}")
      time.sleep(2)
    print()
    print("See you next time!")
    break
  else:
    continue

  
