import tkinter as tk
from tkinter import messagebox
from tkinter import font

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List")
        self.tasks = []

        # Create and configure the listbox to display tasks
        self.task_listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE, font=("Helvetica", 12))
        self.task_listbox.pack(pady=10)

        # Create and configure the entry widget to add new tasks
        self.task_entry = tk.Entry(root, width=50, font=("Helvetica", 12))
        self.task_entry.pack(pady=5)

        # Create buttons to add and remove tasks
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
        self.add_button.pack(pady=5)
        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task, bg="#FF5733", fg="white", font=("Helvetica", 12, "bold"))
        self.remove_button.pack(pady=5)

        # Set background color and center the window on the screen
        root.configure(bg="#f0f0f0")
        root.geometry("400x400")
        root.eval('tk::PlaceWindow . center')

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks.pop(index)
            self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
