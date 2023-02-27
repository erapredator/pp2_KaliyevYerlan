#Write a Python program to print yesterday, today, tomorrow.
import datetime

current_date = datetime.datetime.now()
new_date = current_date - datetime.timedelta(days=1)
new_dat = current_date + datetime.timedelta(days=1)

print("Today is " + current_date.strftime("%A"))
print("Yesterday was " + new_date.strftime("%A"))
print("Tomorrow is " + new_dat.strftime("%A"))

