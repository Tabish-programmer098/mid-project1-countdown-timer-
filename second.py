import time
#to make countdown timer
def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60) #mode
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    print("stop")

countdown(70)