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
		
		#still have to fix this
		if(", " not in selectionText): #no space means argument < 2 
			return selectionText

		args = selectionText.split(", ")
		args.insert(0, args.pop())
				
		print("finalList", args)

		print("final jawn", "(", ', '.join(args), ")")
		return ', '.join(args)

class ReverseTransposeArgsCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		self.view.run_command("expand_selection" , {"to": "brackets"})
		sel = self.view.sel()[0]
		tranposedText = self.reverseTranposeArg(self.view.substr(sel))

		if(not sel.empty()):
			self.view.run_command("left_delete")
			self.view.insert(edit, self.view.sel()[0].begin(), tranposedText)

		else:
			self.view.insert(edit, self.view.sel()[0].begin(), "run command within ()")


	@staticmethod
	def reverseTranposeArg(selectionText):

		#still have to fix this
		if(", " not in selectionText): #no space means argument < 2 
			return selectionText

		args = selectionText.split(", ")
		# args.insert(0, args.pop())
		args.append(args.pop(0))
				
		print("finalList", args)

		print("final jawn", "(", ', '.join(args), ")")
		return ', '.join(args)


		#must do this next
		#work for multi-cursor
		#(dog, cat, monkey) - > (monkey, dog, cat)
		# support for {} and other things
		# support for just two words would have to 
		# go from space word1 word2 space
		# also has to work for this like int x, double y
		# ctrl alt t, show cycle through arguments left to right
		# ctrl shift alt t, would go right to left