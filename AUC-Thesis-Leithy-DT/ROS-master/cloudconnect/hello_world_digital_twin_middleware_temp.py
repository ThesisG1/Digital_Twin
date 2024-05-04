import rospy
from std_msgs.msg import String

import socketio
import os

def middleware_hello_world_callback(data):
    print('IMPLEMENT CALLBACK middleware_hello_world_callback')
 
    #emit your data on the dashboard namespace
    sio.emit('leithy', data.data ,namespace='/dashboard')

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

#Add the definition of your functions here as follows
# @sio.event(namespace='/hello_world_digital_twin_namespace')
# def fn(data):
#     print('data')

rospy.init_node('hello_world_digital_twin_mw')


middleware_hello_world_sub = rospy.Subscriber('/middleware/hello_world',String,middleware_hello_world_callback)
            

receiver_hello_world_pub = rospy.Publisher('/receiver/hello_world', String, queue_size=10)


if __name__ == '__main__':
    sio.connect(os.path.expandvars('http://$HOST_IP:8000/hello_world_digital_twin_namespace'))

    rospy.spin()
