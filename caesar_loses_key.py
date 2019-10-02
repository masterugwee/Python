# round13
def decrypt():
    result = ""
    text = "Uel Pactnia! I jhsg jaatrd tb geft ybue Prlpgotrnpuy sxiylf ;)"
    s = 13
    oddoreven = 1
    for i in range(len(text)):
        char = text[i]
        if ' ' in char or ';' in char or '!' in char or ')' in char:
                oddoreven = oddoreven+1
                result += char
        else:
           if oddoreven % 2 != 0:
                #?print (chr(ord(char)-s+97)
                oddoreven = oddoreven + 1
                if (char.isupper()):
                    #print(chr(((ord(char)-65)-s)%26+65))                    #For some cases this works.
                    result += chr(((ord(char)-65)-s)%26+65)   #Issue happens here
                elif (char.islower()):
                    print(chr(((ord(char)-97)-s)%26+97))                    #For some cases this works.
                    result += chr(((ord(char)-97)-s)%26+97)   #Issue happens here


           else:
                result += char
                oddoreven = oddoreven + 1

    print("Decry Text : " + result)

    print("Cipher text : " + text)


if __name__ == "__main__":
    decrypt()
