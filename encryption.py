import string
import time
import random

with open("/home/johnny/Downloads/VSCODE/all_english_words.txt", "r") as file:
    contents = file.readlines()
def randomWord():
    return random.choice(contents).strip()

def pause():
  input("Press enter to move on")

# c means character (allC = allCharacters)
allC = list(string.ascii_letters + string.digits + string.punctuation)
digitNames = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]



########################################################################################################
# option 1
def CaesarEncrypt(message, shift):
  '''
  STEP 1)
  find all characters in the alphabet (including upper/lowecase) and their index
  STEP 2)
  get message from person
  STEP 3)
  find the index of all the characters in the message
  STEP 4)
  shift the index up by #
  STEP 5)
  convert the shifted indexes into letters
  STEP 6)
  print new encrypted message
  '''
  # STEP 3)
  # message = "The enemy's army will be coming at aproximately t=2200 accross the Nile River."
  # message = "Wkh hqhpB'v dupB zloo eh frplqj dw dsurAlpdwhoB w=2200 dffurvv wkh Qloh Ulyhu."
  messageIndexes = []
  for c in message:
    if c not in allC:
      messageIndexes.append(c)
    else:
      messageIndexes.append(allC.index(c))

  # STEP 4)
  placeInList = 0
  shiftedMessage = []
  for item in messageIndexes:
    if isinstance(item, int):
      item += shift
      if item > 51:
        item -= 52
      shiftedMessage.append(allC[item])
    else:
      shiftedMessage.append(item)    
    placeInList += 1

  # STEP 5 AND 6)
  newMessage = ""
  for item in shiftedMessage:
    if isinstance(item, int):
      newMessage += allC[item]
    else:
      newMessage += item
  print("Encrypted message: ")
  time.sleep(0.6)
  print(newMessage)
  time.sleep(0.3)
  print(f'Characters Shifted:\n{shift}')
  time.sleep(2)


#############################################################################################################
# option 2
def CaesarDecrypt(message, shift):
  '''
  STEP 1)
  convert the message into index
  STEP 2)
  apply reverse shift (52 - shift)
  STEP 3)
  convert the shifted values to letters
  STEP 4)
  print unencrypted message

  its the same thing as encrypt, but shift = 52 - shift
  '''
  shift = 52 - shift
  messageIndexes = []
  for c in message:
    if c not in allC:
      messageIndexes.append(c)
    else:
      messageIndexes.append(allC.index(c))

  placeInList = 0
  shiftedMessage = []
  for item in messageIndexes:
    if isinstance(item, int):
      item += shift
      if item > 51:
        item -= 52
      shiftedMessage.append(allC[item])
    else:
      shiftedMessage.append(item)    
    placeInList += 1

  newMessage = ""
  for item in shiftedMessage:
    if isinstance(item, int):
      newMessage += allC[item]
    else:
      newMessage += item
  print("Decrypted message: ")
  time.sleep(0.6)
  print(newMessage)
  time.sleep(2)


#############################################################################################################
# option 3
'''STEPS TO ENCRYPT
1) get message
2) get the encryption key
3) For each letter in the message, add the index of the corresponding key letter to the index of the message letter.
  3b) If the key is shorter than the message, repeat the key until its the same length as the message. If longer, cut it off.
  3c) OPTIONAL- multiply the shift by the multiplier.
4) convert those shifted values to letters
5) print
(called polyalphabetic cypher)
'''
def complexEncrypt(message, key):
  # convert each letter in message into its index based on allC. spaces are named "space"
  messageAsIndexes = []
  for c in list(message):
    if c == " ":
      messageAsIndexes.append("space")
    else:
      messageAsIndexes.append(allC.index(c))
  
  # removing spaces in key, then making key shorter/longer based on len(message)
  pos = 0
  keyNoSpace = ""
  newKey = ""
  for c in key:
    if c != " ":
      keyNoSpace += c
  
  if len(keyNoSpace) > len(message):
    for c in range(len(message)):
      newKey += keyNoSpace[pos]
      pos += 1
  elif len(keyNoSpace) < len(message):
    for c in range(len(message)):
      newKey += keyNoSpace[pos]
      pos += 1
      if pos >= len(keyNoSpace):
        pos = 0
  else:
    newKey = keyNoSpace

  # converting newKey into indexes
  newKeyIndexes = []
  for c in newKey:
    newKeyIndexes.append(allC.index(c))

  # getting new indexes of the message after appling the shift
  newMessageIndexes = []
  pos = 0
  for c in messageAsIndexes:
    if c == "space":
      newMessageIndexes.append(c)
      pos += 1
    else:
      shiftAmount = messageAsIndexes[pos] + newKeyIndexes[pos]
      if shiftAmount > (len(allC)-1):
        shiftAmount %= (len(allC)-1)
      newMessageIndexes.append(shiftAmount)
      pos += 1

 
  # converting the shifted values into letters to print out
  newMessage = ""
  for item in newMessageIndexes:
    if item == "space":
      newMessage += " "
    else:
      newMessage += allC[item]
    
  print(f'Encrypting your message, "{message}"')
  time.sleep(len(message)/75) # make it seem like its doing work. if its a long message, wait longer. smaller number = longer times
  print(f'Your encrypted message: {newMessage}\nKey used to encrypt: {key}')
  pause()

