import tkinter as tk
import timer as t
class Pomodoro(tk.Tk):

	def __init__(self, *args, **kwargs):

		tk.Tk.__init__(self, *args, **kwargs)
		container = tk.Frame(self) # container for swapping from starting page to main page

		container.pack(side="top", fill="both", expand=True)

		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.focus_duration = tk.StringVar() # stores the input for focus duration
		self.break_duration = tk.StringVar() # stores the input for break duration

		# starting page is displayed first
		frame = StartPage(container, self)
		frame.grid(row=0, column=0, sticky="nsew")
		frame.tkraise()

class StartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		# stores the input values for the focus/break durations and then swaps frames
		def onNext(): 
			controller.focus_duration.set(focus_text.get())
			controller.break_duration.set(break_text.get())
			nextFrame = MainPage(parent, controller)
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

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.focus_duration = int(controller.focus_duration.get()) # retrieves focus duration from the root 
		self.break_duration = int(controller.break_duration.get()) # retrieves break duration from the root
		self.current_session = "Focus"
		self.timer = t.Timer(self.focus_duration) # Timer initialized
		self.focus_ct = 0 # number of completed focus sessions
		self.break_ct = 0 # number of completed break sessions
		self.running = False # controls count down of the timer
		self.label = tk.Label(self, text=self.timer.toStr()) # dynamic label that simulates the timer
		self.label.pack()
		self.start_pause = tk.Button(self, text="Start", command=self.start_pause) # button that starts/pauses the timer
		self.start_pause.pack()


	def start_pause(self):
		if self.running == False:
			self.running = True
			self.start_pause.configure(text="Pause")
			self.start()
		else:
			self.start_pause.configure(text="Start")
			self.pause()

	# starts the timer
	def start(self):
		if self.running != False:
			if self.timer.timesUp():
				self.switch()
			else:
				self.timer.decrement()
			self.label.configure(text=self.timer.toStr())
			self.label.after(1000, self.start)

	# switches the type of session and resets the timer 
	def switch(self):
		if self.current_session == "Focus":
			self.current_session = "Break"
			self.timer.reset(self.break_duration)
		else:
			self.current_session = "Focus"
			self.timer.reset(self.focus_duration)

	# pauses the timer
	def pause(self):
		self.running = False


app = Pomodoro()
app.mainloop()