from Blowfish import *
from time import time

class Constant:
    keyblowfish = 'this is the key'
    cipherkey = Blowfish (keyblowfish)
    times=0
    timee = 0
    def cipherinit():
        cipherkey.initCTR()
        return cipherkey
