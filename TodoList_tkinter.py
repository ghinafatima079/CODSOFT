#ToDo List
"""A To-Do List application is a useful project that helps users manageand organize their tasks efficiently. 
This project aims to create a command-line or GUI-based application using Python, allowing users to create, update, and track their to-do lists"""


import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.geometry("600x600")
root.title('ToDo List')

task_label=tk.Label(root,text='Task',fg="purple",font=('Times New Roman', 12))
task_label.grid(padx=5,pady=5,row=0,column=0)

task_entry=tk.Entry(root,width=20,font=('Times New Roman', 12),fg="red")
task_entry.grid(padx=5,pady=5,row=0,column=1)

todo_list=tk.Listbox(root,width=30,height=20,font=('Times New Roman', 16),fg="red")
todo_list.grid(padx=5,pady=5,row=2,column=0,rowspan=5)


def add_task():
    task=task_entry.get()
    if task!="":
        todo_list.insert(tk.END,task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")
    
    
def update_task():
    update_task_text=task_entry.get()
    if update_task_text!="":
        task_index = todo_list.curselection()[0]
        todo_list.delete(task_index)
        todo_list.insert(task_index,update_task_text)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter what you want to update task to.")

def delete_task():
    todo_list.delete(tk.ANCHOR)

add_button=tk.Button(root,text='Add Task',command=add_task,fg="blue",bg="beige",font=('Times New Roman', 12))
add_button.grid(padx=5,pady=5,row=2,column=1)

update_button=tk.Button(root,text='Update Task',command=update_task,fg="blue",bg="beige",font=('Times New Roman', 12))
update_button.grid(padx=5,pady=5,row=3,column=1)

delete_button=tk.Button(root,text='Delete Task',command=delete_task,fg="blue",bg="beige",font=('Times New Roman', 12))
delete_button.grid(padx=5,pady=5,row=4,column=1)

root.mainloop()
