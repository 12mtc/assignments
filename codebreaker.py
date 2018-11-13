import re
import math

def main ():
    file = open('Cipher Text.txt', 'r')
    cipherText = file.read()
    file.close()

    plainText = decoder(cipherText)
    print(cipherText+"\n")

    print(plainText+"\n")

    print(findKeyLength(cipherText))
    print(findFreq("ll","Hello worldll"))


def decoder(cipherText):
    plainText = cipherText

    return plainText

def findKeyLength(cipherText):
    tempkeyL = []
    foundR = []
    for i in range(2,len(cipherText)):
        temp = findFreq(cipherText[i-2:i],cipherText)
        if temp != 0:
            foundR.append(cipherText[i-2:i])
            tempkeyL.append(temp)
    return tempkeyL

def findFreq(sub,main):
    pos = []
    for i in re.finditer(sub,main):
        pos.append(i.start())
    if len(pos) == 1:
        return 0
    print(sub)
    return pos[1]-pos[0]

if __name__ == '__main__':
    main()