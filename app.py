"""
Example application using Tornado and Curl
"""
import os

import tornado.httpclient
import tornado.ioloop
import tornado.web


tornado.httpclient.AsyncHTTPClient.configure(
    'tornado.curl_httpclient.CurlAsyncHTTPClient')


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello, world')


if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/', MainHandler),
    ])
    app.listen(os.getenv('PORT', 8000))
    tornado.ioloop.IOLoop.instance().start()
