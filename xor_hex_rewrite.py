import codecs
def xor(message, key):
    output = ''
    index = 0
    #ready_string = codecs.decode(message, "hex").decode("utf-8")
    print(ready_string)
    for character in ready_string:
        computation = ord(message[index]) ^ ord(key[index % len(key)])
        # print(computation)
        output += hex(computation)[2:].zfill(2)
        index += 1
        
    print(output)



if __name__ == '__main__':
    xor("68656c6c6f776f726c64", "a")