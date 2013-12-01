from websocket import create_connection
import time, thread

__author__ = 'zhouqi'

#step 1:
#ws = create_connection("ws://0.0.0.0:8888/chat")
#print "Sending 'Hello, World'..."
#ws.send("Hello, World")
#print "Sent"
#print "Reeiving..."
#result =  ws.recv()
#print "Received '%s'" % result
#ws.close()


class User():
    user_name = ''
    connection = None

    def __init__(self, **kwargs):
        self.connection = create_connection("ws://0.0.0.0:8888/chat")
        self.user_name = kwargs['user_name']

    def show(self):
        msg = self.connection.recv()
        print self.user_name + ' has receive: ' + msg

    def say(self, msg):
        self.connection.send(msg)

    def close(self):
        self.connection.close()


def timer(u, interval=1):
    cnt = 0
    while cnt < 10:
        u.show()
        time.sleep(interval)
        cnt += 1
    thread.exit_thread()

if __name__ == "__main__":
    u1 = User(**{'user_name': 'u1'})
    thread.start_new_thread(timer, (u1, ))
    u1.say('hi, i\'m u1.')

    u2 = User(**{'user_name': 'u2'})
    thread.start_new_thread(timer, (u2, ))
    u2.say('hi, i\'m u2.')

    u1.say('nice to meet you. u2')
    u2.say('nice to meet you. too')

    time.sleep(10)
