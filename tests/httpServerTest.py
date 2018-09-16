import sys
import socket
import requests
sys.path.append("..")

import unittest
import requests
from threading import Thread 

class TestGetRequest(unittest.TestCase):
	
	def testBasicGetRequest(self):
		r = requests.get('http://127.0.0.1:8080')
		self.assertEqual(r.status_code, 200)
		self.assertEqual(r.text, "Hello World")



if __name__ == '__main__':
	unittest.main()