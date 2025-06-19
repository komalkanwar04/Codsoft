import tkinter 
from tkinter import *
from PIL import Image, ImageTk
root=Tk()
root.title("To-Do List")
root.geometry("400x650+400+100")
root.resizable(False,False)

task_list = []  # List of tuples (task_text, done)

def format_task_text(task, done):
    return f"[{'✓' if done else ' '}] {task}"

def addTask(task):
    task= task_entry.get()
    task_entry.delete(0, END)

    if task:
        task_list.append((task, False))
        with open("task.txt", "a") as file:
            file.write(f"{task}|False\n")
        listbox.insert(END, format_task_text(task, False))

def save_tasks():
    with open("task.txt", "w") as file:
        for task, done in task_list:
            file.write(f"{task}|{done}\n")

def deleteTask():
    global task_list
    selected_tasks = listbox.curselection()
    if not selected_tasks:
        return
    for index in reversed(selected_tasks):
        task_text = listbox.get(index)
        # Extract task without prefix
        task = task_text[4:]
        # Remove from task_list
        task_list = [t for t in task_list if t[0] != task]
        listbox.delete(index)
    save_tasks()

def toggle_done(event=None):
    global task_list
    selected_tasks = listbox.curselection()
    if not selected_tasks:
        return
    for index in selected_tasks:
        task_text = listbox.get(index)
        task = task_text[4:]
        for i, (t, done) in enumerate(task_list):
            if t == task:
                task_list[i] = (t, not done)
                listbox.delete(index)
                listbox.insert(index, format_task_text(t, not done))
                break
    save_tasks()

def openTaskFile():
    try:
        global task_list
        task_list.clear()
        listbox.delete(0, END)
        with open("task.txt", "r") as file:
            tasks = file.readlines()
            for line in tasks:
                if line.strip():
                    parts = line.strip().split("|")
                    task = parts[0]
                    done = parts[1].lower() == "true" if len(parts) > 1 else False
                    task_list.append((task, done))
                    listbox.insert(END, format_task_text(task, done))
    except:
        file = open("task.txt", "w")
        file.close()

#icon
Image_icon = PhotoImage(file="image/daily-tasks.png")
root.iconphoto(False, Image_icon)

#top bar
TopImage= PhotoImage(file="image/horizontal.png")
Label(root, image=TopImage).pack()

heading = Label(root, text="To-Do List", font=("Arial", 20, "bold"), bg="#32405b", fg="white")
heading.place(x=130, y=8)      

#main
frame= Frame(root, width=400, height=40, bg="white")
frame.place(x=0, y=150)

task=StringVar()
task_entry= Entry(frame, width=15, font=("Arial", 20), bd=0)
task_entry.place(x=8, y=7)
task_entry.focus()

button=Button(frame, text="ADD", font=("Arial", 15, "bold"), width= 6, bg="#32405b",fg="#fff", bd=0, command=lambda: addTask(task_entry.get()))
button.place(x=320, y=2)

#listbox
frame1= Frame(root, bd=3, width=400, height=200, bg="#32405b")
frame1.pack(pady=(160, 0))

listbox = Listbox(frame1, font=("Arial", 12), width=30, height=16, bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff", selectmode=EXTENDED)
listbox.pack(side=LEFT, fill=BOTH, padx=2)

Scrollbar= Scrollbar(frame1)
Scrollbar.pack(side=LEFT, fill=Y)

listbox.config(yscrollcommand=Scrollbar.set)
Scrollbar.config(command=listbox.yview)

openTaskFile()

#delete
# Resize delete button image to smaller size
delete_img = Image.open("image/delete.png")
delete_img = delete_img.resize((30, 30), Image.LANCZOS)
Delete_icon = ImageTk.PhotoImage(delete_img)

# New frame below frame1 for delete button
frame2 = Frame(root, bd=3, width=400, height=50, bg="#32405b")
frame2.pack(pady=(10, 20))

delete_button = Button(frame2, image=Delete_icon, bd=0, command=deleteTask)
delete_button.pack()

# Bind double click on listbox to toggle done status
listbox.bind("<Double-Button-1>", toggle_done)

root.mainloop()
