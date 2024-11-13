import string
import time
import random

def pause():
  input("Press enter to move on")
# c means character (allC = allCharacters)
allC = list(string.ascii_letters + string.digits + string.punctuation)

########################################################################################################

# option 1
def CaesarEncrypt(message, shift):
  # converting message to indexes based on allC
  messageIndexes = [c if c not in allC else allC.index(c) for c in message]

  # adding shift   
  shiftedMessage = [item if item == " " else ((item+shift)%len(allC)) for item in messageIndexes]

  # converting the shifted indexes into letters and printing out
  newMessage = ''.join([item if item == " " else allC[item] for item in shiftedMessage])
  time.sleep(0.3)
  print(f'Encrypted message: {newMessage}\nCharacters shifted: {shift}')
  pause()

#############################################################################################################

# option 2
def CaesarDecrypt(message, shift):
  # converting the message into indexes
  messageIndexes = [c if c not in allC else allC.index(c) for c in message]

  # removing shift
  shiftedMessage = [item if item == " " else (item-shift) % len(allC) for item in messageIndexes ]

  newMessage = ''.join([item if item == " " else allC[item] for item in shiftedMessage])
  time.sleep(0.3)
  print(f'Decrypted message: {newMessage}\nCharacters shifted: {shift}')
  pause()

#############################################################################################################

# option 3
def complexEncrypt(message, key):
  # convert each letter in message into its index based on allC. spaces are named "space"
  messageAsIndexes = [allC.index(c) if c != " " else "space" for c in list(message)]
  
  # removing spaces in key
  keyNoSpace = ''.join(c for c in key if c != " ")

  # making key == len(message)
  '''# Replaced code with below
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
    newKey = keyNoSpace'''
  if len(keyNoSpace) == len(message):    # idk how to make this into a list comprehension
    newKey = keyNoSpace
  else:
    newKey = ''.join([keyNoSpace[x % len(keyNoSpace)] for x in range(len(message))])

  # converts the newKey into indexes. used for shifting
  newKeyIndexes = [allC.index(c) for c in newKey]

  newMessageIndexes = [c if c == "space" else ((c+newKeyIndexes[i]) % (len(allC)-1)) for i, c in enumerate(messageAsIndexes)]
  '''# Replaced code with above. this is still useful to see how the code below works
  # getting new indexes of the message after appling the shift
  newMessageIndexes = []
  pos = 0
  for c in messageAsIndexes:
    if c == "space":
      newMessageIndexes.append(c)
      pos += 1
    else:
      newMessageIndexes.append((c+newKeyIndexes[pos]) % (len(allC)-1))
      pos += 1'''
  '''explanation of how it works
    making the replaced code into a list comprehension
    the enumerate creates a pair of (index, indexOfMessage). it increases index by 1 for every pair.
       does smth like newMessageIndexes = [ (0, index[at pos 0]), (1, index[at pos 2]), (2, index[at pos 3]) ]
    the i after the for accesses the enumerated number (0, 1, 2, etc). the c accesses the index[at pos]
    need enumerate bc u cant do stuff like pos += 1 in a list comprehension'''

  # converting the shifted indexes into letters. spaces turn into " "
  newMessage = ''.join([allC[item] if item != "space" else " " for item in newMessageIndexes])
    
  print(f'Encrypting your message, "{message}"')
  time.sleep(len(message)/75) # make it seem like its doing work. if its a long message, wait longer. smaller number = longer times
  print(f'\nYour encrypted message: {newMessage}\nKey used to encrypt: {key}')
  pause()

#############################################################################################################

# option 4
def complexDecrypt(message, key):
  # convert each letter in message into its index based on allC. spaces are named "space"
  messageIndexes = [allC.index(c) if c != " " else "space" for c in list(message)]

  # removing spaces in key, then making key shorter/longer based on len(message).   Same code as encrypt
  keyNoSpace = [c for c in list(key) if c in list(allC) ]
  
  # making key == len(message)
  if len(keyNoSpace) == len(message):
    newKey = keyNoSpace
  else:
    newKey = ''.join([keyNoSpace[x % len(keyNoSpace)] for x in range(len(message))])
  
  # converts the newKey into indexes. used for shifting
  newKeyIndexes = [allC.index(c) for c in list(newKey)]

  # adding the index of each c in newKeyIndexes to messageIndexes
  '''# Replaced code with below. this is still useful to see how the code below works
  # adding the shift (subtracting the index of)
  newMessageIndexes = []
  pos = 0
  for item in messageIndexes:
    if item == "space":
      newMessageIndexes.append(item)
      pos += 1
    else:
      newMessageIndexes.append((item - newKeyIndexes[pos % len(newKeyIndexes)]) % (len(allC)-1))
      pos += 1'''
  newMessageIndexes = [item if item == "space" else ((item - newKeyIndexes[i % len(newKeyIndexes)]) % (len(allC)-1)) for i, item in enumerate(messageIndexes)]

  # converting the shifted indexes into letters. spaces turn into " "
  newMessage = ''.join([" " if item == "space" else allC[item] for item in newMessageIndexes])

  print(f'Decrypting your message, "{message}"')
  time.sleep(len(message)/65)
  print(f'\nYour decrypted message: {newMessage}\nKey used to encrypt: {key}')
  pause()

#############################################################################################################

while True:

  print("\nMain menu:")
  print("1. Caesar cypher")
  print("2. Decrypt Caesar cypher")
  print("3. Complex cypher")
  print("4. Complex decrypt")
  print("5. Leave")
  option = input("What would you like to do?: ")

  if option == "1":
    message = input("What message do you want to encrypt?: ")
    shift = int(input("How many letters do you want to shift by?: "))
    CaesarEncrypt(message, shift)
  
  elif option == "2":
    message = input("What do you want to decrypt?: ")
    shift = int(input("How many letters was this shifted by?: "))
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


'''STEPS TO ENCRYPT
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
'''
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
