#!/usr/bin/env python3
'''
A simple HTTP server.
'''
import http.server
import cs3280project2

__author__ = 'AndrewStoddard'
__version__ = 'Fall 2020'

class L13Server(http.server.BaseHTTPRequestHandler):
    '''
    Specialized subclass that listens at the HTTP socket, dispatching the requests to a handler.
    '''
    def do_GET(self):
        '''
        Overriding do_GET()
        Ignore pylint warning!
        '''
        self.log_message("path: %s", self.path)
        try:
            path = self.path
            self.log_message("resource: %s", path)
            resource = path[1:]
            print(resource)
            if not resource.startswith('subnet'):
                self.log_message("resource: %s", path)
                self.send_error(404, 'Resource must begin with: subnet')


            start = len('subnet') + 1
            query = resource[start:].split('&')
            print(query)

            body = self.process_and_respond(query)
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(body, 'UTF-8'))

        except Exception as exception:
            self.send_error(500, str(exception))


    def process_and_respond(self, query):
        '''
        Processes content for valid query.
        Parameters:
        query - the parameters provided to the query
        '''
        ip_address = query[0]
        subnet_mask = query[1]
        result = cs3280project2.main(ip_address, subnet_mask)

        if result == 400:
            self.send_error(400, "Invalid Input")


        body = 'Hello, ' + ' The subnet is: ' + result + '!'
        html = "<!DOCTYPE html><html>"
        html += "<head><title>"
        html += "Response from L13Server"
        html += "</title></head>"
        html += "<body><p><h1>"
        html += body
        html += "</h1></p></body>"
        html += "</html>"
        self.log_message("page built")
        return html

def start_server():
    """
    Starts the server
    """
    PORT = 3280
    server = http.server.HTTPServer(('10.0.2.15', PORT), L13Server)
    print('Subnet Calculator running on port {}; Type <Ctrl-C> to stop server.'.format(PORT))
    server.serve_forever()


if __name__ == '__main__':
    PORT = 3280
    server = http.server.HTTPServer(('10.0.2.15', PORT), L13Server)
    print('Subnet Calculator running on port {}; Type <Ctrl-C> to stop server.'.format(PORT))
    server.serve_forever()
