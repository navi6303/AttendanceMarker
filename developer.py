from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk

class developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("PROXYMARKER")
        self.root.state("zoomed")

        #----BACKGROUND IMAGE-----
        img=Image.open(r"photos\background.png")
        img=img.resize((1530,790))
        self.bgphoto=ImageTk.PhotoImage(img)

        bglabel=Label(self.root,image=self.bgphoto)
        bglabel.place(x=0,y=0,width=1530,height=790)

        mainFrame=Frame(bglabel,bg="#f3f5ed")
        mainFrame.place(x=460,y=0,width=650,height=800)

        #-------DEVELOPER PICTURE---------
        heading=Label(mainFrame,text="DEVELOPER",fg="#272343",bg="#f3f5ed",font=("Microsoft YaHei UI Light",50,"bold"))
        heading.place(x=140,y=40)
        dimg=Image.open(r"photos\developer pic.jpg")
        dimg=dimg.resize((380,500))
        self.dphoto=ImageTk.PhotoImage(dimg)

        dlabel=Label(mainFrame,image=self.dphoto)
        dlabel.place(x=155,y=150,width=350,height=500)

        name=Label(mainFrame,text="VAISHNAVI",fg="#272343",bg="#f3f5ed",font=("Microsoft YaHei UI Light",30,"bold"))
        name.place(x=220,y=650)

        line=Label(mainFrame,text="Full Stack Web Developer Enthusiast",fg="#272343",bg="#f3f5ed",font=("Microsoft YaHei UI Light",20,"bold"))
        line.place(x=90,y=700)

if __name__ == "__main__":
    root = Tk()
    obj=developer(root)
    root.mainloop()