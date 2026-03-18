# Progress Bar v1.0
import datetime
import time
t = datetime.datetime.fromtimestamp(time.time())
d = t - datetime.datetime(t.year,1,1,0,0,0,0,None)
if (t.year%4==0): print("{} is {}% complete ({}% remaining)".format(t.year,round((100/31622400)*d.total_seconds(),2),100.0-round((100/31622400)*d.total_seconds(),2)))
else: print("{} is {}% complete ({}% remaining)".format(t.year,round((100/31536000)*d.total_seconds(),2),100.0-round((100/31622400)*d.total_seconds(),2)))