import tkinter as tk

window = tk.Tk()

relief = tk.SUNKEN

def kill():
    label["image"] = photo2

photo1 = tk.PhotoImage(file = r"prePunch.png")

photo2 = tk.PhotoImage(file = r"punch.png")

label = tk.Label(text = "KILL IT", image = photo1, fg = "white" )

label.grid(row=0, column=0,pady = 5)

button = tk.Button(text = "KILL IT", relief = relief, command=kill)

button.grid(row=0,column=0)

window.mainloop()

