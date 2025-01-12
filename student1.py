from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter.messagebox as tsmg
import mysql.connector
import cv2
import os




class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognization System")
        self.root.wm_iconbitmap("Face.ico")
      


        #======Variable=================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.va_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
       

        #First Image
        img=Image.open(r"C:\Users\PC\Desktop\Face_Recognization System\College_image\first.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        firstlbl=Label(self.root,image=self.photoimg)
        firstlbl.place(x=0,y=0,width=500,height=130)
        
        #Second Image
        img1=Image.open(r"C:\Users\PC\Desktop\Face_Recognization System\College_image\allinone.jpeg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        firstlbl=Label(self.root,image=self.photoimg1)
        firstlbl.place(x=500,y=0,width=500,height=130)
         
        #Third Image
        img2=Image.open(r"C:\Users\PC\Desktop\Face_Recognization System\College_image\Background.webp")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        

        firstlbl=Label(self.root,image=self.photoimg2)
        firstlbl.place(x=1000,y=0,width=570,height=130)

     

          #BackgroundImage
        img3=Image.open(r"C:\Users\PC\Desktop\Face_Recognization System\College_image\bg.webp")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,height=710)

        title_label=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font="lucida 35 bold",fg='red')
        title_label.place(x=0,y=0,width=1530,height=45)
        

        mainframe=Frame(bg_img,borderwidth=2,bg="white")
        mainframe.place(x=5,y=55,width=1520,height=610)

        #Left Label frame
        Left_frame=LabelFrame(mainframe,bd=2,relief=RIDGE,bg="white",text="Student Information",font="comicsansms 12 bold")
        Left_frame.place(x=5,y=2,width=735,height=590)


        img4=Image.open(r"C:\Users\PC\Desktop\Face_Recognization System\College_image\hd2.jpeg")
        img4=img4.resize((730,130),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        f_lbl=Label(Left_frame,image=self.photoimg4)
        f_lbl.place(x=0,y=0,width=730,height=130)

         #Current Course Frame
        current_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,bg="white",text="Current Course Information",font="comicsansms 12 bold")
        current_frame.place(x=0,y=125,width=730,height=105)
          
          #Department

        current_label=Label(current_frame,text="Department:",font="lucida 12 bold",bg="white")
        current_label.grid(row=0,column=0,padx=10,sticky=W)
        
        current_combo=ttk.Combobox(current_frame,textvariable=self.var_dep,font="lucida 12 bold",width=17,state="readonly")
        current_combo["values"]=("Select Department","Computer Science","IT","Mechanical","Civil")
        current_combo.current(0)
        current_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


         #Course
        course_label=Label(current_frame,text="Course:",font="comicsansms 12 bold",bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=E)


        course_combo=ttk.Combobox(current_frame,textvariable=self.var_course,font="comicsansms 12 bold",state="readonly",width=17)
        course_combo["values"]=("Select Course","B.Tech","Bsc","M.Tech","MBA")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

         #Year
        year_label=Label(current_frame,text="Year:",font="comicsansms 12 bold",bg="white")
        year_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        year_combo=ttk.Combobox(current_frame,font="comicsansms 12 bold",width=17,textvariable=self.var_year,state="readonly")
        year_combo["values"]=("Select Year","2022-2023","2023-2024","2024-2025","2025-2026")
        year_combo.current(0)
        year_combo.grid(row=3,column=1,padx=2,pady=5,sticky=W)

        #Semester
        sem_label=Label(current_frame,text="Semester:",bg="white",font="comicsansms 12 bold")
        sem_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        sem_combo=ttk.Combobox(current_frame,font="comicsamsms 12 bold",width=17,textvariable=self.var_semester,state="readonly")
        sem_combo["values"]=("Select Semester","Semester-1","Semester-2")
        sem_combo.current(0)
        sem_combo.grid(row=3,column=3,padx=2,pady=5,sticky=E)


        #Class Student Information Label Frame
        class_frame=LabelFrame(Left_frame,text="Class Student Information",bg="white",relief=RIDGE,bd=2,font="comicsansms 12 bold")
        class_frame.place(x=0,y=230,width=730,height=280)        
                  
                  
                  #studentID
        
        studentId_label=Label(class_frame,text="StudentId No:",bg="white",font="comicsansms 12 bold")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
       
        studentId_entry=Entry(class_frame,font="comicsansms 12 bold",width=17,relief=RIDGE,bd=2,textvariable=self.va_std_id)
        studentId_entry.grid(row=0,padx=5,pady=5,column=1,sticky=W)
   
              #Student Name

        studentName_label=Label(class_frame,text="Student Name:",bg="white",font="comicsansms 12 bold")
        studentName_label.grid(row=0,column=3,padx=10,sticky=W)

        studentName_entry=Entry(class_frame,font="comicsansms 12 bold",width=17,relief=RIDGE,bd=2,textvariable=self.var_std_name)
        studentName_entry.grid(row=0,column=4,padx=2,pady=10,sticky=E)


              #Class Division
        Cd_label=Label(class_frame,text="Class Division:",bg="white",font="comicsansms 12 bold")
        Cd_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        #cd_Entry=Entry(class_frame,font="comicsansms 12 bold",width=17,bg="white",textvariable=self.var_div,relief=RIDGE,bd=2)
        #cd_Entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        cd_combo=ttk.Combobox(class_frame,width=15,textvariable=self.var_div,font="comicsansms 12 bold",state="readonly")
        cd_combo["values"]=("A","B","C")
        cd_combo.current(0)
        cd_combo.grid(row=1,column=1,padx=5,pady=10,sticky=W)

              #Roll No.
        rollNo_label=Label(class_frame,text="Roll No:",bg="white",font="comicsansms 12 bold")
        rollNo_label.grid(row=1,column=3,padx=10,pady=10,sticky=W)

        rollNo_entry=Entry(class_frame,font="comicsansms 12 bold",width=17,relief=RIDGE,bd=2,textvariable=self.var_roll)
        rollNo_entry.grid(row=1,column=4,padx=2,pady=10,sticky=E)
          
          #Gender
       
        Gender_label=Label(class_frame,text="Gender:",bg="white",font="comicsansms 12 bold")
        Gender_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        #Gender_entry=Entry(class_frame,font="comicsansms 12 bold",width=17,bd=2,relief=RIDGE,bg="white",textvariable=self.var_gender)
        #Gender_entry.grid(row=2,column=1,padx=5,pady=1,sticky=W)           
        
        gender_combo=ttk.Combobox(class_frame,state="readonly",width=15,textvariable=self.var_gender,font="comicsansms 12 bold")
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=5,pady=10,sticky=W)

        
        
              #DOB
        DOB_label=Label(class_frame,text="DOB:",bg="white",font="comicsansms 12 bold")
        DOB_label.grid(row=2,column=3,padx=10,pady=10,sticky=W)

        DOB_entry=Entry(class_frame,font="comicsansms 12 bold",width=17,relief=RIDGE,bd=2,textvariable=self.var_dob)
        DOB_entry.grid(row=2,column=4,padx=2,pady=10,sticky=E)
              #Email
        email_label=Label(class_frame,text="Email",bg="white",font="comicsansms 12 bold")
        email_label.grid(row=3,column=0,padx=10,pady=10,sticky=W)

        email_entry=Entry(class_frame,font="comicsansms 12 bold",width=17,relief=RIDGE,bd=2,textvariable=self.var_email)
        email_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)

               #phone no.
        PhoneNo_label=Label(class_frame,text="Phone No:",bg="white",font="comicsansms 12 bold")
        PhoneNo_label.grid(row=3,column=3,padx=10,pady=10,sticky=W)

        PhoneNo_entry=Entry(class_frame,font="comicsansms 12 bold",width=17,relief=RIDGE,bd=2,textvariable=self.var_phone)
        PhoneNo_entry.grid(row=3,column=4,padx=2,pady=10,sticky=E)       
                 # ADDRESS
        address_label=Label(class_frame,text="Address:",bg="white",font="comicsansms 12 bold")
        address_label.grid(row=4,column=0,padx=10,pady=10,sticky=W)
        
        address_entry=Entry(class_frame,font="comicsansms 12 bold",width=17,relief=RIDGE,bd=2,textvariable=self.var_address)
        address_entry.grid(row=4,column=1,padx=5,pady=5,sticky=W) 

                     
        
               # Teacher Name
        TeacherName_label=Label(class_frame,text="Teacher Name:",bg="white",font="comicsansms 12 bold")
        TeacherName_label.grid(row=4,column=3,padx=10,pady=10,sticky=W)
                        
        TeacherName_entry=Entry(class_frame,font="comicsansms 12 bold",width=17,relief=RIDGE,bd=2,textvariable=self.var_teacher)
        TeacherName_entry.grid(row=4,column=4,padx=2,pady=10,sticky=E)
      

             #Radio BUTTON
        self.var_radio1=StringVar()
        radiobuttton1=ttk.Radiobutton(class_frame,variable=self.var_radio1,text="take photo sample",value="Yes")
        radiobuttton1.grid(row=5,column=0)

        
        radiobuttton2=ttk.Radiobutton(class_frame,text="No Photo Sample",value="No",variable=self.var_radio1)
        radiobuttton2.grid(row=5,column=1)

           # Left Tird Frame for BUTTON

        button_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,bg="white")
        button_frame.place(x=0,y=510,width=730,height=30)

        save_btn=Button(button_frame,bg="blue",cursor="hand2",fg="white",text="SAVE",width=22,font="comicsansms 10 bold",relief=RIDGE,command=self.add_data)
        save_btn.grid(row=0,column=0)

        update_btn=Button(button_frame,bg="blue",cursor="hand2",fg="white",text="UPDATE",width=22,font="comicsansms 10 bold",relief=RIDGE,command=self.update_data)
        update_btn.grid(row=0,column=1)


        delete_btn=Button(button_frame,bg="blue",cursor="hand2",fg="white",text="DELETE",width=22,font="comicsansms 10 bold",relief=RIDGE,command=self.delete_data)
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(button_frame,bg="blue",cursor="hand2",fg="white",text="RESET",width=22,font="comicsansms 10 bold",relief=RIDGE,command=self.reset_data)
        reset_btn.grid(row=0,column=3)



         
        #Left Fourth Frame
        last_frame=LabelFrame(Left_frame,bg="white",bd=2,relief=RIDGE)
        last_frame.place(x=0,y=540,width=730,height=27) 
         

        addphoto_btn=Button(last_frame,bg="blue",cursor="hand2",fg="white",text="ADD PHOTO SAMPLE",width=90,font="comicsansms 10 bold",relief=RIDGE,command=self.genrate_dataset)
        addphoto_btn.grid(row=1,column=0,)

        


        #Right Label Frame
        Right_frame=LabelFrame(mainframe,bd=2,relief=RIDGE,bg="white",text="Student Details",font="comicsansms 12 bold")
        Right_frame.place(x=750,y=2,width=735,height=590)

        img5=Image.open(r"C:\Users\PC\Desktop\Face_Recognization System\College_image\hd2.jpeg")
        img5=img5.resize((730,130),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        f_lbl=Label(Right_frame,image=self.photoimg5)
        f_lbl.place(x=0,y=0,width=730,height=130)

           # ===================Search System===================
        
        viewstudent_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,bg="white",text="View Student Details",font="comicsansms 12 bold")
        viewstudent_frame.place(x=0,y=135,width=730,height=70)

        Search_label=Label(viewstudent_frame,text="Details",bg="red",font="comicsansms 20 bold",fg="white",width=45)
        Search_label.place(x=0,y=0)
        

        

      #    RIGHT TABLE FRAME

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=0,y=200,width=730,height=350)

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")

        self.student_table.heading("gender",text="Gender")

        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

       #=====================Function Decleration fro adding data ===================== 
    def add_data(self):
      if self.var_dep.get()=="select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            tsmg.showerror("Error","All Fields are required",parent=self.root)
      else:
          try:
            conn=mysql.connector.connect(host="localhost",username="root",password="T#9758@qlph",database="face_recognition_system")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.va_std_id.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_radio1.get()
                                                                                                              ))
            conn.commit()
            self.fetch_data()
            conn.close()
            tsmg.showinfo("Success","Student details has been added Successfully",parent=self.root)
          except Exception as es:
               tsmg.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    #===================Fetch Data=====================
    
    
    def fetch_data(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="T#9758@qlph",database="face_recognition_system")
         my_cursor=conn.cursor()
         my_cursor.execute("Select * from Student")
         data=my_cursor.fetchall()

         if len(data)!=0:
             self.student_table.delete(*self.student_table.get_children())
             for i in data:
                 self.student_table.insert("",END,values=i)
             conn.commit()
         conn.close()


