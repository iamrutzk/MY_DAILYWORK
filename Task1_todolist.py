import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.tasks = []
        self.task_number = 1

        self.task_list = tk.Listbox(root, width=40)
        self.task_list.pack(padx=10, pady=10)

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add task", command=self.add_task)
        self.add_button.pack(padx=10, pady=10)

        self.delete_button = tk.Button(root, text="Delete task", command=self.delete_task)
        self.delete_button.pack(padx=10, pady=10)

        self.update_button = tk.Button(root, text="Update task", command=self.update_task)
        self.update_button.pack(padx=10, pady=10)

        self.done_button = tk.Button(root, text="Mark as done", command=self.mark_done)
        self.done_button.pack(padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "done": False})
            self.task_list.insert(self.task_number, task)
            self.task_number += 1
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            self.task_list.delete(task_index)
            del self.tasks[task_index]
        except IndexError:
            messagebox.showerror("Error", "Select a task to delete")

    def update_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            task = self.task_entry.get()
            if task:
                self.tasks[task_index]["task"] = task
                self.task_list.delete(task_index)
                self.task_list.insert(task_index, task)
                self.task_entry.delete(0, tk.END)
        except IndexError:
            messagebox.showerror("Error", "Select a task to update")

    def mark_done(self):
        try:
            task_index = self.task_list.curselection()[0]
            self.tasks[task_index]["done"] = True
            task = self.tasks[task_index]["task"]
            self.task_list.delete(task_index)
            self.task_list.insert(task_index, f"{task} (Task Completed)")
        except IndexError:
            messagebox.showerror("Error", "Select a task to mark as done")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("To-Do List")
    todo = ToDoList(root)
    root.mainloop()