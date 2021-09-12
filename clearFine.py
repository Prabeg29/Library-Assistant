import tkinter as tk

HEIGHT=550
WIDTH=1300

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
