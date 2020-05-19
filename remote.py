"""
TransparentRemote
Copyright (C) 2020-current Mehmet-Ali Asar
"""

import socket
from base64 import b64encode

class Remote():
	def __init__(self,tvip,tvport=55000):
		self.tvip=tvip
		self.tvport=tvport
		self.sock=None
		
	def prepare(self):
		"""Prepares the socket"""
		self.sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def connect(self):
		"""Connects to the TV's webservice"""
		self.sock.connect((self.tvip,self.tvport))

	def authenticate(self):
		"""Asking for TV to give the remote the needed permission"""
		self.sock.send(((3*chr(0x00))+chr(len(chr(0x64)))+chr(0x00)+chr(0x64)).encode())

	def sendKey(self,key):
		"""Sends codes to the webservice of the TV"""
		self.sock.send(((8*(b"\x00")).decode("utf-8")+chr(len(b64encode(key)))+chr(0x00)+(b64encode(key)).decode("utf-8")).encode('utf-8'))

	def close(self):
		"""Closes the connection to the webservice"""
		self.sock.close()
		self.sock=None
		
	def autoSwitch(self):
		"""Switches from HDMI to HDMI input automatically"""
		self.prepare()
		self.connect()
		self.authenticate()
		self.sendKey(b"KEY_HDMI")
		self.close()
