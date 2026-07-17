import time
from playsound import playsound
t=int(input("Enter the time in seconds: "))
while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
print("                                      Time's up! (x_x)")
playsound(r"C:\Users\marwa\.vscode\cli\alarm.wav")