#==========Get Cursor=========# For updating the database information
    def get_cursor(self,event=""): 
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)   #for table content we use item()
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        
        self.var_year.set(data[2]),
             
        self.var_semester.set(data[3]),
        self.va_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

   #Update Function==================
    def update_data(self):
      if self.var_dep.get()=="select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            tsmg.showerror("Error","All Fields are required",parent=self.root)

      else:
         try:
            update=tsmg.askyesno("Update","Do you want to update the student details",parent=self.root)
            if update > 0:
                  conn=mysql.connector.connect(host="localhost",username="root",password="T#9758@qlph",database="face_recognition_system")
                  my_cursor=conn.cursor()
                  my_cursor.execute("Update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Name=%s,PhotoSample=%s where Student_id=%s",(
                                    
                                    
                                    
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_radio1.get(),
                                                                                                            self.va_std_id.get()
                                    
                                    
                                    
                                                                                                                                             ))

            else:
              if not update:
                  return  
        
            tsmg.showinfo("Success","Student details successfully updates",parent=self.root)
            conn.commit()
            self.fetch_data()
            conn.close()
         except Exception as es:
            tsmg.showerror("Error",f"Due to :{str(es)}",parent=self.root)  
   
   # Delete Function Button
    def delete_data(self):
        if self.va_std_id.get()=="":
            tsmg.showerror("Error","Student id must required",parent=self.root)
        else:
            try:
                delete=tsmg.askyesno("Student Data Delete Page","Do you want to delete this student data",parent=self.root)
                if delete>0:
                  conn=mysql.connector.connect(host="localhost",username="root",password="T#9758@qlph",database="face_recognition_system")
                  my_cursor=conn.cursor()
                  sql="delete from student where Student_id=%s"
                  val=(self.va_std_id.get(),)
                  my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                tsmg.showinfo("Delete","Successfully deleted student detials",parent=self.root)
            except Exception as es:
                  tsmg.showerror("Error",f"Due to :{str(es)}",parent=self.root)      
    #============Reset Button================
    def reset_data(self):
      self.var_dep.set("Select Department"),
      self.var_course.set("Select Course"),
      self.var_year.set("Select Year"),
      self.var_semester.set("Select Semester"),
      self.va_std_id.set(""),
      self.var_std_name.set(""),
      self.var_div.set("Select Division"),
      self.var_roll.set(""),
      self.var_gender.set("Male"),
      self.var_dob.set(""),
      self.var_email.set(""),
      self.var_phone.set(""),
      self.var_address.set(""),
      self.var_teacher.set(""),
      self.var_radio1.set("")
 
    #=================Genrate Data set and take PHOTo Samples ====================   
    def genrate_dataset(self):
      if self.var_dep.get()=="select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            tsmg.showerror("Error","All Fields are required",parent=self.root)

      else:
          try:
            conn=mysql.connector.connect(host="localhost",username="root",password="T#9758@qlph",database="face_recognition_system")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from student")
            myresult=my_cursor.fetchall()
            id=0
            for x in myresult:
                id+=1
            my_cursor.execute("Update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Name=%s,PhotoSample=%s where Student_id=%s",(
                                    
                                    
                                    
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_radio1.get(),
                                                                                                            self.va_std_id.get()==id+1
                                                                                                                                ))
                                    
                                    
                                                                                                                                        
            
                
            conn.commit()
            self.fetch_data()
            self.reset_data()
            conn.close()
            #==============================Load Predefine data on face frontal from opencv=====================

            face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")#C:\\Users\\PC\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
            
            def face_cropped(img):
              
              print(os.path.isfile("haarcascade_frontalface_default.xml"))
              print("Welcome 1")
              gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   #BGRColor image into grey image
              faces=face_classifier.detectMultiScale(gray,1.3,5)
              # 1.3 means Scaling Factor
              #Minimum Neighbour = 5
              for (x,y,w,h) in faces: #for making Triangle
                face_cropped=img[y:y+h,x:x+w]
                print("Welcom 2")  
                return face_cropped
               
                #====For opening the Camera=======
            cap=cv2.VideoCapture(0)  # 0 means bydefault laptop camera will open
            img_id=0
            while True:
                ret,my_frame=cap.read()
                if face_cropped(my_frame) is not None:
                  img_id+=1
                  face=cv2.resize(face_cropped(my_frame),(450,450))
                  face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                  file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                  cv2.imwrite(file_name_path,face)
                  cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                  cv2.imshow("Cropped Face",face)

                if cv2.waitKey(1)==13 or int(img_id)==100:
                    break
            print("Welcome 3")
            cap.release()
            cv2.destroyAllWindows()
            tsmg.showinfo("Result","Generating data sets completed!!!")
          except Exception as es:
              tsmg.showerror("Error",f"Due To:{str(es)}",parent=self.root)
          print("Welcome 4")     
if __name__ == "__main__":
    root=Tk()
    obj= student(root)
    root.mainloop()

