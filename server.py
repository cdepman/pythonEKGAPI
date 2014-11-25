## this code sets up a simple python server that awaits instructions from
## our Node.js server using Zerorpc

import zerorpc
from mssql import connect

class rpc(object):
    print "Python server ENGAGE!"

    # receives confirmation from Node server 
    def hello(self, name):
        print "Node greeting request received, response sending..."
        return "This is python. Hello, %s" % name

    def nodeRequest(self, startTime, endTime):
        print "Node data request received, response sending..."
        return connect(self, startTime, endTime)   

server = zerorpc.Server(rpc())
server.bind("tcp://0.0.0.0:4242")
server.run()