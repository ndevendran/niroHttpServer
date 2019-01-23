import niroResponse
import commonResponses
import re

urlTupleDict = {'/': [('GET', 'roseIndexPage')], '/rose': [('GET', 'roseRoseRose')], '/inline' : [('GET', 'roseAgain')]}

def buildResponseFromTupleDict(request, module):
	router = mockRouter.Router()
	return router.buildResponseFromTupleDict(request, module)



def roseIndexPage():
	return commonResponses.textResponse("This is the rose index page")


def roseRoseRose():
	return commonResponses.textResponse("Rose, rose, rose...")


def roseAgain():
	return commonResponses.textResponse("Edited the rose page while the server was running...")