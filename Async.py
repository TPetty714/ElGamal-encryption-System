import SetUp
import Encryption
import Decryption

def main(seed):
    SetUp.setup(seed)
    Encryption.encrypt(seed)
    Decryption.decrypt()

if __name__ == "__main__":
    seed = input("Input a seed\n")
    main(seed)