import datetime
import time
from tkinter import *
import tkinter as tk
from tkinter import font

import requests
from PIL import Image, ImageTk
root = Tk()

height = 400
width = 600

canvas = Canvas(root, height= height, width= width)
canvas.pack()

image = ImageTk.PhotoImage( Image.open('back.jpg'))
background_lable = Label(root, image=image)
background_lable.place(x=0,y=0, relwidth=1, relheight=1)

frame = Frame(root,bg='#00e9ff')
frame.place(relx=0.15, rely=0.1, relwidth=0.7, relheight=0.08)


def format_weaher(weather):

    try:
        name = weather['name']
        dec = weather['weather'][0]['description']
        temp = weather['main']['temp']
        min_temp = weather['main']['temp_min']
        max_temp = weather['main']['temp_max']
        return f'city: {name}\nweather: {dec}\ntemprature: {temp}°C\nmin temp: {min_temp}°C\nmaxt temp: {max_temp}°C'
    except:
        pass


def getweather(city):
    key = '2edd4666ddf158b39550c48336c535f5'
    url = r'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID' : key,'q': city,'units': 'Metric'}
    response = requests.get(url, params)
    weather = response.json()
    lable['text'] = format_weaher(weather)


b = Button(frame, text='see weather',font=('Courier',13), command= lambda: getweather(entry.get()))
b.place(relx=0.67, rely=0.05, relwidth=0.32, relheight=0.9)



# api.openweathermap.org/data/2.5/forecast/hourly?q={city name},{country code}

entry = Entry(frame, font=('Courier',13), bg='white')
entry.place(relx=0.01, rely=0.05, relwidth=0.65, relheight=0.9)

lframe = Frame(root,bg='#00e9ff')
lframe.place(relx=0.15, rely=0.25 , relwidth=0.7, relheight=0.6)
lable = Label(lframe,   font=('Courier',16))
lable.place(relx=0.01, rely=0.015, relwidth=0.98, relheight=0.97)
root.mainloop()