import tkinter as tk
HEIGHT=480
WIDTH=800
top=tk.Tk()
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

#BOOK LISTS
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
tk.Radiobutton(frame1,text="Engineering Drawing",padx = 4,variable=v,value=3).pack()
tk.Radiobutton(frame1, text="Applied Mechanics",padx = 4, variable=v,value=4).pack()
tk.Radiobutton(frame1,text="Hydraulics",padx = 4,variable=v,value=5).pack()
tk.Radiobutton(frame1, text="RF and Microwave Engineering",padx = 4, variable=v,value=6).pack()
tk.Radiobutton(frame1,text="Remote Sensing",padx = 4,variable=v,value=7).pack()
tk.Radiobutton(frame1, text="Digital Signal Processing",padx = 4, variable=v,value=8).pack()
tk.Radiobutton(frame1,text="Filter Design",padx = 4,variable=v,value=9).pack()
#tk.Radiobutton(frame1, text="Microprocessor",padx = 4, variable=v,value=10).pack()
#tk.Radiobutton(top,text="Electrical Machine",padx = 4,variable=v,value=11).pack()
#tk.Radiobutton(top, text="Control System",padx = 4, variable=v,value=12).pack()
#tk.Radiobutton(top,text="Digital and Analog Communication System",padx = 4,variable=v,value=13).pack()
#tk.Radiobutton(top, text="Telecommunication",padx = 4, variable=v,value=14).pack()
#tk.Radiobutton(top,text="Wireless Communication ",padx = 4,variable=v,value=15).pack()
#tk.Radiobutton(top, text="Optical Fiber Comunication",padx = 4, variable=v,value=16).pack()


#SEARCH	
#E1 = tk.Entry(top, bd =3)
#E1.place(relx=0.2,rely=0.323,relwidth=0.4,relheight=0.09)
#L1=tk.Button(top,text="SEARCH BOOK",fg='brown',font="verdana 15 bold")
#L1.place(relx=0.61,rely=0.323,relwidth=0.4,relheight=0.09)




#buttons
addbook=tk.Button(top,text='ADD BOOK',fg='red',height=1,width=20,font="verdana 15 bold")
addbook.pack()
scan=tk.Button(top,text='SCAN BOOK',fg='red',height=1,width=20,font="verdana 15 bold")
scan.pack()
button2=tk.Button(top,text='RETURN BOOK',fg='red',height=1,width=20,font="verdana 15 bold")
button2.pack()
button3=tk.Button(top,text='EXIT',command = top.destroy,fg='red',height=1,width=20,font="verdana 15 bold")
button3.pack()
#ENDING ISSUE WINDOW MAINLOOP
top.mainloop()
	
