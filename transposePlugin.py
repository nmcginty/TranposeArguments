import sublime, sublime_plugin, random, re
# from subprocess import call

class TransposeArgsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.run_command("expand_selection" , {"to": "brackets"})
		selection = self.view.sel() #list of all current selections / cursors
		
		for sel in selection:
			if(not sel.empty()):
				tranposedText = self.tranposeArg(self.view.substr(sel))
				self.view.replace(edit, sel, tranposedText)

			else:
				self.view.replace(edit, sel, "run command within ()")

		#sets cursor(s) back to beginning	
		self.view.run_command("move" , {"by": "characters", "forward": False})

	@staticmethod
	def tranposeArg(selectionText):
		
		#still have to fix this
		if("," not in selectionText): #no space means argument < 2 
			return selectionText

		args = selectionText.split(",")
		args.insert(0, args.pop())

		# args = [' '.join(arg.split()) for arg in args]
				
		print("finalList", args)

		print("final jawn", "(", ', '.join(args), ")")
		return ', '.join([' '.join(arg.split()) for arg in args])

class ReverseTransposeArgsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.run_command("expand_selection" , {"to": "brackets"})
		selection = self.view.sel() #list of all current selections / cursors
		
		for sel in selection:
			if(not sel.empty()):
				tranposedText = self.reverseTranposeArg(self.view.substr(sel))
				self.view.replace(edit, sel, tranposedText)

			else:
				self.view.replace(edit, sel, "run command within ()")

		#sets cursor(s) back to beginning	
		self.view.run_command("move" , {"by": "characters", "forward": False})

	@staticmethod
	def reverseTranposeArg(selectionText):

		#still have to fix this
		if("," not in selectionText): #no space means argument < 2 
			return selectionText

		args = selectionText.split(",")
		# args.insert(0, args.pop())
		args.append(args.pop(0))
				
		print("finalList", args)
		print("final jawn", "(", ', '.join(args), ")")

		return ', '.join([' '.join(arg.split()) for arg in args])

class RandTransposeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.run_command("expand_selection" , {"to": "brackets"})
		selection = self.view.sel() #list of all current selections / cursors
		
		for sel in selection:
			if(not sel.empty()):
				tranposedText = self.randTransposeArg(self.view.substr(sel))
				self.view.replace(edit, sel, tranposedText)

			else:
				self.view.replace(edit, sel, "run command within ()")

		#sets cursor(s) back to beginning	
		self.view.run_command("move" , {"by": "characters", "forward": False})

	@staticmethod
	def randTransposeArg(selectionText):
		#still have to fix this
		if("," not in selectionText): #no space means argument < 2 
			return selectionText

		args = selectionText.split(",")
		random.shuffle(args) #randomizes array

		print("finalList", args)
		print("final jawn", "(", ', '.join(args), ")")

		return ', '.join([' '.join(arg.split()) for arg in args])

class SelectAllArgsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.run_command("expand_selection" , {"to": "brackets"})
		sel = self.view.sel()[0] #string of arguments
		formattedText = self.formatArgs(self.view.substr(sel))
		count = formattedText.count(',')

		if(not sel.empty()):
			self.view.run_command("left_delete")
			self.view.insert(edit, sel.begin(), formattedText)
			self.selectAllArgs(self, count)

		else:
			self.view.insert(edit, sel.begin(), "run command within ()")

	@staticmethod		
	def formatArgs(selText):
		#still have to fix this
		if("," not in selText): #no space means argument < 2 
			return selText

		# the craziest peice of crazyness
		return ', '.join([' '.join(arg.split()) for arg in selText.split(",")])

	@staticmethod
	def selectAllArgs(self, count):

		#to position the cursor at the beginning of first argument
		self.view.run_command("move_to" , {"to": "brackets"})

		#mark the first argument
		self.view.run_command("mark_and_move_do_it_all")

		for x in range(count):
			while(True):
				sel = self.view.sel()[0] #string of arguments
				self.view.run_command("move", {"by": "characters", "forward": True})
				self.view.run_command("move" , {"by": "characters", "forward": True, "extend": True})
				char  = self.view.substr(sel)
				print("Current Char", char)

				if(char == ','):
					print("I MARKED HERE")
					self.view.run_command("move", {"by": "characters", "forward": True})
					self.view.run_command("mark_and_move_do_it_all")
					break

		self.view.run_command("mark_and_move_do_it_all")