import datetime as dt
current_month = dt.date.today().month

import random as rnd

current_temperatue = int

if current_month == 1:
    current_temperatue = rnd.uniform(-6,7)
elif current_month == 2:
    current_temperatue = rnd.uniform(-5,11)
elif current_month == 3:
    current_temperatue = rnd.uniform(-2,12)
elif current_month == 4:
    current_temperatue = rnd.uniform(3,23)
elif current_month == 5:
    current_temperatue = rnd.uniform(8,27)
elif current_month == 6:
    current_temperatue = rnd.uniform(13,29)
elif current_month == 7:
    current_temperatue = rnd.uniform(16,32)
elif current_month == 8:
    current_temperatue = rnd.uniform(16,32)
elif current_month == 9:
    current_temperatue = rnd.uniform(11,25)
elif current_month == 10:
    current_temperatue = rnd.uniform(6,18)
elif current_month == 11:
    current_temperatue = rnd.uniform(1,12)
elif current_month == 12:
    current_temperatue = rnd.uniform(-3,8)

moisture_numb = rnd.uniform(0,12)
moisture_lvl = ""
if moisture_numb < 4:
    moisture_lvl = "low"
elif moisture_numb >= 4 and moisture_numb < 8:
    moisture_lvl = "medium"
elif moisture_numb >=8 and moisture_numb < 12:
    moisture_lvl = "high"

print (current_temperatue)