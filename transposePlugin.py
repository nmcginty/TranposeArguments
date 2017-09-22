import sublime, sublime_plugin
from subprocess import call

# class ExampleCommand(sublime_plugin.TextCommand):
# 	def run(self, edit):
# 		self.view.insert(edit, self.view.sel()[0].begin(), "Hello, World!")

class TransposeArgsCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		self.view.run_command("expand_selection" , {"to": "brackets"})
		sel = self.view.sel()[0]
		tranposedText = self.tranposeArg(self.view.substr(sel))

		if(not sel.empty()):
			self.view.run_command("left_delete")
			self.view.insert(edit, self.view.sel()[0].begin(), tranposedText)

		else:
			self.view.insert(edit, self.view.sel()[0].begin(), "run command within ()")

	@staticmethod
	def tranposeArg(selectionText):

		args = []
		text = ""

		if(' ' not in selectionText): #no space means argument < 2 
			return selectionText

		for c in selectionText:
			
			if(c == " "):
				args.append(text)
				print("text", text)
				text = ""
			else:
			 	text += c
		args.append(text)

		print("args", args)

		for x in range(len(args)):
			args[x] = (args[x][:-1]) if (args[x][-1] == ',') else (args[x])

		newList = []
		newList.append(args[-1]) # adds last element to list

		for x in range(len(args)-1):
			newList.append(args[x])
				
		print("newList", newList)


		for x in range(len(newList)-1):
			newList[x] += ", "

		print("newList", newList)

		return ''.join(newList)

class ReverseTransposeArgsCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		self.view.run_command("expand_selection" , {"to": "brackets"})
		sel = self.view.sel()[0]
		tranposedText = self.tranposeArg(self.view.substr(sel))

		if(not sel.empty()):
			self.view.run_command("left_delete")
			self.view.insert(edit, self.view.sel()[0].begin(), tranposedText)

		else:
			self.view.insert(edit, self.view.sel()[0].begin(), "run command within ()")

	@staticmethod
	def tranposeArg(selectionText):

		args = []
		text = ""

		if(' ' not in selectionText): #no space means argument < 2 
			return selectionText

		for c in selectionText:
			
			if(c == " "):
				args.append(text)
				print("text", text)
				text = ""
			else:
			 	text += c
		args.append(text)

		print("args", args)

		for x in range(len(args)):
			args[x] = (args[x][:-1]) if (args[x][-1] == ',') else (args[x])

		print("args", args)

		newList = [arg for arg in args[1:]] #creates list with everything but first element
				
		newList.append(args[0]) # adds last element to list
		print("newList", newList)

		# print("THIIIISS", newList[:len(newList)-1])
		finalList = [arg + ", " for arg in newList[:len(newList)]] #add ", " to every string except last
		finalList[-1] = finalList[-1][:-2] #delete the extra ", " from last element
		# finalList[-1] = finalList[-1][:-1]

		# for x in range(len(newList)-1):
		# 	newList[x] += ", "

		print("finalList", finalList)
		print(''.join(finalList))
		return ''.join(finalList) #puts all elements into empty string



		






		# args = args[::-1] #reverses list


				# for c in args:
		# 	if(c.strip()[-1] == ','): #ends with ,
		# 		c = c[:-1] #then take it away

		# for x in range(len(args)-1):
		# 	if(args[x].strip()[-1] == ','): #ends with ,
		# 		args[x] = (args[x])[:-1] #then take it away


		#must do this next
		#work for multi-cursor
		#(dog, cat, monkey) - > (monkey, dog, cat)
		# support for {} and other things
		# support for just two words would have to 
		# go from space word1 word2 space
		# also has to work for this like int x, double y
		# ctrl alt t, show cycle through arguments left to right
		# ctrl shift alt t, would go right to left