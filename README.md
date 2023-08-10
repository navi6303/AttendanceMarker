
# AttendanceMarker

A desktop application called proxymarker or face 
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
## Screenshots
- Home page![home page](https://user-images.githubusercontent.com/94692993/170837655-67ca838c-5ebc-43a1-9430-e5bf00b29032.png)

- Student details![student details](https://user-images.githubusercontent.com/94692993/170837714-28c7f91d-7dfd-4649-a4c8-298494093797.png)

- Dataset![dataset](https://user-images.githubusercontent.com/94692993/170837966-53945a5d-aef1-47f2-a822-0bbc2c555ff4.png)

- Train dataset![train dataset](https://user-images.githubusercontent.com/94692993/170838137-8157f1e3-09dc-41bb-9b0e-409ff68ae8d5.png)

- Face recognition![face recognition](https://user-images.githubusercontent.com/94692993/170837918-656ab527-b8a3-4f35-8a92-836a6c98779a.png)

- Attendance system![student attendance system](https://user-images.githubusercontent.com/94692993/170850886-82e28c07-7369-49ad-bfb1-d91eb0366b0a.png)



