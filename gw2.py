# PvZ: GW22 Next Quest Reset v1.0
import time

base = 1773777600
increment = 165600

rn = time.time()

while base < rn:
    base += increment

arg = nsb_args.split()[0]
times = 1
if arg.isnumeric():
    arg = int(arg)
    if arg > 0:
        times = arg

if (times > 1):
    print("## Next {} quest resets:".format(times))
    for k in range(0, times):
        print("{}. <t:{}> - <t:{}:R>".format(k, base, base))
        base += increment
else:
    print("## Next quest reset:")
    print("<t:{}> - <t:{}:R>".format(base, base))