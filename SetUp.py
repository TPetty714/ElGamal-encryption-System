import secrets
import random

_keysize_ = 64


def setup(seed):
    random.seed(seed)
    g = 2
    p = generatePrime("p")
    d = generatePrime("d")
    while (d >= p-2):
        d = generatePrime("d")
    e2 = SquareAndMultiply(g, p, "{0:b}".format(d))
    # print("p: " + str(p) + " d: " + str(d) + " e2: " + str(e2))
    f = open("pubkey.txt", "w")
    f.write(str(p) + " " + str(g) + " " + str(e2))
    f.close()
    f = open("prikey.txt", "w")
    f.write(str(p) + " " + str(g) + " " + str(d))
    f.close()


def generatePrime(x):
    # while(q%12 != 5):
    b = "1"
    p = 0
    while (True):
        q = secrets.randbits(_keysize_-1)
        qb = "{0:b}".format(q)
        qb = "1" + qb[1:]
        if (qb.__len__() != _keysize_-1):
            continue
        q = int(qb,2)
        if SquareAndMultiply(q, 12, b) != 5:
            continue
        # else:
        #     break
        if MillerRabin(q) == False:
            continue
        p = 2*q + 1
        if MillerRabin(p) == False:
            continue
        else:
            break
    pb = "{0:b}".format(p)
    print(x + ": " + str(p) + " | " + str(pb.__len__()) + " bits")
    return p


# Based on psuedocode from Mocas's slides for Square and Multiply
def SquareAndMultiply(a, n, b, m=1):
    # a^b mod n where b is binary of exponent and k is binary length
    k = b.__len__()
    f=1
    for i in range(0, k, 1):
        f = (f*f)*m % n
        if b[i] == "1":
            f = (f*a)*m % n
    # print(f)
    return f

# Based on pseudocode from Mocas's slides
def MillerRabin(n):
    # 1. Find integers k > 0, q odd, so that(n–1) = 2^kq
    count = 0
    temp = n
    while temp != 0:
        temp = temp//2
        count+=1
    for k in range(count, 0, -1):
        q = int((n-1)/(2**k))
        if q % 2 == 0:
            continue
        if q*(2**k) == n-1:
            break
    # 2. Select a random integer a, 1 < a < n–1
    a = random.randint(1,n-1)
    # 3. if a^q mod n = 1 then return (“maybe prime");
    if SquareAndMultiply(a, n, "{0:b}".format(q)) == 1:
        return True
    # 4. for j = 0 to k – 1 do
    for j in range(k-1, -1, -1):
    # 5. if (a^(2^j*q) mod n = n-1) then return ("maybe prime")
        if SquareAndMultiply(a, n, "{0:b}".format((2**j)*q)) == n-1:
            return True
    # 6. return ("composite")
    return False

if __name__ == "__main__":
    seed = input("Input a seed\n")
    setup(seed)