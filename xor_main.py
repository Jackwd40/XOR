import base64

def xor(hexmessage, key):

    # ready_message = bytes.fromhex(hexmessage)
    ready_key = bytes.fromhex(key)

    ready_message = base64.b64decode(hexmessage)
    output = b''
    index = 0
    for ch in ready_message:
        output += bytes([ready_message[index] ^ ready_key[index % len(ready_key)]])
        index += 1
    passback = bytes.hex(output)
    return(passback)


    
if __name__ == '__main__':
    print(xor("XUBdTFdScw5XCVRGTglJXEpMSFpOQE5AVVxJBRpLT10aYBpIVwlbCVZATl1WTBpaTkBOQFVcSQdH", "3a29"))