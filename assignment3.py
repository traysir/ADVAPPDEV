# Assignment3.py
# IT3883/Section XLS
# Bayden Blackwell
# Assignment 3
# 2/23/2025
# Tkinter documentation

import tkinter as tk

# convert
MPG_TO_KML = 0.425143707

def convert():
    """Converts MPG to KM/L and updates the label."""
    user_input = mpg_entry.get()
    if user_input.strip():  
        try:
            mpg_value = float(user_input)  # convert input to float
            kml_value = round(mpg_value * MPG_TO_KML, 2)  
            result_label.config(text=f"{kml_value} KM/L")  
        except ValueError:
            result_label.config(text="Enter a valid number") 
    else:
        result_label.config(text="") 

# main window
root = tk.Tk()
root.title("MPG to KM/L Converter")
root.geometry("320x180")
root.resizable(False, False)
mpg_entry = tk.Entry(root, font=("Arial", 14), width=10)
mpg_entry.pack(pady=10)
mpg_entry.bind("<KeyRelease>", lambda event: convert())  

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()

root.mainloop()
