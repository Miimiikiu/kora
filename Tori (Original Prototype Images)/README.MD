## Tori Robot

This was my first major robotics endeavor and is a crude but ambitious rough draft of Kora.

Tori was developed using ROS Noetic. I used a custom version of [ROS Reality](https://github.com/h2r/ros_reality) for human control using VR (I'll upload an updated version soon). I used this data to train the walking model, which worked well in simulation, but once I tried getting the physical robot to walk, there was too much deflection in the legs for it to move. Kora will have a more rigid structure so that this won't be a problem.
                                                                                                                                              
If you see a cable along the head of the version that has a face, I didn't want it to fall over so I had it suspended along a wire running along my room.

I also used [Detectron2](https://github.com/facebookresearch/detectron2) for computer vision, and customized it to also get the distance to recognized objects via the pointcloud data from the depth camera. I'll upload my fork once I update it to ROS2, but the ROS script for CV2 is in the `machine_learning` folder.
                                                                                                                                              
