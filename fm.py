# TF2 Next Full Moon v1.0
import time

base = 1734217200
increment = 2551392
pm = 86400

rn = time.time()

base += pm
while base < rn:
    base += increment

argslen = int(nsb_argslen)
arg = "1"
if (argslen > 1):
    arg = nsb_args.split()[1]
    
times = 1
if arg.isnumeric():
    arg = int(arg)
    if arg > 0:
        times = arg

if (times > 1):
    print("## Next {} full moons:".format(times))
    for k in range(0, times):
        print("{}. <t:{}> - <t:{}>".format(k, base - pm - pm, base))
        base += increment
else:
    print("## Next full moon:")
    print("<t:{}> - <t:{}>".format(base - pm - pm, base))