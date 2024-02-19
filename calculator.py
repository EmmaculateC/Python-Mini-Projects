import tkinter as tk

def button_click(symbol):
    if symbol == "C":
        entry.delete(0, tk.END)
    elif symbol == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, symbol)

root = tk.Tk()
root.title("Calculator")

# Styling
root.configure(bg="#333333")
root.option_add('*Button.background', '#666666')
root.option_add('*Button.foreground', 'white')
root.option_add('*Button.font', ('Arial', 12, 'bold'))
root.option_add('*Button.borderwidth', 0)
root.option_add('*Button.activebackground', '#999999')
root.option_add('*Button.highlightthickness', 0)

# Create entry widget
entry = tk.Entry(root, width=30, borderwidth=5, font=('Arial', 14), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

# Define button symbols and colors
buttons = [
    ('7', '#555555'), ('8', '#555555'), ('9', '#555555'), ('/', '#ff8c00'),
    ('4', '#555555'), ('5', '#555555'), ('6', '#555555'), ('*', '#ff8c00'),
    ('1', '#555555'), ('2', '#555555'), ('3', '#555555'), ('-', '#ff8c00'),
    ('C', '#ff6347'), ('0', '#555555'), ('=', '#228b22'), ('+', '#ff8c00')
]

# Function to create and place buttons
def create_button(symbol, color, r, c):
    return tk.Button(root, text=symbol, bg=color, padx=20, pady=20, command=lambda: button_click(symbol)).grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

# Loop to create and place buttons
for i, (symbol, color) in enumerate(buttons):
    row = i // 4 + 1
    col = i % 4
    create_button(symbol, color, row, col)

# Configure grid
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(i+1, weight=1)

root.mainloop()
