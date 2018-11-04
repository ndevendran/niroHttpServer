import niroResponse


urlDict = {'/': 'indexPage', '/rose': 'rosePage'}

def buildResponse(request):
	path = request.getPath()
	if(path in urlDict.keys()):
		print "The path is in urlDict"
		response = indexPage()
		functions = globals()
		functionName = urlDict[path]
		print functions.keys()
		if functionName in functions.keys():
			print "We got to functions of keys"
			response = functions[functionName]()
		else:
			response = pageNotFoundResponse()
	else:
		response = pageNotFoundResponse()
	
	return response



def indexPage():
	responseObject = niroResponse.niroResponse()
	responseObject.setContentType("text/html")
	responseObject.setContentEncoding("none")
	responseObject.setStatusCode("HTTP/1.1 200 OK")
	responseObject.setBody("Hello World. This time with routing")
	return responseObject


def pageNotFoundResponse():
	responseObject = niroResponse.niroResponse()
	responseObject.setContentType("text/html")
	responseObject.setContentEncoding("none")
	responseObject.setStatusCode("HTTP/1.1 404 NOT FOUND")
	responseObject.setBody("PAGE NOT FOUND")
	return responseObject


def rosePage():
	responseObject = niroResponse.niroResponse()
	responseObject.setContentType("text/html")
	responseObject.setContentEncoding("none")
	responseObject.setStatusCode("HTTP/1.1 200 OK")
	responseObject.setBody("This is the rose page")
	return responseObject
