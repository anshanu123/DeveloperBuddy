import sublime, sublime_plugin
from threading import Thread
import json



def goToLineHandler(params, printing = True):
    line = params["line"] - 1
    job_view = sublime.active_window().active_view()
        
    pt = job_view.text_point(line, 0)
    job_view.sel().clear()
    job_view.sel().add(sublime.Region(pt))
    job_view.show(pt)

    if(printing):
        print("DeveloperBuddy: Go To line " + str(line))



def select_line(params, printing=True):
    line = params["line"] - 1

    job_view = sublime.active_window().active_view()
    line_start = job_view.text_point(line,0)
    line = job_view.line(sublime.Region(line_start))
    job_view.sel().add(line)



def commentLineHandler(params, printing = True):
    line = params["line"]
    job_view = sublime.active_window().active_view()
        
    target_region = sublime.Region(line, line)

    job_view.sel().clear()
    job_view.sel().add(sublime.Region(job_view.text_point(line-1, 0)))
    #job_view.run_command("insert", {"pos":0,"characters":"#"})
    job_view.run_command("toggle_comment", {"block":False})
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
    "commentLines": {"params":["startLine", "endLine"], "callback":commentLinesHandler},
    "goToLine": {"params":["line"], "callback": goToLineHandler},
    "select_line": {"params":["line"], "callback": select_line},
    "findAllSelected": {"params":[], "callback": "find_all_under", "view": False},
    "undo": {"params":[], "callback": "undo", "view": True},
    "redo": {"params":[], "callback": "redo_or_repeat", "view": True}
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
        if isinstance(processing_entry["callback"],str):
            if(processing_entry["view"]):
                job_view = sublime.active_window().active_view()
                job_view.run_command(processing_entry["callback"])
            else:
                window = sublime.active_window()
                window.run_command(processing_entry["callback"])
        else:
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