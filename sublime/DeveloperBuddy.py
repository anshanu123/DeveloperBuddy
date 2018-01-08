import sublime, sublime_plugin
#from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread
import json
#from flask import Flask, request, redirect

#app = Flask(__name__)



def commentLineHandler(params, printing = True):
    line = params["line"]
    jobView = sublime.active_window().active_view()
        
    target_region = sublime.Region(line, line)

    jobView.sel().clear()
    jobView.sel().add(sublime.Region(jobView.text_point(line-1, 0)))
    jobView.run_command("insert", {"pos":0,"characters":"#"})
    if(printing):
        print("DeveloperBuddy: Commented line " + str(line))

def commentLinesHandler(params):
    startLine = params["startLine"]
    endLine = params["endLine"]
    startLine = min(startLine, endLine)
    endLine = max(startLine, endLine)
    for line in range(startLine, endLine):
        comment_line_handler_params = {"line":line}
        commentLineHandler(comment_line_handler_params, printing = False)
    print("DeveloperBuddy: Commented lines " + str(startLine) + " through " + str(endLine))



processing_dict = {
    "commentLine": {"params":["line"], "callback":commentLineHandler},
    "commentLines": {"params":["startLine", "endLine"], "callback":commentLinesHandler}
}



# kill server command
class ExampleCommand(sublime_plugin.TextCommand):
   def run(self, view):
       unload_handler()



class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
 
  # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()
 
        # Send message back to client
        message = "Running!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode("utf-8"))
        command = data["command"]
        params = data["params"]
        
        processing_entry = processing_dict[command]
        callback = processing_entry["callback"](params)

        # response        
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(bytes("done", "utf8"))
        return


def start_server():
    server.serve_forever()

def unload_handler():
    global server
    print('Killing server...')
    if server:
        server.shutdown()
        server.server_close()

def plugin_loaded():
    """Called at the start of the sublime plugin"""
    global server
    print("loaded plugin")
    #app.run(host = "0.0.0.0", port=8080)

    print('starting server...')
 
    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ('0.0.0.0', 8081)
    server = HTTPServer(server_address, testHTTPServer_RequestHandler)
    #sublime.message_dialog('Running DeveloperBuddy Server on port 8081')
    print('Running DeveloperBuddy Server on port 8081')
    Thread(target=start_server, args=[]).start()
    #httpd.serve_forever()

    """global SESSIONS, server

    # Load settings
    settings = sublime.load_settings("rsub.sublime-settings")
    port = settings.get("port", 52698)
    host = settings.get("host", "localhost")

    # Start server thread
    server = TCPServer((host, port), ConnectionHandler)
    Thread(target=start_server, args=[]).start()
    say('Server running on ' + host + ':' + str(port) + '...')"""