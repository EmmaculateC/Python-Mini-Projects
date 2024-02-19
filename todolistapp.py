import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style
import json

class Task:
    def __init__(self, text, state):
        self.text = text
        self.state = state

class TaskManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("My Tasks")
        self.geometry("400x400")

        # Initialize styles
        style = Style(theme="cyborg")
        style.configure("Custom.TEntry", foreground="darkgray")
        style.configure("Title.TLabel", font=("Helvetica", 20, "bold"))
        style.configure("Custom.TButton", font=("Helvetica", 12))

        # Create category buttons
        ttk.Label(self, text="Categories of Tasks", style="Title.TLabel").pack(pady=10)
        ttk.Button(self, text="Personal", command=lambda: self.open_category("Personal"), style="Primary.TButton", width=15).pack(pady=5)
        ttk.Button(self, text="Work", command=lambda: self.open_category("Work"), style="Primary.TButton", width=15).pack(pady=5)
        ttk.Button(self, text="School", command=lambda: self.open_category("School"), style="Primary.TButton", width=15).pack(pady=5)

    def open_category(self, category):
        category_window = CategoryWindow(self, category)
        category_window.title(category)  # Set window title to the selected category
        category_window.geometry("600x400")

class CategoryWindow(tk.Toplevel):
    def __init__(self, master, category):
        super().__init__(master)

        self.category = category

        # Initialize styles
        style = Style(theme="cyborg")
        style.configure("Custom.TEntry", foreground="darkgray")
        style.configure("Title.TLabel", font=("Helvetica", 20, "bold"))
        style.configure("Custom.TButton", font=("Helvetica", 12))

        # Create task input field
        self.task_entry = ttk.Entry(self, font=("Helvetica", 16), width=30, style="Custom.TEntry")
        self.task_entry.pack(pady=10)
        self.task_entry.insert(0, f"Enter your {category.lower()} task here...")

        # Bind events for input field
        self.task_entry.bind("<FocusIn>", self.clear_placeholder)
        self.task_entry.bind("<FocusOut>", self.restore_placeholder)

        # Buttons for task actions
        ttk.Button(self, text="Add Task", command=self.add_task, style="Primary.TButton", width=15).pack(pady=5)
        ttk.Button(self, text="In Progress", command=self.mark_in_progress, style="Primary.TButton", width=15).pack(pady=5)
        ttk.Button(self, text="Completed", command=self.mark_completed, style="Success.TButton", width=15).pack(pady=5)
        ttk.Button(self, text="Delete", command=self.delete_task, style="Danger.TButton", width=15).pack(pady=5)
        ttk.Button(self, text="Summary Statistics", command=self.view_stats, style="Info.TButton", width=15).pack(pady=5)

        # Task list display
        self.task_listbox = tk.Listbox(self, font=("Helvetica", 16), height=10, selectmode=tk.SINGLE, bg="lightgray")
        self.task_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Keep track of completed tasks
        self.completed_tasks = []

        # Load existing tasks
        self.load_tasks()

    def add_task(self):
        task_text = self.task_entry.get()
        if task_text != f"Enter your {self.category.lower()} task here...":
            task = Task(text=task_text, state="Added")
            self.task_listbox.insert(tk.END, task.text)
            self.task_entry.delete(0, tk.END)
            self.restore_placeholder(None)  # Clear and restore placeholder
            self.save_tasks()

    def mark_in_progress(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_text = self.task_listbox.get(selected_index)
            if "(Completed)" not in task_text:
                self.task_listbox.delete(selected_index)
                task_text = f"{task_text.split(' (')[0]} (In Progress)"
                self.task_listbox.insert(tk.END, task_text)
                self.save_tasks()

    def mark_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_text = self.task_listbox.get(selected_index)
            if "(In Progress)" in task_text and "(Completed)" not in task_text:
                self.task_listbox.delete(selected_index)
                task_text = f"{task_text.split(' (')[0]} (Completed)"
                self.task_listbox.insert(tk.END, task_text)
                self.completed_tasks.append(task_text)
                self.save_tasks()

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_text = self.task_listbox.get(selected_index)
            if "(Completed)" in task_text:
                self.completed_tasks.remove(task_text)
            self.task_listbox.delete(selected_index)
            self.save_tasks()

    def view_stats(self):
        in_progress_count = sum(1 for i in range(self.task_listbox.size()) if "(In Progress)" in self.task_listbox.get(i))
        completed_count = len(self.completed_tasks)
        deleted_count = sum(1 for i in range(self.task_listbox.size()) if "Deleted" in self.task_listbox.get(i))

        stats_message = (
            f"In Progress: {in_progress_count}\n"
            f"Completed: {completed_count}\n"
            f"Deleted: {deleted_count}"
        )

        messagebox.showinfo("Summary Statistics", stats_message)

    def clear_placeholder(self, event):
        if self.task_entry.get() == f"Enter your {self.category.lower()} task here...":
            self.task_entry.delete(0, tk.END)
            self.task_entry.configure(style="TEntry")

    def restore_placeholder(self, event):
        if not self.task_entry.get():
            self.task_entry.insert(0, f"Enter your {self.category.lower()} task here...")
            self.task_entry.configure(style="Custom.TEntry")

    def load_tasks(self):
        try:
            with open(f"{self.category.lower()}_tasks.json", "r") as file:
                data = json.load(file)
                for task_data in data:
                    self.task_listbox.insert(tk.END, task_data["text"])
                    if "(Completed)" in task_data["text"]:
                        self.completed_tasks.append(task_data["text"])
        except FileNotFoundError:
            pass

    def save_tasks(self):
        data = [{"text": self.task_listbox.get(i)} for i in range(self.task_listbox.size())]
        with open(f"{self.category.lower()}_tasks.json", "w") as file:
            json.dump(data, file)

if __name__ == '__main__':
    app = TaskManagerApp()
    app.mainloop()
