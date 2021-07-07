from tkinter import *
from speedtest import Speedtest

def update_text():
    speed_test = Speedtest()
    download = speed_test.download()
    upload = speed_test.upload()
    download_speed = round(download / (1025*1025))
    upload_speed = round(upload / (1025*1025))
    down_label.config(text= "Download Speed - " + str(download_speed) + "Mbps")
    up_label.config(text= "Upload Speed - " + str(upload_speed) + "Mbps")


root = Tk()
root.title("Internet Speed Tracker")
root.geometry('300x300')
button = Button(root, text="Get Speed", width=30, command=update_text)
button.pack()
down_label = Label(root, text="")
down_label.pack()
up_label = Label(root, text="")
up_label.pack()

root.mainloop()