import tkinter as tk
import timer as t
class Pomodoro(tk.Tk):

	def __init__(self, *args, **kwargs):

		tk.Tk.__init__(self, *args, **kwargs)
		container = tk.Frame(self)

		container.pack(side="top", fill="both", expand=True)

		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.focus_duration = tk.StringVar()
		self.break_duration = tk.StringVar()

		frame = StartPage(container, self)
		frame.grid(row=0, column=0, sticky="nsew")
		frame.tkraise()

class StartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

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
		self.focus_duration = int(controller.focus_duration.get())
		self.break_duration = int(controller.break_duration.get())
		self.current_session = "Focus"
		self.timer = t.Timer(self.focus_duration)
		self.focus_ct = 0
		self.break_ct = 0
		self.running = True
		self.label = tk.Label(self, text=self.timer.toStr())
		self.label.pack()
		start_btn = tk.Button(self, text="Start", command=self.countdown)
		start_btn.pack()

	def countdown(self):
		if self.running != False:
			if self.timer.timesUp():
				self.switch()
			else:
				self.timer.decrement()
			self.label.configure(text=self.timer.toStr())
			self.label.after(1000, self.countdown)

	def switch(self):
		if self.current_session == "Focus":
			self.current_session = "Break"
			self.timer.reset(self.break_duration)
		else:
			self.current_session = "Focus"
			self.timer.reset(self.focus_duration)


app = Pomodoro()
app.mainloop()