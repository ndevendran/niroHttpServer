import niroResponse


urlList = [('/', 'indexPage')]

def buildResponse(request):
	response = indexPage()
	return response



def indexPage():
	responseObject = niroResponse.niroResponse()
	responseObject.setContentType("text/html")
	responseObject.setContentEncoding("none")
	responseObject.setStatusCode("HTTP/1.1 200 OK")
	responseObject.setBody("Hello World. This time with routing")
	return responseObject
