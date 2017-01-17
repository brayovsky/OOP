#This is a high level example of OOP 
#The example seeks to demonstrate OOP from the point of a company KFCP(Kariobangi Fried Chicken and Potatoes) extending itself to its branches

class KFCPY(object):
	def __init__(self,funds,store):
		self.funds=funds
		self.store=store #say taken from a database and passed to the constructor
		self.name="Kariobangi Fried Chicken and Potatoes"
	    self.logo = "@KfcP"

	#serves as an abstract method. A customer can only be served from a branch
	def serve_customer():
		pass
	#serves as an abstract method. Branches have to market themselves using the logo
	def market():
		pass


