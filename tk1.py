"""
import tkinter as tk

window_name = tk.Tk()

window_name.title('starting raghva')
button = tk.Button(window_name, text="Stop", command = window_name.destroy)
button.pack()

label = tk.Label(
    text="raghav agarwal!",
    foreground="white", #Set the text color to white
    background="black", # set the back ground color to black
    width = 30,
    height = 10
    )
label.pack()
button = tk.Button(
    text ="press the button",
    width=20,
    height=7,
    bg="blue",
    fg="yellow",
)


button.pack()
label = tk.Label(
    text="name"
)
entry = tk.Entry(fg="yellow" ,bg="blue", width=50)
label.pack()
entry.delete(0)
entry.pack()
name = entry.get()
print(name)

w = tk.Canvas(width=40,height=60)
w.pack()
canvas_height=20
canvas_width=200
y = int(canvas_height/2)
w.create_line(0,y,canvas_width,y)
window_name.mainloop()
"""
"""
from tkinter import *
master = Tk()
var1 = IntVar()
Checkbutton(master,text="male",variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master,text="female",variable=var2).grid(row=1, sticky=W)
Label(master, text="first name").grid(row=0)
Label(master, text="last name").grid(row=1)
e1=Entry(master)
e2=Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1,column=1)
"""
"""
from tkinter import *

master = Tk()
frame = Frame(master)
frame.pack()
bottomframe = Frame(master)
bottomframe.pack(side = BOTTOM)
redbutton = Button(frame, text="Red", fg ="white", bg="red")
redbutton.pack(side=LEFT)
greenbutton = Button(frame, text="green" , fg="white", bg="green")
greenbutton.pack(side=RIGHT)
bluebutton = Button(frame,text="blue", fg="white",bg="blue")
bluebutton.pack(side=LEFT)
blackbutton = Button(bottomframe, text="black", fg="white", bg="black")
blackbutton.pack(side=BOTTOM)
master.mainloop()
"""
"""
from tkinter import *
root = Tk()
root.title("tic tac toe")
frame=Frame(root)
frame.pack(side=LEFT)
frameleft=Frame(root)
frameleft.pack(side=RIGHT)
Button(frame,width=10,height=4, bg="grey").grid(row=0,column=0)
Button(frame,width=10,height=4, bg="grey").grid(row=0,column=1)
Button(frame,width=10,height=4, bg="grey").grid(row=0,column=2)
Button(frame,width=10,height=4, bg="grey").grid(row=1,column=0)
Button(frame,width=10,height=4, bg="grey").grid(row=1,column=1)
Button(frame,width=10,height=4, bg="grey").grid(row=1,column=2)
Button(frame,width=10,height=4, bg="grey").grid(row=2,column=0)
Button(frame,width=10,height=4, bg="grey").grid(row=2,column=1)
Button(frame,width=10,height=4, bg="grey").grid(row=2,column=2)
Label(frameleft,width=20,text="first player X").grid(row=0)
Label(frameleft,width=20,text="second player O").grid(row=1)
e1=Entry(frameleft)
e2=Entry(frameleft)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
root.mainloop()
"""
import tkinter.messagebox
from tkinter import *

root = Tk()
root.geometry("1350x750+0+0")
root.title("tic tac toe")
root.configure(background="cadet blue")

Tops = Frame(root,bg = "cadet blue", pady=2, width=1350, height=100, relief=RIDGE)
Tops.grid(row=0,column=0)

lblTitle= Label(Tops,font=('arial',50,'bold'), text="advanced tic tac toe Game", bd=21,bg='cadet blue', fg='cornsilk', justify=CENTER)
lblTitle.grid(row=0,column=0)

MainFrame = Frame(root,bg = "powder blue", pady=2, width=1350, height=600, relief=RIDGE)
MainFrame.grid(row=1,column=0)

