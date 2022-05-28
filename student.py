#------IMPORTING LIBRARIES-------
import string
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from cv2 import HOUGH_STANDARD
import mysql.connector
from requests import delete
import cv2


class studentDetails:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("PROXYMARKER")
        self.root.state("zoomed")

        #----------VARIABLES----------
        self.var_dept=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_rollNo=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()

        #----BACKGROUND IMAGE-----
        img=Image.open(r"photos\Student details wallpaper.png")
        img=img.resize((1530,790))
        self.bgphoto=ImageTk.PhotoImage(img)

        bglabel=Label(self.root,image=self.bgphoto)
        bglabel.place(x=0,y=0,width=1530,height=790)

        mainFrame=Frame(bglabel,bd=2,bg="white")
        mainFrame.place(x=40,y=190,width=1450,height=570)

        #-------LEFT LABEL FRAME-------
        leftFrame=LabelFrame(mainFrame,bd=2,text="Information",font=("Microsoft YaHei UI Light",12,"bold"),bg="white")
        leftFrame.place(x=20,y=10,width=690,height=535)

        #DEPARTMENT
        deptLabel=Label(leftFrame,text=" Department: ",font=("Microsoft YaHei UI Light",12,"bold"),bg="white")
        deptLabel.grid(row=0,column=0,padx=5,sticky=W)

        deptBox=ttk.Combobox(leftFrame,textvariable=self.var_dept,font=("Microsoft YaHei UI Light",11,"bold"),width=16, state="readonly")
        deptBox["values"]=("Select Department","Computer","IT","ECE","Civil","Mechanical","Production")
        deptBox.current(0)
        deptBox.grid(row=0,column=1,padx=5,pady=22,sticky=W)

        #COURSE
        courseLabel=Label(leftFrame,text=" Course: ",font=("Microsoft YaHei UI Light",12,"bold"),bg="white")
        courseLabel.grid(row=0,column=2,padx=5,sticky=W)

        courseBox=ttk.Combobox(leftFrame,textvariable=self.var_course,font=("Microsoft YaHei UI Light",12,"bold"),width=14, state="readonly")
        courseBox["values"]=("Select Course","FE","SE","TE","BE")
        courseBox.current(0)
        courseBox.grid(row=0,column=3,padx=5,pady=22,sticky=W)

        #YEAR
        yearLabel=Label(leftFrame,text=" Year: ",font=("Microsoft YaHei UI Light",12,"bold"),bg="white")
        yearLabel.grid(row=1,column=0,padx=5,sticky=W)

        yearBox=ttk.Combobox(leftFrame,textvariable=self.var_year,font=("Microsoft YaHei UI Light",12,"bold"),width=14, state="readonly")
        yearBox["values"]=("Select Year","2021-22","2022-23","2023-24")
        yearBox.current(0)
        yearBox.grid(row=1,column=1,padx=5,pady=22,sticky=W)

        #SEMESTER
        semLabel=Label(leftFrame,text=" Semester: ",font=("Microsoft YaHei UI Light",12,"bold"),bg="white")
        semLabel.grid(row=1,column=2,padx=5,sticky=W)

        semBox=ttk.Combobox(leftFrame,textvariable=self.var_semester,font=("Microsoft YaHei UI Light",12,"bold"),width=14, state="readonly")
        semBox["values"]=("Select Semester","1","2","3","4","5","6","7","8")
        semBox.current(0)
        semBox.grid(row=1,column=3,padx=5,pady=22,sticky=W)

        #STUDENT ID
        StudentIDLabel=Label(leftFrame,text=" Student ID: ",font=("Microsoft YaHei UI Light",12,"bold"),bg="white")
        StudentIDLabel.grid(row=2,column=0,padx=5,pady=22,sticky=W)

        studentID_entry=ttk.Entry(leftFrame,textvariable=self.var_std_id,width=16,font=("Microsoft YaHei UI Light",12,"bold"))
        studentID_entry.grid(row=2,column=1,padx=5,pady=22,sticky=W)

        #STUDENT NAME
        StudentNameLabel=Label(leftFrame,text=" Student Name: ",font=("Microsoft YaHei UI Light",12,"bold"),bg="white")
        StudentNameLabel.grid(row=2,column=2,padx=5,pady=22,sticky=W)

        studentName_entry=ttk.Entry(leftFrame,textvariable=self.var_std_name,width=16,font=("Microsoft YaHei UI Light",12,"bold"))
        studentName_entry.grid(row=2,column=3,padx=5,pady=22,sticky=W)

        #STUDENT DIVISION
        StudentDivLabel=Label(leftFrame,text=" Student Division: ",font=("Microsoft YaHei UI Light",12,"bold"),bg="white")
        StudentDivLabel.grid(row=3,column=0,padx=5,pady=22,sticky=W)
        
        divBox=ttk.Combobox(leftFrame,textvariable=self.var_div,font=("Microsoft YaHei UI Light",12,"bold"),width=14, state="readonly")
        divBox["values"]=("Select Division","A","B","C","D")
        divBox.current(0)
        divBox.grid(row=3,column=1,padx=5,pady=22,sticky=W)

        #STUDENT ROLLNO
        StudentRollNoLabel=Label(leftFrame,text=" Student RollNo: ",font=("Microsoft YaHei UI Light",12,"bold"),bg="white")
        StudentRollNoLabel.grid(row=3,column=2,padx=5,pady=22,sticky=W)

        studentRollNo_entry=ttk.Entry(leftFrame,textvariable=self.var_rollNo,width=16,font=("Microsoft YaHei UI Light",12,"bold"))
        studentRollNo_entry.grid(row=3,column=3,padx=5,pady=22,sticky=W)

        #STUDENT GENDER
        StudentGenderLabel=Label(leftFrame,text=" Student Gender: ",font=("Microsoft YaHei UI Light",12,"bold"),bg="white")
        StudentGenderLabel.grid(row=4,column=0,padx=5,pady=22,sticky=W)

        genderBox=ttk.Combobox(leftFrame,textvariable=self.var_gender,font=("Microsoft YaHei UI Light",12,"bold"),width=14, state="readonly")
        genderBox["values"]=("Select Gender","Male","Female","Other")
        genderBox.current(0)
        genderBox.grid(row=4,column=1,padx=5,pady=22,sticky=W)

        #STUDENT EMAIL
        StudentEmailLabel=Label(leftFrame,text=" Student Email: ",font=("Microsoft YaHei UI Light",12,"bold"),bg="white")
        StudentEmailLabel.grid(row=4,column=2,padx=5,pady=22,sticky=W)

        studentEmail_entry=ttk.Entry(leftFrame,textvariable=self.var_email,width=16,font=("Microsoft YaHei UI Light",12,"bold"))
        studentEmail_entry.grid(row=4,column=3,padx=5,pady=22,sticky=W)

        #LAST BUTTONS FRAME
        lastButtonFrame=Frame(leftFrame,bd=2,bg="white")
        lastButtonFrame.place(x=10,y=380,width=670,height=50)

        save_btn=Button(lastButtonFrame,text="Save",command=self.addData,width=14,font=("Microsoft YaHei UI Light",12,"bold"),bg="#272343",fg="white",border=0)
        save_btn.grid(row=0,column=0,padx=9,pady=4)

        update_btn=Button(lastButtonFrame,text="Update",command=self.updateData,width=14,font=("Microsoft YaHei UI Light",12,"bold"),bg="#272343",fg="white",border=0)
        update_btn.grid(row=0,column=1,padx=9,pady=4)

        delete_btn=Button(lastButtonFrame,text="Delete",command=self.deleteData,width=14,font=("Microsoft YaHei UI Light",12,"bold"),bg="#272343",fg="white",border=0)
        delete_btn.grid(row=0,column=2,padx=9,pady=4)

        reset_btn=Button(lastButtonFrame,text="Reset",command=self.resetData,width=14,font=("Microsoft YaHei UI Light",12,"bold"),bg="#272343",fg="white",border=0)
        reset_btn.grid(row=0,column=3,padx=9,pady=4)

        #TAKE PHOTO SAMPLE BUTTON
        photoButtonFrame=Frame(leftFrame,bd=2,bg="white")
        photoButtonFrame.place(x=90,y=420,width=470,height=55)

        take_photo_btn=Button(photoButtonFrame,command=self.generateDataset,text="Take Photo Sample",width=20,font=("Microsoft YaHei UI Light",12,"bold"),bg="#272343",fg="white",border=0)
        take_photo_btn.grid(row=0,column=2,padx=145,pady=9)

        #-------RIGHT LABEL FRAME-------
        rightFrame=LabelFrame(mainFrame,bd=2,text="Search System",font=("Microsoft YaHei UI Light",12,"bold"),bg="white")
        rightFrame.place(x=730,y=10,width=690,height=535)

        #SEARCH BY BOX
        searchByLabel=Label(rightFrame,text=" Search by: ",font=("Microsoft YaHei UI Light",12,"bold"),bg="white")
        searchByLabel.grid(row=0,column=0,padx=7,pady=20,sticky=W)
        self.var_searchValue=StringVar()

        searchBox=ttk.Combobox(rightFrame,textvariable=self.var_searchValue,font=("Microsoft YaHei UI Light",12,"bold"),width=13, state="readonly")
        searchBox["values"]=("Select","Roll No","Name")
        searchBox.current(0)
        searchBox.grid(row=0,column=1,padx=7,pady=20,sticky=W)

        #ENTER SEARCH BY DATA
        self.var_search=StringVar()
        search_entry=ttk.Entry(rightFrame,width=14,textvariable=self.var_search,font=("Microsoft YaHei UI Light",12,"bold"))
        search_entry.grid(row=0,column=2,padx=7,pady=20,sticky=W)

        #SEARCH BUTTONS
        search_photo_btn=Button(rightFrame,text="Search",command=self.searchData,width=10,font=("Microsoft YaHei UI Light",12,"bold"),bg="#272343",fg="white",border=0)
        search_photo_btn.grid(row=0,column=3,padx=7,pady=20)

        showAll_btn=Button(rightFrame,text="Show All",command=self.fetchData,width=10,font=("Microsoft YaHei UI Light",12,"bold"),bg="#272343",fg="white",border=0)
        showAll_btn.grid(row=0,column=4,padx=7,pady=20)

        #-------TABLE FRAME--------
        tableFrame=Frame(rightFrame,bd=2, relief=RIDGE, bg="white")
        tableFrame.place(x=6,y=80,width=670,height=420)

        #SCROLLBARS
        scroll_x=ttk.Scrollbar(tableFrame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tableFrame,orient=VERTICAL)

        #TREEVIEW TABLE 
        self.student_table=ttk.Treeview(tableFrame,columns=("dept","course","year","semester","studentID","studentName","division","rollNo","gender","email"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        #HEADINGS IN TABLE
        self.student_table.heading("dept",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("semester",text="Semester")
        self.student_table.heading("studentID",text="StudentID")
        self.student_table.heading("studentName",text="StudentName")
        self.student_table.heading("division",text="Division")
        self.student_table.heading("rollNo",text="RollNo")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("email",text="Email")
        self.student_table["show"]="headings"

        #TABLE HEADINGS WIDTH SIZE SETTING 
        self.student_table.column("dept",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("semester",width=100)
        self.student_table.column("studentID",width=100)
        self.student_table.column("studentName",width=100)
        self.student_table.column("division",width=100)
        self.student_table.column("rollNo",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("email",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetchData()

    #------------FUNCTION DECLARATION-------------

    #ADD DATA IN DATABSE
    def addData(self):
        if self.var_dept.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester"or self.var_std_id.get()=="" or self.var_std_name.get()==""or self.var_div.get()=="Select Division" or self.var_rollNo.get()=="" or self.var_gender.get()=="Select Gender" or self.var_email.get()=="":
            messagebox.showerror("Error","All fields are required!",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Navisharma@06",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.var_dept.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_std_id.get(),
                self.var_std_name.get(),
                self.var_div.get(),
                self.var_rollNo.get(),
                self.var_gender.get(),
                self.var_email.get()
                ))

                conn.commit()
                self.fetchData()
                conn.close()
                messagebox.showinfo("Success","All Records are Saved",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    

    #FETCH DATA FROM DATABASE
    def fetchData(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Navisharma@06",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    

    #CURSOR 
    def get_cursor(self,event=""):
        cursorFocus=self.student_table.focus()
        content=self.student_table.item(cursorFocus)
        data=content["values"]

        self.var_dept.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_rollNo.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_email.set(data[9])


    #UPDATE DATA IN DATABASE
    def updateData(self):
        if self.var_dept.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester"or self.var_std_id.get()=="" or self.var_std_name.get()==""or self.var_div.get()=="Select Division" or self.var_rollNo.get()=="" or self.var_gender.get()=="Select Gender" or self.var_email.get()=="":
            messagebox.showerror("Error","All fields are required!",parent=self.root)
        else:
            try:
                Update1=messagebox.askyesno("Update","Do you want to update?",parent=self.root)
                if Update1>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Navisharma@06",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set dept=%s,course=%s,year=%s,semester=%s,studentName=%s,division=%s,rollNo=%s,gender=%s,email=%s where studentID=%s",(
                    self.var_dept.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_rollNo.get(),
                    self.var_gender.get(),
                    self.var_email.get(),
                    self.var_std_id.get()
                    ))
                else:
                    if not Update1:
                        return
                messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
                conn.commit()
                self.fetchData()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    

    #DELETE DATA IN DATABASE
    def deleteData(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student ID must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to delete this data?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Navisharma@06",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where studentID=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetchData()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)


    #RESET DATA TO DEAFULT VALUES
    def resetData(self):
        self.var_dept.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_rollNo.set("")
        self.var_gender.set("Select Gender")
        self.var_email.set("")

    
    #------------SEARCH FRAME FUNCTIONS-------------
    def searchData(self):
        if self.var_search.get()=="" or self.var_searchValue.get()=="Select":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Navisharma@06",database="face_recognizer")
                my_cursor=conn.cursor()
                sql = "SELECT StudentID,studentName,dept,course,year,semester,division,gender,RollNo,email FROM student where rollNo='" +str(self.var_search.get()) + "'" 
                my_cursor.execute(sql)
                rows=my_cursor.fetchall()        
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    #------------GENEREATE DATASET-----------------
    def generateDataset(self):
        if self.var_dept.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester"or self.var_std_id.get()=="" or self.var_std_name.get()==""or self.var_div.get()=="Select Division" or self.var_rollNo.get()=="" or self.var_gender.get()=="Select Gender" or self.var_email.get()=="":
            messagebox.showerror("Error","All fields are required!",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Navisharma@06",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                result=my_cursor.fetchall()
                id=0
                for x in result:
                    id+=1
                my_cursor.execute("update student set dept=%s,course=%s,year=%s,semester=%s,studentName=%s,division=%s,rollNo=%s,gender=%s,email=%s where studentID=%s",(
                self.var_dept.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_std_name.get(),
                self.var_div.get(),
                self.var_rollNo.get(),
                self.var_gender.get(),
                self.var_email.get(),
                self.var_std_id.get()==id+1
                ))
                conn.commit()
                self.fetchData()
                self.resetData()
                conn.close()

                #--------------LOADING DATA(HAARCASCADE FRONTAL FACE FILE FROM OPENCV)-----------------
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def faceCropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5) #scaling factor,minimum neighbour

                    for (x,y,w,h) in faces:
                        faceCropped=img[y:y+h,x:x+w]
                        return faceCropped
                    
                cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
                imgID=0
                while True:
                    ret,myframe=cap.read()
                    if faceCropped(myframe) is not None:
                        imgID+=1
                        face=cv2.resize(faceCropped(myframe),(300,300))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        fileNamePath="Data/student."+str(id)+"."+str(imgID)+".jpg"
                        cv2.imwrite(fileNamePath,face)
                        cv2.putText(face,str(imgID),(50,50),cv2.FONT_HERSHEY_DUPLEX,1,(0,255,0),1)
                        cv2.imshow("Capture Images",face)

                    if cv2.waitKey(1)==13 or int(imgID)==25:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Information","Capturing photos completed!")
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 

if __name__ == "__main__":
    root = Tk()
    obj=studentDetails(root)
    root.mainloop()