class EncodeDecode:

    def __init__(self, input):
        self.__input = input

    def encodeInput(self, input):
        asciiList = []

        for char in input:
            asciiVal = ord(char)
            asciiVal += 3
            asciiList.append(asciiVal)

        encodedString = "".join([chr(a) for a in asciiList])

        print("Your encoded word: " + encodedString)

    def decodeInput(self, input):
        asciiList = []

        for char in input:
            asciiVal = ord(char)
            asciiVal -= 3
            asciiList.append(asciiVal)
            # Hallo

        decodedString = "".join([chr(a) for a in asciiList])

        print("Your decoded word: " + decodedString)