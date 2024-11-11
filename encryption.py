import string
import time

def pause():
  input("Press enter to move on")

# c means character (allC = allCharacters)
allC = list(string.ascii_letters + string.digits + string.punctuation)
# specialC = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
# digits = list(string.digits)
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
'''STEPS
MORE COMPLEX CYPHER-
STEPS TO ENCRYPT
1) get message
2) get the encryption key
3) For each letter in the message, add the index of the corresponding key letter to the index of the message letter.
  3b) If the key is shorter than the message, repeat the key until its the same length as the message. If longer, cut it off.
  3c) OPTIONAL- multiply the shift by the multiplier.
4) convert those shifted values to letters
5) print
(called polyalphabetic cypher)

STEPS TO DECRYPT
1) get message
2) get key
For each letter zin the encrypted message, subtract the index of the corresponding key letter from the index of the encrypted letter (reversing the shift)
  3b) If they key is shorter than the message, repeat until its the same length. If longer, cut it off.
  3c) OPTIONAL- multiplier. divide the shift by the multiplier (???)
4) convert the shifted values to letters
5) print
'''
def complexEncrypt(message, key):
  # all the comments here are useful for debugging and seeing what is going on
  messageToList = list(message)

  # convert each letter in message into its index based on allC. spaces are named "space"
  messageAsIndexes = []
  for c in messageToList:
    if c == " ":
      messageAsIndexes.append("space")
    else:
      messageAsIndexes.append(allC.index(c))
  
  # removing spaces in key, then making key shorter/longer based on len(message)
  pos = 0
  keyNoSpace = ""
  newKey = ""

  for c in key:   #removing spaces in key
    if c != " ":
      keyNoSpace += c
  
  if len(keyNoSpace) > len(message):     # if len of key is > len of message, cut of the key
    for c in range(len(message)):
      newKey += keyNoSpace[pos]
      pos += 1
  elif len(keyNoSpace) < len(message):   # if len of key is < len of message, repeat key until satisfied
    for c in range(len(message)):
      newKey += keyNoSpace[pos]
      pos += 1
      if pos >= len(keyNoSpace):
        pos = 0
  else:                                  # if len of key = len of message, dont do anything
    newKey = keyNoSpace
  # print(f'Key: {newKey}')   #works
  # pause()

  # converting newKey into indexes
  newKeyIndexes = []
  for c in newKey:
    newKeyIndexes.append(allC.index(c))
  # useful for debugging- print(f'Key indexes: {newKeyIndexes}')   #works
  # useful for debugging- pause()

  # getting new indexes of the message after appling the shift
  # comments useful for debugging and seeing what is happening
  newMessageIndexes = []
  pos = 0
  for c in messageAsIndexes:
    # print(f"INDEX {c}.  CHARACTER -{messageToList[pos]}-")
    if c == "space":
      newMessageIndexes.append(c)
      # print(f"ADDED SPACE {newMessageIndexes}")
      # pause()
      pos += 1
    else:
      # print(f"ADDING SHIFT ({newKeyIndexes[pos]})")
      # pause()
      shiftAmount = messageAsIndexes[pos] + newKeyIndexes[pos]
      if shiftAmount > (len(allC)-1):
        shiftAmount %= (len(allC)-1)
      #   print(f"ROLLED BACK TO INDEX {shiftAmount}")
      #   pause()
      # print(f'ADDED SHIFT. NEW allC INDEX: {shiftAmount}')
      newMessageIndexes.append(shiftAmount)
      # print(f"MESSAGE NOW {newMessageIndexes}")
      # pause()
      pos += 1
  # print(f'NEW MESSAGE INDEXES {newMessageIndexes}')
 
  # converting the shifted values into letters to print out
  newMessage = ""
  for item in newMessageIndexes:
    if item == "space":
      newMessage += " "
    else:
      newMessage += allC[item]
    
  print(f'Encrypting your message, "{message}"')
  time.sleep(len(message)/25) # make it seem like its doing work. if its a long message, wait longer. smaller number = longer times
  print(f'Your encrypted message: {newMessage}\nKey used to encrypt: {key}')
  pause()

complexEncrypt("Time to invade: 14:00.", "Srgt. Sanders")


#############################################################################################################


'''
while True:
  print("Main menu:")
  print("1. Caesar cypher")
  print("2. Decrypt Caesar cypher")
  print("3. Complex cypher")
  print("4. Leave")
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
  
  elif option == 2:
    message = input("What do you want to decrypt?: ")
    while True:
      shift = int(input("How many letters was this shifted by?: "))
      if shift > 51:
        print("Shift can't be greater than 51")
        continue
      else:
        break
    CaesarDecrypt(message, shift)

  elif option == 3:
    message = input("What do you want to encrypt?: ")
    key = input("What key will you use to encrypt it?: ")
    complexEncrypt(message, key)
  else:
    break
'''