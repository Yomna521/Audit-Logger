"""
    Server handler for HTTP requests
    Authentication: Basic HTTP Authorization
"""
import json
from http.server import BaseHTTPRequestHandler

from service import logger
from database import audit_logs_db, user


class Handler(BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_AUTHHEAD(self):
        self.send_response(401)
        self.send_header(
            'WWW-Authenticate', 'Basic realm="Audit Logger"')
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_FAILHEAD(self):
        self.send_error(500)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()

    def do_GET(self):
        # Check authorization in the request's header
        # if authorization is sent to none -> send error response
        if self.headers.get('Authorization') is None:
            self.do_AUTHHEAD()
            self.wfile.write('No Authentication Header Received'.encode('utf-8'))
            pass

        # if authorization is set with correct key -> process query
        elif self.headers.get('Authorization') == 'Basic ' + str(user.user_key()):
            # if there's no query
            if self.path == '/log/':
                # Welcome to Audit Logger
                self.do_HEAD()
                self.wfile.write("Welcome to Audit Logger".encode('utf-8'))
            else:
                # Extract the query from path
                query = get_content(self.path.replace("/log/?", ""))
                try:
                    # query database
                    results = audit_logs_db.findAll(query)

                    # create a an AuditLogger instance
                    msg_logger = logger.AuditLogger()
                    msg_logger.set_http_request(self.command, self.client_address, query)
                    # save log to database

                    # audit_logs_db.save_log(vars(msg_logger))

                    # delete AuditLogger instance
                    del msg_logger

                    message_parts = ['QUERY SUCCESSFUL',
                                     'QUERY:',
                                     '{}'.format(query),
                                     '',
                                     'QUERY RESULTS:',
                                     '{}'.format(results)]
                    message = '\r\n'.join(message_parts)

                    self.do_HEAD()
                    self.wfile.write(message.encode('utf-8'))
                except:
                    # Query failed
                    self.do_FAILHEAD()
                    self.wfile.write("Failed to query database. Please try again.".encode('utf-8'))
            pass
        else:
            self.do_AUTHHEAD()
            self.wfile.write('Invalid credentials'.encode('utf-8'))
            pass

    def do_POST(self):
        # Check authentication in the request's header
        # if authentication is sent to none -> send error response
        if self.headers.get('Authorization') is None:
            self.do_AUTHHEAD()
            self.wfile.write('No Authentication Header Received'.encode('utf-8'))
            pass

        # if authentication is set with correct key -> process query
        elif self.headers.get('Authorization') == 'Basic ' + str(user.user_key()):
            # extract the event to be logged
            length = int(self.headers.get('Content-Length'))
            event = get_content(self.rfile.read(length).decode('utf-8'))
            try:
                # create a an AuditLogger instance
                msg_logger = logger.AuditLogger()
                msg_logger.set_event(event)
                msg_logger.set_http_request(self.command, self.client_address)
                # save log to database
                audit_logs_db.save_log(vars(msg_logger))
                # delete AuditLogger instance
                del msg_logger

                # Events logged successfully
                self.do_HEAD()
                self.wfile.write("Event logged successfully".encode('utf-8'))
            except:
                # Event couldn't be logged
                self.do_FAILHEAD()
                self.wfile.write("Failed to log event. Please try again.".encode('utf-8'))
            pass
        else:
            self.do_AUTHHEAD()
            self.wfile.write(bytes(json.dumps('Invalid credentials'), 'utf-8'))
            pass


def get_content(path: str) -> 'str':
    """
    Get content sent in a request as a dictionary
    :param path:
    :return:
    """
    path = path.replace("+", " ")
    result = dict((a.strip(), b.strip())
                  for a, b in (element.split('=')
                               for element in path.split('&')))
    return result

