# encoding:utf-8
import tornado.ioloop
import tornado.web
from handlers import *

__author__ = 'zhouqi'


application = tornado.web.Application([
    (r"/chat", ChatHandler),
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()