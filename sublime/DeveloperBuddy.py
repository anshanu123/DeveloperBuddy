import sublime, sublime_plugin
from flask import Flask, request, redirect

app = Flask(__name__)

def commentLineHandler(request_form):
	line = request.form['line']
	print("got here")
	#sublime edit line

processing_dict = {
	"commentLine": {"params":["line"], "callback":commentLineHandler}
}

@app.route('/alexa', methods=['POST'])
def alexa():
    """processing handle for alexa app"""
    command = request.form['command'] #ex. comment, delete
    callback = processing_dict[command]["callback"]
    callback(request.form)
    #line = request.form['line']
    #line_start = request.form['line_start']
    #line_end = request.form['line_end']
    #list_name = request.form['list_name']
    return "success"


#class ExampleCommand(sublime_plugin.TextCommand):
#	def run(self, edit):
#		self.view.insert(edit, 0, "Hello, World!")

def plugin_loaded():
	"""Called at the start of the sublime plugin"""
	print("loaded plugin")
	app.run(host = "0.0.0.0", port=8080)