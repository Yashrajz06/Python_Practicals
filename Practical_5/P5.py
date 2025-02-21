# Write a program to print 24 hours of day
# with suitable suffixes like
# AM, PM, Noon and Midnight.

for i in range(24):
    if i == 0:
        print(i, "Midnight")
    elif i < 12:
        print(i, "AM")
    elif i == 12:
        print(i, "Noon")
    elif i > 12:
        print(i - 12, "PM")
