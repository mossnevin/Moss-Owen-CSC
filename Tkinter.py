import tkinter as tk
import json
import os
# import route_maker

def clear():
    os.system("cls")

def clear_frame():
    for widget in content_frame.winfo_children():
        widget.destroy()

def close_app(event=None):
    root.destroy()

def home():
    clear_frame()

    title_label.config(text="Home")

    

    header = tk.Label(content_frame, font=("Arial", 30, "underline"), text="Welcome")
    header.pack(pady=10)

    main_text = tk.Label(content_frame, font=("Arial", 15), text="words, words, words", wraplength=600)
    main_text.pack()

def inventory_page():
    clear_frame()

    title_label.config(text="Hold Inventory")




root = tk.Tk()
root.title("Climbing App")
root.geometry("1080x720")



top_bar = tk.Frame(root, bg="slateblue3")
top_bar.pack(fill="x")

centre_frame = tk.Frame(top_bar, bg="slateblue3")
centre_frame.pack()

home_button = tk.Button(centre_frame, text="Home", font=("Arial", 15), command=home, bg="slateblue3", activeforeground="white", activebackground="slateblue4")
home_button.pack(side="left", padx=1)

inventory_button = tk.Button(centre_frame, text="Inventory", font=("Arial", 15), command=inventory_page, bg="slateblue3", activeforeground="white", activebackground="slateblue4")
inventory_button.pack(side="left", padx=1)

page3_button = tk.Button(centre_frame, text="Page3", font=("Arial", 15), bg="slateblue3", activeforeground="white", activebackground="slateblue4")
page3_button.pack(side="left", padx=1)
 
content_frame = tk.Frame(root)
content_frame.pack(fill="both", expand=True)

title_label = tk.Label(root, font=("Arial", 21, "bold", "underline"), bg="slateblue3")
title_label.place(x=5, y=1)







clear()
home()

root.mainloop()