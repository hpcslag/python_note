from Tkinter import *

class GUI(Frame):
	_text = 'Hello world'
	count = 0
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.grid()
		self.createWidgets()

	def createWidgets(self):
		self.inputText = Label(self)
		self.inputText["text"] = "Input: "
		self.inputText.grid(row=0, column=0)
		self.inputField = Entry(self)
		self.inputField["width"] = 50
		self.inputField.insert(0, self._text)
		self.inputField.grid(row=0, column=1, columnspan=6)

		self.new = Button(self)
		self.new['text'] = 'new'
		self.new.grid(row=2,column=2)
		self.new["command"] = self.newMethod #run event (newMethod)

	def newMethod(self):
		self.inputField.delete(0,200)
		self.inputField.insert(0,"Who are you?")
		self.count += 1
		print ("Someone click the button! count:",self.count)

if __name__ == '__main__':
    root = Tk()
    root.title("Hello world")
    app = GUI(master=root)
    app.mainloop()
