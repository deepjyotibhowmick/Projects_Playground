import time as t
import pytz


print(t.ctime(0)) # Showing time starting date (epoch time)
print(t.time()) # showing epoch time //second passed from Thu Jan  1 05:30:00 1970

print(f"Current date/time: {t.ctime(t.time())}")
sum=0
st= t.time()
st1= t.perf_counter()
for i in range(1000):
    sum +=i
en= t.time()
en1= t.perf_counter()
print(f"time differences: {en-st} // {en1-st1}")

print(f"Time taken by thred to complete the process: {t.thread_time()}")

print(f"Time formatting: {t.strftime('%Y-%m-%d %H:%M:%S',t.localtime())}")

print(t.strptime("30 Nov 00", "%d %b %y"))

# Define IST and GMT timezones
ist = pytz.timezone('Asia/Kolkata')
gmt = pytz.timezone('GMT')

# Current IST time
ist_time =t.gmtime()
print("Current IST Time:", ist_time)