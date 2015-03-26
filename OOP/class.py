#coding=UTF-8

class Account:
	def __init__(self,name):
		self.name = name
		print(name)
	def show(self):
		print ("Your name is: ",self.name)

A = Account(1)
A.show()
