from websocket import create_connection

__author__ = 'zhouqi'

ws = create_connection("ws://0.0.0.0:8888/chat")
print "Sending 'Hello, World'..."
ws.send("Hello, World")
print "Sent"
print "Reeiving..."
result =  ws.recv()
print "Received '%s'" % result
ws.close()