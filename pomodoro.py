import tkinter as tk
import timer as t
class Pomodoro(tk.Tk):

	def __init__(self, *args, **kwargs):

		tk.Tk.__init__(self, *args, **kwargs)
		container = tk.Frame(self) # container for swapping from starting page to main page

		container.grid(row=0, column=0, sticky="nesw")

		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.focus_duration = tk.StringVar() # stores the input for focus duration
		self.break_duration = tk.StringVar() # stores the input for break duration

		# starting page is displayed first
		frame = StartPage(container, self)
		frame.grid(row=0, column=0, sticky="nsew")
		frame.tkraise()

class StartPage(tk.Frame):

	def __init__(self, container, controller):
		tk.Frame.__init__(self, container)

		# stores the input values for the focus/break durations and then swaps frames
		def onNext(): 
			controller.focus_duration.set(focus_text.get())
			controller.break_duration.set(break_text.get())
			nextFrame = MainPage(container, controller)
			nextFrame.grid(row=0, column=0, sticky="nsew")
			nextFrame.tkraise()

		# labels
		focus_label = tk.Label(self, text="Focus duration:")
		break_label = tk.Label(self, text="Break duration:")
		focus_label.grid(row=0, sticky='W') 
		break_label.grid(row=1, sticky='W') 

		# inputs
		focus_text = tk.StringVar()
		break_text = tk.StringVar()
		focus_input = tk.Entry(self, textvariable=focus_text, width=5)
		break_input = tk.Entry(self, textvariable=break_text, width=5)
		focus_input.grid(row=0, column=1)
		break_input.grid(row=1, column=1)

		# button
		next_button = tk.Button(self, text="Next", command=onNext)
		next_button.grid(row=2, columnspan=3, sticky='NESW')

		# time frame labels
		time_label1 = tk.Label(self, text="min(s)")
		time_label2 = tk.Label(self, text="min(s)")
		time_label1.grid(row=0, column=2)
		time_label2.grid(row=1, column=2)


	
		

class MainPage(tk.Frame):

	def __init__(self, container, controller):
		tk.Frame.__init__(self, container)
		self.grid_columnconfigure((0,1), weight=1)
		self.focus_duration = int(controller.focus_duration.get()) # retrieves focus duration from the root 
		self.break_duration = int(controller.break_duration.get()) # retrieves break duration from the root
		self.current_session = tk.StringVar() # variable for current session label
		self.current_session.set("Focus")
		self.session_label = tk.Label(self, textvariable=self.current_session) # current session label
		self.session_label.grid(row=0, column=0, columnspan=2)
		self.timer = t.Timer(self.focus_duration) # initialize timer
		self.focus_ct = 0 # number of completed focus sessions
		self.break_ct = 0 # number of completed break sessions
		self.running = False # controls count down of the timer
		self.time = tk.Label(self, text=self.timer.toStr()) # dynamic label that simulates the timer
		self.time.grid(row=1, column=0, columnspan=2)
		self.start_pause_btn = tk.Button(self, text="Start", command=self.start_pause) # button that starts/pauses the timer
		self.start_pause_btn.grid(row=2, column=0, sticky="E")
		self.skip_btn = tk.Button(self, text="Skip", command=self.skip)
		self.skip_btn.grid(row=2, column=1, sticky="W")

	def start_pause(self):
		self.running ^= 1 # flips the value of this boolean
		if self.running == True:
			self.start()
			self.start_pause_btn.configure(text="Pause")
		else:
			self.start_pause_btn.configure(text="Start")

	# starts the timer
	def start(self):
		if self.running != False:
			if self.timer.timesUp(): # switch the type of session when the timer is up
				self.switch()
			else:
				self.timer.decrement() # decrements the timer by 1 second
			self.time.configure(text=self.timer.toStr())
			self.time.after(1000, self.start) # recurse after 1 second

	# switches the type of session and resets the timer 
	def switch(self):
		if self.current_session.get() == "Focus":
			self.current_session.set("Break")
			self.timer.reset(self.break_duration)
		else:
			self.current_session.set("Focus")
			self.timer.reset(self.focus_duration)
		self.time.configure(text=self.timer.toStr())

	# pauses the timer
	def pause(self):
		self.running = False

	def skip(self):
		self.running = False
		self.switch()
		self.start_pause_btn.configure(text="Start")


app = Pomodoro()
app.mainloop()