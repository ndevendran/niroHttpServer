import sys
import socket
import requests
sys.path.append("..")

import unittest
import requests
from threading import Thread 

class TestGetRequest(unittest.TestCase):
	
	def testBasicGetRequest(self):
		requests.get('http://127.0.0.1:8080')



if __name__ == '__main__':
	unittest.main()