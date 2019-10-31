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




### And coding style tests

Explain what these tests test and why

```
Give an example
```


## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the GPLv3 License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
