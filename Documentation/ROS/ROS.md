![yapps_logo.svg](../../Resources/images/logos/yapps_logo.svg)
# ROS - The Robot Operating System


[TOC]: # " "

- [ROS - The Robot Operating System](#ros---the-robot-operating-system)
    - [Robot Operating System](#robot-operating-system)
        - [ROS Master](#ros-master)
        - [ROS Nodes](#ros-nodes)
        - [ROS Topics](#ros-topics)
        - [ROS Messages](#ros-messages)
    - [Setting up ROS](#setting-up-ros)
        - [ROS Workspace Environment](#ros-workspace-environment)
        - [Starting ROS](#starting-ros)
        - [catkin Build System](#catkin-build-system)



## Robot Operating System


### ROS Master
The ros master manages the communication between [ros nodes](#ros-nodes). during startup each node has to register at the master.

### ROS Nodes
A ros node is is single-purpose executable program. Each node is individually compiled, executed and managed by the [ros master](#ros-master). A node is organized in a package, to run a rode on you type:
```console
rosrun package_name node_name
```
To view all active nodes on a system, type:
```console
rosnode list
```
To view information about a node, type:
```console
rosnode info node_name
```

### ROS Topics
Topics are used by [ros nodes](#ros-nodes) to communicate with each other. A node can publish or subscribe to a topic. The name of the topic is used to identify [ros messages](#ros-messages) that a certain node is interested in.
To list all active topics on a master, type:
```console
rostopic list
```
To subscribe and print the contents of a topic, type:
```console
rostopic echo /topic_name
```
To get information about a topic, type:
```console
rostopic info /topic_name
```

### ROS Messages
A message is a packet or data structure that defines the type of a [topic](#ros-topics). It is build up by a nested structure of variables like: strings, objects, arrays, integers, booleans enz. Messages are stored in `.msg` files. To view the type of a topic, type:
```console
rostopic type /topic_name
```
To publish a message on a topic, type:
```console
rostopic pub /topic_name variable_type arguments
```

## Setting up ROS

### ROS Workspace Environment
The ROS workspace environment defines the context of the current workspace.

### Starting ROS
When you have your system installed and you want to try to run some [ros nodes](#ros-nodes) you have to start a [ros master](#ros-master) by running:
```console
roscore
```
This will start a ros master and allows you to run nodes by typing:
```console
rosrun package_name node_name
```


### catkin Build System
The catkin build system is used to generate executables, libraries and interfaces for ROS. To navigate to your catkin workspace you type"
```console
cd ~/catkin_ws
```
When you want to build a package you type:
```console
catkin build package_name
```
Whenever you want to build a new package or update your envoronment, type:
```console
source devel/setup.bash
```
To clean the build and development workspace, type:
```console
catkin clean
```
To view the workspace setup, type:
```console
catkin config
```
To configure a setting in your workspace, type:
```console
catkin build --setting-args
    --the_settings_you_want_to_configure
```
![nhlstendenMadeByStudents.png](../../Resources/images/logos/nhlstendenMadeByStudents.png)

<hr>
This page (the documentation) is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.