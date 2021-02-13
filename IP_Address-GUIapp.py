from tkinter import *
import socket
win=Tk()
win.title("IP ADDRESS")
win.geometry("310x80+520+300") 
win.resizable(0,0)
win.configure(bg="white")
########################
var=StringVar()
lb=Label(win,textvariable=var,fg="#0067a3",font=("arial",15),bg="white",)
lb.pack(side="bottom")
#######################
entry=Entry(win,width=27,bg="#0067a3",fg="white")
entry.place(x=10,y=18)
#######################
def getip():
    url=entry.get()
    var.set(socket.gethostbyname(url))
bt=Button(win,text="Get IP",command=getip,bg="white",bd=2,fg="#0067a3",relief="groove",activeforeground="white",activebackground="#0067a3")
bt.place(x=235,y=15)
######################3
if __name__=='__main__':
    win.mainloop()


#coded by @chouaibcher7
