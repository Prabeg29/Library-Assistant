import tkinter as tk
from camera import *

HEIGHT=550
WIDTH=1300


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

label3=tk.Label(root,text=" WELCOME TO THE COLLEGE LIBRARY ",fg='blue' ,bd=5, padx=5,pady=5,font="verdana 30 bold")
label3.place(relx=0.1,rely=0.3,relwidth=0.85,relheight=0.1)

label4=tk.Label(root,text=" Please look at the camera ",anchor='n',fg='red',font="verdana 20 bold",padx=5,pady=2)
label4.pack()

button=tk.Button(root,text='camera', command=faceRecog)
button.pack()

root.mainloop()
