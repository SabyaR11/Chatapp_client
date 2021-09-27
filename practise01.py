import tkinter as tk
from tkinter import Button, font
from tkinter.constants import CENTER, END, NORMAL
from tkinter.font import BOLD, names
from typing import Text

loginPage = tk.Tk() 
loginPage.title('Login Window')             
loginPage.resizable(0,0)              #resizable(0,0) restrict the size of the window
loginPage.configure(bg="yellow",)     #set the background colour of the window
loginPage.geometry("300x400")         #geometry used for giving overall dimension of the page


#frame is the main area within which the wodgets are placed
#this is the main frame/parent frame in the program
frame = tk.Frame(height=300,width=400, bg="yellow")
label = tk.Label(
    master=frame, 
    height=3, 
    text = "My First Chatting App", 
    font=('TIMES NEW ROMAN', 18 ,BOLD), 
    fg="#090de6", 
    bg="yellow"
    )
label.pack()


#using second frame to create a gap between the two input bars
#calling the parent frame in frame1 (frame within frame) to set the second frame within the first frame
farame1 = tk.Frame(frame, height=10, width=10)
label1 = tk.Label(master=farame1, width=31, height = 1, bg="yellow")
label1.pack()

#using this frame for spacing between widgets
farame2 = tk.Frame(frame, height=10, width=21)
label2 = tk.Label(master=farame2, width=31, height = 1, bg="yellow")
label2.pack()

#using this frame for spacing between widgets
farame3 = tk.Frame(frame, height=20, width=21)
label3 = tk.Label(master=farame3, width=31, height = 1, bg="yellow")
label3.pack()

#definig function for click action in entry widget for delecting 
#the default text in the entry area when mouse is clicked in it
def click(event):
    username.configure(state=NORMAL)
    username.delete(0,END)
    username.unbind('<Button-1>',click)

def click1(event):
    passward.configure(state=NORMAL, show="*")
    passward.delete(0,END)
    passward.unbind('<Button-1>',click1)
    

def enter1():                          #function to get output entered in the entry part
    name = username.get()              #getting the username given by user
    print(name)

    id = passward.get()                #getting the password entered by the user
    print(id)



#label used for displaying any text message
greeting = tk.Label(
    master=frame,
    text="USER LOGIN",
    font=('TIMES NEW ROMAN', 12 ,BOLD),
    foreground="black",                #set tect colour
    background="#edf261",              #set background colour
    width=21,                          #set width area of the text
    height=3)                          #set height area of the text"""

#entry widget for taking input from user
username = tk.Entry(                   #taking the username
    master=frame,
    bg="#ecede4",
    bd=5,
    width=20
)

passward = tk.Entry(                   #taking password as input
    master=frame,
    bg="#ecede4",
    bd=5
)


#button creates a clickable button
button = tk.Button(
    master=frame,
    activebackground="grey",
    activeforeground="white",
    padx=2,                           #padding around the button along x axis
    pady=2,                           #padding around the button along y axis
    text ="login",                    #text on the button
    font=('TIMES NEW ROMAN', 12, BOLD),
    width=10,                         #button width
    height=1,                         #button height
    fg="#3a3d38",                     #button text colour
    bg="#87ed39",                     #button background/button colour
    command=enter1                    #commadnd used for action while buttton is clicked
)

#.pack() is used to add the widgwts to the window for implementation
frame.pack()
greeting.pack()
farame3.pack()
username.insert(5, " Username")
click=username.bind('<Button-1>',click)
username.pack()
farame1.pack()
passward.insert(5, " Password")
click1=passward.bind('<Button-1>',click1)
passward.pack()
farame2.pack()
button.pack()

#.mainloop() reun the tkinter event loop
loginPage.mainloop()