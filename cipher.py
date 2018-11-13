

def main ():
    key = "test"

    text = readFile('input.txt')

    cipherText = encrypt(key,text)
    print(text+'\n')
    print(cipherText+'\n')
    print(decrypt(key,cipherText))

    file = open('Cipher Text.txt', 'w')
    file.write(cipherText)
    file.close()

def encrypt(key, plainText):
    kLength = len(key)
    key = [(ord(x)-97) for x in key]
    plainText = [(ord(x)-97) for x in plainText]
    cipherText = ""

    for count in range(len(plainText)):
        value = (plainText[count]+key[count%kLength])%26
        cipherText += chr(value+97)
    return cipherText

def decrypt(key, cipherText):
    kLength = len(key)
    key = [(ord(x) - 97) for x in key]
    cipherText = [(ord(x) - 97) for x in cipherText]
    plainText = ""

    for count in range(len(cipherText)):
        value = (cipherText[count] - key[count % kLength]) % 26
        plainText += chr(value + 97)
    return plainText

def readFile(fileName):
    file = open(fileName, 'r')
    plainText = ""

    while 1:
        char = file.read(1)
        if not char: break

        if (ord(char) >= 97 and ord(char) <= 122) or (ord(char) >= 65 and ord(char) <= 90):
            plainText += char.lower()

    file.close()
    return plainText

if __name__ == '__main__':
    main()