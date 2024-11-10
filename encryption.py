import string
import time

# c means character (allC = allCharacters)
allC = string.ascii_letters

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



while True:
  print("Main menu:")
  print("1. Caesar cypher")
  print("2. Decrypt Caesar cypher")
  print("Anything else to leave")
  option = int(input("What would you like to do?: "))

  if option == 1:
    message = input("What message do you want to encrypt?: ")
    while True:
      shift = int(input("How many letters do you want to shift by?: "))
      if shift > 51:
        print("Shift can't be greater than 51")
        continue
      else:
        break
    CaesarEncrypt(message, shift)
  
  if option == 2:
    message = input("What do you want to decrypt?: ")
    while True:
      shift = int(input("How many letters was this shifted by?: "))
      if shift > 51:
        print("Shift can't be greater than 51")
        continue
      else:
        break
    CaesarDecrypt(message, shift)