from Blowfish import *
from RC4 import *
from Constant import *
from time import time

key = Constant.keyblowfish
cipher = Constant.cipherkey
##cipher = Blowfish(key)
cipher.initCTR()
    
if __name__ == '__main__':
    if not Blowfish.testVectors():
        print "WARNING: The implementation doesn't pass algorithm test vectors!"
    else:
        print "The implementation passes algorithm test vectors (ECB)."

    t1=time();
    Constant.times = t1;
    text = "pavan aravindh giridhar information security"
##    self:encryptBlowfish(text)
##    print "Testing encryption:"
##    xl = 123456
##    xr = 654321
##    print "\tPlain text: (%s, %s)" %(xl, xr)
##    cl, cr = cipher.cipher (xl, xr, cipher.ENCRYPT)
##    print "\tCrypted is: (%s, %s)" %(cl, cr)
##    dl, dr = cipher.cipher (cl, cr, cipher.DECRYPT)
##    print "\tUnencrypted is: (%s, %s)" %(dl, dr)
##
##    print "Testing block encrypt:"
##    text = 'testtest'
##    print "\tText:\t\t%s" %text
##    crypted = cipher.encrypt(text)
##    print "\tEncrypted:\t%s" % repr(crypted)
##    decrypted = cipher.decrypt(crypted)
##    print "\tDecrypted:\t%s" %decrypted

##    cipher = Constant.cipherkey
    print "Blowfish CTR Mode encryption:"
##    cipher.initCTR()
    print 'Cipher Instance\t\t',cipher
    print 'Cipher Key is\t',key
    print "\tPlain Text is:\t\t", text
    crypted = cipher.encryptCTR(text)
    print "\tBlowfish Cipher Text:\t", repr(crypted)
    
##    print 'RC4\n'
##    print '\t2 text\t\t',text
##    crypted = encrypt((crypted), key)
##    print '\t2 Encrypted text\t',(crypted)
##    crypted = decrypt(crypted, key)
##    print '\t2 Decrypted text\t',(crypted)
##    
##    cipher.initCTR()
##    decrypted = cipher.decryptCTR(crypted)
##    print "\tDecrypted:\t", decrypted

##    print "Testing CBC encrypt:"
##    cipher.initCBC()
##    text = "Owen's Ornery Old Oryx Obstructed Olga's Optics."
####    text = "The implementation passes algorithm test vectors (ECB)."
##    print "\t1 Text:\t\t", text
##    
##    crypted = cipher.encryptCBC(text)
##    print "\t1 Encrypted:\t", repr(crypted)
####    cipher.initCBC()
####    decrypted = cipher.decryptCBC(crypted)
####    print "\tDecrypted:\t", decrypted
##
##    print 'RC4\n'
##    print '\t2 text\t\t',text
##    crypted = encrypt(crypted, key)
##    print '\t2 Encrypted text\t',(crypted)
##    crypted = decrypt(crypted, key)
##    print '\t2 Decrypted text\t',(crypted)
##
##    cipher.initCBC()
##    decrypted = cipher.decryptCBC(crypted)
##    print "\t1 Decrypted:\t", decrypted

    import pavanclient
    pavanclient.send(crypted)
    
##    print "Testing speed"
##    from time import time
##    t1 = time()
##    n = 0
##    tlen = 0
##    while True:
##        for i in xrange(1000):
##            tstr = "The quick brown fox jumps over the lazy dog %d" % i
##            enc = cipher.encryptCTR(tstr)
##            tlen += len(tstr)
##        n += 1000
##        t2 = time()
##        if t2 - t1 > 5:
##            break
##    t = t2 - t1
##    print "%d encryptions in %0.1f seconds: %0.1f enc/s, %0.1f bytes/s" % (n, t, n / t, tlen / t)
##

def decryptBlowfish(data):
##    cipher.initCTR()
##    print 'key\t\t',cipher
    data = cipher.decryptCTR(data)
    return data

def encryptBlowfish(text):
##    cipher.initCTR()

##    print 'key\t\t',cipher
    print "\tText:\t\t", text
    crypted = cipher.encryptCTR(text)
    print "\tEncrypted:\t", repr(crypted)
    return crypted
