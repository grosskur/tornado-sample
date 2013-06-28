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
    @tornado.web.asynchronous
    def get(self):
        client = tornado.httpclient.AsyncHTTPClient()
        client.fetch('http://www.google.com/', self.handle_request)

    def handle_request(self, response):
        if response.error:
            self.write('Error: {}'.format(response.error))
        else:
            self.write(response.body)
        self.finish()


if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/', MainHandler),
    ])
    app.listen(os.getenv('PORT', 8000))
    tornado.ioloop.IOLoop.instance().start()
