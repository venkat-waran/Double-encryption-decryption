from Crypto.Cipher import Blowfish
from base64 import b64encode, b64decode
passw='secretPassword12'
ntext='helloworld123456'

cipher=Blowfish.new(passw, Blowfish.MODE_ECB)
encStr=b64encode(cipher.encrypt(data))
print encStr
