import tkinter as tk

HEIGHT=550
WIDTH=1300

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
	button2=tk.Button(top,text='ISSUE BOOK',fg='red',height=1,width=20,font="verdana 15 bold")
	button2.pack()
	button3=tk.Button(top,text='EXIT',command = top.destroy,fg='red',height=1,width=20,font="verdana 15 bold")
	button3.pack()
	
	#ENDING RETURN WINDOW MAINLOOP
	top.mainloop()


