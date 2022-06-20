def encrypt(text, s):
    result = ""
    
    for i in range(len(text)):
        char = text[i]
        if(char==' '):
            result += char;
        #Encrypt uppercase
        elif (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        #Encrypt lowercase 
        else:
            result += chr((ord(char) + s-97) % 26 + 97)
            
    return result   

def decrypt(message):
    
    LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for key in range(len(LETTERS)):
        translated = ""
        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(LETTERS)
                translated = translated + LETTERS[num]
            else:
                translated = translated + symbol
        print('Hacking key #%s: %s' % (key, translated))
    

text = "Koleci Alexandru Paul"
s = 12

print(text)
print(str(s))
coded = encrypt(text,s)
print(coded)
decrypt(coded)