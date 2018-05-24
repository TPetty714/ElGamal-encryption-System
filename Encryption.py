import binascii
import random
import SetUp

def encrypt(seed):
    random.seed(seed)
    f = open("pubkey.txt", "r")
    key = f.read()
    f.close()
    keyList = key.split()
    p = int(keyList[0])
    g = int(keyList[1])
    e2 = int(keyList[2])
    f = open("ptext.txt", "r")
    ptext = f.read()
    f.close()
    ptextb = binascii.hexlify(ptext.encode())
    f = open("ctext.txt", "w")
    first = True
    for i in range(0, len(ptextb), 8):
        m = ptextb[i:i+8]
        if len(m) < 8:
            m = m.ljust(8, b'0')
        mInt = int(m.decode(),16)
        k = random.randint(0, p-1)
        c1 = SetUp.SquareAndMultiply(g, p, "{0:b}".format(k))
        c2 = SetUp.SquareAndMultiply(e2, p, "{0:b}".format(k)) * (mInt % p) % p
        if first:
            f.write(str(c1) + " " + str(c2))
            first = False
        else:
            f.write(" " + str(c1) + " " + str(c2))
        print("c1: " + str(c1) + " c2: " + str(c2))
    f.close()


if __name__ == "__main__":
    seed = input("Input a seed\n")
    encrypt(seed)