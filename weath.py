from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=f38679db9e8cf202e3099930b1a76e0d").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(data["main"]["temp"]-273.15))
    per_label1.config(text=data["main"]["pressure"])











win = Tk()
win.title("Weather Tech")
win.config(bg="light blue")
win.geometry("800x800")

name_label= Label(win,text="Weather TECH App",font=("Timee New Roman",40,"bold"))
name_label.place(x=55,y=70,height=70,width=650)

city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text="Weather TECH App",values=list_name,font=("Timee New Roman",20,"bold"),textvariable=city_name)
com.place(x=120,y=170,height=60,width=500)

w_label= Label(win,text="Weather Climate",font=("Timee New Roman",20,"bold"))
w_label.place(x=55,y=420,height=50,width=300)

w_label1= Label(win,text=".",font=("Timee New Roman",20,"bold"))
w_label1.place(x=410,y=420,height=50,width=300)


wb_label= Label(win,text="Weather Discription",font=("Timee New Roman",20,"bold"))
wb_label.place(x=55,y=500,height=50,width=300)

wb_label1= Label(win,text=".",font=("Timee New Roman",20,"bold"))
wb_label1.place(x=410,y=500,height=50,width=300)

temp_label= Label(win,text="Temperature",font=("Timee New Roman",20,"bold"))
temp_label.place(x=55,y=580,height=50,width=300)

temp_label1= Label(win,text=".",font=("Timee New Roman",20,"bold"))
temp_label1.place(x=410,y=580,height=50,width=300)

per_label= Label(win,text="Pressure",font=("Timee New Roman",20,"bold"))
per_label.place(x=55,y=660,height=50,width=300)

per_label1= Label(win,text=".",font=("Timee New Roman",20,"bold"))
per_label1.place(x=410,y=660,height=50,width=300)


done_button = Button(win,text="DONE",font=("Timee New Roman",20,"bold"),command=data_get)
done_button.place(y= 289,height=70,width=120,x=320)



win.mainloop()