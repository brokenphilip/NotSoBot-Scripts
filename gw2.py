# PvZ: GW22 Next Daily Script v1.0
# Requires 'arg' ({arg:0})
import time

base = 1773777600
increment = 165600

rn = time.time()

while base < rn:
    base += increment

times = 1
if arg.isnumeric():
    arg = int(arg)
    if arg > 0:
        times = arg

if (times > 1):
    print("## Next {} star dailies:".format(times))
else:
    print("## Next star daily:")

for k in range(0, times):
    print("{}. <t:{}> - <t:{}:R>".format(k, base, base))
    base += increment