class niroRequest:
	"""A model to hold HTTP Request data"""

	headers = {}
	body = ''

	def __init__(self, firstHeader):
		headers = {}
		body = ''
		headers["VERB"] = firstHeader