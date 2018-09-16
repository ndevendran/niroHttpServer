class niroRequest:
	"""A model to hold HTTP Request data"""

	headers = {}
	body = ''
	startLine = ""

	def __init__(self, startLine, headers):
		self.headers = headers 
		self.startLine = startLine

