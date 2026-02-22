import customtkinter as ctk
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app=ctk.CTk()
app.geometry("500x300")
app.title("Window Colour Changer")

def make_red():
    print("You picked red")
    app.configure(fg_color="red")
    title_label.configure(text="You picked red!")

def make_cyan():
    print("You picked cyan")
    app.configure(fg_color="cyan")
    title_label.configure(text="You picked cyan")
def make_purple():
    print("You picked purple")
    app.configure(fg_color="purple")
    title_label.configure(text="You picked purple")
def make_pink():
    print("You picked pink")
    app.configure(fg_color="hot pink")
    title_label.configure(text="You picked pink")

def make_coral():
    print("You picked coral")
    app.configure(fg_color="coral")
    title_label.configure(text="You picked coral")

def make_orange():
    print("You picked orange")
    app.configure(fg_color="orange")
    title_label.configure(text="You picked orange")

def make_yellow():
    print("You picked yellow")
    app.configure(fg_color="yellow")
    title_label.configure(text="You picked yellow")

def make_maroon():
    print("You picked maroon")
    app.configure(fg_color="maroon")
    title_label.configure(text="You picked maroon")

def make_green():
    print("You picked green")
    app.configure(fg_color="green")
    title_label.configure(text="You picked green")

def make_dark_blue():
    print("You picked blue")
    app.configure(fg_color="dark blue")
    title_label.configure(text="You picked blue")

title_label=ctk.CTkLabel(app,text="Pick a colour!",font=("Arial",30),text_color="black")
title_label.grid(row=0,column=3)

btn_red=ctk.CTkButton(app,text="Red" , command=make_red,width=120,height=50)
btn_red.grid(row=1, column=0,columnspan=2 ,rowspan=2,padx=10,pady=10)

btn_cyan=ctk.CTkButton(app,text="Cyan" , command=make_cyan,width=120,height=50)
btn_cyan.grid(row=1, column=3,columnspan=2 ,rowspan=2,padx=10,pady=10)

btn_purple=ctk.CTkButton(app,text="purple" , command=make_purple,width=120,height=50)
btn_purple.grid(row=1, column=6,columnspan=2 ,rowspan=2,padx=10,pady=10)

btn_pink=ctk.CTkButton(app,text="pink" , command=make_pink,width=120,height=50)
btn_pink.grid(row=3, column=0,columnspan=2 ,rowspan=2,padx=10,pady=10)

btn_pink=ctk.CTkButton(app,text="coral" , command=make_coral,width=120,height=50)
btn_pink.grid(row=3, column=3,columnspan=2 ,rowspan=2,padx=10,pady=10)


btn_orange=ctk.CTkButton(app,text="orange" , command=make_orange,width=120,height=50)
btn_orange.grid(row=3, column=6,columnspan=2 ,rowspan=2,padx=10,pady=10)

btn_yellow=ctk.CTkButton(app,text="yellow" , command=make_yellow,width=120,height=50)
btn_yellow.grid(row=5, column=0,columnspan=2 ,rowspan=2,padx=10,pady=10)

btn_maroon=ctk.CTkButton(app,text="maroon" , command=make_maroon,width=120,height=50)
btn_maroon.grid(row=5, column=3,columnspan=2 ,rowspan=2,padx=10,pady=10)

btn_green=ctk.CTkButton(app,text="green" , command=make_green,width=120,height=50)
btn_green.grid(row=5, column=6,columnspan=2 ,rowspan=2,padx=10,pady=10)

btn_blue=ctk.CTkButton(app,text="blue" , command=make_dark_blue,width=120,height=50)
btn_blue.grid(row=7, column=0,columnspan=2 ,rowspan=2,padx=10,pady=10)

app.mainloop()