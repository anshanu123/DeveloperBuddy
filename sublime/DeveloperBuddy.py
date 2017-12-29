import sublime, sublime_plugin
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread
import cgi
#from flask import Flask, request, redirect

#app = Flask(__name__)

def commentLineHandler(request_form):
    line = request.form['line']
    print("got here")
    #sublime edit line

processing_dict = {
    "commentLine": {"params":["line"], "callback":commentLineHandler}
}

#@app.route('/alexa', methods=['POST'])
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
        message = "Hello world!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
        if ctype == 'multipart/form-data':
            postvars = cgi.parse_multipart(self.rfile, pdict)
        elif ctype == 'application/x-www-form-urlencoded':
            length = int(self.headers.getheader('content-length'))
            postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
        else:
            postvars = {}
        print(postvars)


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
    server_address = ('127.0.0.1', 8081)
    server = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
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