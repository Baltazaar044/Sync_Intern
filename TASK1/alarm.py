#importing libraries for alarm clock
from tkinter import *
import datetime
import time
import winsound
  
def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time=datetime.datetime.now()
        now=current_time.strftime("%H:%M:%S")
        date=current_time.strftime("%d/%m/%Y")
        print("The Set date is:",date)
        print(now)
        if now == set_alarm_timer:
            print("Time to wake up")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break
def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock=Tk()
clock.title("Alarm Clock")
clock.geometry("400x200")
addTime=Label(clock,text="Hour Min Second  ",font=20).place(x=110)
setAlarm=Label(clock,text="SET ALARM TIME ",fg="black",relief="solid",font=("Helevetica",9,"bold")).place(x=0, y=29)

#variables for alarm 
hour=StringVar()
min=StringVar()
sec=StringVar()


#Time required to alarm clock
hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=110,y=30)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=150,y=30)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 10).place(x=200,y=30)
#submit time
submit= Button(clock, text ="Set Alarm " ,fg="red",command=actual_time ).place(x=110,y=70)


#execution
clock.mainloop()