LeftFrame= Frame(MainFrame, bd=10, width=750, height=500, pady=2, padx=10 ,bg='cadet blue', relief=RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame= Frame(MainFrame, bd=10, width=560, height=500, pady=2, padx=10 ,bg='cadet blue', relief=RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1= Frame(RightFrame, bd=10, width=560, height=200, pady=2, padx=10 ,bg='cadet blue', relief=RIDGE)
RightFrame1.grid(row=0, column=0)

RightFrame2= Frame(RightFrame, bd=10, width=560, height=200, pady=2, padx=10 ,bg='cadet blue', relief=RIDGE)
RightFrame2.grid(row=1, column=0)

playerx = IntVar()
playero = IntVar()

playerx.set(0)
playero.set(0)

buttons = StringVar()
click =True
def checker(buttons):
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"]  = "X"
        click = False
        scoreKeeper()
    elif buttons["text"] == " " and click == False:
        buttons["text"]  = "O"
        click = True
        scoreKeeper()


def scoreKeeper():
    if button1['text'] == "X" and button2['text'] == "X" and button3['text'] == "X":
        button1.configure(background="powder blue")
        button2.configure(background="powder blue")
        button3.configure(background="powder blue")
        n = float(playerx.get())
        score = (n+1)
        playerx.set(score)
        tkinter.messagebox.showinfo("Winner X", "You have just won a Game")

    elif button4['text'] == "X" and button5['text'] == "X" and button6['text'] == "X":
        button4.configure(background="powder blue")
        button5.configure(background="powder blue")
        button6.configure(background="powder blue")
        n = float(playerx.get())
        score = (n+1)
        playerx.set(score)
        tkinter.messagebox.showinfo("Winner X", "You have just won a Game")

    elif button7['text'] == "X" and button8['text'] == "X" and button9['text'] == "X":
        button7.configure(background="powder blue")
        button8.configure(background="powder blue")
        button9.configure(background="powder blue")
        n = float(playerx.get())
        score = (n+1)
        playerx.set(score)
        tkinter.messagebox.showinfo("Winner X", "You have just won a Game")

    elif button1['text'] == "O" and button2['text'] == "O" and button3['text'] == "O":
        button1.configure(background="powder blue")
        button2.configure(background="powder blue")
        button3.configure(background="powder blue")
        n = float(playero.get())
        score = (n + 1)
        playero.set(score)
        tkinter.messagebox.showinfo("Winner O", "You have just won a Game")

    elif button4['text'] == "O" and button5['text'] == "O" and button6['text'] == "O":
        button4.configure(background="powder blue")
        button5.configure(background="powder blue")
        button6.configure(background="powder blue")
        n = float(playero.get())
        score = (n + 1)
        playero.set(score)
        tkinter.messagebox.showinfo("Winner O", "You have just won a Game")

    elif button7['text'] == "O" and button8['text'] == "O" and button9['text'] == "O":
        button7.configure(background="powder blue")
        button8.configure(background="powder blue")
        button9.configure(background="powder blue")
        n = float(playero.get())
        score = (n + 1)
        playero.set(score)
        tkinter.messagebox.showinfo("Winner O", "You have just won a Game")

    elif button1['text'] == "X" and button4['text'] == "X" and button7['text'] == "X":
        button1.configure(background="powder blue")
        button4.configure(background="powder blue")
        button7.configure(background="powder blue")
        n = float(playerx.get())
        score = (n+1)
        playerx.set(score)
        tkinter.messagebox.showinfo("Winner X", "You have just won a Game")

    elif button2['text'] == "X" and button5['text'] == "X" and button8['text'] == "X":
        button2.configure(background="powder blue")
        button5.configure(background="powder blue")
        button8.configure(background="powder blue")
        n = float(playerx.get())
        score = (n+1)
        playerx.set(score)
        tkinter.messagebox.showinfo("Winner X", "You have just won a Game")

    elif button3['text'] == "X" and button6['text'] == "X" and button9['text'] == "X":
        button3.configure(background="powder blue")
        button6.configure(background="powder blue")
        button9.configure(background="powder blue")
        n = float(playerx.get())
        score = (n+1)
        playerx.set(score)
        tkinter.messagebox.showinfo("Winner X", "You have just won a Game")

    elif button1['text'] == "O" and button4['text'] == "O" and button7['text'] == "O":
        button1.configure(background="powder blue")
        button4.configure(background="powder blue")
        button7.configure(background="powder blue")
        n = float(playero.get())
        score = (n + 1)
        playero.set(score)
        tkinter.messagebox.showinfo("Winner O", "You have just won a Game")

    elif button2['text'] == "O" and button5['text'] == "O" and button8['text'] == "O":
        button2.configure(background="powder blue")
        button5.configure(background="powder blue")
        button8.configure(background="powder blue")
        n = float(playero.get())
        score = (n + 1)
        playero.set(score)
        tkinter.messagebox.showinfo("Winner O", "You have just won a Game")

    elif button3['text'] == "O" and button6['text'] == "O" and button9['text'] == "O":
        button3.configure(background="powder blue")
        button6.configure(background="powder blue")
        button9.configure(background="powder blue")
        n = float(playero.get())
        score = (n + 1)
        playero.set(score)
        tkinter.messagebox.showinfo("Winner O", "You have just won a Game")


    elif button1['text'] == "X" and button5['text'] == "X" and button9['text'] == "X":
        button1.configure(background="powder blue")
        button5.configure(background="powder blue")
        button9.configure(background="powder blue")
        n = float(playerx.get())
        score = (n + 1)
        playerx.set(score)
        tkinter.messagebox.showinfo("Winner X", "You have just won a Game")

    elif button3['text'] == "X" and button5['text'] == "X" and button7['text'] == "X":
        button3.configure(background="powder blue")
        button5.configure(background="powder blue")
        button7.configure(background="powder blue")
        n = float(playerx.get())
        score = (n + 1)
        playerx.set(score)
        tkinter.messagebox.showinfo("Winner X", "You have just won a Game")

    elif button1['text'] == "O" and button5['text'] == "O" and button9['text'] == "O":
        button1.configure(background="powder blue")
        button5.configure(background="powder blue")
        button9.configure(background="powder blue")
        n = float(playero.get())
        score = (n + 1)
        playero.set(score)
        tkinter.messagebox.showinfo("Winner O", "You have just won a Game")

    elif button3['text'] == "O" and button5['text'] == "O" and button7['text'] == "O":
        button3.configure(background="powder blue")
        button5.configure(background="powder blue")
        button7.configure(background="powder blue")
        n = float(playero.get())
        score = (n + 1)
        playero.set(score)
        tkinter.messagebox.showinfo("Winner O", "You have just won a Game")


def reset():
    global click
    click = True
    button1["text"] = " "
    button2["text"] = " "
    button3["text"] = " "
    button4["text"] = " "
    button5["text"] = " "
    button6["text"] = " "
    button7["text"] = " "
    button8["text"] = " "
    button9["text"] = " "

    button1.configure(background = "gainsboro")
    button2.configure(background="gainsboro")
    button3.configure(background="gainsboro")
    button4.configure(background="gainsboro")
    button5.configure(background="gainsboro")
    button6.configure(background="gainsboro")
    button7.configure(background="gainsboro")
    button8.configure(background="gainsboro")
    button9.configure(background="gainsboro")



def NewGame():
    playerx.set(0)
    playero.set(0)
    reset()



lblplayerx= Label(RightFrame1,font=('arial',40,'bold'), text="Player X :", padx=2, pady=2 ,bg='cadet blue')
lblplayerx.grid(row=0,column=0, sticky = W)
txtplayerx = Entry(RightFrame1 , font= ('arial', 40, 'bold'), bd=2, fg='black', textvariable =playerx, width=14,justify=LEFT ).grid(row=0, column=1)

lblplayero= Label(RightFrame1,font=('arial',40,'bold'), text="Player O :", padx=2, pady=2 ,bg='cadet blue')
lblplayero.grid(row=1,column=0, sticky = W)
txtplayero = Entry(RightFrame1 , font= ('arial', 40, 'bold'), bd=2, fg='black', textvariable =playero, width=14,justify=LEFT ).grid(row=1, column=1)

btnReset =Button(RightFrame2,text="Reset ", font= ('Times 26 bold'), height = 3 , width= 20, bg='gainsboro', command = lambda :reset())
btnReset.grid(row=1, column=0 )

btnNewGame =Button(RightFrame2 ,text="New Game ", font= ('Times 26 bold'), height = 3 , width= 20, bg='gainsboro', command = lambda :NewGame())
btnNewGame.grid(row=2, column=0 )


button1 =Button(LeftFrame,text=" ", font= ('Times 26 bold'), height = 3 , width= 8, bg='gainsboro', command = lambda :checker(button1))
button1.grid(row=1, column=0 , sticky= S+N+E+W)

button2 =Button(LeftFrame,text=" ", font= ('Times 26 bold'), height = 3 , width= 8, bg='gainsboro', command = lambda :checker(button2))
button2.grid(row=1, column=1 , sticky= S+N+E+W)

button3 =Button(LeftFrame,text=" ", font= ('Times 26 bold'), height = 3 , width= 8, bg='gainsboro', command = lambda :checker(button3))
button3.grid(row=1, column=3 , sticky= S+N+E+W)

button4 =Button(LeftFrame,text=" ", font= ('Times 26 bold'), height = 3 , width= 8, bg='gainsboro', command = lambda :checker(button4))
button4.grid(row=2, column=0 , sticky= S+N+E+W)

button5 =Button(LeftFrame,text=" ", font= ('Times 26 bold'), height = 3 , width= 8, bg='gainsboro', command = lambda :checker(button5))
button5.grid(row=2, column=1 , sticky= S+N+E+W)

button6 =Button(LeftFrame,text=" ", font= ('Times 26 bold'), height = 3 , width= 8, bg='gainsboro', command = lambda :checker(button6))
button6.grid(row=2, column=3 , sticky= S+N+E+W)

button7 =Button(LeftFrame,text=" ", font= ('Times 26 bold'), height = 3 , width= 8, bg='gainsboro', command = lambda :checker(button7))
button7.grid(row=3, column=0 , sticky= S+N+E+W)

button8 =Button(LeftFrame,text=" ", font= ('Times 26 bold'), height = 3 , width= 8, bg='gainsboro', command = lambda :checker(button8))
button8.grid(row=3, column=1 , sticky= S+N+E+W)

button9 =Button(LeftFrame,text=" ", font= ('Times 26 bold'), height = 3 , width= 8, bg='gainsboro', command = lambda :checker(button9))
button9.grid(row=3, column=3 , sticky= S+N+E+W)

root.mainloop()
