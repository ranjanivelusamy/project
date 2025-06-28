# ALARM CLOCK
import time():
def set_alarm():
    alarm_time = input("enter alarm time in HH:MM:SS format:")
    print(f"alarm is set for{alarm_time}....")
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("\n wake up!!!")
            for i in range(5):
                print("ALARM")
                time.sleep(1)
            break
        time.sleep(1)

set_alarm()        
