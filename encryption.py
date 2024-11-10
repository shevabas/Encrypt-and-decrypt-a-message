import string
import time

def pause():
  input("")

# c means character (allC = allCharacters)
allC = string.ascii_letters
specialC = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
digits = list(string.digits)
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
'''
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
# option 3
def complexEncrypt(message, key):
  messageToList = list(message)

  # convert each letter in message into its index. numbers are named itself. specialC arent changed. " " are named space
  messageAsIndexes = []
  for c in messageToList:
    if c == " ":
      messageAsIndexes.append("space")
    elif c in allC:
      messageAsIndexes.append(allC.index(c))
    elif c == "0":
      messageAsIndexes.append("zero")
    elif c == "1":
      messageAsIndexes.append("one")
    elif c == "2":
      messageAsIndexes.append("two")
    elif c == "3":
      messageAsIndexes.append("three")
    elif c == "4":
      messageAsIndexes.append("four")
    elif c == "5":
      messageAsIndexes.append("five")
    elif c == "6":
      messageAsIndexes.append("six")
    elif c == "7":
      messageAsIndexes.append("seven")
    elif c == "8":
      messageAsIndexes.append("eight")
    elif c == "9":
      messageAsIndexes.append("nine")
    else:
      messageAsIndexes.append(c)

  # remove spaces or special characters from key
  cOnlyKey = ""
  for c in key:
    if c in allC:
      cOnlyKey += c
    else:
      continue
  
  # making key shorter/longer based on len(message)
  pos = 0
  newKey = ""
  if len(cOnlyKey) > len(message):
    for c in range(len(message)):
      newKey += cOnlyKey[pos]
      pos += 1
  elif len(cOnlyKey) < len(message):
    for c in range(len(message)):
      newKey += cOnlyKey[pos]
      pos += 1
      if pos >= len(cOnlyKey):
        pos = 0
  else:
    newKey = cOnlyKey
  
  # converting newKey into indexes
  newKeyIndexes = []
  for c in newKey:
    newKeyIndexes.append(allC.index(c))

  # getting new shifted value and looping them if its larger
  # lots of commented out things were debugging things
  newMessageIndexes = []
  pos = 0
  # print(f'INDEXES      {messageAsIndexes}')
  # print(f'KEY INDEXES  {newKeyIndexes}')
  for c in messageAsIndexes:
    # print("1. " + str(c) + "  character: " + messageToList[pos])
    try:
      if allC[c]:
        # if allC[c] in list(allC):
          # print(f'allC[c] {allC[c]}')
          # print("2. " + str(c))
          newMessageIndexes.append(c + newKeyIndexes[pos])
          # print(f'3. ADDED SHIFT {messageAsIndexes[pos]} + {newKeyIndexes[pos]}.  {newMessageIndexes[pos]}')
          # pause()
          if newMessageIndexes[pos] > 51:
            newMessageIndexes[pos] %= 51
            # print(f'4. ROLLED BACK {messageAsIndexes[pos]} + {newKeyIndexes[pos]}.  {newMessageIndexes[pos]}')
          pos += 1
        # print("7. END")
        # print(newMessageIndexes)
        # pause()
    except:
      if c == "space":
          newMessageIndexes.append("space")
          # pause()
      elif c in digitNames:
          # print("5. " + str(c))
          newMessageIndexes.append(c)
      else:
        # print("6. " + str(c))
        newMessageIndexes.append(c)
      pos += 1
      # print("7. END")
      # print(newMessageIndexes)
      # pause()
  # print(f'AFTER SHIFT  {newMessageIndexes}')

  # converting the shifted values into letters to print out
  # lots of commented out things were debugging things
  newMessage = ""
  for item in newMessageIndexes:
    # print(f'ITEM {item}')
    # pause()
    try:
      if allC[item] in list(allC):
        # print(f'YES ITS IN ALL C   {item}')
        newMessage += allC[item]
        # print(newMessage)
        # pause()
    except:
      if item in digitNames:
        # print(f'ITS A DIGIT  {item}')
        # pause()
        if item == "zero":
          newMessage += "0"
        if item == "one":
          newMessage += "1"
        if item == "two":
          newMessage += "2"
        if item == "three":
          newMessage += "3"
        if item == "four":
          newMessage += "4"
        if item == "five":
          newMessage += "5"
        if item == "six":
          newMessage += "6"
        if item == "seven":
          newMessage += "7"
        if item == "eight":
          newMessage += "8"
        if item == "nine":
          newMessage += "9"
        # print(newMessage)
        # pause()
      elif item == "space":
        # print("ITS A SPACE")
        newMessage += " "
        # print(newMessage)
        # pause()
      else:
        # print(f'NOT A DIGIT OR SPACE {item}')
        # pause()
        newMessage += item
        # print(newMessage)
        # pause()
  print(f'Encrypting your message, "{message}"')
  time.sleep(len(message)/30)
  print(f'Your encrypted message: {newMessage}\nKey used to encrypt:    {key}')
  pause()

complexEncrypt("Time to invade: 14:00", "key")


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