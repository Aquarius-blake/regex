import re

def CheckValidHexaCode(str):
		regex = "^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"

			p = re.compile(regex)

				if(str == None):
							return False

								if(re.search(p, str)):
											return True
												else:
													