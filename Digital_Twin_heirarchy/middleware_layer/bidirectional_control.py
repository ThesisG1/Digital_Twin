import rospy
from mavros_msgs.msg import State, PositionTarget
from std_msgs.msg import String
import json
import socketio
import os


sio = socketio.Client()
@sio.event(namespace='/control')
def connect():
    print('Successfully connected to the server')

@sio.event(namespace='/control')
def connect_error():
    print('Failed to connect to the server')

@sio.event(namespace='/control')
def disconnect():
    print('Disconnected from the server')

@sio.event(namespace='/control')
def position(data):
    print(data)
    pub.publish(data)
    

if __name__ == '__main__':
    sio.connect(os.path.expandvars('http://$HOST_IP:8000/control'))
    print(os.path.expandvars('http://$HOST_IP:8000'))
    #rospy.init_node('sensorsMiddlewareDig', anonymous=True)
    rospy.init_node('controlReceived', anonymous=True)
    pub = rospy.Publisher("/middleware/control", String, queue_size=1)
    rospy.spin()