# complexEncrypt("Time to invade: 14:00.", "python")


#############################################################################################################
# option 4
'''STEPS TO DECRYPT
STEP 1) convert message into indexes
  make each character a list by list(message)
  spaces are ignored and replaced by "space"

STEP 2) convert the indexes into characters
  find the indexes of STEP 1) (ignore spaces) in allC and assign that to a list.
  that list will contain the indexes of the characters after the shift

STEP 3) subtract the shift from each index in the key from the index of each character
  get key and make it have same characters as len(message).
    remove spaces from it as well
  get index of each c in the newKey
  subract the index at a pos (STEP 2)) by the index of the newKey at that same pos (prev step)
    if its a negative, you need to wrap around by adding len(allC) to it


STEP 4) convert those new indexes into characters and put them into final message
  find those indexes in allC and add them into a final message

STEP 5) print final message
'''
def complexDecrypt(message, key):
  # comments are useful for debugging
  # convert to indexes
  messageIndexes = []
  for c in list(message):
    if c == " ":
      messageIndexes.append("space")
    else:
      messageIndexes.append(allC.index(c))

  # removing spaces from key
  keyNoSpace = []
  for c in list(key):
    if c in list(allC):
      keyNoSpace.append(c)

  # making key same len as message.   same code as encrypt
  newKey = ""
  pos = 0
  if len(keyNoSpace) > len(message):
    for c in range(len(message)):
      newKey += keyNoSpace[pos]
      pos += 1
  elif len(keyNoSpace) < len(message):
    for c in range(len(message)):
      newKey += keyNoSpace[pos]
      pos += 1
      if pos >= len(keyNoSpace):
        pos = 0
  else:
    newKey = keyNoSpace

  # index of each c in newKey
  newKeyIndexes = []
  for c in list(newKey):
    newKeyIndexes.append(allC.index(c))

  # adding the shift (subtracting the index of)
  newMessageIndexes = []
  pos = 0
  for item in messageIndexes:
    if item == "space":
      newMessageIndexes.append(item)
      pos += 1
    else:
      shiftAmount = messageIndexes[pos] - newKeyIndexes[pos]
      if shiftAmount < 0:
        shiftAmount += len(allC)-1
      newMessageIndexes.append(shiftAmount)
      pos += 1

  # converting the values into letters and printing
  newMessage = ""
  for item in newMessageIndexes:
    if item == "space":
      newMessage += " "
    else:
      newMessage += allC[item]
  print(f'Decrypting your message, "{message}"')
  time.sleep(len(message)/65)
  print(f'Your decrypted message: {newMessage}\nKey used to encrypt: {key}')
  pause()
# complexDecrypt("8GFl GD BuJnsCd &(}/*?", "python")


#############################################################################################################



while True:
  print("Main menu:")
  print("1. Caesar cypher")
  print("2. Decrypt Caesar cypher")
  print("3. Complex cypher")
  print("4. Complex decrypt")
  print("4. Leave")
  option = input("What would you like to do?: ")

  if option == "1":
    message = input("What message do you want to encrypt?: ")
    while True:
      shift = int(input("How many letters do you want to shift by?: "))
      if shift > 51:
        print("Shift can't be greater than 51")
        continue
      else:
        break
    CaesarEncrypt(message, shift)
  
  elif option == "2":
    message = input("What do you want to decrypt?: ")
    while True:
      shift = int(input("How many letters was this shifted by?: "))
      if shift > 51:
        print("Shift can't be greater than 51")
        continue
      else:
        break
    CaesarDecrypt(message, shift)

  elif option == "3":
    message = input("What do you want to encrypt?: ")
    key = input("What key will you use to encrypt it (longer keys are more secure)?: ")
    complexEncrypt(message, key)
  
  elif option == "4":
    message = input("What do you want to decrypt?: ")
    key = input("What was the key used?: ")
    complexDecrypt(message, key)
  
  else:
    break
