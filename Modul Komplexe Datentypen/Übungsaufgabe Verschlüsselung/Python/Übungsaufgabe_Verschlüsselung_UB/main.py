from EncodeDecode import EncodeDecode

encodeOrDecodeInput = input("Type yes for encode or no for decode.\t")

if encodeOrDecodeInput == "yes":
    x = EncodeDecode(encodeOrDecodeInput)
    encodeInput = input("Type in your word for encoding.\t")
    x.encodeInput(encodeInput)
elif encodeOrDecodeInput == "no":
    x = EncodeDecode(encodeOrDecodeInput)
    decodeInput = input("Type in your word for decoding.\t")
    x.decodeInput(decodeInput)

