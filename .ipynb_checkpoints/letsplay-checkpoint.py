from tkinter import*
from PIL import Image,ImageTk

def two048():
    import two048tkinter
def ttt():
    import TkinterTicTacToe
def sudoku():
    import sudokutkinter
mnwin=Tk()

mnwin.geometry('1000x700')

c1=Canvas(mnwin,height=700,width=1000)
bglp=ImageTk.PhotoImage(Image.open('bg2.jpg'))
bgi=Image.open('two0.png')
bgi=bgi.resize((250,250),Image.ANTIALIAS)
bgs=Image.open('bg3.jpg')
bgs=bgs.resize((225,225),Image.ANTIALIAS)
bgt=Image.open('bg4.jpg')
bgt=bgt.resize((250,250),Image.ANTIALIAS)
bg2=ImageTk.PhotoImage(bgi)
bg3=ImageTk.PhotoImage(bgs)
bg4=ImageTk.PhotoImage(bgt)

c1.create_image(0,0,image=bglp,anchor='nw')
#label=Label(c1,image=bg)
#label.pack(fill=BOTH,expand=YES)

c1.pack()
l1=Label(c1,text="Let's Play!!!!",font=('Times New Roman',40))
#l1.place(x=380,y=5)
c1.create_text(520,35,text="Let's Play!!!!",font=('Eras Bold ITC',40),fill='darkblue')
b1=Button(c1,image=bg2,font=('Times New Roman',30),command=two048,height=224,width=221)
b1.place(x=100,y=230)
b2=Button(c1,image=bg4,font=('Times New Roman',30),command=ttt,height=224,width=221)
b2.place(x=680,y=230)
b3=Button(c1,image=bg3,font=('Times New Roman',30),command=sudoku,height=224,width=221)
b3.place(x=390,y=230)



#c1.create_image(20, 20, anchor=NW, image=img)
