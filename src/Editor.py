from tkinter import *
from tkinter.ttk import *


project_opened = False


root = Tk()
root.title("MQEdit V1.0a")

weapon_name_edit = Label(root, text = "Weapon Name:")
weapon_desc_edit = Label(root, text = "Weapon Description:")

weapon_name_text = Entry(root)
weapon_desc_text = Entry(root)

def WeaponEditor():
    if weapon_name_edit.winfo_ismapped():
        weapon_name_edit.grid_remove()
        weapon_desc_edit.grid_remove()
        weapon_name_text.grid_remove()
        weapon_desc_text.grid_remove()
        
    else:    
        weapon_name_edit.grid(row = 0, column = 0)
        weapon_desc_edit.grid(row = 1, column = 0)

        weapon_name_text.grid(row = 0, column = 1)
        weapon_desc_text.grid(row = 1, column = 1)



menuBar = Menu(root)

#File dropdown menu
filemenu = Menu(menuBar, tearoff = 0)
menuBar.add_cascade (label = "File", menu = filemenu)
filemenu.add_command(label = "Open Project", command = None)
filemenu.add_command(label = "Save Project", command = None)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = None)

#Edit dropdown menu
editmenu = Menu(menuBar, tearoff = 0)
menuBar.add_cascade(label = "Edit", menu = editmenu)
editmenu.add_command(label = "Weapons", command = WeaponEditor)

#Help dropdown menu
helpmenu = Menu(menuBar, tearoff = 0)
menuBar.add_cascade(label =  "Help", menu = helpmenu)
helpmenu.add_command(label = "About", command = None)



#Window Properties
win_x = (root.winfo_screenwidth() // 2)
win_y = (root.winfo_screenheight() // 2)
win_width = (root.winfo_screenwidth() // 2)
win_height = (root.winfo_screenheight() // 2)

root.geometry(f"{win_width}x{win_height}+{win_x // 2}+{win_y // 2}")

#Weirdly the icon must go under the geometry otherwise it will change the windows centered position?
icon = PhotoImage(file = 'mqeditlogo.png')
root.iconphoto(False, icon)



root.config(menu = menuBar)
root.mainloop(0)