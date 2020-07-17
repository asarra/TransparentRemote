"""
TransparentRemote
Copyright (C) 2020-current Mehmet-Ali Asar
"""
from socket import *

class Webserver():
    def __init__(self,myip=gethostbyname(gethostname()),myport=69):
        self.myip=myip
        self.myport=myport
        
    def prepare(self):
        """Creates the socket"""
        self.server=socket(AF_INET,SOCK_STREAM)

    def listen(self):
        """Starts to listen to the socket"""
        self.server.bind((myip,myport))
        self.server.listen(1)

    def serve(self):
        """Awaits and sends the data of our hook handler client to our remote"""
        while(1):
            try:
                (client,_)=self.server.accept()
                data=client.recv(16)
                if(data==b"SWITCH_HDMI" or data==b"CLOSE_FILE"):
                    return data
                client.shutdown(SHUT_WR)
                client.close()
            except:
                pass

    def close(self):
        """Closes the socket of the webserver"""
        self.server.close()

    def auto(self):
        """Because I am lazy"""
        self.prepare()
        self.listen()
        self.serve()
        self.close()
