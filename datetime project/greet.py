import datetime
greeting = " "
current_time = datetime.datetime.now()
print(current_time) # prints the current time 
print("Enter the current time in 24-hrs formate :- ")
hrs = int(input("Enter the hour:- "))
min = int(input("Enter the minutes:- "))
sec = int(input("Enter the seconds:- "))

if 0 <= hrs <12:
    greeting = "Good Morning"

elif 12<= hrs < 16 :
    greeting = "Good Afternoon"

elif 16<= hrs < 21 :
    greeting = "Good Evening"

elif 21<= hrs < 24 :
    greeting = "Good Night"

else:
    greeting -= "its invalid time !!"

print(greeting + " Sir/Mam")


