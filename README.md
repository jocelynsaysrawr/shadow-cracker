# Shadow Cracker

A python utility tool for brute force password cracking of /etc/shadow files.

### Requirements
* A large password/dictionary file.
    * replace `rockyou.txt` with your file name
* The /etc/shadow file you are trying to crack
    * replace `shadow.txt` with your file name

### References
* [PassLib Docs](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.sha512_crypt.html)
* [Using crypt module instead of passlib](https://security.stackexchange.com/questions/108872/unable-to-get-correct-base-for-cracking-crypt3-sha-512-on-linux-with-python)
* [Encryption used for shadow files](http://man7.org/linux/man-pages/man3/crypt.3.html)
* [Reason for the "ISO-8859-1" encoding](https://stackoverflow.com/questions/19699367/unicodedecodeerror-utf-8-codec-cant-decode-byte)
* [How I found passlib](https://stackoverflow.com/questions/21090312/hashlib-vs-crypt-crypt-in-python-why-different-results)
* [Password lists](https://wiki.skullsecurity.org/Passwords)
