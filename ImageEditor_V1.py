import tkinter as tk

def importButton_callback():
    pass

def saveButton_callback():
    pass

def closeButton_callback():
    window.destroy()

window = tk.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window.geometry(f'{screen_width}x{screen_height}')

Frame1 = tk.Frame(window, height=20, width=200)
Frame1.pack(anchor=tk.N)

importButton = tk.Button(Frame1, text="Import", padx=10, pady=5, command=importButton_callback)
importButton.grid(row=0, column=0)

saveButton = tk.Button(Frame1, text="Save", padx=10, pady=5, command=saveButton_callback)
saveButton.grid(row=0, column=1)

closeButton = tk.Button(Frame1, text="Close", padx=10, pady=5, command=closeButton_callback)
closeButton.grid(row=0, column=2)

tk.mainloop()