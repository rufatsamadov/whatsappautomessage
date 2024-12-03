import pyautogui as pg
import webbrowser as web
import time
import pandas as pd

data = pd.read_csv("numbers.csv")
data_dict = data.to_dict('list')
leads = data_dict['Number']
messages = data_dict['Message']
combo = zip(leads,messages)
first=True
sending_time=input("Enter the time that you want to send message (ex. 12:00:31)>>>")

def type():
    for lead,message in combo:
        time.sleep(3)
        web.open("https://web.whatsapp.com/send?phone="+lead+"&text="+message)
        if first:
            time.sleep(3)
            first=False
        width,height = pg.size()
        time.sleep(3)
        pg.click(width/2,height/2)
        time.sleep(1)
        pg.press('enter')
        time.sleep(3)
        pg.hotkey('ctrl', 'w')
while True:
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    if  current_time==sending_time :
        type()
    continue
    
    


