import tkinter as tk
from camera import *
from database import *
import datetime

HEIGHT=550
WIDTH=1300

def addButtonPressed(v):
        shelf = v.get()
       # print(shelf)
       # logic to on idicators
       # logic to confirm book removed

def scanButtonPressed(profile, v):
        date = str(datetime.datetime.now().date())
        bookName = ""
        shelf = v.get()
        if shelf == 1:
                bookName = "Remote Sensing"
        elif shelf == 2:
                bookname = "Engineering Physics"
        elif shelf == 3:
                bookname = "OOP"
        QRcode = QRscan()
        id = profilel[0]
        # update database records
        insertRecords(id, QRcode, bookName, date)
        
def issue_book(profile):        
	top=tk.Toplevel()
	top.title("ISSUE BOOK")  #title for page
	#canvas creation
	canvas1=tk.Canvas(top,height=HEIGHT,width=WIDTH)
	canvas1.pack()
	#background image for issue window
	ba_image=tk.PhotoImage(file='l.png')
	ba_label=tk.Label(top,image=ba_image)
	ba_label.place(relwidth=1,relheight=1)

	#frame1 
	frame_issue1=tk.Frame(top)
	frame_issue1.place(relx=0.5,rely=0,relwidth=0.29,relheight=0.20,anchor='n')
	#creatinglogo 
	logo_image=tk.PhotoImage(file='logo.png')  
	logo_label=tk.Label(frame_issue1,image=logo_image)
	logo_label.place(relwidth=1,relheight=1)

	

	#labels creation
	label3=tk.Label(top,text="ISSUE BOOK",fg='blue' ,bd=3, padx=2,pady=1,font="verdana 30 bold")
	label3.place(relx=0.3,rely=0.22,relwidth=0.4,relheight=0.1)

	booklist=tk.Label(top,text="BOOK LIST",fg='blue' ,bd=3, padx=2,pady=1,font="verdana 30 bold")
	booklist.place(relx=0.3,rely=0.22,relwidth=0.4,relheight=0.1)
	tk.Label(top, text="""Choose a book:""",padx = 4).place(relx=0.38,rely=0.33,relwidth=0.25,relheight=0.08)
	frame1=tk.Frame(top,height=5,width=8)
	frame1.place(relx=0.4,rely=0.43)
	scrollbar1 =tk.Scrollbar(frame1)
	scrollbar1.pack( side ='right', fill ='y' )

	#radio buttons
	v = tk.IntVar()
	tk.Radiobutton(frame1,text="Remote sensing",padx = 4,variable=v,value=1).pack()
	tk.Radiobutton(frame1, text="Engineering Physics",padx = 4, variable=v,value=2).pack()
	tk.Radiobutton(frame1,text="OOP",padx = 4,variable=v,value=3).pack()

	#buttons
	addbook=tk.Button(top,text='ADD BOOK',fg='red',height=1,width=20,font="verdana 15 bold", command=lambda:addButtonPressed(v))
	addbook.pack()
	button2=tk.Button(top,text='Scan',fg='red',height=1,width=20,font="verdana 15 bold",command=lambda: scanButtonPressed(profile, v))
	button2.pack()
	button3=tk.Button(top,text='EXIT',command = top.destroy,fg='red',height=1,width=20,font="verdana 15 bold")
	button3.pack()
	#ENDING ISSUE WINDOW MAINLOOP
	top.mainloop()
