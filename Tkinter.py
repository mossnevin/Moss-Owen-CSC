import tkinter as tk
import json
import os
import subprocess
# import route_maker

def clear():
    os.system("cls")

def clear_frame():
    for widget in content_frame.winfo_children():
        widget.destroy()

def close_app(event=None):
    root.destroy()


def home_page():
    clear_frame()

    title_label.config(text="Home")

    

    header = tk.Label(content_frame, font=("Arial", 30, "underline"), text="Welcome")
    header.pack(pady=10)

    main_text = tk.Label(content_frame, font=("Arial", 15), text="words, words, words", wraplength=600)
    main_text.pack()

def inventory_page():
    clear_frame()
    title_label.config(text="Hold Inventory")

    

    def load_inventory():
        if os.path.exists("inventory.json"):
            with open("inventory.json", "r") as f:
                content = f.read()
                if not content.strip():
                    return []
                return json.loads(content)
        return []

    inventory = load_inventory()

    def save_inventory(inventory):
        with open("inventory.json", "w") as f:
            json.dump(inventory, f, indent=4)

    def add_hold():
        type = type_entry.get()
        colour = colour_entry.get()
        size = size_entry.get()

        if type:
            hold = {
                "name": type,
                "colour": colour,
                "size": size
            }
            inventory.append(hold)
            save_inventory(inventory)
            update_inventory_list()
            type_entry.delete(0, tk.END)
            colour_entry.delete(0, tk.END)
            size_entry.delete(0, tk.END)

    def update_inventory_list():
        listbox.delete(0, tk.END)
        for hold in inventory:
            listbox.insert(tk.END, hold)

    tk.Label(content_frame, text="Type:").pack()
    type_entry = tk.Entry(content_frame)
    type_entry.pack()

    tk.Label(content_frame, text="Colour:").pack()
    colour_entry = tk.Entry(content_frame)
    colour_entry.pack()

    tk.Label(content_frame, text="Size:").pack()
    size_entry = tk.Entry(content_frame)
    size_entry.pack()

    tk.Button(content_frame, text="Add Hold", command=add_hold).pack()

    listbox = tk.Listbox(content_frame)
    listbox.pack(fill="x", padx=10)
    
    
    update_inventory_list()

def route_maker_page():
    clear_frame()
    title_label.config(text="Route Maker")

    def launch_route_maker():
        subprocess.Popen(["python", "route_maker.py"])


    button = tk.Button(content_frame, text="Launch Route Maker", command=launch_route_maker)
    button.pack(pady=20)





root = tk.Tk()
root.title("Climbing App")
root.geometry("1080x720")



top_bar = tk.Frame(root, bg="slateblue3")
top_bar.pack(fill="x")

centre_frame = tk.Frame(top_bar, bg="slateblue3")
centre_frame.pack()

home_button = tk.Button(centre_frame, text="Home", font=("Arial", 15), command=home_page, bg="slateblue3", activeforeground="white", activebackground="slateblue4")
home_button.pack(side="left", padx=1)

inventory_button = tk.Button(centre_frame, text="Inventory", font=("Arial", 15), command=inventory_page, bg="slateblue3", activeforeground="white", activebackground="slateblue4")
inventory_button.pack(side="left", padx=1)

route_maker_button = tk.Button(centre_frame, text="Route Maker", font=("Arial", 15), command=route_maker_page, bg="slateblue3", activeforeground="white", activebackground="slateblue4")
route_maker_button.pack(side="left", padx=1)
 
content_frame = tk.Frame(root)
content_frame.pack(fill="both", expand=True)

title_label = tk.Label(root, font=("Arial", 21, "bold", "underline"), bg="slateblue3")
title_label.place(x=5, y=1)







clear()
home_page()

root.mainloop()