
# AttendanceMarker

A desktop application called attendancemarker or face 
recognition attendance system using OpenCV and python 
with a Tkinter GUI interface. It simply recognizes faces 
and marks attendance for the recognized faces at first 
glance in an excel sheet.

## Logo

![Screenshot_2023-08-10_104540-removebg-preview](https://github.com/navi6303/AttendanceMarker/assets/94692993/42d596ff-4ee5-47d3-ae83-e0581e55fe79)

## Features

- With interactive GUI support, it's simple to use.
- Create, update, and delete a student information database during registration.
- Generates a dataset from the webcam.
- It identifies the student's face and marks present on the excel sheet.
- Every time, a new CSV file is created for attendance, recorded with the correct date and time.


## Tech Used

**Language:** Python 3.8

**Modules:** OpenCV Contrib 4.5.5.64, Tkinter, Numpy, Pillow, Datetime, Filedialog, CSV

**Algorithm Used:** HaarCascade, LBPH(Local Binary Pattern Histogram)

**Software:** Visual Studio Code, Git 


## Installation

**Download or Clone the project**
- To download the project from github press Download Zip.
- You can clone the project with git bash.To clone the project using git bash first open the git bash and write the following code:

```bash
  https://github.com/navi6303/ProxyMarker.git
```
**Installing the Packages**

Open a terminal or command line and paste the code from below to install the packages.
```bash
  pip install opencv-contrib-python
```
```bash
  pip install numpy
```
```bash
  pip install Pillow
```
    
## Note
MySQL Database Credentials are:
- Host: localhost
- Username: root 
- Password: Navisharma@06
- Port: 3306
- Database: face_recognizer
This application's main file is main.py
## How to run?
- First download or clone the project
- Import the project to VS Code
- Install all the packages
- Go through the note once
- Run the project using the command line or your IDE Run Button
```bash
  python main.py
```



