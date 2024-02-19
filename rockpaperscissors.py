import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from random import choice

class RPS:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('Rock Paper Scissors')
        self.win.configure(bg='#f0f0f0')  # Set background color

        self.user_score = 0
        self.comp_score = 0
        self.tie_score = 0

        self.load_images()
        self.gui_elements()
        self.win.mainloop()

    def load_images(self):
        # Load and resize images
        self.rock_img = self.resize_image("rock.png", (100, 100))
        self.paper_img = self.resize_image("paper.png", (100, 100))
        self.scissors_img = self.resize_image("scissors.png", (100, 100))

    def resize_image(self, filename, size):
        image = Image.open(filename)
        image = image.resize(size)
        return ImageTk.PhotoImage(image)

    def gui_elements(self):
        # Header
        header = ttk.Label(self.win, text='Rock Paper Scissors', font=('Arial', 14))
        header.grid(row=0, column=0, pady=(10, 20))

        # User Choice Buttons
        choices = ttk.Frame(self.win, style='TFrame')
        rock_button = ttk.Button(choices, image=self.rock_img, command=lambda: self.play('rock'))
        rock_button.grid(row=0, column=0, padx=5, pady=5)
        paper_button = ttk.Button(choices, image=self.paper_img, command=lambda: self.play('paper'))
        paper_button.grid(row=0, column=1, padx=5, pady=5)
        scissors_button = ttk.Button(choices, image=self.scissors_img, command=lambda: self.play('scissors'))
        scissors_button.grid(row=0, column=2, padx=5, pady=5)
        choices.grid(row=1, column=0, padx=10)

        # User Score
        self.user_frame = ttk.Frame(self.win, style='TFrame')
        self.user_score_label = ttk.Label(self.user_frame, text="Wins: 0", font=('Arial', 12))
        self.user_score_label.pack()
        self.user_frame.grid(row=2, column=0, pady=10)

        # Tie Score
        self.tie_frame = ttk.Frame(self.win, style='TFrame')
        self.tie_score_label = ttk.Label(self.tie_frame, text="Ties: 0", font=('Arial', 12))
        self.tie_score_label.pack()
        self.tie_frame.grid(row=3, column=0, pady=10)

        # Comp Score 
        self.comp_frame = ttk.Frame(self.win, style='TFrame')
        self.comp_score_label = ttk.Label(self.comp_frame, text="Losses: 0", font=('Arial', 12))
        self.comp_score_label.pack()
        self.comp_frame.grid(row=4, column=0, pady=10)

        # Style
        style = ttk.Style()
        style.configure('TFrame', background='#f0f0f0')  # Light gray background

    def play(self, user_choice):
        choices = ['rock', 'paper', 'scissors']
        comp_choice = choice(choices)

        if user_choice == comp_choice:
            self.tie_score += 1
            messagebox.showinfo('Round Result', 'It is a tie!')
        elif (user_choice == 'rock' and comp_choice == 'scissors') or (user_choice == 'paper' and comp_choice == 'rock') or (user_choice == 'scissors' and comp_choice == 'paper'):
            self.user_score += 1
            messagebox.showinfo('Round Result', 'You won!')
        else:
            self.comp_score += 1
            messagebox.showinfo('Round Result', 'You lost!')

        self.update_scores()

    def update_scores(self):
        self.user_score_label.config(text=f"Wins: {self.user_score}")
        self.tie_score_label.config(text=f"Ties: {self.tie_score}")
        self.comp_score_label.config(text=f"Losses: {self.comp_score}")

game = RPS()
