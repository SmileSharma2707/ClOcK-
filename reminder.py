import time
from plyer import notification

if __name__=="__main__":
    while True:
            notification.notify(
                title="Time to join next class",
                message="Its the time for next class to join now on Microsoft teams or classroom otherwise you will be not allowed in class",
                app_icon="D:\s1.ico.ico",
                timeout=20
            )
            time.sleep(60*60)
