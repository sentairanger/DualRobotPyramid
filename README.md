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
* `development.ini`: File used to run the app with the `pserve` command.
* 
To run the code, run `pserve development.ini --reload` and then go to a browser and type `localhost:6543` and you should see the app running now.

## Running the App on Multiple Platforms

### Linux

Since python 3 is already installed just run `pip install -r requirements.txt` command to install the needed modules. After that you are good to go. Optionally you should run this in a virtual environment to avoid package conflicts.

### Windows

To install python 3, follow this [link](https://www.python.org/downloads/windows/) to download python and then follow the instructions. Pip should be installed as well. Then run `pip install -r requirements` to install the needed modules. Optionally, you can install a python virtual environment and then install the needed modules.

### MacOS

Install python 3 with `brew install python` and optionally install a python virtual environment. Then install the needed modules with `pip install -r requirements.txt`

### Android

You can use an IDE like Pydroid to run the app remotely. Make sure to run `pip install -r requirements.txt` to install the libraries. 

### iOS

I recommend using an IDE like Pythonista to run the app. Make sure to also run `pip install -r requirements.txt` to install the libraries.

## Running on Docker
To run this app as a container on Docker, install docker following this [link](https://docs.docker.com/get-docker/). After that build the image with `docker build -t pyramid-dualrobot .`. Check if the image was created with `docker images`. Run the app with `docker run -d -p 6543:6543 pyramid-dualrobot`. Check if it runs with `docker ps`. Then go to a browser and type `localhost:6543` and it should work. You can optionally tag the container with `docker tag pyramid-dualrobot linuxrobotgeek/pyramid-dualrobot:tag-version`. Then push the image with `docker push linuxrobotgeek/pyramid-dualrobot:tag-version`.

## Running on Kubernetes
To run this on kubernetes, I recommend installing kind which can be found [here](https://kind.sigs.k8s.io/docs/user/quick-start/) and then install kubectl. However you can use the vagrant file provided to install k3s which can be found !here](https://k3s.io/). To use the Vagrantfile make sure VirtualBox is installed first. Then install vagrant using this [link](https://www.vagrantup.com/downloads). Then run `vagrant up` and then ssh into the VM using `vagrant ssh`. When running kubectl in Vagrant, be sure to run `sudo su` since kubectl cannot run under a regular account. To create a deploy run `kubectl create deploy pyramid-dualrobot --image=/linuxrobotgeek:tag-version`. Then check if the pod was created with `kubectl get po`. Once it runs you can run it with `kubectl port-forward po/pyramid-dualrobot-id-number --address 0.0.0.0 6543:6543` inside of the Vagrantbox. This can also be done locally but remove the `--address` option. Then check to see if it ran by going to a browser and either typing `localhost:6543` or `192.168.50.4:6543` which is the address of the Vagrant box. Then the app should be displayed.


## Running on ArgoCD

To run on ArgoCD follow [this](https://argoproj.github.io/argo-cd/getting_started/). This can be installed locally or on the Vagrantbox. Then once it runs go to `localhost:8080` or `192.168.50.4:8080` and it should display the Login page. Login with the given credentials, in this case `admin` and a password that is generated by you. Then you can choose any of the `.yaml` files provided to run the app. Just run `kubectl apply -f` and then choose the `yaml` file you want such as `argocd-dualpyramid.yaml` and it should display on ArgoCD. Then the pod should be created and there you can run the pod using `kubectl port-forward` as before and then you should see the app running. 

## Pictures
