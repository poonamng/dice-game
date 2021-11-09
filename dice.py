from tkinter import*
import random
root=Tk()
root.title("The Dice Game")
root.geometry("600x500")
l1=Label(root,font=("Ani",300,"bold"),text="",fg="blue")
def roll_Dice():
    dice_number=["\u2680","\u2681","\u2682","\u2683","\u2684","\u2685"]
    l1.configure(text=f'{random.choice(dice_number)}')
    l1.pack()
b1=Button(root,font=("Ani",55,"bold"),text="lets play Dice Rolling Game",command=roll_Dice,bg="light green")
b1.place(x=300,y=0)
b1.pack()
root.mainloop()  
