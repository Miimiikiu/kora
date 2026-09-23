#!/usr/bin/env python2
"""

Copyright (c) 2023 Kieran Aponte
This software is licensed under the MIT License.

"""


import sensor_msgs.msg
import rospy
import cv2
import communicate
import time
import sys
import numpy
from cv_bridge import CvBridge

numpy.set_printoptions(threshold=sys.maxsize)
bridge = CvBridge()
server = communicate.Server(55443)


def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + ' ' + data.data)
    #print(data.header)
    cv_image = bridge.imgmsg_to_cv2(data, desired_encoding='bgr8') # cv_image is numpy.ndarray
    #nparr = np.frombuffer(data.data, np.uint8)
    #img_np = cv2.imdecode(nparr, flags=1)#, cv2.CV_LOAD_IMAGE_COLOR) # cv2.IMREAD_COLOR in OpenCV 3.1
    #print(type(cv_image))
    cv2.imshow('image', cv_image)
    cv2.waitKey(1)
    #print(str(cv_image))
    server.send_message(str(id(cv_image)))
    time.sleep(2)
    

rospy.init_node('vision_listener', anonymous=True)
sub = rospy.Subscriber('/camera1/image_raw', sensor_msgs.msg.Image, callback)
rospy.spin()