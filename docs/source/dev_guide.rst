.. _developer_guide:

***************
Developer Guide
***************

This guide is intended to show developers how to use the SDK to create their own digital twin applications

YAML File
---------
The YAML file will include all the ros nodes that will be in the digital twin and from this file all worklow is going to be created. 
Files created from the yaml file will create a files in each layer to relay from the ROS layer to the middleware layer and to the namespace layer.

The yaml file is found under the SDK_NL directory inside the ros_layer directory.

The structure of the YAML file is as follows:

.. code-block:: yaml

    ros_node:
        name: latency_test
        flow_flag: 0         #(1:Bottom-Up Flow, 0:Top-Down Flow)
        topics:
            publish:
                topic_1:
                    name: "middleware/test"
                    type:  "nav_msgs/Odometry"
                    middleware_flag: 1    
            subscribe:
                topic_1:
                    name: "test"
                    type:  "nav_msgs/Odometry"
                    middleware_flag: 1

Code Generators
---------------

For each layer in our worklow, we have a generator