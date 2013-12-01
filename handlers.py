# encoding:utf-8
from tornado import websocket, web

__author__ = 'zhouqi'

class MainHandler(web.RequestHandler):
    def get(self):
        self.write("Hello, world")


connections = []

class ChatHandler(websocket.WebSocketHandler):
    def open(self):
        connections.append(self)
        print "WebSocket opened"

    def on_message(self, message):
        self.write_message(u"You said: " + message)
        for c in connections:
            if c != self:
                c.write_message(u"Others said: " + message)

    def on_close(self):
        connections.remove(self)
        print "WebSocket closed"