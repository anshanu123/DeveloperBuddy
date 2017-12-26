import sublime, sublime_plugin
from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/alexa', methods=['POST'])
def alexa():
    """processing handle for alexa app"""
    #tag_name = request.form['tag_name']
    #list_name = request.form['list_name']
    return "success"


class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Hello, World!")

def plugin_loaded():
	"""Called at the start of the sublime plugin"""
	print("loaded plugin")
	app.run(host = "0.0.0.0", port=8080)