import rospy
from nav_msgs.msg import Odometry

import socketio
import os

def middleware_test_callback(data):
    print('IMPLEMENT CALLBACK middleware_test_callback')

 
    #emit your data on the dashboard namespace
    sio.emit('latency_test_data', data.data ,namespace='/dashboard')

sio = socketio.Client()
@sio.event(namespace='/dashboard')
def connect(): 
    print('Successfully connected to the server')

@sio.event(namespace='/dashboard')
def connect_error(): 
    print('Failed to connect to the server')

@sio.event(namespace='/dashboard')
def disconnect(): 
    print('Disconnected from the server')

rospy.init_node('latency_test_mw')


middleware_test_sub = rospy.Subscriber('/middleware/test',Odometry,middleware_test_callback)
            

test_pub = rospy.Publisher('/test', Odometry, queue_size=10)


if __name__ == '__main__':
    sio.connect(os.path.expandvars('http://$HOST_IP:8000/'))

    rospy.spin()