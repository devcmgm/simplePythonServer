import os
from http.server import HTTPServer, CGIHTTPRequestHandler

# Set Directory to expose files to data
os.chdir('./data')

#create server on port 3001 to listen for request
handler = CGIHTTPRequestHandler
handler.extensions_map=({
    '.html': 'text/html',
    '.txt': 'text/plain',
    '.png': 'image/png',
    '.jpg': 'image/jpg',
    '.svg': 'image/svg+xml',
    '.css': 'text/css',
    '.json': 'application/json',
    '': 'text/plain', # Default
    })
server_object = HTTPServer(server_address=('', 3001), RequestHandlerClass=handler)

#Run Server
server_object.serve_forever()
