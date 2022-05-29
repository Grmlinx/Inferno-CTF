#!/usr/bin/python3


import SocketServer
import time
import threading
import os

class Service(SocketServer.BaseRequestHandler):

    def handle( self ):
	
	script_dir =os.path.dirname(__file__)
	rel_path = "key.private"
	abs_path = os.path.join(script_dir,rel_path)
        


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
    port = 50666
    host = '127.0.0.1'
    
    service = Service
    server = ThreadedService((host,port), service)

    server.allow_reuse_address = True

    server_thread = threading.Thread(target = server.serve_forever)

    server_thread.daemon = True
    server_thread.start()

    print "fraud started on port", port

    while (True) :time.sleep(60)

if (__name__=="__main__"):
    main()
