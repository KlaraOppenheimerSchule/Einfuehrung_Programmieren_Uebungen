MORSE_CODE = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE[letter] + " "
        else:
            cipher += " "
    return cipher

def decrypt(message):
    message += " "
    decipher = ""
    citext = ""
    for letter in message:
        if (letter != " "):
            i = 0
            citext += letter
        else:
            decipher += list(MORSE_CODE.keys())[list[MORSE_CODE.values()].index(citext)]
            citext = ""
    
    return decipher
    
def main():
    message = input("Gib hier deine Nachricht ein: ")
    result = encrypt(message.upper())
    print("Morsecode:")
    print (result)
if __name__ == '__main__':
    main()