import niroResponse
import commonResponses
import re

# def buildResponse(request):
# 	path = request.getPath()
# 	if(path in urlDict.keys()):
# 		print("The path is in urlDict")
# 		response = indexPage()
# 		functions = globals()
# 		functionName = urlDict[path]
# 		if functionName in functions.keys():
# 			response = functions[functionName]()
# 		else:
# 			response = commonResponses.pageNotFound()
# 	else:
# 		response = commonResponses.pageNotFound()
	
# 	return response

# urlDict = {'/': 'indexPage', '/rose': 'rosePage'}

urlTupleDict = {'/': [('GET', 'indexPage')],'/rose': [('GET','roseModule')]}

def buildResponseFromTupleDict(request, module):
	router = Router()
	return router.buildResponseFromTupleDict(request, module)


class Router():

	def buildResponseFromTupleDict(self, request, module):
		leftovers = ""

		if(module != None):
			moduleDirectory = dir(module)
		
		(requestPath, requestVerb) = request.getPathAndVerb()

		uriToMatch = request.getUriToMatch()
		if(uriToMatch != None):
			currentUri = uriToMatch
		else:
			currentUri = requestPath

		functions = globals()

		
		while (currentUri not in module.urlTupleDict.keys() and currentUri != "/"):
			print("Working on URI: " + currentUri)
			newUri = ""
			uriList = currentUri.split('/')
			leftovers += "/" + "".join(uriList[len(uriList)-1:])
			uriList = uriList[0:len(uriList)-1]
			
			newUri = "/".join(uriList)

			if(newUri == ""):
				return commonResponses.pageNotFound()
			else:
				currentUri = newUri

		print("Current URI We are Looking Up: " + currentUri)

		if(currentUri not in module.urlTupleDict.keys()):
			return commonResponses.pageNotFound
			
		for tuple in urlTupleDict[currentUri]:
			if (tuple[0] == requestVerb):
				targetName = tuple[1]
				try:
					print("Trying to import " + targetName)
					targetModule = __import__(targetName, globals(), locals(), [], 0)
					routerFunctions = dir(targetModule)
					print("Successful import")
					if 'buildResponseFromTupleDict' in routerFunctions and 'urlTupleDict' in routerFunctions:
						print("Found routing function in imported module")
						if(leftovers == ""):
							leftovers += "/"
						request.setNextMatch(leftovers)

						return targetModule.buildResponseFromTupleDict(request, targetModule)
				except Exception as e:
					if targetName in functions.keys():
						return functions[targetName]()
					else:
						print(e)

		return commonResponses.pageNotFound()



def panicEcho():
	print("PANIC")

def indexPage():
	return commonResponses.textResponse("Hello World. This time with routing")


def rosePage():
	return commonResponses.textResponse("This is the rose page")

def privateRosePage():
	return commonResponse.textResponse("You shouldn't be in here!!!")
