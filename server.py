#!/usr/bin/python2.7

import SimpleHTTPServer
import SocketServer
import sys
import subprocess

FOLDER = sys.path[0]

PORT = 8080
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

class CustomHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        subprocess.check_call(['%s/updateGit.sh' % FOLDER, FOLDER])
        self.send_response(301)
        self.send_header('Location','/')
        self.end_headers()
        return

httpd = SocketServer.TCPServer(("", PORT), CustomHandler)

print("serving at port %d" % PORT)
httpd.serve_forever()
