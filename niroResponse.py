class niroResponse:
	""" A model to hold response data """

	headers = {}
	body = ""

	def __init__(self):
		headers = {}
		statusCode = ""
		body = ""



	def setContentType(self, contentType):
		self.headers['content-type'] = contentType

	def setCacheControl(self, directive):
		self.headers['cache-control'] = directive

	def setContentEncoding(self, encoding):
		self.headers['content-encoding'] = encoding

	def setContentLength(self):
		if(self.body != None):
			self.headers['content-length'] = str(len(self.body))
		else:
			self.headers['content-length'] = str(0)

	def setTrailer(self, trailer):
		self.headers['trailer'] = trailer


	def setBody(self, body):
		self.body = body

	def setStatusCode(self, status):
		self.statusCode = status


	def getContentType(self):
		if self.headers.has_key("content-type"):
			return self.headers['content-type']
		else:
			return None


	def getCacheControl(self):
		if self.headers.has_key("cache-control"):
			return self.headers['cache-control']
		else:
			return None

	def getContentEncoding(self):
		if self.headers.has_key("content-encoding"):
			return self.headers['content-encoding']
		else:
			return None
	
	def getTrailer(self):
		if self.headers.has_key("trailer"):
			return self.headers['trailer']
		else:
			return None

	def getBody(self):
		return self.body

	def getStatusCode(self):
		return self.statusCode

	def buildHeaders(self):
		self.setContentLength()
		responseHeaders = ""
		responseHeaders = self.getStatusCode() + "\r\n"
		for key,value in self.headers.items():
			responseHeaders = responseHeaders + key + ":" + value + "\r\n"

		responseHeaders = responseHeaders + "\r\n"

		return responseHeaders

