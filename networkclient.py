from twisted.internet import reactor
from twisted.internet.protocol import Protocol
from twisted.internet.endpoints import TCP4ClientEndpoint, connectProtocol
from Blowfish import *
from Constant import *
from time import time

cipher = Constant.cipherkey
key = Constant.keyblowfish

class Greeter(Protocol):
    message=""
    def sendMessage(self):
        self.transport.write(self.message)
        
    def dataReceived(self,data):

        cipher.initCTR()
        print 'Cipher Instance is \t\t',cipher

        data = cipher.decryptCTR(data)
        print "\n\tDecrypted Plain Text:\t", repr(data)
        a = open("1.mp3", 'w');
        a.write(repr(data));
        a.flush();
        a.close();
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
