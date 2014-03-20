from twisted.internet import reactor
from twisted.internet.protocol import Protocol
from twisted.internet.endpoints import TCP4ClientEndpoint, connectProtocol
from Blowfish import *
from Constant import *
from time import time

cipher = Constant.cipherkey
key = Constant.keyblowfish
##cipher = Blowfish(key)
class Greeter(Protocol):
    message=""
    def sendMessage(self):
        self.transport.write(self.message)
        #reactor.stop()
    def dataReceived(self,data):
##        print "\tServer response : \t"+repr(data)
        cipher.initCTR()
        print 'Cipher Instance is \t\t',cipher
##        print 'key\t',key
        data = cipher.decryptCTR(data)
        print "\tDecrypted Plain Text:\t", repr(data)
        Constant.timee = time();
        print '\tExecution time for Double Encryption:\t' , (Constant.timee - Constant.times) ,'seconds'

def gotProtocol(p):
    p.sendMessage()
        
    
def send(m):
    point = TCP4ClientEndpoint(reactor, "localhost", 1234)
    g = Greeter()
    g.message = m
    d = connectProtocol(point,g)
    d.addCallback(gotProtocol)
    reactor.run()
