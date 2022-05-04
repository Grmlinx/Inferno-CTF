#!/usr/bin/python3


import SocketServer
import time
import threading
import random

class Service(SocketServer.BaseRequestHandler):

    def handle( self ):

        print ("someone connected!")

        handle = open('/dev/urandom')
        
        offset = random.randint( 15, 45 )
        starting_time = int(time.time())


        while ( True ):
            if ( int(time.time()) != starting_time + offset ):
                self.send(handle.read(1), newline = False )
            else:
                flag = 'ExecuteOrder666'
                self.send( flag, newline = False )

                offset = random.randint( 14, 45 )

    def send( self, string, newline = True ):

        if newline:
            string = string + "\n"
        self.request.sendall(string)

    def receive( self, prompt = " > "):
        self.send( prompt, newline = False )
        return self.request.recv( 4096 ).strip()

class ThreadedService(SocketServer.ThreadingMixIn, SocketServer.TCPServer, SocketServer.DatagramRequestHandler):
    pass

def main ():
    port = 60666
    host = '127.0.0.1'
    
    service = Service
    server = ThreadedService((host,port), service)

    server.allow_reuse_address = True

    server_thread = threading.Thread(target = server.serve_forever)

    server_thread.daemon = True
    server_thread.start()

    print "server started on port", port

    while (True) :time.sleep(60)

if (__name__=="__main__"):
    main()
