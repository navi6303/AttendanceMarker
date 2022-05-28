#-----IMPORTING LIBRARIES------
from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk  #pip install Pillow
from student import studentDetails
import os
from train import trainDataset
from faceRecognition import faceRecognition
from studentAttendance import studentAttendance
from developer import developer

class face_recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")  
        self.root.title("PROXYMARKER")
        self.root.state("zoomed")

        #----BACKGROUND IMAGE-----
        img=Image.open(r"photos\project wallpaper.png")
        img=img.resize((1530,790))
        self.bgphoto=ImageTk.PhotoImage(img)

        bglabel=Label(self.root,image=self.bgphoto)
        bglabel.place(x=0,y=0,width=1530,height=790)


        #------BUTTONS--------
        #STUDENT DETAILS BUTTON
        buttonImage1=Image.open(r"photos\student details.png")
        buttonImage1=buttonImage1.resize((170,170))
        self.imageButton1=ImageTk.PhotoImage(buttonImage1)

        b1=Button(bglabel,image=self.imageButton1,command=self.student_details,cursor="hand2",border=0)
        b1.place(x=250,y=230,width=170,height=170)

        b1_1=Button(bglabel,text="Student Details",command=self.student_details,cursor="hand2",font=("Microsoft YaHei UI Light",14,"bold"),bg="#272343",fg="white",border=0)
        b1_1.place(x=250,y=400,width=170,height=50)

        #FACE RECOGNITION BUTTON
        buttonImage2=Image.open(r"photos\detect face.png")
        buttonImage2=buttonImage2.resize((170,170))
        self.imageButton2=ImageTk.PhotoImage(buttonImage2)

        b2=Button(bglabel,image=self.imageButton2,command=self.faceRecognition,cursor="hand2",border=0)
        b2.place(x=650,y=230,width=170,height=170)

        b2_2=Button(bglabel,text="Face Recognition",cursor="hand2",command=self.faceRecognition,font=("Microsoft YaHei UI Light",14,"bold"),bg="#272343",fg="white",border=0)
        b2_2.place(x=650,y=400,width=170,height=50)

        #ATTENDANCE BUTTON
        buttonImage3=Image.open(r"photos\attendance pic.png")
        buttonImage3=buttonImage3.resize((170,170))
        self.imageButton3=ImageTk.PhotoImage(buttonImage3)

        b3=Button(bglabel,image=self.imageButton3,command=self.Attendance,cursor="hand2",border=0)
        b3.place(x=1050,y=230,width=170,height=170)

        b3_3=Button(bglabel,text="Attendance",command=self.Attendance,cursor="hand2",font=("Microsoft YaHei UI Light",14,"bold"),bg="#272343",fg="white",border=0)
        b3_3.place(x=1050,y=400,width=170,height=50)

        #TRAIN DATA BUTTON
        buttonImage4=Image.open(r"photos\train data.png")
        buttonImage4=buttonImage4.resize((170,170))
        self.imageButton4=ImageTk.PhotoImage(buttonImage4)

        b4=Button(bglabel,image=self.imageButton4,cursor="hand2",command=self.train,border=0)
        b4.place(x=250,y=500,width=170,height=170)

        b4_4=Button(bglabel,text="Train Data",cursor="hand2",command=self.train,font=("Microsoft YaHei UI Light",14,"bold"),bg="#272343",fg="white",border=0)
        b4_4.place(x=250,y=670,width=170,height=50)

        #DATASET BUTTON
        buttonImage5=Image.open(r"photos\photos.png")
        buttonImage5=buttonImage5.resize((170,170))
        self.imageButton5=ImageTk.PhotoImage(buttonImage5)

        b5=Button(bglabel,image=self.imageButton5,cursor="hand2",command=self.openImg,border=0)
        b5.place(x=650,y=500,width=170,height=170)

        b5_5=Button(bglabel,text="Photos",cursor="hand2",command=self.openImg,font=("Microsoft YaHei UI Light",14,"bold"),bg="#272343",fg="white",border=0)
        b5_5.place(x=650,y=670,width=170,height=50)

        #DEVELOPER BUTTON
        buttonImage6=Image.open(r"photos\developer.png")
        buttonImage6=buttonImage6.resize((170,170))
        self.imageButton6=ImageTk.PhotoImage(buttonImage6)

        b6=Button(bglabel,command=self.Developer,image=self.imageButton6,cursor="hand2",border=0)
        b6.place(x=1050,y=500,width=170,height=170)

        b6_6=Button(bglabel,text="Developer",command=self.Developer,cursor="hand2",font=("Microsoft YaHei UI Light",14,"bold"),bg="#272343",fg="white",border=0)
        b6_6.place(x=1050,y=670,width=170,height=50)


    #------BUTTONS FUNCTION------
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=studentDetails(self.new_window)

    def train(self):
        self.new_window=Toplevel(self.root)
        self.app=trainDataset(self.new_window)

    def openImg(self):
        os.startfile("Data")

    def faceRecognition(self):
        self.new_window=Toplevel(self.root)
        self.app=faceRecognition(self.new_window)

    def Attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=studentAttendance(self.new_window)

    def Developer(self):
        self.new_window=Toplevel(self.root)
        self.app=developer(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj=face_recognition_system(root)
    root.mainloop()