import re

class niroRequest:
	"""A model to hold HTTP Request data"""

	headers = {}
	body = ''
	startLine = ""

	def __init__(self, startLine, headers):
		self.headers = headers 
		self.startLine = startLine


	def getPath(self):
		# get path from startline
		if(self.startLine != None):
			result = re.match("([A-Za-z]+) (.*) HTTP/[0-9]\.[0-9]", self.startLine)
			result = result.group(2)
			return result
		else:
			return None


