from tkinter import *
import time

def breaking(minits = 0,seconds = 0):
    canves.itemconfig(output_state,text = 'Break')
    seconds = seconds
    minits = minits
    if minits!=5:
        seconds+=1
        if seconds>=60:
            seconds = 0
            minits+=1
        canves.itemconfig(output_time,text=f'{str(minits).zfill(2)}:{str(seconds).zfill(2)}')
        window.after(2,breaking,minits,seconds)

def working(minits = 0,seconds = 0):
    minits = minits
    seconds = seconds
    if minits>=30:
        breaking()
    else:
        seconds+=1
        if seconds>=60:
            minits+=1
            seconds = 0
        canves.itemconfig(output_time,text=f'{str(minits).zfill(2)}:{str(seconds).zfill(2)}')
        window.after(2,working,minits,seconds)

def start():
    working()
    
def reset():
    start()
    print('reset')

is_timer_on = True
window = Tk()
seconds = 0
minits = 0
window.config(background='white')
image = PhotoImage(file="tomato.png")
image_width = image.width()
image_hight = image.height()
window.geometry(f"{image_width+200}x{image_hight+150}")
canves = Canvas(width=image_width+200,height=image_hight+150,bg='white',highlightthickness=0)
canves.create_image(200,180,image=image)
canves.pack()
output_time = canves.create_text(200,195,text='12:12',font=("timesnewroman",40,"bold"))
output_state = canves.create_text(200,35,text='work',font=("timesnewroman",40,"bold"),fill="black")
start_button = Button(command=start,text='Start',highlightthickness=0)
reset_button = Button(command=reset,text='Reset',highlightthickness= 0)
start_window = canves.create_window(80,320,window=start_button)
reset_window = canves.create_window(320,320,window=reset_button)


window.mainloop()