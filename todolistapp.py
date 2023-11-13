from tkinter import *
from tkinter import messagebox

app=Tk()

app.geometry("700x600")
app.title("To-Do-list-app")
app.configure(bg="light blue")
app.resizable(height=False,width=False) #to make the window non-resizable

#creating a list
tasks=[]
#creating functions
def update_listbox():
    clear_listbox()
    for task in tasks:
        lb_tasks.insert("end",task)
def clear_listbox():
    lb_tasks.delete(0,"end")
def add_task():
    task=txt_input.get()
    if task !="":
        tasks.append(task)
        update_listbox()
    else:
        messagebox.showwarning("warning","please enter a task")
    txt_input.delete(0,"end")
def del_all():
    confirmed=messagebox.askyesno("please confirm","do you really want to delete all")
    if confirmed==True:
        global tasks
        tasks=[]
        update_listbox()    
def del_one():
    task=lb_tasks.get("active")
    if task in tasks:
        tasks.remove(task)
    update_listbox()
def sort_asc():
    tasks.sort()
    update_listbox()
def sort_desc():
    tasks.sort()
    tasks.reverse()
    update_listbox()
def choose_color():
    color=askcolor()
    print(color)
def exit():
    confirm=messagebox.askyesno("please confirm","do you really want to exit")
    if confirm==True:
        app.destroy()
#creating widgets
lbl_title=Label(app,text="To-Do-List",font=("bold",30),bg="blue")
lbl_title.place(x=150,y=10)
lbl_display=Label(app,text="Enter the task",font=("bold",15),bg="light blue")   
lbl_display.place(x=10,y=80)    
txt_input=Entry(app,width=25,font=("bold",15))          
txt_input.place(x=200,y=80)
btn_add=Button(app,text="Add task",font=("bold",15),bg="light blue",command=add_task)
btn_add.place(x=10,y=130)
btn_del_all=Button(app,text="Delete all",font=("bold",15),bg="light blue",command=del_all)
btn_del_all.place(x=100,y=130)
btn_del_one=Button(app,text="Delete",font=("bold",15),bg="light blue",command=del_one)
btn_del_one.place(x=220,y=130)
btn_sort_asc=Button(app,text="Sort(ASC)",font=("bold",15),bg="light blue",command=sort_asc)
btn_sort_asc.place(x=300,y=130)
btn_sort_desc=Button(app,text="Sort(DESC)",font=("bold",15),bg="light blue",command=sort_desc)
btn_sort_desc.place(x=400,y=130)
lb_tasks=Listbox(app,height=10,width=50,font=("bold",15))
lb_tasks.place(x=10,y=200)
btn_exit=Button(app,text="Exit",font=("bold",15),bg="orange",command=exit)
btn_exit.place(x=10,y=450)
btn_color=Button(app,text="Choose color",font=("bold",15),bg="light blue",command=choose_color)
btn_color.place(x=300,y=450)
app.mainloop()

