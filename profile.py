import datetime
import tkinter as tk
from issue import *
from clearFine import *
from return1 import *

HEIGHT=550
WIDTH=1300

def issueButtonPressed(profile):
        if profile[4] == None:
                issue_book(profile)
        else:
                std_details(profile)
                
def fineButtonPressed():
        clear_fine()

def returnButtonPressed():
        return_book()
        

def std_details(profile):
	root=tk.Toplevel()
	root.title("STUDENT DETAILS")
	canvas=tk.Canvas(root,height=HEIGHT,width=WIDTH,bg='PeachPuff')
	canvas.pack()
	
	#background image for 2nd window
	background_image=tk.PhotoImage(file='l.png')
	background_label=tk.Label(root,image=background_image)
	background_label.place(relwidth=1,relheight=1)

	#frame1
	fr1=tk.Frame(root)
	fr1.place(relx=0.5,rely=0,relwidth=0.29,relheight=0.20,anchor='n')

	#creatinglogo 
	b_image=tk.PhotoImage(file='logo.png')  
	b_label=tk.Label(fr1,image=b_image)
	b_label.place(relwidth=1,relheight=1)

	#frame2
	frame=tk.Frame(root)
	frame.place(relx=0.5,rely=0.23,relwidth=0.5,relheight=0.15,anchor='n')
	label3=tk.Label(frame,text="NAME:", font='courier 20 bold',anchor='n',fg='black',bd=2,padx=2,pady=2)
	label3.grid(row=0,column=0,sticky='W')
	label4=tk.Label(frame,text=str(profile[1]), font='courier 15 bold',anchor='n',fg='black',bd=2,padx=2,pady=2)
	label4.grid(row=0,column=1,sticky='W')
	label5=tk.Label(frame,text="ROLL NO:", font='courier 20 bold',anchor='n',fg='black',bd=2,padx=2,pady=2)
	label5.grid(row=1,column=0,sticky='W')
	label6=tk.Label(frame,text=str(profile[0]), font='courier 15 bold',anchor='n',fg='black',bd=2,padx=2,pady=2)
	label6.grid(row=1,column=1,sticky='W')
	label7=tk.Label(frame,text="FACULTY:", font='courier 20 bold',anchor='n',fg='black',bd=2,padx=2,pady=2)
	label7.grid(row=2,column=0,sticky='W')
	label8=tk.Label(frame,text="Electronics and Communication Engineering", font='courier 15 bold',anchor='n',fg='black',bd=2,padx=2,pady=2)
	label8.grid(row=2,column=1,sticky='W')

	#frame3
	book=tk.Frame(root,bg='grey')
	book.place(relx=0.5,rely=0.45,relwidth=0.5,relheight=0.34,anchor='n')
	l1=tk.Label(book,text="BOOK DETAILS",anchor="center",fg='blue',font='courier 20 bold',bd=2,padx=2,pady=2)
	l1.grid(row=0,columnspan=5)
	l2=tk.Label(book,text="SN",fg='blue',bd=4,padx=3,pady=3,height=2,width=3)
	l2.grid(row=1,column=2)
	l3=tk.Label(book,text="BOOK NAME",fg='blue',bd=4,padx=2,pady=2,height=2,width=20)
	l3.grid(row=1,column=3)
	l4=tk.Label(book,text="DUE DATE",fg='blue',bd=4,padx=2,pady=2,height=2,width=20)
	l4.grid(row=1,column=4)
	l5=tk.Label(book,text="ISSUE DATE",fg='blue',bd=4,padx=2,pady=2,height=2,width=20)
	l5.grid(row=1,column=5)
	l6=tk.Label(book,text="FINE",fg='blue',bd=4,padx=2,pady=2,height=2,width=20)
	l6.grid(row=1,column=6)
	l7=tk.Label(book,text="1",fg='blue',bd=4,padx=2,pady=2,height=2,width=3)
	l7.grid(row=2,column=2)
	l8=tk.Label(book,text="None",fg='blue',bd=4,padx=2,pady=2,height=2,width=20)
	l8.grid(row=2,column=3)
	l9=tk.Label(book,text="None",fg='blue',bd=4,padx=2,pady=2,height=2,width=20)
	l9.grid(row=2,column=4)
	l10=tk.Label(book,text="None",fg='blue',bd=4,padx=2,pady=2,height=2,width=20)
	l10.grid(row=2,column=5)
	l11=tk.Label(book,text='100',fg='blue',bd=4,padx=2,pady=2,height=2,width=20)
	l11.grid(row=2,column=6)

        
	#BUTTONS
	button1=tk.Button(root,text='ISSUE BOOK',fg='red',height=1,width=20,font="verdana 15 bold", command = lambda: issueButtonPressed(profile))
	button1.place(relx=0.24,rely=0.8,anchor='n')
	button2=tk.Button(root,text='RETURN BOOK' ,fg='red',height=1,width=20,font="verdana 15 bold", command = returnButtonPressed)
	button2.place(relx=0.75,rely=0.8,anchor='n')
	button3=tk.Button(root,text='EXIT',fg='red',height=1,width=20,font="verdana 15 bold", command = root.destroy)
	button3.place(relx=0.5,rely=0.9,anchor='n')
	button4=tk.Button(root,text='CLEAR FINE',fg='red',height=1,width=20,font="verdana 15 bold", command=fineButtonPressed)
	button4.place(relx=0.5,rely=0.8,anchor='n')
	#ENDING MAINLOOP
	root.mainloop()


