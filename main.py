import tkinter as tk
import cv2
import numpy as np
import database as db

HEIGHT=550
WIDTH=1300

global button2

def camera():
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    cap = cv2.VideoCapture(0)
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    recognizer.read("recognizer/training.yml")
    font = cv2.FONT_HERSHEY_PLAIN
    counter = 0
    id = 0
    profile = []
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret:
            counter += 1 

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect face
        face = faceCascade.detectMultiScale(
            gray,
            scaleFactor = 1.1,
            minNeighbors = 5
            )

        # Draw rectangle around faces
        for x,y,w,h in face:
            id, conf= recognizer.predict(gray[y:y+h, x:x+w])
            profile = db.getProfile(id)
            if profile != None and conf < 85:
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, str(profile[2]),(x, y+h+30), font, 1, (0, 255, 0), 2)
            break
        
        # Display the resulting frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q') or counter == 50:
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    if profile != None and id != None:
        std_details(profile)


# GUI
def issueButtonPressed(profile):
    if profile[4] == None:
        issue_book(profile)

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
	v = tk.IntVar()
	tk.Radiobutton(frame1,text="Engineering Mathematics",padx = 4,variable=v,value=1).pack()
	tk.Radiobutton(frame1, text="Engineering Physics",padx = 4, variable=v,value=2).pack()
        
	#buttons
        #button2=tk.Button(top,text='Scan',command=return_book,fg='red',height=1,width=20,font="verdana 15 bold")
        #button2.pack()
	addbook=tk.Button(top,text='ADD BOOK',fg='red',height=1,width=20,font="verdana 15 bold")
	addbook.pack()
	button2=tk.Button(top,text='Scan',command=QRdetect,fg='red',height=1,width=20,font="verdana 15 bold")
	button2.pack()
	button2=tk.Button(top,text='RETURN BOOK',command=return_book,fg='red',height=1,width=20,font="verdana 15 bold")
	button2.pack()
	button3=tk.Button(top,text='EXIT',command = top.destroy,fg='red',height=1,width=20,font="verdana 15 bold")
	button3.pack()
	#ENDING ISSUE WINDOW MAINLOOP
	top.mainloop()
	
def return_book():
	top=tk.Toplevel()
	top.title("RETURN BOOK")
	#canvas creation for return page
	canvas=tk.Canvas(top,height=HEIGHT,width=WIDTH)
	canvas.pack()
	#background image for return page
	ba_image=tk.PhotoImage(file='l.png')
	ba_label=tk.Label(top,image=ba_image)
	ba_label.place(relwidth=1,relheight=1)

	#frame1 
	frame_return1=tk.Frame(top)
	frame_return1.place(relx=0.5,rely=0,relwidth=0.29,relheight=0.20,anchor='n')
	#creatinglogo 
	logo_image=tk.PhotoImage(file='logo.png')  
	logo_label=tk.Label(frame_return1,image=logo_image)
	logo_label.place(relwidth=1,relheight=1)

	#labels creation
	#label3=tk.Label(top,text="RETURN BOOK",fg='blue' ,bd=5, padx=2,pady=1,font="verdana 30 bold")
	#label3.place(relx=0.3,rely=0.22,relwidth=0.4,relheight=0.1)

	#SCANNING
	scan=tk.Button(top,text='SCAN BOOK',fg='brown',height=1,width=4,font="verdana 30 bold")
	scan.place(relx=0.29,rely=0.35,relwidth=0.42,relheight=0.1)
	#NOTICE
	notice=tk.Label(top,text='Please scan QR CODE of book and place book on shelf',bd=3,padx=2,pady=1,font="calibri 30 bold")
	notice.place(relx=0.21,rely=0.49,relwidth=0.7,relheight=0.1)

	#BUTTONS
	button2=tk.Button(top,text='ISSUE BOOK',command=issue_book,fg='red',height=1,width=20,font="verdana 15 bold")
	button2.pack()
	button3=tk.Button(top,text='EXIT',command = top.destroy,fg='red',height=1,width=20,font="verdana 15 bold")
	button3.pack()
	
	#ENDING RETURN WINDOW MAINLOOP
	top.mainloop()

