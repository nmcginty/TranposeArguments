import sublime
import sublime_plugin


class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# self.view.insert(edit, 0, "Hello, World!")
		# allcontent = sublime.Region(0, self.view.size())
		# self.view.replace(edit, allcontent, 'Hello, world!')
		#will replace entire text in file with Hello World
		self.view.insert(edit, self.view.sel()[0].begin(), "Hello, World!")


		# pos = self.view.sel()[0].begin()
		# pos = self.view.sel()
		# self.view.insert(edit, pos.start(), 'HELLO WORLD')
		
		# below works for multiple selections
		# for pos in self.view.sel():
  #   		self.view.insert(edit, pos.begin(), timestamp)



class TranposeArgsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Hello, World!")
