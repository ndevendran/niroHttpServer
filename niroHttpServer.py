import socket
import logging
import errno
from time import sleep
import re
from niroRequest import niroRequest
import mockRouter



serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
CHUNK_SIZE = 2

serversocket.bind(('127.0.0.1', 8080))
serversocket.listen(5)
logging.basicConfig(filename='../HTTPServer/logs/server.log',level=logging.DEBUG)
logging.info("Server started...")


def readRequest(sock):
	headers = {}
	startLine = readStartLine(sock)
	while 1:	
		(key, header) = readNextHeader(sock)
		if(header == None):
			#read all headers
			break
		headers[key] = header

	newRequest = niroRequest(startLine, headers)
	return newRequest

def readStartLine(sock):
	startLine = ""
	expectingLF = False
	chunk = sock.recv(CHUNK_SIZE).decode("utf-8")
	while len(chunk):	
		startLine += chunk
		if '\r\n' in startLine:
			return startLine
		chunk = sock.recv(CHUNK_SIZE).decode("utf-8")

	return None

def readNextHeader(sock):
	#code to read header here
	headerKey = ""
	headerValue = ""
	haveKey = False
	while not haveKey:
		print("Parsing header keys...")
		chunk = sock.recv(CHUNK_SIZE).decode("utf-8")
		if '\r\n' in chunk:
			print("Returning none...")
			return (None, None)
		if chunk == ':':
			haveKey = True
		else:
			headerKey += chunk

	while '\r\n' not in headerValue:
		print("Parsing header value...")
		chunk = sock.recv(CHUNK_SIZE).decode("utf-8")
		if not chunk:
			return (None, None)
		headerValue += chunk

	return (headerKey, headerValue)





def readBody(sock, contentLength):
	# Given a content length read next message
	try:
		chunk = sock.recv(contentLength)
		print("Received %d bytes" % (len(chunk)))
		print("Expected %d bytes" % (contentLength))
	except e:
		err = e.args[0]
		if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
			sleep(1)
			print('No data available')
		else:
			print(e)


def buildResponse(startLine, requestHeaders, requestBody):
	startArray = startLine.split(" ")
	version = startArray[2]
	statusLine = version.rstrip() + " 200 OK"
	body = "Hello World"
	contentLength = "Content-Length: " + str(len(body))
	contentType = "Content-Type: text/html"
	response = statusLine + "\r\n" + contentLength + "\r\n" + contentType + "\r\n\r\n"
	return (response, body)



def run():
	while 1:
		(clientsocket, address) = serversocket.accept()
		logging.info('Got connection')
		request = readRequest(clientsocket)
		print("Read in request...")
		body = ""
		contentLengthKey = "Content-Length"
		if contentLengthKey in request.headers:
			messageLength = headers[contentLengthKey]
			body = readBody(clientsocket, messageLength)

		print(request.headers)
		print(request.startLine)

		#(response, body) = buildResponse(request)
		router = mockRouter.Router()
		targetModule = __import__('mockRouter', globals(), locals(), [], 0)
		response = router.buildResponseFromTupleDict(request, targetModule)
		clientsocket.send(response.buildHeaders().encode())
		clientsocket.send(response.getBody().encode())
		logging.info('Sent response')
		clientsocket.close()


run()
