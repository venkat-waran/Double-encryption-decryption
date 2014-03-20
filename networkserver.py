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
                a=open("2.txt", 'w');
                a.write(repr(data));
                a.flush();
                a.close();
                print '\nEncrypted file is saved!.\t\t'
                x = open("2.txt").read();
                data = decrypt(x, key)
                print '\n\t2 RC4 Decrypted Text from saved file: \t',repr(data)
                self.transport.write(data)


class ADFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return AD()

reactor.listenTCP(1234, ADFactory())
reactor.run()
