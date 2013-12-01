# encoding:utf-8
from tornado import websocket

__author__ = 'zhouqi'

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


class ChatHandler(websocket.WebSocketHandler):
    def open(self):
        print "WebSocket opened"

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print "WebSocket closed"