from twisted.internet import protocol, reactor
from RC4 import *
key = 'this is the key'
msg=''
class AD(protocol.Protocol):
        
	def dataReceived(self,data):
		
		print "The encrypted data that has been recieved is "+repr(data)
		print 'RC4\n'
                
                data = encrypt(data, key)
                print '\t2 RC4 Encrypted Cipher Text\t',repr(data)
                print '\t' 
                data = decrypt(data, key)
                print '\t2 RC4 Decrypted Text\t',repr(data)
                self.transport.write(data)


class ADFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return AD()

reactor.listenTCP(1234, ADFactory())
reactor.run()
