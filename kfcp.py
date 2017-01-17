#This is a high level example of OOP 
#The example seeks to demonstrate OOP from the point of a company KFCP(Kariobangi Fried Chicken and Potatoes) extending itself to its branches

class KFCPY(object):
	def __init__(self,funds,storage):
		self.funds=funds 
		self.storage=storage
		self.name="Kariobangi Fried Chicken and Potatoes"
	    self.logo = "@KfcP"

	#serves as an abstract method. A customer can only be served from a branch
	def serve_customer(self):
		pass
	#serves as an abstract method. Branches have to market themselves using the logo
	def market(self):
		pass
	#each class branch can pretend it has its own money but we all know its at the HQ
	def release_funds(self,ammount):
		if(ammount>self.funds):
			print("We don't have that kind of money")
		else:
		    self.funds -= ammount
	#all profits are hendled at the main
 	def deposit_profit(self,ammount):
 		self.funds+=ammount

class KariobangiNorthBranch(KFCP):
	def __init__(self,funds,storage):
		super().__init__(funds,storage)
		self.local_name = "Kariobangi North Branch"

	#implement serve custmer
	def serve_customer(self):
		print("Welcome to %s %s"%(self.name,self.local_name))

	def market(self):
		print("We have the best fried Potatoes and Chicken in %s %s" %(self.name,self.local_name))

class KariobangiSouthBranch(KFCP):
	def __init__(self,funds,storage):
		super().__init__(funds,storage)
		self.local_name = "Kariobangi South Branch"
		#unique to Kariobangi South
		self.mantra = "East, West, South is the best"

	#implement serve custmer
	def serve_customer(self):
		print("Welcome to %s %s. %s"%(self.name,self.local_name,self.mantra))

	def market(self):
		print("We have the best fried Potatoes and Chicken in %s %s.%s" %(self.name,self.local_name,self.mantra))