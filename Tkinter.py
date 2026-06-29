import tkinter as tk
from tkinter import ttk
import json
import os
import sys
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

    mode = tk.StringVar(value="modify")

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

    def update_mode(*args):
        if mode.get() == "search":
            add_hold_button.grid_remove()
            clear_inventory_button.grid_remove()
            listbox.pack_forget() 
            search_button.grid(row=2, column=3, padx=10, sticky="w")
            clear_search_button.grid(row=3, column=3, padx=10, sticky="w")
            search_results_box.pack()
        elif mode.get() == "modify":
            search_button.grid_remove()
            clear_search_button.grid_remove()
            search_results_box.pack_forget()
            add_hold_button.grid(row=2, column=3, padx=10, sticky="w")
            clear_inventory_button.grid(row=3, column=3, padx=10, sticky="w")
            listbox.pack()

    def add_hold():
        name = name_entry.get()
        type = type_entry.get()
        colour = colour_entry.get()
        size = size_entry.get()

        if type:
            hold = {
                "name": name,
                "type": type,
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
            listbox.insert(tk.END, f"{hold['name']} | {hold['type']} | {hold['colour']} | {hold['size']}")
        remove_button.config(state="disabled")  # deselect clears the button

    def on_listbox_select(event):
        if listbox.curselection():
            remove_button.config(state="normal")
            remove_button.grid(row=3, column=0, padx=10, sticky="e")
        else:
            remove_button.config(state="disabled")
            

    def remove_selected():
        selected = listbox.curselection()
        if not selected:
            return
        index = selected[0]
        del inventory[index]
        save_inventory(inventory)
        update_inventory_list()
        remove_button.grid_remove()

    def clear_inventory_entry():
        name_entry.delete(0, tk.END)
        type_entry.set('')
        colour_entry.set('')
        size_entry.set('')

    def search_inventory():
        search_results_box.delete(0, tk.END)
        search_name = name_entry.get().lower()
        search_type = type_entry.get().lower()
        search_colour = colour_entry.get().lower()
        search_size = size_entry.get().lower()

        for hold in inventory:
            if ((not search_name or search_name in hold['name'].lower()) and
                (not search_type or search_type == hold['type'].lower()) and
                (not search_colour or search_colour == hold['colour'].lower()) and
                (not search_size or search_size == hold['size'].lower())
                ):
                search_results_box.insert(tk.END, f"{hold['name']} | {hold['type']} | {hold['colour']} | {hold['size']}")

    def clear_search():
        name_entry.delete(0, tk.END)
        type_entry.set('')
        colour_entry.set('')
        size_entry.set('')
        search_results_box.delete(0, tk.END)

    input_frame = tk.Frame(content_frame)
    input_frame.pack(pady=10)

    # MODIFY / SEARCH
    
    tk.Button(input_frame, text="Modify Mode", command=lambda: mode.set("modify")).grid(row=1, column=0, padx=10, sticky="e")
    tk.Button(input_frame, text="Search Mode", command=lambda: mode.set("search")).grid(row=2, column=0, padx=10, sticky="e")

    # NAME
    tk.Label(input_frame, text="Name:").grid(row=0, column=1, padx=10, sticky="w")
    name_entry = tk.Entry(input_frame, width=23)
    name_entry.grid(row=1, column=1, padx=10)

    # TYPE
    tk.Label(input_frame, text="Type:").grid(row=2, column=1, padx=10, sticky="w")
    type_entry = ttk.Combobox(input_frame, values=["Jug", "Crimp", "Sloper", "Pinch", "Pocket"], state="readonly")
    type_entry.grid(row=3, column=1, padx=10)

    # COLOUR
    tk.Label(input_frame, text="Colour:").grid(row=0, column=2, padx=(10, 0), sticky="w")
    colour_entry = ttk.Combobox(input_frame, values=["Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Black"], state="readonly")
    colour_entry.grid(row=1, column=2, padx=10)

    # SIZE
    tk.Label(input_frame, text="Size:").grid(row=2, column=2, padx=(10, 0), sticky="w")
    size_entry = ttk.Combobox(input_frame, values=["Tiny", "Small", "Medium", "Large"], state="readonly")
    size_entry.grid(row=3, column=2, padx=10)

    # ADD HOLD
    add_hold_button = tk.Button(input_frame, text="Add Hold", command=add_hold, bg="green3")
    add_hold_button.grid(row=2, column=3, padx=10, sticky="w")

    # CLEAR INVENTORY
    clear_inventory_button = tk.Button(input_frame, text="Clear", command=clear_inventory_entry, bg="red2")
    clear_inventory_button.grid(row=3, column=3, padx=10, sticky="w")

    listbox = tk.Listbox(content_frame, width=80)
    listbox.pack()
    listbox.bind("<<ListboxSelect>>", on_listbox_select)

    remove_button = tk.Button(input_frame, text="Remove", command=remove_selected, bg="red2", state="disabled")
    
    

    # SEARCH
    search_button = tk.Button(input_frame, text="Search", bg="green3", command=search_inventory)

    # CLEAR SEARCH
    clear_search_button = tk.Button(input_frame, text="Clear", bg="red2", command=clear_search)


    # SEARCH RESULTS BOX
    search_results_box = tk.Listbox(content_frame, width=80)



    mode.trace_add("write", update_mode)
    
    
    update_inventory_list()

def route_maker_page():
    clear_frame()
    title_label.config(text="Route Maker")

    def launch_route_maker():
        subprocess.Popen([sys.executable, "Route_maker/route_maker.py"])


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
inventory_page()

root.mainloop()