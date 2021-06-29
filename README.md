# DualRobotPyramid

## Introduction

After successfully running my robots using Flask and Django I moved on to the most difficult web framework, Pyramid. This was the most challenging framework I've ever used. And like my previous projects I now integrated them to Docker, Kubernetes and ArgoCD. I will show you how to run the app on its own, then on Docker, Kubernetes and then on ArgoCD.

## Getting started

### Hardware
To get things started I used my two Raspberry Pi Robots I've used in previous projects and my Ubuntu PC to run the project. If you are to do this on your own you can use any Windows, Mac or Linux machine. 

### Software
For software here is what I used. If you do this on your own it will vary and you can use any software as long as the app works.
* Raspberry Pi OS Lite (On Linus)
* Raspberry Pi OS (On Torvalds)
* Ubuntu 20.04 (To control both robots but any software will do)
* `gpiozero`, `pyramid`, `waitress`, and `pigpio` which is provided in `requirements.txt`. You can install this on your own machine by running `pip install -r requirements.txt`

## Pyramid File Structure and Code Explanation

* `setup.py`: This is used to install the needed libraries and modules. This is done via the `pip install -e .` and `pip install "[.dev]"`.
* The tutorial-egg.into directory contains the following files:
* `top_level.txt`: empty file
* `requires.txt`: File containing all the required modules
* `entry_points.txt`: File that defines the main directory
* `dependency_links.txt`: Empty file
* `SOURCES.txt`: Listing all the files in their directories
* `PKG-INFO`: Lists the directory information and version
* `__init__.py`: Initiates the app and lists the routes of the app
* `dual.pt`: The HTML file that contains the CSS and Javascript of the app
* `tests.py`: This tests the app and if all tests pass then that means the app is good.
* `views.py`: The main logic of the app where the views are defined as well as the controls for both robots.

## Running the App on Multiple Platforms

## Running on Docker

## Running on Kubernetes

## Running on ArgoCD

## Pictures
