from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk
from secrets import *


root = Tk()
root.title("WeatherApp")
root.geometry("920x490+300+300")
root.configure(bg="#0c6ab2")
root.resizable(False, False)

def getWeather():
    city = textfield.get()    
    geolocator = Nominatim(user_agent="geoapisExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()  
      
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        
    timezone.config(text=result)
    long_lat.config(text=f"Lat: {round(location.latitude,4)}°N\nLon: {round(location.longitude,4)}°E")
    
    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    
    #weather
    response = requests.get("https://api.openweathermap.org/data/2.5/forecast?lat="+str(location.latitude)+
                "&lon="+str(location.longitude)+f"&units=metric&lang=de&exclude=hourly&APPID={API_KEY}")            
    
    if response.status_code == 404:
        print('City not found')
        
    try:
        json_data = response.json()
        temp = round(json_data['list'][0]['main']['temp'])
        humidity = json_data['list'][0]['main']['humidity']
        pressure = json_data['list'][0]['main']['pressure']
        wind = json_data['list'][0]['wind']['speed']
        description = json_data['list'][0]['weather'][0]['description']
        
        t.config(text=(temp,"°C"))
        h.config(text=(humidity,"%"))
        p.config(text=(pressure,"hPa"))
        w.config(text=(wind,"m/s"))
        d.config(text=(description))
        
        daily_weather_icon = []
        day_time_data = []
        show_time = []

        for index, day_data in enumerate(json_data['list']):
            icon = day_data['weather'][0]['icon']
            dayTime = day_data['dt']
            
            if index < 7:
                daily_weather_icon.append(icon)
                day_time_data.append(dayTime)
            else:
                break
            
        
        for i, times in enumerate(day_time_data):
            weather_time = datetime.utcfromtimestamp(times)
            show_times = weather_time.strftime("%I:%M %p")
            
            if i < 7:
                show_time.append(show_times)           
            
        
        
        #firstbox
        firstdayImage = daily_weather_icon[0]
        
        photo1 = ImageTk.PhotoImage(file=f"utils/icons/wetterIcons/{firstdayImage}@2x.png")
        firstImage.config(image=photo1)
        firstImage.image=photo1
        
        
        #secondbox
        seconddayImage = daily_weather_icon[1]
        
        img =(Image.open(f"utils/icons/wetterIcons/{seconddayImage}@2x.png"))
        resized = img.resize((50,50))
        photo2 = ImageTk.PhotoImage(resized)
        secondImage.config(image=photo2)
        secondImage.image=photo2
        
        
        # thirdbox
        thirddayImage = daily_weather_icon[2]
        
        img =(Image.open(f"utils/icons/wetterIcons/{thirddayImage}@2x.png"))
        resized = img.resize((50,50))
        photo3 = ImageTk.PhotoImage(resized)
        thirdImage.config(image=photo3)
        thirdImage.image=photo3
        
        
        # #fourthbox
        fourthdayImage = daily_weather_icon[3]
        
        img =(Image.open(f"utils/icons/wetterIcons/{fourthdayImage}@2x.png"))
        resized = img.resize((50,50))
        photo4 = ImageTk.PhotoImage(resized)
        fourthImage.config(image=photo4)
        fourthImage.image=photo4
        
        
        # #fifthbox
        fifthdayImage = daily_weather_icon[4]
        
        img =(Image.open(f"utils/icons/wetterIcons/{fifthdayImage}@2x.png"))
        resized = img.resize((50,50))
        photo5 = ImageTk.PhotoImage(resized)
        fifthImage.config(image=photo5)
        fifthImage.image=photo5
        
        
        # #sixthbox
        sixthdayImage = daily_weather_icon[5]
        
        img =(Image.open(f"utils/icons/wetterIcons/{sixthdayImage}@2x.png"))
        resized = img.resize((50,50))
        photo6 = ImageTk.PhotoImage(resized)
        sixthImage.config(image=photo6)
        sixthImage.image=photo6
        
        
        # #seventhbox
        seventhdayImage = daily_weather_icon[6]
        
        img =(Image.open(f"utils/icons/wetterIcons/{seventhdayImage}@2x.png"))
        resized = img.resize((50,50))
        photo7 = ImageTk.PhotoImage(resized)
        seventhImage.config(image=photo7)
        seventhImage.image=photo7
        
                
        #times
              
        time1.config(text= show_time[0])
        time2.config(text= show_time[1])
        time3.config(text= show_time[2])
        time4.config(text= show_time[3])
        time5.config(text= show_time[4])
        time6.config(text= show_time[5])
        time7.config(text= show_time[6])
        

    except (KeyError, TypeError):
        print('Unabble to print the data for that city')
    

#Icon 
image_icon=PhotoImage(file="utils/icons/appIcon.png")
root.iconphoto(False, image_icon)

Round_box = PhotoImage(file="utils/icons/rectangle.png")
Label(root, image=Round_box, bg="#0c6ab2").place(x=30, y=100)

#label
label1 = Label(root, text="Temperature", font=('Helvetica', 11), fg='#f9b8f6', bg="#000000")
label1.place(x=40, y=110)

label2 = Label(root, text="Humidity", font=('Helvetica', 11), fg='#f9b8f6', bg="#000000")
label2.place(x=40, y=140)

label3 = Label(root, text="Pressure", font=('Helvetica', 11), fg='#f9b8f6', bg="#000000")
label3.place(x=40, y=170)

label4 = Label(root, text="Wind Speed", font=('Helvetica', 11), fg='#f9b8f6', bg="#000000")
label4.place(x=40, y=200)

label5 = Label(root, text="Description", font=('Helvetica', 11), fg='#f9b8f6', bg="#000000")
label5.place(x=40, y=230)

#Search box
Search_image = PhotoImage(file= "utils/icons/search.png")
myimage=Label(image=Search_image, bg="#0c6ab2")
myimage.place(x=500, y=100)

weat_image = PhotoImage(file= "utils/icons/weat.png")
weatimage = Label(root, image=weat_image, bg="#0c6ab2")
weatimage.place(x=415, y=105)

textfield =tk.Entry(root, justify='center', width=22, font=('Helvetica', 18, 'bold'), 
                    bg="#fff", border=0, fg='#000')
textfield.place(x=520, y=116)
textfield.focus()

Search_icon=PhotoImage(file= "utils/icons/search_icon.png")
myimage_icon=Button(image=Search_icon, cursor='hand2', borderwidth=0, bg='#0c6ab2',
                    activebackground='#0c6ab2', command=getWeather)
myimage_icon.place(x=825,y=107)

#Bottombox
frame = Frame(root, width=920, height=180,  bg="#59c6cc")
frame.pack(side=BOTTOM)

#bottom boxes
firstBox = PhotoImage(file="utils/icons/box1.png")
secondBox = PhotoImage(file="utils/icons/miniBox.png")


Label(frame, image=firstBox, bg="#59c6cc").place(x=30, y=20)
Label(frame, image=secondBox, bg="#59c6cc").place(x=300, y=30)
Label(frame, image=secondBox, bg="#59c6cc").place(x=400, y=30)
Label(frame, image=secondBox, bg="#59c6cc").place(x=500, y=30)
Label(frame, image=secondBox, bg="#59c6cc").place(x=600, y=30)
Label(frame, image=secondBox, bg="#59c6cc").place(x=700, y=30)
Label(frame, image=secondBox, bg="#59c6cc").place(x=800, y=30)

#clock
clock = Label(root, font=('Helvetica', 30, "bold"), fg="#f9b8f6", bg="#0c6ab2")
clock.place(x=40, y=20)


#timezone
timezone = Label(root, font=('Helvetica', 15), fg="#f9b8f6", bg="#0c6ab2")
timezone.place(x=500, y=20)

long_lat = Label(root, font=('Helvetica', 10), fg="#f9b8f6", bg="#0c6ab2", justify='left')
long_lat.place(x=500, y=50)

# temp wind descriptio
t=Label(root, font=('Helvetica', 11), fg='#f9b8f6', bg="#000000")
t.place(x=160, y=110)
h=Label(root, font=('Helvetica', 11), fg='#f9b8f6', bg="#000000")
h.place(x=160, y=140)
p=Label(root, font=('Helvetica', 11), fg='#f9b8f6', bg="#000000")
p.place(x=160, y=170)
w=Label(root, font=('Helvetica', 11), fg='#f9b8f6', bg="#000000")
w.place(x=160, y=200)
d=Label(root, font=('Helvetica', 11), fg='#f9b8f6', bg="#000000")
d.place(x=160, y=230)


# first box
firstFrame=Frame(root, width=250, height=140, bg='#95f4bb')
firstFrame.place(x=32, y=332)

time1 = Label(firstFrame, font=('Helvetica', 20), fg='#000', bg='#95f4bb', justify='left')
time1.place(x=10, y=5)

firstImage = Label(firstFrame, bg='#95f4bb', width=70, height=50)
firstImage.place(x=3, y=60)

# second box
secondFrame=Frame(root, width=80, height=120, bg='#95f4bb')
secondFrame.place(x=302, y=342)

time2 = Label(secondFrame, font=('Helvetica', 10), fg='#000', bg='#95f4bb', justify='left')
time2.place(x=3, y=5)

secondImage = Label(secondFrame, bg='#95f4bb')
secondImage.place(x=2, y=25)


# third box
thirdFrame=Frame(root, width=80, height=120, bg='#95f4bb')
thirdFrame.place(x=402, y=342)

time3 = Label(thirdFrame, font=('Helvetica', 10), fg='#000', bg='#95f4bb', justify='left')
time3.place(x=3, y=5)

thirdImage = Label(thirdFrame, bg='#95f4bb')
thirdImage.place(x=2, y=25)

# fourth box
fourthFrame=Frame(root, width=80, height=120, bg='#95f4bb')
fourthFrame.place(x=502, y=342)

time4 = Label(fourthFrame, font=('Helvetica', 10), fg='#000', bg='#95f4bb', justify='left')
time4.place(x=3, y=5)

fourthImage = Label(fourthFrame, bg='#95f4bb')
fourthImage.place(x=2, y=25)

# fifth box
fifthFrame=Frame(root, width=80, height=120, bg='#95f4bb')
fifthFrame.place(x=602, y=342)

time5 = Label(fifthFrame, font=('Helvetica', 10), fg='#000', bg='#95f4bb', justify='left')
time5.place(x=3, y=5)

fifthImage = Label(fifthFrame, bg='#95f4bb')
fifthImage.place(x=2, y=25)

# sixth box
sixthFrame=Frame(root, width=80, height=120, bg='#95f4bb')
sixthFrame.place(x=702, y=342)

time6 = Label(sixthFrame, font=('Helvetica', 10), fg='#000', bg='#95f4bb', justify='left')
time6.place(x=3, y=5)

sixthImage = Label(sixthFrame, bg='#95f4bb')
sixthImage.place(x=2, y=25)

# seventh box
seventhFrame=Frame(root, width=80, height=120, bg='#95f4bb')
seventhFrame.place(x=802, y=342)

time7 = Label(seventhFrame, font=('Helvetica', 10), fg='#000', bg='#95f4bb', justify='left')
time7.place(x=3, y=5)

seventhImage = Label(seventhFrame, bg='#95f4bb')
seventhImage.place(x=2, y=25)



root.mainloop()