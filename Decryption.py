import SetUp

def decrypt():
    f = open("prikey.txt", "r")
    key = f.read()
    f.close()
    keyList = key.split()
    p = int(keyList[0])
    g = int(keyList[1])
    d = int(keyList[2])
    f = open("ctext.txt", "r")
    ctext = f.read()
    f.close()
    ctext = ctext.replace("\n", " ")
    ctextList = ctext.split(" ")
    message = ""
    for i in range(0, len(ctextList), 2):
        c1 = int(ctextList[i])
        c2 = int(ctextList[i+1])
        m = (SetUp.SquareAndMultiply(c1, p, "{0:b}".format(p-1-d)) * (c2 % p)) % p
        mb = bin(m)[2:]
        mb = mb.zfill(32)
        for i in range(0, mb.__len__(), 8):
            if int(mb[i:i+8]) != 0:
                message += (chr(int(mb[i:i+8],2)))
    f = open("dtext.txt", "w")
    f.write(message)
    f.close()





if __name__ == "__main__":
    decrypt()