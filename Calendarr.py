import tkinter as tk
import csv
import datetime
import os.path
from tkinter import messagebox
from Calendar import Calendar
from CalendarView import CalendarView

root = tk.Tk()
root.title("Calendar")
#Tikinter Vars
username = tk.StringVar()
password = tk.StringVar()
name = tk.StringVar()
loggedInLabel = tk.StringVar()
task = tk.StringVar()
hours = tk.IntVar()
minutes = tk.IntVar()
#Functions
def setup():
	#Used to make the two textfiles if they don't already exist
	file_exists = os.path.isfile("users.txt")
	if file_exists:
		pass
	else:
		file = open("users.txt", "w+")
		file.close()
	file_exists = os.path.isfile("Tasks.txt")
	if file_exists:
		pass
	else:
		file = open("Tasks.txt", "w+")
		file.close()
def raiseFrame(frame):
	frame.tkraise()
def moveToReg():
	raiseFrame(regFrame)
def moveToLogin():
	raiseFrame(start)
def moveToBook():
	raiseFrame(AddTask)
	# Calendar
def moveToUser():
	raiseFrame(userFrame)
def register():
	entries = []
	with open ("users.txt",'a',newline="") as userFile:
		writer = csv.writer(userFile)
		writeList = [name.get(),username.get(),password.get()]
		writer.writerow(writeList)
		userFile.close()
	#Clear entry boxes
	username.set("")
	password.set("")
	raiseFrame(start)

def LogInTask(calendarViewFrame):
	#Format date
	date = str(datePickercalendar.day_selected)+"/"+str(datePickercalendar.month_selected)+"/"+str(datePickercalendar.year_selected)
	#Format time
	minutesString=str(minutes.get())
	if minutes.get()==0:
		minutesString = "00"
	time = str(hours.get())+":"+minutesString
	with open ("Tasks.txt",'a',newline="") as appFile:
		writer = csv.writer(appFile)
		writeList = [name.get(),task.get(),date,time]
		writer.writerow(writeList)
		appFile.close()
	messagebox.showinfo("Success!","Task logged In!")
	calendarViewFrame = tk.Frame(userFrame, borderwidth=5, bg="lightblue")
	calendarViewFrame.grid(row=2, column=1, columnspan=5)
	viewCalendar = CalendarView(calendarViewFrame, {name.get()})
	raiseFrame(userFrame)

def alarm():
	alarmH = hours.get()
	alarmM = minutes.get()
	while (1 == 1):
		if (alarmH == datetime.datetime.now().hour and
				alarmM == datetime.datetime.now().minute):
			print("Time to wake up")
			messagebox.showinfo("Reminder", 'This is a reminder of your task')
			break

def login():
	with open("users.txt",'r') as userFile:
		reader = csv.reader(userFile)
		for row in reader:
			#removes empty list from loop
			if len(row)>0:
				if username.get()==row[1] and password.get()==row[2]:
					print(row[0]+" has logged in!")
					#Set welcome message
					loggedInLabel.set("Welcome, "+row[0])
					# Calendar View
					global calendarViewFrame
					calendarViewFrame = tk.Frame(userFrame, borderwidth=5, bg="lightblue")
					calendarViewFrame.grid(row=2, column=1, columnspan=5)
					viewCalendar = CalendarView(calendarViewFrame, {row[0]})
					name.set(row[0])
					raiseFrame(userFrame)

def logOut():
	#Clear Entry boxes
	name.set("")
	username.set("")
	password.set("")
	raiseFrame(start)
#Call setup
setup()
#Define Frame
start = tk.Frame(root)
regFrame = tk.Frame(root)
userFrame = tk.Frame(root)
AddTask = tk.Frame(root)
frameList=[start,regFrame,userFrame,AddTask]
#Configure all (main) Frames
for frame in frameList:
	frame.grid(row=0,column=0, sticky='news')
	frame.configure(bg='lightblue')


