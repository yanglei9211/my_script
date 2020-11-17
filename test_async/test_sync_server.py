import http.server
from pprint import pprint
from wsgiref.simple_server import make_server
from http.server import HTTPServer, BaseHTTPRequestHandler
from wsgiref.simple_server import demo_app
import json

data = {'result': '111'}
host = {'localhost', '8008'}


class Request(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())


def do_t1(env, start_response):
    status = "200 OK"
    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)
    path = env['PATH_INFO'][1:] or "test_1"
    # print(env)
    print(type(env))
    pprint(env)
    return [b'<h1> %s </h1>' % path.encode()]


def run_t1():
    server = make_server('localhost', 8001, do_t1)
    print('serving http on 8001...')
    server.serve_forever()


def run_demo():
    port = 8001
    with make_server('', port, demo_app) as httpd:
        print('serving http on port: %d' % port)
        httpd.serve_forever()
        httpd.handle_request()


if __name__ == '__main__':
    # run_t1()
    run_demo()
#     server = HTTPServer(host, Request)


