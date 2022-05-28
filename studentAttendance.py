#-------IMPORTING LIBRARIES-------
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from time import strftime
from datetime import datetime
import os
import csv
from tkinter import filedialog


data=[]
class studentAttendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("PROXYMARKER")
        self.root.state("zoomed")

        #----------VARIABLES-------------
        self.var_id=StringVar()
        self.var_rollNo=StringVar()
        self.var_studentName=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_status=StringVar()

        #----BACKGROUND IMAGE-----
        img=Image.open(r"photos\attendance wallpaper.png")
        img=img.resize((1530,790))
        self.bgphoto=ImageTk.PhotoImage(img)

        bglabel=Label(self.root,image=self.bgphoto)
        bglabel.place(x=0,y=0,width=1530,height=790)

        mainFrame=Frame(bglabel,bd=2,bg="white")
        mainFrame.place(x=685,y=250,width=750,height=330)

        #-------LABEL FRAME-------
        tableFrame=LabelFrame(mainFrame,bd=2,text="Attendance Details",font=("Microsoft YaHei UI Light",12,"bold"),bg="white")
        tableFrame.place(x=30,y=18,width=685,height=290)

        tableFrame=Frame(tableFrame,bd=2,relief=RIDGE,bg="white")
        tableFrame.place(x=15,y=10,width=645,height=250)


        #SCROLL BAR
        scroll_x=ttk.Scrollbar(tableFrame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tableFrame,orient=VERTICAL)

        self.table=ttk.Treeview(tableFrame,column=("id","rollNo","studentName","time","date","status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        #-----SCROLLBARS-----
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.table.xview)
        scroll_y.config(command=self.table.yview)

        self.table.heading("id",text="ID")
        self.table.heading("rollNo",text="RollNo")
        self.table.heading("studentName",text="StudentName")
        self.table.heading("time",text="Time")
        self.table.heading("date",text="Date")
        self.table.heading("status",text="Status")
        
        #TABLE HEADINGS WIDTH SIZE SETTING
        self.table["show"]="headings"
        self.table.column("id",width=120)
        self.table.column("rollNo",width=120)
        self.table.column("studentName",width=120)
        self.table.column("time",width=120)
        self.table.column("date",width=120)
        self.table.column("status",width=120)

        self.table.pack(fill=BOTH,expand=1)
    
    
        #LAST BUTTONS
        importCSV_btn=Button(self.root,text="Import CSV",command=self.importCsv,width=10,font=("Microsoft YaHei UI Light",18,"bold"),bg="#272343",fg="white",border=0)
        importCSV_btn.place(x=730,y=650,width=328,height=55)

        exportCSV_btn=Button(self.root,text="Export CSV",command=self.exportCSV,width=10,font=("Microsoft YaHei UI Light",18,"bold"),bg="#272343",fg="white",border=0)
        exportCSV_btn.place(x=1080,y=650,width=330,height=55)

    #---------FETCH DATA----------
    def fetchData(self,rows):
        global data
        data=rows
        self.table.delete(*self.table.get_children())
        for i in rows:
            self.table.insert("",END,values=i)

    #IMPORT CSV
    def importCsv(self):
        data.clear()
        f=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("Attendance","*.*")),parent=self.root)
        with open(f) as file:
            csvRead=csv.reader(file,delimiter=",")
            for i in csvRead:
                data.append(i)
            self.fetchData(data)

    #EXPORT CSV
    def exportCSV(self):
        try:
            if len(data)<1:
                messagebox.showerror("Error","No data found!",parent=self.root)
                return False
            f=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("Attendance","*.*")),parent=self.root)
            with open(f,mode="w",newline="") as file:
                exportCSVFile=csv.writer(file,delimiter=",")
                for i in data:
                    exportCSVFile.writerow(i)
                messagebox.showinfo("Success","Successfully Exported ",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj=studentAttendance(root)
    root.mainloop()