"""
TransparentRemote
Copyright (C) 2020-current Mehmet-Ali Asar
"""

from remote import Remote
from threading import Thread

def web_loop(remote,file,stop):
    from webserver import Webserver
    while(not stop):

        #Checks the received data for matching strings and acts accordingly when the matching is successful
        web_data=Webserver().auto()
        if web_data==b"CLOSE_FILE":
            remote.autoSwitch()
            file.close()
            break
        elif web_data==b"SWITCH_HDMI":
            remote.autoSwitch()

    #This will make sure that our keyboard_loop thread will be stopped
    stop=True

def keyboard_loop(remote,file,stop):
    from struct import unpack
    
    #We make sure that we have everything neutralized
    left_alt,right_alt=False,False
    
    while(not stop):

        #This reads and unpacks file that contains the keyboard data stream
        data=file.read(24)
        key,pressed=unpack('4IHHI',data)[5:7]

        #This checks if the left ALT button is pressed
        if(key==56 and pressed==1 and left_alt==False):
            left_alt=True
        elif(key==56 and pressed==0):
            left_alt=False

        #This checks if the right ALT button is pressed
        if(key==100 and pressed==1 and right_alt==False):
            right_alt=True
        elif(key==100 and pressed==0):
            right_alt=False

        #If both ALT buttons are actively being pressed, a command to switch the HDMI input is being sent to the TV's web API.
        if(left_alt==True and right_alt==True):
            remote.autoSwitch()
            left_alt=False
            right_alt=False

try:
    remote=Remote("192.168.178.92")
    file=open("/dev/input/by-id/usb-SEM_USB_Keyboard-event-kbd","rb")
    stop=False

    #Here we create two seperate threads inside the same CPU core to run two seperate while loops
    web=Thread(target=web_loop,args=(remote,file,stop,))
    keyboard=Thread(target=keyboard_loop,args=(remote,file,stop,))
    web.start()
    keyboard.start()

    #And finally we wait for both of them to peacefully end
    web.join()
    keyboard.join()
except Exception as e:
    #If shit hits the fan, we get error message printed on our CLI.
    print(e)
