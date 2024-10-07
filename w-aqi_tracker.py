from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import random
import requests

def get_weather(api_key, city_name):
    try:
        # OpenWeatherMap API endpoint for current weather data
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            current_temp = data['main']['temp']
            current_temp = round(int(current_temp)-273.15,2)
            
            # OpenWeatherMap API endpoint for daily forecast
            url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}"
            forecast_response = requests.get(url)
            forecast_data = forecast_response.json()

            if forecast_response.status_code == 200:
                # Extracting highest and lowest temperatures from the forecast data
                daily_temps = [item['main']['temp'] for item in forecast_data['list']]
                max_temp = round(max(daily_temps)-273.15,2)
                min_temp = round(min(daily_temps)-273.15,2)

                return f"Current Temperature in {city_name}: {current_temp} °C\nHighest Temperature: {max_temp} °C\nLowest Temperature: {min_temp} °C"
            else:
                return "Error retrieving forecast information"

        else:
            return "Error retrieving weather information"

    except Exception as e:
        return f"An error occurred: {e}"

def get_weather_info():
    city_name = pwd.get()
    api_key = "dc5af83450ac8b7598990fbb96f32712"  # Replace with your OpenWeatherMap API key
    weather_info = get_weather(api_key, city_name)
    root1=Tk()
    root1.title('Weather Page')
    root1.geometry('804x504')
    img=PhotoImage(file=r"C:\Users\gonel\OneDrive\Desktop\Engineering Projects\Sem-1\nature1.png",master=root1)
    img_label=Label(root1,image=img)
    img_label.place(x=0,y=0)
    inp=Label(root1,text=weather_info,font='Arial 15')
    inp.place(relx=0.275,rely=0.4)
    root1.mainloop()
    # messagebox.showinfo("Weather Information", weather_info)


def check_city_exists(api_key, p):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": p, "appid": api_key}
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        return True
    except requests.exceptions.HTTPError as errh:
        # Handle HTTP errors (4xx client errors or 5xx server errors)
        print(f"HTTP Error: {errh}")
        return False
    except requests.exceptions.RequestException as err:
        # Handle non-HTTP errors (e.g., network issues)
        print(f"Error: {err}")
        return False

def on_check_city_exists():
    p=pwd.get()
    api_key = "dc5af83450ac8b7598990fbb96f32712"
    if check_city_exists(api_key,p):
        #messagebox.showinfo("City Exists", f"{p} exists.")
        pg2 = Tk()
        pg2.title("Second Page")
        pg2.geometry('804x504')
        img=PhotoImage(file=r"C:\Users\gonel\OneDrive\Desktop\Engineering Projects\Sem-1\nature1.png",master=pg2)
        img_label=Label(pg2,image=img)
        img_label.place(x=0,y=0)
        btn1 = Button(pg2, text = 'AQI information', bd = '3',font=('comic sans ms',9))
        btn1.place(relx=0.5, rely=0.47, anchor='center')
        btn2 = Button(pg2, text = 'Weather information', bd = '3',font=('comic sans ms',9),command=get_weather_info)
        btn2.place(relx=0.5, rely=0.57, anchor='center')
        pg2.mainloop()
    else:
        messagebox.showerror("City Not Found", f"{p} does not exist.")

def page1():
    pg1 = Tk()
    pg1.title("First Page")
    pg1.geometry('804x504')
    img=PhotoImage(file=r"C:\Users\gonel\OneDrive\Desktop\Engineering Projects\Sem-1\nature1.png",master=pg1)
    img_label=Label(pg1,image=img)
    img_label.place(x=0,y=0)
    inp=Label(pg1,text='Enter city name for weather info',font=('comic sans ms',12))
    inp.place(relx=0.35,rely=0.4)
    global pwd
    pwd= Entry(pg1,width=20,font=('comic sans ms',11))
    pwd.pack()
    pwd.place(relx=0.39,rely=0.47)
    btn1 = Button(pg1, text = 'Submit', bd = '3',font=('comic sans ms',9),command=on_check_city_exists)
    btn1.place(relx=0.5, rely=0.57, anchor='center')
    pg1.mainloop()

root = Tk()
root.title("Green Track")
root.geometry('804x504')
img=PhotoImage(file=r"C:\Users\gonel\OneDrive\Desktop\Engineering Projects\Sem-1\nature1.png",master=root)
img_label=Label(root,image=img)
img_label.place(x=0,y=0)
img1=PhotoImage(file=r"C:\Users\gonel\OneDrive\Desktop\Engineering Projects\Sem-1\logo.png",master=root)
img1_label=Label(root,image=img1)
img1_label.place(x=0.5,y=0.5)

L=['Since 1953, hurricanes and tropical storms have been given names.',
   'Before it blows against a thing, the wind is silent.',
   'Since 1880, the average global temperature has risen by 0.94°C (1.7°F).',
   'Wildfires can generate fire whirls, which are essentially fire tornadoes.',
   '1 billion tonnes of rainfall on the Earth every minute of the day.',
   "An average water molecule will spend 10 to 12 days in the Earth's atmosphere.",
   'On average, 100 lightning strikes the Earth each second.',
   'A raindrop can only impact you at a speed of 18 mph.',
   'Ordinary fog typically contains less than a gallon of water per cubic mile.',
   'The Mississippi river froze over its whole length in 1899 due to extreme weather.']

n=random.randint(0,len(L)-1)
    
inp1=Label(root,text='Fact for you:',font=('comic sans ms',15))
inp1.place(relx=0.17,rely=0.35)

#inp3=Label(root,text='Hello,',font=('comic sans ms',15))
inp4=Label(root,text='Welcome to Green Track',font=('comic sans ms',12))
#inp3.place(relx=0.03,rely=0.15)
inp4.place(relx=0.03,rely=0.22)

inp2=Label(root,text=L[n],font=('comic sans ms',11))
inp2.place(relx=0.17,rely=0.42)

btn1 = Button(root, text = 'Proceed to Application', bd = '3',font=('comic sans ms',9),command=page1)
btn1.place(relx=0.5, rely=0.53, anchor='center')

root.mainloop()