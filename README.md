# Introduction

RHex is a bio-inspired, hexapedal robot designed for locomotion in rough terrain. It can drive over rocks, mud, sand, snow, and railroad tracks. ARHex adds an arm to this configuration, hence the name.

![alt text](https://raw.githubusercontent.com/svaichu/ARHex/master/media/ARHex.png)
<p align="center">illustration of ARHex</p>

This gives robot, the capability to interact and manipulate objects around it. The endeffector can be modified for pick & place, spraying gun, welding torch, camera, etc. Also the arm can be retracted easily into the base, this would particularly useful when robot topples as it scales rough terrain with are what legged robots working area.

## Prerequisites

To run the package you need the following installed and configured.
* ROS Melodic Morenia
* Gazebo-9

## Installing

Navigate to `~/catkin_ws/src` your catkin_workspace.

Clone the repository
```
git clone https://github.com/svaichu/ARHex.git
```
And build the catkin_workspace
```
catkin_make --source src/ARHex
```
Overlay the current catkin_workspace on top of your environment.
```
source devel/setup.bash
```
Load the robot model in Gazebo
```
roslaunch arhex_gazebo arhex.launch
```
In another terminal, start the controllers
```
roslaunch arhex_control arhex_control.launch
```
to make it walk, in another terminal
```
rosrun arhex_control arhex_control.py
```

## Simulation Video
[![play](https://raw.githubusercontent.com/svaichu/ARHex/master/media/Sim.png)](https://youtu.be/Af0Ggii6uZU)

Visit the [channel](https://www.youtube.com/channel/UCnfsN-BSJe98hWcyonWuqLw) for more videos.

## Authors

* **Vaishnava Hari** - [website](http://vaishnavahari.me) - [github](https://github.com/svaichu)
  <p>advised by <a href="https://www.amrita.edu/faculty/t-mohanraj"> Dr. T. Mohanraj</a></p>

<p>*I am looking for potential colloborators to make advancements.</p>

## License

This project is licensed under the GPLv3 License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Group mates - Rahul, Subrammaniyan and Monish
* Inspiration from [Kod*lab](https://www.grasp.upenn.edu/labs/kodlab), [MiniRhex](https://github.com/robomechanics/MiniRHex), etc
