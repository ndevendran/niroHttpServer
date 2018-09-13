import socket
import logging
import errno
from time import sleep
import re
from niroRequest import niroRequest


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
CHUNK_SIZE = 8

serversocket.bind(('127.0.0.1', 8080))
serversocket.listen(5)
logging.basicConfig(filename='../HTTPServer/logs/server.log',level=logging.DEBUG)
logging.info("Server started...")


def readHeaders(sock):
	chunks = []
	chunk = 'blah'
	sock.setblocking(False)
	bytes_recd = 0
	while 1:
		try:
			chunk = sock.recv(CHUNK_SIZE)
			print "Received %d bytes" % (len(chunk))
			chunks.append(chunk)
			bytes_recd = bytes_recd + len(chunk)
			if(len(chunk) == 0):
				break
		except socket.error, e:
			err = e.args[0]
			if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
				sleep(1)
				print 'No data available'
				#check to see if last chunk was end of message
				endOfHeaders = re.compile('.*\r\n\r\n')
				if endOfHeaders.match(chunk):
					break
				continue
			else:
				print e
				break
		
	return b''.join(chunks)

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

def buildRequestObject(message):
	# parse all possible headers
	# stick body message in
	startLinePattern = '([A-Z]{3,7}) (.+) HTTP.+([0-9].+[0-9])'
	headerPattern = '([A-Za-z]+\-?[A-Za-z]+\-?[A-Za-z]+):(.*)[\r\n]{1}'
	headerDict = {}
	startLine = re.search(startLinePattern, message)
	headers = re.split(headerPattern, message)
	if startLine:
		print "Parsing start line successfull"
	else:
		print "Failure. Start Line could not be parsed"

	if headers:
		index = 1
		while index < len(headers):
			headerValue = str(headers[index+1]).strip()
			headerKey = str(headers[index]).strip()
			headerDict[headerKey] = headerValue
			index = index + 3	# incrementing by 3 to pass over the value and an empty entry
						# the empty entry is a relic of the process being used
	else:
		print "Failure. Headers could not be parsed"

	return headerDict

def buildResponse(requestHeaders, requestBody):


def run():
	while 1:
		(clientsocket, address) = serversocket.accept()
		logging.info('Got connection')
		request = readHeaders(clientsocket)
		headers = buildRequestObject(request)
		body = ""
		contentLengthKey = "Content-Length"
		if contentLengthKey in headers:
			messageLength = headers[contentLengthKey]
			body = readBody(clientsocket, messageLength)

		(response, responseBody) = buildResponse(headers, body)

		clientsocket.send(response)
		clientsocket.send(responseBody)
		logging.info('Sent response')
		clientsocket.close()


run()
