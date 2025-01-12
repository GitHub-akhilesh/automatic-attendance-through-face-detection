from tkinter import *
from tkinter import ttk
from tkinter import messagebox as tsmg
from PIL import Image,ImageTk
from student1 import student
import os
from time import strftime
from datetime import datetime
from train import Train
from face_recognition import Face_Recognition
from attendence import Attendence
from developer import Developer
from help import Help


class Face_Recognization_system:
#============Main==================  
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognization System")
        self.root.wm_iconbitmap("Face.ico")
         

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
        firstlbl.place(x=1000,y=0,width=550,height=130)
        
        #BackgroundImage
        img3=Image.open(r"C:\Users\PC\Desktop\Face_Recognization System\College_image\bg.webp")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("Helvetica",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        #=================Time============
        def time():
               string=strftime('%H:%M:%S %p') # strftime hold current time for am pm we use %p
               lbl.config(text=string)
               lbl.after(1000,time)

        lbl=Label(title_lbl,font=('times new roman',14,'bold'),bg='white',fg='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()
               

        #Student Button 1
        img4=Image.open(r"C:\Users\PC\Desktop\Face_Recognization System\College_image\student.webp")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="Darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

        #Face Detector Button 2
        img5=Image.open(r"C:\Users\PC\Desktop\Face_Recognization System\College_image\Second_2.webp")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="Darkblue",fg="white",command=self.face_data)
        b1_1.place(x=500,y=300,width=220,height=40)
        

         #Attendence face Button 3
        img6=Image.open(r"C:\Users\PC\Desktop\Face_Recognization System\College_image\Attendence.jpeg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendence_data)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendence",cursor="hand2",font=("times new roman",15,"bold"),bg="Darkblue",fg="white",command=self.attendence_data)
        b1_1.place(x=800,y=300,width=220,height=40)


         #Help Desk Button 4
        img7=Image.open(r"C:\Users\PC\Desktop\Face_Recognization System\College_image\helpdesk.jpeg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="Darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)



         #Train face Button 5
        img8=Image.open(r"C:\Users\PC\Desktop\Face_Recognization System\College_image\Traindata.jpeg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,command=self.train_data,image=self.photoimg8,cursor="hand2")
        b1.place(x=200,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="Darkblue",fg="white")
        b1_1.place(x=200,y=600,width=220,height=40)

        #Photos face Button 6
        img9=Image.open(r"C:\Users\PC\Desktop\Face_Recognization System\College_image\Photos.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_image)
        b1.place(x=500,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="Darkblue",fg="white",command=self.open_image)
        b1_1.place(x=500,y=600,width=220,height=40)

        # Developer Button 7
        img10=Image.open(r"C:\Users\PC\Desktop\Face_Recognization System\College_image\developer.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="Darkblue",fg="white")
        b1_1.place(x=800,y=600,width=220,height=40)

        #Exit Button 8
        img11=Image.open(r"C:\Users\PC\Desktop\Face_Recognization System\College_image\exit.jpeg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="Darkblue",fg="white")
        b1_1.place(x=1100,y=600,width=220,height=40)
    #========================for opening captured images========================
    def open_image(self):
         os.startfile("data")


    #=====EXIT ======
    def iExit(self):
           self.iExit=tsmg.askyesno("Face Recognition","Are you sure exit this project")
           if self.iExit > 0:
                  self.root.destroy()
           else:
                  return
          #================================Functions Details==============
    def student_details(self):
            self.new_window=Toplevel(self.root)
            self.app=student(self.new_window)
    def train_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Train(self.new_window)
     
    def face_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Face_Recognition(self.new_window)

    def attendence_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Attendence(self.new_window)

    def developer_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Developer(self.new_window)

    def help_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Help(self.new_window)                 

     

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognization_system(root)
    root.mainloop()


