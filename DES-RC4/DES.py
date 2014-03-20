from pyDes import *
data = "key key"
k = des("DESCRYPT" ,CBC,"\0\0\0\0\0\0\0\0", pad =None, padmode = PAD_PKCS5)
d = k.encrypt(data)
print "Encrypted : %r" %d
print "Decrypted : %r" % k.decrypt(d)
assert k.decrypt(d,padmode=PAD_PKCS5) == data
