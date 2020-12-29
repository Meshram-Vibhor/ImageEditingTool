import tkinter as tk

def importButton_callback():
    pass

def saveButton_callback():
    pass

def closeButton_callback():
    window.destroy()

def brightness_callback(brightness_pos):
    print(brightness_pos)

def contrast_callback(contrast_pos):
    print(contrast_pos)

window = tk.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window.geometry(f'{screen_width}x{screen_height}')

Frame1 = tk.Frame(window, height=20, width=200)
Frame1.pack(anchor=tk.N)

Frame2 = tk.Frame(window, height=20)
Frame2.pack(anchor=tk.NW)

importButton = tk.Button(Frame1, text="Import", padx=10, pady=5, command=importButton_callback)
importButton.grid(row=0, column=0)

saveButton = tk.Button(Frame1, text="Save", padx=10, pady=5, command=saveButton_callback)
saveButton.grid(row=0, column=1)

closeButton = tk.Button(Frame1, text="Close", padx=10, pady=5, command=closeButton_callback)
closeButton.grid(row=0, column=2)

brightnessSlider = tk.Scale(Frame2, label="Brightness", from_=0, to=2, orient=tk.HORIZONTAL,
                            length=screen_width, resolution=0.1, command=brightness_callback)
brightnessSlider.pack(anchor=tk.N)

contrastSlider = tk.Scale(Frame2, label="Contrast", from_=0, to=255, orient=tk.HORIZONTAL,
                          length=screen_width, command=contrast_callback)
contrastSlider.pack(anchor=tk.N)

tk.mainloop()