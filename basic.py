import re 
text = "Anonymous"
data = re.compile("[a-zA-Z]+")
dt = data.findall(text)
print(dt)
print("----------------------------------------------------------------------------")
import _thread
import time

def a(msg):
    count = 0
    while count < 5:
        count +=1
        time.sleep(1)
        print(msg)
def b(msg):
    count = 0
    while count < 5:
        count +=1
        time.sleep(1)
        print(msg)

try:
    _thread.start_new_thread(a,("Thread One",))
    _thread.start_new_thread(b,("Thread Two",))
except:
    print("error to start thread")

while 1:
    pass

