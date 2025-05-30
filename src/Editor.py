from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
import Weapons
import Enemies
import Scripts
import Items
import Magic
import Npcs


project_opened = False


root = Tk()
root.title("MQEdit V1.0a")

#Labels / Text
weapon_name_edit = Label(root, text = "Weapon Name:")
weapon_desc_edit = Label(root, text = "Weapon Description:")
weapon_base_damage_edit = Label(root, text = "Base Damage:")

#Entery fields
weapon_name_text = Entry(root)
weapon_desc_text = Entry(root)

#Num box
weapon_base_damage = Spinbox(root, from_= Weapons.weapon_min_damage, to= Weapons.weapon_max_damage, increment = 1)

#Scroll bar
weapons_list_scrollbar = Scrollbar(root)
weapons_list = Listbox(root, yscrollcommand=weapons_list_scrollbar.set)
weapons_list_scrollbar.config()



#Weapons editor function will hide on start unless you click the drop down menu
def WeaponEditor():
    if weapon_name_edit.winfo_ismapped():
        weapon_name_edit.grid_remove()
        weapon_desc_edit.grid_remove()
        weapon_base_damage_edit.grid_remove()

        weapon_name_text.grid_remove()
        weapon_desc_text.grid_remove()

        weapon_base_damage.grid_remove()
        
        weapons_list_scrollbar.grid_remove()
        weapons_list.grid_remove()

    else:    
        weapon_name_edit.grid(row = 0, column = 0)
        weapon_desc_edit.grid(row = 1, column = 0)
        weapon_base_damage_edit.grid(row = 2, column = 0)

        weapon_name_text.grid(row = 0, column = 1)
        weapon_desc_text.grid(row = 1, column = 1)

        weapon_base_damage.grid(row = 2, column = 1)

        weapons_list_scrollbar.grid(row = 5, column = 0)
        weapons_list.grid(row = 5, column = 1)

        for name in Weapons.default_weapon_names:
            weapons_list.insert(END, name)



#Open files must use the main folder where the game is stored as an exe or other type of executable
def ProjectOpen():
    file_path = filedialog.askopenfile(
        title = "Open Morlequariat folder",
        filetypes = (("Morlequariat main folder", "*.asdf"), ("All files", "*.*"))
    )

    if file_path:
        print("Selected file: ", file_path)
        if file_path.readable:
            f = open(file_path, "r")
            print(f.read())
        
        else:
            print("File is not readable!")


# WORK ON FILE OPENING!!!



#Where main program starts
menuBar = Menu(root)

#File dropdown menu
filemenu = Menu(menuBar, tearoff = 0)
menuBar.add_cascade (label = "File", menu = filemenu)
filemenu.add_command(label = "Open Project", command = ProjectOpen)
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