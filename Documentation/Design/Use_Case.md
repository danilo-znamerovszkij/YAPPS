![yapps_logo.svg](../../Resources/images/logos/yapps_logo.svg)
# Use Case & User Stories
This document shows the use case's of this project (Product Backlog) and the User Stories (Sprint Backlog).

[TOC]: # " "

- [Use Case & User Stories](#use-case--user-stories)
    - [Product Backlog](#product-backlog)
        - [Actor - Developer](#actor---developer)
        - [Actor - User](#actor---user)
    - [Reference List](#reference-list)

## Product Backlog
### Actor - Developer
- **As a** developer, **I want to** install a development environment **so that** I am able to contribute code to the project.
- **As a** developer, **I want to** install ([ROS](http://www.ros.org)) on the SD card of the raspberry pi **so that** we can test the production environment.
- **As a** developer **I want to** install OpenCV on the raspberry pi **so that** we can test the computer vision code on a production environment.
- **As a** developer **I want to** create the skeleton of a python application **so that** it can be used for creating our software in a standardized way.
- **As a** Developer **I want to** create a setup.py file **so that** other people can easily install our software and dependencies.
- **As a** Developer **I want to** create a setup.cfg **so that** we can configure our python wheel.
- **As a** Developer **I want to** create a MANIFEST.in file **so that** other developers know what non python dependencies our project has.
- **As a** Developer **I want to** create a README.rst file for the project **so that** other developers can read the documentation and to be more compatible with the python eco system.
- **As a** Developer **I want to** creat a DESCRIPTION.rst **so that** we could easily do a future release of our project on PyPI.
- **As a** Developer **I want to** add a LICENCE file to our project **so that** its clear for other developers what they are allowed to do with our code.
- **As a** Developer **I want to** setup a .travis.yml file **so that** we can use continuous integration on our repository.
- **As a** Developer **I want to** setup a tests folder with a tox.ini file **so that** all deployments will be tested on multiple platforms.
- **As a** Developer **I want to** create a docs folder with basic usage documentation **so that** other developers know how to use our software and to make it easier for them if they want to contribute.
- **As a** Developer **I want to** add a requirements.txt to our project **so that** other developers know what python dependencies are needed to use our software.
- **As a** Developer **I want to** add .gitignore file **so that** unwanted information doesn't leak into version management.
- **As a** Developer **I want to** add a CHANGELOG file **so that** other developers know what changes where made in each version.
- **As a** Developer **I want to** add a CONTRIBUTING file **so that** its clear to other developers how they can contribute to our project.
- **As a** Developer **I want to** add a AUTHORS file **so that** its clear who contributed to our project.
- **As a** Developer **I want to** create the software package skeleton **so that** we can start adding the software modules of this project to it.
- **As a** Developer **I want to**  **so that**

### Actor - User

- **As a** User **I want to** be able to place the dice on a grid **so that** it can be manipulated by the UR10 later.
- **As a** User **I want to** be able to install the software on a  system **so that** he or she can execute or debug our software.
- **As a** User **I want to** be able to start the software on the raspberry pi **so that** he or she can use or test the software.
- **As a** User **I want to** be able to remove the software **so that** it frees the resources used on the system.
- **As a** User **I want to** be able to choose between different tasks that our software can perform **so that** the correct program can be executed.
- **As a** User **I want to** be able to quickly stop the system **so that** in case of an emergency the arm will stop moving.
- **As a** User **I want to** be able to select dice detection mode **so that** the user can see the objects detected by our software.
- **As a** User **I want to** be able to see the location (grid coordinates) of the objects **so that** I can validate the computer vision system.
- **As a** User **I want to** be able to see the corrected way-points that would be send to the UR10 for manipulating a object. **so that** he or se can validate that the data is correct before executing it on the UR10.
- **As a** User **I want to** see a list of way-points with the corresponding commands that would be executed when for a certain task. **so that** he or se can validate that the commands are correct.
- **As a** User **I want to** be able to activate a task in a extra slow phase **so that** there is more time to react when something goes wrong.
- **As a** User **I want to** be able to activate a task in a normal phase **so that** the task will execute.
- **As a** User **I want to** be able to active a task in a fast phase **so that** the robot will perform the task as quick as possible.
- **As a** User **I want to** be able to activate parts of a task step by step **so that** its easy to track all actions or commands that get executed on the UR10.
- **As a** User **I want to** be able to activate the dice pickup task **so that** the UR10 will pickup a specified dice.
- **As a** User **I want to** be able to activate the dice move task **so that** the UR10 will pickup move and drop the dice on specified locations.
- **As a** User **I want to** be able to activate the dice swap task **so that** the UR10 will pickup a dice, place it on a temporary free location, pickup the second dice, place it on the first location and then move the first dice to the final position.
- **As a** User **I want to** be able to activate the line up program **so that** the UR10 will line up all dice in a straight line on the grid.
- **As a** User **I want to** be able to activate the ascending sorting task **so that** the UR10 will sort the dice in ascending order.
- **As a** User **I want to** be able to activate the descending soring task **so that** the UR10 will sort the dice in descending order.
- **As a** User **I want to** be able to activate the scramble task **so that** it will scramble the positions of the dice randomly on the grid.
- **As a** User **I want to** be able to activate the current system information panel that shows information about current state **so that** he or she can monitor the state of the UR10, attached tool or the raspberry pi.
- **As a** User **I want to** be able to configure what items will be shown in the current system information panel **so that** he or she can select the data that is relevant to him or her.



Connect the UR10 controller and the Raspberry to the router.
As a developer, I want to set up the basic structure of the program of the UR10 controller so that it can be used correctly.
Make a basic design of the program of the UR10 controller.
As a developer, I want to add functionality to the UR10 controller so that it can communicate with the Raspberry Pi.
Add a block with which the incoming data can be received and actions can be performed on it.
As a developer, I want the entire system to be scalable so that it can be taken over for future projects.
Ensure that in OpenCV it is possible to identify multiple dice by shape and position.
Ensure that in OpenCV it is possible to send information from multiple dice.
Making connections available so that multiple sensors can be connected to the entire system.
As a developer, I want a repository with which a future project can access the source code so that every member can access the code.
Create a Github repository.
As a developer, I want a clear README in the repository so that everyone is aware of the goals of the project.
Write a clear README in the repository.
As a group leader, I want all members to have access to the repository so that each member can work on the project.
Send each member and any future member an invitation to participate in the repository.
As a developer, I want the Raspberry Pi to communicate with the UR10 controller so that the entire system can work correctly.
Establish a connection.
Send data from the Raspberry Pi and receive it at the UR10 controller
As a developer, I want to be able to connect multiple devices to the UR10 controller through a router so that each device can communicate with each other.
Connect all system cables.
Set the router as a hub.
Specify ip addresses of the devices connected to the router.
As a developer, I want the UR10 controller to be able to communicate with the robot arm so that it can give instructions to the robot arm.
Connect the Raspberry Pi to the robot arm.
As a developer, I want communication over UTP ethernet so that each component uses the same protocol.
Allow all systems to use the same protocol.
Connect all components of the entire system with an ethernet cable.
As a developer, I want to send the location where the robot arm should move
As a developer, I want to receive multiple positions of objects so that I can control the robot arm correctly.
Connect the Raspberry Pi to the robot arm.
Receive the positions of multiple dice.
Being able to send commands to the robot arm.
Have the robot arm respond correctly to the input.
As a developer, I want to receive the position of an object so that I can correctly control the robot arm.
Get the positions of a dice through the Raspberry Pi.
As a developer, I want to receive the number of dots on an object so that I can correctly calculate the Yahtzee score.
Receive the dots of a dice via the Raspberry Pi.
As a developer, I want to receive the position of multiple objects so that I can control the robot arm correctly.
Receive the positions of multiple dice via the Raspberry Pi.



## Reference List
- Virsual Paradigm. (n.d.). User Story vs Use Case for Agile Software Development. Retrieved April 6, 2019, from https://www.visual-paradigm.com/guide/agile-software-development/user-story-vs-use-case/
- Jacobson, I., Spence, I., & Bittner, K. (2012, July). USE-CASE 2.0. Retrieved April 6, 2019, from https://www.ivarjacobson.com/sites/default/files/field_iji_file/article/use_case_2.0_e-book_dutch_version.pdf


![nhlstendenMadeByStudents.png](../../Resources/images/logos/nhlstendenMadeByStudents.png)

<hr>
This page (the documentation) is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.