#--------------------------#
# Module 10 practice
#
#
#--------------------------#
import tkinter as tk
from tkinter import ttk

# -- window_root (tk.TK)
#   -- lbl_math_info (tk.label)
application_window = tk.Tk() # creates a root node
application_window.geometry("400x100+400+100")# Define the size of the window
#second two inputs define location
application_window.title("Your title here!") # add title to window

# Create a label object in the window and get a reference
lbl_your_label = ttk.Label(application_window, text="Your Label Here!")

# add label to the root container using the pack layout manager method
lbl_your_label.grid(row=1, column=1, sticky=tk.NW, padx=5,pady=5)

# create a button and add it it to a grid container
btn_add = ttk.Button(application_window, text="Add", width=10) # button def
btn_add.grid(row=2, column=1, sticky=tk.NW, padx=10, pady=5) # button on grid

# create a button and add it it to a grid container
btn_subtract = ttk.Button(application_window, text="Subtract", width=10) # button def
btn_subtract.grid(row=2, column=2, sticky=tk.NW, padx=10, pady=5) # button on grid

# create a button and add it it to a grid container
btn_multiply = ttk.Button(application_window, text="Multiply", width=10) # button def
btn_multiply.grid(row=2, column=3, sticky=tk.NW, padx=10, pady=5) # button on grid

# create a button and add it it to a grid container
btn_divide = ttk.Button(application_window, text="Divide", width=10) # button def
btn_divide.grid(row=2, column=4, sticky=tk.NW, padx=10, pady=5) # button on grid

# example with windows at ~35min into module 10 video

# Display the window
application_window.mainloop() # displays window UI
