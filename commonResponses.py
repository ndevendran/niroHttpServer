import niroResponse

def pageNotFound():
	responseObject = niroResponse.niroResponse()
	responseObject.setContentType("text/html")
	responseObject.setContentEncoding("none")
	responseObject.setStatusCode("HTTP/1.1 404 NOT FOUND")
	responseObject.setBody("PAGE NOT FOUND")
	return responseObject


def textResponse(body):
	responseObject = niroResponse.niroResponse()
	responseObject.setContentType("text/html")
	responseObject.setContentEncoding("none")
	responseObject.setStatusCode("HTTP/1.1 200 OK")
	responseObject.setBody(body)
	return responseObject