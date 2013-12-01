# encoding:utf-8
import tornado.ioloop
import tornado.web
from handlers import *

__author__ = 'zhouqi'

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

application = tornado.web.Application([
    (r"/chat", ChatHandler),
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()