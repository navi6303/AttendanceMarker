#-------IMPORTING LIBRARIES---------
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime


class faceRecognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("PROXYMARKER")
        self.root.state("zoomed")

        #----BACKGROUND IMAGE-----
        img=Image.open(r"photos\Face Recognition.png")
        img=img.resize((1530,790))
        self.bgphoto=ImageTk.PhotoImage(img)

        bglabel=Label(self.root,image=self.bgphoto)
        bglabel.place(x=0,y=0,width=1530,height=790)

        #FACE RECOGNITION BUTTON
        fr=Button(self.root,text="FACE RECOGNITION",command=self.fr,width=30,font=("Microsoft YaHei UI Light",20,"bold"),bg="#272343",fg="#f3f5ed",border=0)
        fr.place(x=920,y=560,height=91,width=350)



    #---------------MARK ATTENDANCE FUNCTION------------------
    def markAttendance(Self,i,r,n):
        with open("Attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            nameList=[]
            for line in myDataList:
                entry=line.split((","))
                nameList.append(entry[0])
            if((i not in nameList) and (n not in nameList) and (r not in nameList)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dt=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{r},{dt},{d1},Present")


    #-----------FACE RECOGNITION FUNCTION-----------
    def fr(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            points=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(227,228,173),2)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="Navisharma@06",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select studentName from student where studentID="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select rollNo from student where studentID="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select studentID from student where studentID="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)



                if confidence > 80:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_DUPLEX,0.8,(227,228,173),2)
                    cv2.putText(img,f"RollNo:{r}",(x,y-55),cv2.FONT_HERSHEY_DUPLEX,0.8,(227,228,173),2)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_DUPLEX,0.8,(227,228,173),2)
                    self.markAttendance(i,r,n)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(60,20,220),2)
                    cv2.putText(img,"UNKNOWN",(x,y-30),cv2.FONT_HERSHEY_DUPLEX,0.8,(60,20,220),2)
                
                points=[x,y,w,h]

            return points
        
        def recognize(img,clf,faceCascade):
            points=draw_boundary(img,faceCascade,1.1,10,(227,228,173),"FACE",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("PROXYMARKER",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj=faceRecognition(root)
    root.mainloop()