def clear_fine():
	top=tk.Toplevel()
	top.title("CLEAR FINE")  #title for page
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
	label3=tk.Label(top,text="PLEASE ENTER THE CODE PROVIDED TO CLEAR THE FINE",fg='blue' ,bd=3, padx=2,pady=1,font="verdana 30 bold")
	label3.place(relx=0,rely=0.22,relwidth=1,relheight=0.1)
	#FOR ENTERING CODE
	E1 = tk.Entry(top, bd =3)
	E1.place(relx=0.3,rely=0.423,relwidth=0.4,relheight=0.1)
	L1=tk.Button(top,text="CONFIRM",fg='brown',height=1,width=20,font="verdana 15 bold")
	L1.place(relx=0.4,rely=0.5)

	#ENDING RETURN WINDOW MAINLOOP
	top.mainloop()

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
	l8=tk.Label(book,text=str(profile[4]),fg='blue',bd=4,padx=2,pady=2,height=2,width=20)
	l8.grid(row=2,column=3)
	l9=tk.Label(book,text=str(profile[5]),fg='blue',bd=4,padx=2,pady=2,height=2,width=20)
	l9.grid(row=2,column=4)
	l10=tk.Label(book,text=str(profile[6]),fg='blue',bd=4,padx=2,pady=2,height=2,width=20)
	l10.grid(row=2,column=5)
	l11=tk.Label(book,text=str(profile[7]),fg='blue',bd=4,padx=2,pady=2,height=2,width=20)
	l11.grid(row=2,column=6)

        
	#BUTTONS
	button1=tk.Button(root,text='ISSUE BOOK',fg='red',height=1,width=20,font="verdana 15 bold", command = lambda: issueButtonPressed(profile))
	button1.place(relx=0.24,rely=0.8,anchor='n')
	button2=tk.Button(root,text='RETURN BOOK',command = return_book, fg='red',height=1,width=20,font="verdana 15 bold")
	button2.place(relx=0.75,rely=0.8,anchor='n')
	button3=tk.Button(root,text='EXIT',command = root.destroy,fg='red',height=1,width=20,font="verdana 15 bold")
	button3.place(relx=0.5,rely=0.9,anchor='n')
	button4=tk.Button(root,text='CLEAR FINE',command=clear_fine,fg='red',height=1,width=20,font="verdana 15 bold")
	button4.place(relx=0.5,rely=0.8,anchor='n')
	#ENDING MAINLOOP
	root.mainloop()

#MAIN WINDOW
root=tk.Tk()
root.title("WELCOME")
canvas=tk.Canvas(root,height=HEIGHT,width=WIDTH,bg='PeachPuff')
canvas.pack()
#For background image
background_image=tk.PhotoImage(file='l.png')
background_label=tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)

#frame1
fr1=tk.Frame(root)
fr1.place(relx=0.5,rely=0,relwidth=0.29,relheight=0.20,anchor='n')
#FOR LOGO'SAGARMATHA ENG. COLLEGE'
b_image=tk.PhotoImage(file='logo.png')  
b_label=tk.Label(fr1,image=b_image)
b_label.place(relwidth=1,relheight=1)

label3=tk.Label(root,text="	WELCOME TO THE COLLEGE LIBRARY  ",fg='blue' ,bd=5, padx=5,pady=5,font="verdana 30 bold")
label3.place(relx=0.1,rely=0.3,relwidth=0.85,relheight=0.1)

label4=tk.Label(root,text=" Please look at the camera ",anchor='n',fg='red',font="verdana 20 bold",padx=5,pady=2)
label4.pack()

button=tk.Button(root,text='camera', command = camera)
button.pack()

root.mainloop()
