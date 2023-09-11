import win32api
import win32con
import time
user_lr = input("Left or Right click(l/r)")
user = int(input("How much clicks(0 for endless clicks: "))
user_pause = float(input("Pause between clicks?(0 for no pause): "))
user_pause = user_pause
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("Go")
count = int(0)
if user_lr == "l":
    def click():
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(user_pause)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
else:
    def click():
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
        time.sleep(user_pause)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)

if user == 0:
    while True:
        click()
else:
    while count < user:
        click()
        count += 1
