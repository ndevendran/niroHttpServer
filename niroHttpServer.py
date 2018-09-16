import socket
import logging
import errno
from time import sleep
import re
from niroRequest import niroRequest



serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
CHUNK_SIZE = 1

serversocket.bind(('127.0.0.1', 8080))
serversocket.listen(5)
logging.basicConfig(filename='../HTTPServer/logs/server.log',level=logging.DEBUG)
logging.info("Server started...")


def readRequest(sock):
	headers = {}
	currentLine = bytearray()
	chunk = 'CURRENT_BYTE'
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
	startLine = bytearray()
	expectingLF = False
	while 1:
		chunk = sock.recv(CHUNK_SIZE)
		if(chunk == '\r'):
			if not expectingLF:
				expectingLF = True
			if expectingLF:
				print startLine.decode("utf-8")
				#raise SyntaxError("Received CR when expecting LF")
		if(chunk == '\n'):
			if expectingLF:
				startLine.append(chunk)
				return startLine.decode("utf-8")
			else:
				raise SyntaxError("Received LF before CR")
		startLine.append(chunk)

def readNextHeader(sock):
	#code to read header here
	headerKey = bytearray()
	headerValue = bytearray()
	keyString = ""
	valueString = ""
	expectingLF = False
	haveKey = False
	while 1:
		chunk = sock.recv(CHUNK_SIZE)
		if(chunk == '\r'):
			if not expectingLF:
				expectingLF = True
		if(chunk == '\n'):
			if expectingLF:
				if not haveKey:
					return (None,None)
				else:
					headerValue.append(chunk)
					valueString = headerValue.decode("utf-8")
					keyString = headerKey.decode("utf-8")
					return (keyString, valueString)
		if(chunk == ':'):
			if not haveKey:
				haveKey = True
				continue
		if haveKey:
			headerValue.append(chunk)
		else:
			headerKey.append(chunk)





def readBody(sock, contentLength):
	# Given a content length read next message
	try:
		chunk = sock.recv(contentLength)
		print "Received %d bytes" % (len(chunk))
		print "Expected %d bytes" % (contentLength)
	except socket.error, e:
		err = e.args[0]
		if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
			sleep(1)
			print 'No data available'
		else:
			print e


def buildResponse(requestHeaders, requestBody):
	return "Hello World"


def run():
	while 1:
		(clientsocket, address) = serversocket.accept()
		logging.info('Got connection')
		request = readRequest(clientsocket)
		body = ""
		contentLengthKey = "Content-Length"
		if contentLengthKey in request.headers:
			messageLength = headers[contentLengthKey]
			body = readBody(clientsocket, messageLength)

		print request.headers
		print request.startLine

		response = buildResponse(request.headers, body)

		clientsocket.send(response)
		logging.info('Sent response')
		clientsocket.close()


run()
