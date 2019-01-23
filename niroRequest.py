import re

class niroRequest:
	"""A model to hold HTTP Request data"""

	headers = {}
	body = ''
	startLine = ""
	path = ""
	httpVerb = ""
	uriToMatch = None

	def __init__(self, startLine, headers):
		self.headers = headers 
		self.startLine = startLine


	def getPath(self):
		# get path from startline
		if(self.startLine != None):
			result = re.match("([A-Za-z]+) (.*) HTTP/[0-9]\.[0-9]", self.startLine)
			result = result.group(2)
			self.path = result
			return result
		else:
			return None


	def getPathAndVerb(self):
		# get path from startline
		if(self.startLine != None):
			result = re.match("([A-Za-z]+) (.*) HTTP/[0-9]\.[0-9]", self.startLine)
			self.path = result.group(2)
			self.httpVerb = result.group(1)
			return (result.group(2), result.group(1))
		else:
			return None


	def setPath(self, path):
		self.path = path

	def setNextMatch(self, nextMatch):
		self.uriToMatch = nextMatch

	def getUriToMatch(self):
		return self.uriToMatch


