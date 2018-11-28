#!/usr/bin/env python
import crypt
from passlib.hash import sha512_crypt

def testPass(cryptPass):
    salt = cryptPass[3:11]
    print("[+] Salt: ", salt)
    dictFile = open('rockyou.txt', encoding = 'ISO-8859-1')
    for word in dictFile: 
        word = word.strip('\n')
        cryptword = sha512_crypt.using(salt=salt, rounds=5000).hash(word)
        if (cryptword == cryptPass):
            print("[+] Found password: " + word + "\n")
            return
    print("[-] Password not found.\n")
    return


def main():
    passfile = open('shadow.txt')
    for line in passfile:
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print("[*] Cracking password for: ", user)
            testPass(cryptPass)

if __name__ == '__main__':
    main()