from pyowm.owm import OWM
import pyowm
import pyttsx3
import speech_recognition
import pyaudio
from datetime import date, datetime


engine = pyttsx3.init()


recognizer = speech_recognition.Recognizer()
try:
    with speech_recognition.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
        audio = recognizer.listen(mic)

        text_recognized = recognizer.recognize_google(audio)
        text_recognized = text_recognized.lower()

        print(text_recognized)
except speech_recognition.UnknownValueError:
    pass


def show_weather():
    owm = OWM('406dcaa6de9b1912bd3aa716474ec9f3')
    mgr = owm.weather_manager()


    city = ("germany")

    mgr = owm.weather_manager()
    location = mgr.weather_at_place(city)
    w = location.weather

    temps = w.temperature('celsius')
    humidity = w.humidity
    wind = w.wind()

    temps_str = str(temps)
    humidity_str = str(humidity)
    wind_str = str(wind)

    temps_str = temps_str.replace("_", " ")
    temps_str = temps_str.replace("temp", " ")
    temps_str = temps_str.replace("min", "minimum")
    temps_str = temps_str.replace("max", "maximum")
    temps_str = temps_str.replace(",", " celsius  ,")
    temps_str = temps_str.replace("'", "  ")
    temps_str = temps_str.replace("kf", " ")
    temps_str = temps_str.replace("None", " ")

    print(temps_str)

    humidity_str = humidity_str.replace("'", " ")
    humidity_str = humidity_str.replace("{", " ")
    humidity_str = humidity_str.replace("}", " ")
    wind_str = wind_str.replace("'", " ")
    wind_str = wind_str.replace("{", " ")
    wind_str = wind_str.replace("}", " ")
    engine.say(f'The Temperature today is: {temps_str}')
    engine.runAndWait()

def time_rn():


    now_time = datetime.now()

    current_time = now_time.strftime("%H:%M:%S")
    engine.say(f"It is currently {current_time}")
    print(current_time)
    engine.runAndWait()


def date_rn():

    now_date = datetime.now().date()
    print(now_date)
    engine.say(f"It is the {now_date} today")
    engine.runAndWait()


def day_of_year_rn():
    now_day_year = day_of_year = datetime.now().timetuple().tm_yday
    print(now_day_year)
    engine.say(f"it is the {now_day_year} day of this year ")
    engine.runAndWait()































if text_recognized == "weather":
    show_weather()
elif text_recognized ==  "time":
    time_rn()
elif text_recognized ==  "date":
    date_rn()
elif text_recognized == "day of year":
    day_of_year_rn()