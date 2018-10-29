import re

class niroRequest:
	"""A model to hold HTTP Request data"""

	headers = {}
	body = ''
	startLine = ""

	def __init__(self, startLine, headers):
		self.headers = headers 
		self.startLine = startLine


	def getPath():
		# get path from startline
		if(self.startLine != None):
			result = re.match("([A-Za-z]+) (.*) HTTP/[0-9]\.[0-9]", self.startLine)
			return result.group(2)
		else:
			return None


