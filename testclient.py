from Blowfish import *
from RC4 import *
from Constant import *
from time import time

key = Constant.keyblowfish
cipher = Constant.cipherkey
cipher.initCTR()
    
if __name__ == '__main__':
    if not Blowfish.testVectors():
        print "WARNING: The implementation doesn't pass algorithm test vectors!"
    else:
        print "The implementation passes algorithm test vectors (ECB)."

    t1=time();
    Constant.times = t1;
    file = raw_input("Enter the file name:");
    text = open(file).read()
    print "Blowfish CTR Mode encryption:"
    print 'Cipher Instance\t\t',cipher
    print 'Cipher Key is\t',key
    print "\t\tPlain Text from file is:\t", text
    crypted = cipher.encryptCTR(text)
    print "\n\n\t\t\Blowfish Cipher Text:\t", repr(crypted)
##    x = file[-3:];
##    if(x == "txt"):
##        frmat=1;
##    else:
##        frmat=0;

    import networkclient
    #networkclient.send(frmat)
    networkclient.send(crypted)
    
    

def decryptBlowfish(data):
    data = cipher.decryptCTR(data)
    return data

def encryptBlowfish(text):
    print "\tText in file:\t\t", text
    crypted = cipher.encryptCTR(text)
    print "\tEncrypted:\t", repr(crypted)
    return crypted