#Labels
tk.Label(start,text="CALENDAR",font=("Courier", 65),bg='lightblue').grid(row=0,column=1,columnspan=5)
tk.Label(start,text="Username: ",font=("Courier", 22),bg='lightblue').grid(row=2,column=1)
tk.Label(start,text="Password: ",font=("Courier", 22),bg='lightblue').grid(row=3,column=1)

tk.Label(regFrame,text="Register",font=("Courier", 44),bg='lightblue').grid(row=1,column=1,columnspan=5)
tk.Label(regFrame,text="Name: ",font=("Courier", 22),bg='lightblue').grid(row=2,column=1)
tk.Label(regFrame,text="Username: ",font=("Courier", 22),bg='lightblue').grid(row=3,column=1)
tk.Label(regFrame,text="Password: ",font=("Courier", 22),bg='lightblue').grid(row=4,column=1)

tk.Label(userFrame,textvariable = loggedInLabel,font=("Courier", 44),bg='lightblue',fg="blue").grid(row=1,column=1,columnspan=5)

tk.Label(AddTask,text="Add a task",font=("Courier", 44),bg='lightblue').grid(row=1,column=1,columnspan=5)
tk.Label(AddTask,text="Task: ",font=("Courier", 22),bg='lightblue').grid(row=5,column=1)
tk.Label(AddTask,text="Select a Time: ",font=("Courier", 22),bg='lightblue').grid(row=3,column=1)
#Entry Boxes
tk.Entry(start,textvariable=username,font=("Courier", 22),bg='lightblue').grid(row=2,column=2)
tk.Entry(start,textvariable=password,font=("Courier", 22),bg='lightblue').grid(row=3,column=2)

tk.Entry(regFrame,textvariable=name,font=("Courier", 22),bg='lightblue').grid(row=2,column=2)
tk.Entry(regFrame,textvariable=username,font=("Courier", 22),bg='lightblue').grid(row=3,column=2)
tk.Entry(regFrame,textvariable=password,font=("Courier", 22),bg='lightblue').grid(row=4,column=2)

tk.Entry(AddTask,textvariable=task,font=("Courier", 20),bg='lightblue').grid(row=5,column=2)
#Buttons
tk.Button(start,font=("Courier", 22),bg='cyan',text="Login",command=login).grid(row=4,column=2)
tk.Button(start,font=("Courier", 22),bg='cyan',text="Register",command=moveToReg).grid(row=4,column=1)

tk.Button(regFrame,font=("Courier", 22),bg='cyan',text="Register",command=register).grid(row=5,column=2)
tk.Button(regFrame,font=("Courier", 22),bg='cyan',text="Back",command=moveToLogin).grid(row=5,column=1)

tk.Button(userFrame,font=("Courier", 22),bg='cyan',text="Log Out",command=logOut).grid(row=3,column=1)
tk.Button(userFrame,font=("Courier", 22),bg='cyan',text="Add a task",command=moveToBook).grid(row=3,column=2)

tk.Button(AddTask,font=("Courier", 20),bg='cyan',text="Add Task",command=lambda :LogInTask(calendarViewFrame)).grid(row=7,column=2)
tk.Button(AddTask,font=("Courier", 20),bg='cyan',text="Back",command=moveToUser).grid(row=7,column=1)


#Time Selector
timeSelectFrame = tk.Frame(AddTask,borderwidth=5,bg="lightblue")
timeSelectFrame.grid(row=3,column=2)
tk.Spinbox(timeSelectFrame,from_=1, to=24,bg="lightblue",width=2,textvariable=hours).grid(row=1,column=1)
tk.Label(timeSelectFrame,text=":",bg="lightblue").grid(row=1,column=2)
tk.Spinbox(timeSelectFrame,width=2,textvariable=minutes,values=(0,15,30,45),bg="lightblue").grid(row=1,column=3)

calendarFrame = tk.Frame(AddTask, borderwidth=5, bg="lightblue")
calendarFrame.grid(row=2, column=2, columnspan=5)
datePickercalendar = Calendar(calendarFrame, {})
#Raise Initial Frame
raiseFrame(start)
root.mainloop()