# PvZ: GW22 Next Town Hall Event v1.0
import datetime

def increment_month():
    global event_count
    event_count += 1
    if event_count > 11:
        event_count = 0
        
    global base_month
    global base_year
    base_month += 1
    if base_month == 13:
        base_year += 1
        base_month = 1
        
    global base_date
    base_date = datetime.datetime(base_year, base_month, 22)
    
# Monday = 0, Sunday = 6
def find_first_dow(year, month, dow):
    d = datetime.datetime(year, int(month), 7)
    offset = -((d.weekday() - dow) % 7)
    return d + datetime.timedelta(offset)

event_name = [
    "Tactical Team-Up",
    "To Heal or Not To Heal",
    "Rando's Rapid Revenge",
    "Lawnathon 1",
    "Lawnathon 2",
    "Legends of the Brawl",
    "To Heal or Not To Heal",
    "Rando's Rapid Revenge",
    "Lawnathon 1",
    "Lawnathon 2",
    "Legends of the Brawl",
    "Capture the Taco"
]

event_count = 0
base_year = 2025
base_month = 5
base_date = datetime.datetime(base_year, base_month, 22)

rn = datetime.datetime.now()

while base_date < rn:
    increment_month()

# 14:00:00 in seconds
bst_1500 = 50400

argslen = int(nsb_argslen)
arg = 1
if (argslen > 1):
    arg = nsb_args.split()[1]

times = 1
if arg.isnumeric():
    arg = int(arg)
    if arg > 0:
        times = arg

if (times > 1):
    print("## Next {} town hall events:".format(times))
    for k in range(0, times):
        dt_from = find_first_dow(base_year, base_month, 1) + datetime.timedelta(seconds=bst_1500)
        dt_to = dt_from + datetime.timedelta(days=14)
        print("{}. <t:{}> - <t:{}> ({})".format(k, int(dt_from.timestamp()), int(dt_to.timestamp()), event_name[event_count]))
        if dt_from.day == 1:
            dt_from += datetime.timedelta(days=7)
            dt_to += datetime.timedelta(days=7)
            print("  - or <t:{}> - <t:{}>".format(int(dt_from.timestamp()), int(dt_to.timestamp())))
        increment_month()
else:
    print("## Next town hall event:")
    dt_from = find_first_dow(base_year, base_month, 1) + datetime.timedelta(seconds=bst_1500)
    dt_to = dt_from + datetime.timedelta(days=14)
    print("<t:{}> - <t:{}> ({})".format(int(dt_from.timestamp()), int(dt_to.timestamp()), event_name[event_count]))
    if dt_from.day == 1:
        dt_from += datetime.timedelta(days=7)
        dt_to += datetime.timedelta(days=7)
        print("  - or <t:{}> - <t:{}>".format(int(dt_from.timestamp()), int(dt_to.timestamp())))