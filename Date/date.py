
import datetime

# Current Date - Time

cdt = datetime.datetime.now()

print(cdt)

# Current Month Full Name

print(cdt.strftime("%B")) # Short Name use "%b" (ex : jun)

# Current Day - Full Name 

print(cdt.strftime("%A"))  # Short Name use "%a" (ex : mon)

# Creating Date Objects

y = datetime.datetime(2002,2,19)

print(y)