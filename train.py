#-------IMPORTING LIBRARIES---------
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class trainDataset:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("PROXYMARKER")
        self.root.state("zoomed")

        #----BACKGROUND IMAGE-----
        img=Image.open(r"photos\Train data wallpaper.png")
        img=img.resize((1530,790))
        self.bgphoto=ImageTk.PhotoImage(img)

        bglabel=Label(self.root,image=self.bgphoto)
        bglabel.place(x=0,y=0,width=1530,height=790)
        
        #TARIN DATASET BUTTON
        trainButton=Button(self.root,text="TRAIN DATASET",command=self.trainingData,width=30,font=("Microsoft YaHei UI Light",35,"bold"),bg="#272343",fg="#f3f5ed",border=0)
        trainButton.place(x=470,y=537,height=98,width=588)

    def trainingData(self):
        dataDir=("Data")
        path=[os.path.join(dataDir,file) for file in os.listdir(dataDir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')   #GRAY SCALE IMAGE
            pic=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(pic)
            ids.append(id)

            cv2.imshow("Training Data",pic)
            cv2.waitKey(1)==13
            
        ids=np.array(ids)

        #------------TRAINING CLASSIFIER-------------
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Output","Training Dataset Completed!")
    

if __name__ == "__main__":
    root = Tk()
    obj=trainDataset(root)
    root.mainloop()