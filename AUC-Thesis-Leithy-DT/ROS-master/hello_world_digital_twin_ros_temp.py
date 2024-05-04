import rospy
from std_msgs.msg import String

def receiver_hello_world_callback(data):
    print('IMPLEMENT CALLBACK receiver_hello_world_callback')
    middleware_hello_world_pub.publish("Hello World from Digital Twin")
rospy.init_node('hello_world_digital_twin')


middleware_hello_world_pub = rospy.Publisher('/middleware/hello_world', String, queue_size=10)


receiver_hello_world_sub = rospy.Subscriber('/receiver/hello_world',String,receiver_hello_world_callback)
            
if __name__ == '__main__':
    rospy.spin()