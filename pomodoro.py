import tkinter as tk

class Pomodoro(tk.Tk):
	def __init__(self, *args, **kwargs):

		tk.Tk.__init__(self, *args, **kwargs)
		container = tk.Frame(self)

		container.pack(side="top", fill="both", expand=True)

		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {} # dictionary for the different pages in the app
		self.focus_duration = tk.StringVar()
		self.break_duration = tk.StringVar()

		for F in (StartPage, MainPage): # loop to initialize the different pages of the app

			frame = F(container, self)

			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage) 

	def show_frame(self, cont): # function to switch frames
		frame = self.frames[cont]
		frame.tkraise()

class StartPage(tk.Frame):


	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		def onNext():
			controller.focus_duration.set(focus_text.get())
			controller.break_duration.set(break_text.get())
			controller.show_frame(MainPage)

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
		self.current_session = "Focus"
		self.current_time = (controller.focus_duration, 0) # (minutes, seconds)
		self.focus_ct = 0
		self.break_ct = 0
		label = tk.Label(self, text=self.current_session)
		label.pack()



app = Pomodoro()
app.mainloop()