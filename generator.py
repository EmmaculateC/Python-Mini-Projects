import random
import string
import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title('Password Generator')
root.config(bg='white')

# Configure grid
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# Create frames 
header_frame = ttk.Frame(root)
input_frame = ttk.Frame(root)
pass_frame = ttk.Frame(root)
button_frame = ttk.Frame(root)

header_frame.grid(row=0, column=0, pady=20)
input_frame.grid(row=1, column=0)
pass_frame.grid(row=2, column=0, pady=20) 
button_frame.grid(row=3, column=0, pady=20)

# Header content
logo = tk.PhotoImage(file='logo.png')
logo_label = tk.Label(header_frame, image=logo, bg='white')
logo_label.grid(row=0, column=0)

title_label = ttk.Label(header_frame, text="Password Generator", font=("TkDefaultFont", 24))
title_label.grid(row=0, column=0)

# Input content
length_label = ttk.Label(input_frame, text="Length:")  
length_entry = ttk.Entry(input_frame, width=10)

length_label.grid(row=0, column=0, padx=10, sticky='W')  
length_entry.grid(row=0, column=1)

# Password content
pass_label = ttk.Label(pass_frame, text="Generated Password:")
pass_entry = ttk.Entry(pass_frame, width=24)

pass_label.grid(row=0, column=0, padx=10, sticky='W')
pass_entry.grid(row=0, column=1)

# Button content 
gen_button = ttk.Button(button_frame, text="Generate") 

gen_button.grid(row=0, column=0, pady=10)

# Password generator function  
def generate_password():
  
  # Get password length 
  length = int(length_entry.get())
    
  # Define character sets
  lower = string.ascii_lowercase
  upper = string.ascii_uppercase
  num = string.digits
  symbols = string.punctuation

  # Combine all character sets
  all = lower + upper + num + symbols
    
  # Generate random password
  password = ''.join(random.sample(all,length))
    
  # Insert into pass_entry
  pass_entry.delete(0, tk.END)
  pass_entry.insert(0, string=password)

    
# Bind button event   
gen_button.config(command=generate_password)

root.mainloop()