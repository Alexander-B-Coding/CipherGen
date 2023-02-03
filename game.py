import random
import pandas as pd
import pygame as pg

def goodnessFormula(info:list):
  #info[1] = difficulty value
  #info[2] = accuracy
  #info[3] = length of text
  #info[0] = time to solve in seconds]
  return ((info[1]*.20)+(info[2]*.5)+(info[3]*.30))/(info[0])
  
def dataBase():
  userInfo = pd.read_csv("userInfo.csv")
  while (True):
    name = list()
    name = input().split()
    if (name[0] == 'q'):
      break
    name[1] = float(name[1])
    userInfo.loc[len(userInfo.index)] = name
  userInfo.to_csv("userInfo.csv", index=False)

  print(userInfo)

def caesarCipher(name):
  encrypted = ""
  shift = random.randint(0, 25)
  for x in name:
    if x == ' ':
      encrypted += ' '
    if ord(x) >= ord('A') and ord(x) <= ord('Z'):
      encrypted += chr(((ord(x) - 65) + shift) % 26 + 65)
    elif ord(x) >= ord('a') and ord(x) <= ord('z'):
      encrypted += chr(((ord(x) - 97) + shift) % 26 + 97)
  return encrypted

def monoalphabetic(text):
  letters = dict()
  used_keys = list()

  for i in range(97, 123):
    temp_rand = random.randint(97, 122)
    while (i == temp_rand or temp_rand in used_keys):
      temp_rand = random.randint(97, 122)
    letters[i] = temp_rand
    used_keys.append(temp_rand)

  encrypted_name = ""
  for i in range(len(text)):
    char = chr(letters[ord(text[i])])
    encrypted_name += char
  return encrypted_name

def playFairCipher(text):
    playFairMatrix = [['A', 'B', 'C', 'D',' E'],['F', 'G', 'H', 'I','K'],['L', 'M', 'N', 'O', 'P'],['Q', 'R', 'S', 'T', 'U'],['V', 'W', 'X','Y', 'Z']]
  
    cipherList = list()
    for index, letter in enumerate(text):
        if letter == ' ':
            continue
        if index == len(text) - 1:
           cipherList.append(letter) 
        elif index % 2 == 1 and cipherList[index - 1] == letter:
            cipherList.append('X')
        else:
            cipherList.append(letter)

    if len(cipherList) % 2 == 1:
        cipherList.append('X')

    letters = {
        'A': [0, 0], 'B': [0, 1], 'C': [0, 2], 'D': [0, 3], 'E': [0, 4],
        'F': [1, 0], 'G': [1, 1], 'H': [1, 2], 'I': [1, 3], 'K': [1, 4],
        'L': [2, 0], 'M': [2, 1], 'N': [2, 2], 'O': [2, 3], 'P': [2, 4],
        'Q': [3, 0], 'R': [3, 1], 'S': [3, 2], 'T': [3, 3], 'U': [3, 4],
        'V': [4, 0], 'W': [4, 1], 'X': [4, 2], 'Y': [4, 3], 'Z': [4, 4]
    }

    coords = list()
    for i in range(1, len(cipherList), 2):
        x = letters[cipherList[i - 1]][0]
        y = letters[cipherList[i - 1]][1]

        x1 = letters[cipherList[i]][0]
        y1 = letters[cipherList[i]][1]
        coords.append([x, y, x1, y1])
    
    i = 0
    for coordinates in coords:
        
        if(coordinates[0] == coordinates[2]):
            cipherList[i] = (playFairMatrix[coordinates[0]][(coordinates[1] + 1) % 5])
            cipherList[i + 1] = (playFairMatrix[coordinates[2]][(coordinates[3] + 1) % 5])
            
        elif(coordinates[1] == coordinates[3]):
            cipherList[i] = (playFairMatrix[(coordinates[0] + 1) % 5][coordinates[1]])
            cipherList[i + 1] = (playFairMatrix[(coordinates[2] + 1) % 5][coordinates[3]])
        
        else:
            cipherList[i] = (playFairMatrix[coordinates[0]][coordinates[3]])
            cipherList[i + 1] = (playFairMatrix[coordinates[2]][coordinates[1]])
        i += 2
    print(cipherList)

def vigenere(plain_text, key):
  plain_text = plain_text.upper()
  encrypted = ""
  keystream = ""
  for i in range(len(plain_text)):
    x = i % len(key)
    if plain_text[i] == ' ':
      keystream += ' '
    else:
      keystream += key[x].upper()
  for i in range(len(plain_text)):
    if keystream[i] == ' ':
      encrypted += ' '
    elif (plain_text[i] != " "):
      encrypted += chr(65 + ((ord(plain_text[i]) + ord(keystream[i])) % 26))
  return encrypted

playFairCipher("BALLOON")