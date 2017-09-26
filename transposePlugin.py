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

		args = [arg.strip() for arg in args]
				
		print("finalList", args)

		print("final jawn", "(", ', '.join(args), ")")
		return ', '.join(args)

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
		args = [arg.strip() for arg in args]
				
		print("finalList", args)

		print("final jawn", "(", ', '.join(args), ")")
		return ', '.join(args)

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

		args = [arg.strip() for arg in args]
				
		print("finalList", args)

		print("final jawn", "(", ', '.join(args), ")")
		return ', '.join(args)

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


		# self.view.run_command("expand_selection" , {"to": "brackets"})
		# selection = self.view.sel() #list of all current selections / cursors
		
		# for sel in selection:
		# 	if(not sel.empty()):
		# 		formattedText = self.formatArgs(self.view.substr(sel))
		# 		count = formattedText.count(',')
		# 		self.view.replace(edit, sel, formattedText)	
		# 		# self.view.run_command("left_delete")
		# 		# self.view.insert(edit, sel.begin(), formattedText)
		# 		self.selectAllArgs(self, count)

		# 	else:
		# 		self.view.replace(edit, sel, "run command within ()")
				
		# #sets cursor(s) back to beginning	
		# self.view.run_command("move" , {"by": "characters", "forward": False})


	@staticmethod		
	def formatArgs(selectionText):
		#still have to fix this
		if("," not in selectionText): #no space means argument < 2 
			return selectionText

		args = selectionText.split(",") #dumps all args into array
		args = [arg.strip() for arg in args] #take away any white space

		print("final jawn", "(", ', '.join(args), ")")
		return ', '.join(args) #formatted string is return

	@staticmethod
	def selectAllArgs(self, count):

		#to position the cursor at the beginning of first argument
		self.view.run_command("move_to" , {"to": "brackets"})
		# self.view.run_command("move_to" , {"to": "brackets"})
		self.view.run_command("mark_and_move_do_it_all")

		for x in range(count):
			self.view.run_command("move" , {"by": "word_ends", "forward": True})
			# while()
			# 	self.view.run_command("move" , {"by": "word_ends", "forward": True})

			self.view.run_command("move" , {"by": "characters", "forward": True})
			self.view.run_command("move" , {"by": "characters", "forward": True})
			self.view.run_command("mark_and_move_do_it_all")	

		#to execute to final command and initiate the cursors visually
		self.view.run_command("mark_and_move_do_it_all")	

		#highlight each argument
		self.view.run_command("find_under_expand")
		# self.view.run_command("find_under_expand")

		#must do this next
		#work for multi-cursor
		#(dog, cat, monkey) - > (monkey, dog, cat)
		# support for {} and other things
		# support for just two words would have to 
		# go from space word1 word2 space
		# also has to work for this like int x, double y
		# ctrl alt t, show cycle through arguments left to right
		# self.view.run_command("move_to" , {"to": "brackets"})
		# self.view.run_command("move_to" , {"to": "brackets"})
		# self.view.run_command("find_under_expand")


		# sel = self.view.sel()[0]
		# tranposedText = self.randTranspose(self.view.substr(sel))

		# if(not sel.empty()):
		# 	self.view.run_command("left_delete")
		# 	self.view.insert(edit, sel.begin(), tranposedText)

		# else:
		# 	self.view.insert(edit, sel.begin(), "run command within ()")
		# ctrl shift alt t, would go right to left