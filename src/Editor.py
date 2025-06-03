from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
import Weapons
import Enemies
import Scripts
import Items
import Magic
import Npcs

#NEON   [Black, Pink, Light Blue]
#Lime   [Green]
#Snow   [Blue gray, pink gray, soft whites?]
#Candy  [Light pink, soft pink, soft black]
#Lemon  [Yellow]
#Doom   [Red, Yellow, Black]
#Pharoh [Gold, Black, Purple]
#Galaxy [Black, Purple, Blue]
#Fish   [Gray, Light blue, tan?]

editor_styles = ["neon", "lime", "snow", "candy", "lemon", "doom", "pharaoh", "galaxy", "fish"]
window_title = "MQEdit V1.0a"

project_opened = False
file_data_weapons = Weapons.weapon_data


root = Tk()
root.title(window_title)

#Labels / Text
weapon_name_label =          Label(root, text = "Weapon Name:")
weapon_desc_label =          Label(root, text = "Weapon Description:")
weapon_base_damage_label =   Label(root, text = "Base Damage:")
weapon_commit_1_label = Label(root, text = "Commit 1 Damage:")
weapon_commit_2_label = Label(root, text = "Commit 2 Damage:")
weapon_commit_3_label = Label(root, text = "Commit 3 Damage:")

#Entery fields
weapon_name_text_field = Entry(root)
weapon_desc_text_field = Entry(root)

#Num box
weapon_base_damage =     Spinbox(root, from_= Weapons.weapon_min_damage,        to= Weapons.weapon_max_damage,        increment = 1)
weapon_commit_1_damage = Spinbox(root, from_= Weapons.weapon_min_commit_damage, to= Weapons.weapon_max_commit_damage, increment = 1)
weapon_commit_2_damage = Spinbox(root, from_= Weapons.weapon_min_commit_damage, to= Weapons.weapon_max_commit_damage, increment = 1)
weapon_commit_3_damage = Spinbox(root, from_= Weapons.weapon_min_commit_damage, to= Weapons.weapon_max_commit_damage, increment = 1)

#Scroll bar
weapons_list_scrollbar = Scrollbar(root)
weapons_list = Listbox(root, yscrollcommand=weapons_list_scrollbar.set)
weapons_list_scrollbar.config(command = weapons_list.yview)





#Weapons editor function will hide on start unless you click the drop down menu
def WeaponEditor():
    if weapon_name_label.winfo_ismapped():
        weapon_name_label        .grid_remove()
        weapon_desc_label        .grid_remove()
        weapon_base_damage_label .grid_remove()

        weapon_name_text_field .grid_remove()
        weapon_desc_text_field .grid_remove()

        weapon_base_damage     .grid_remove()
        weapon_commit_1_damage .grid_remove()
        weapon_commit_2_damage .grid_remove()
        weapon_commit_3_damage .grid_remove()
        
        weapons_list_scrollbar .grid_remove()
        weapons_list           .grid_remove()

    else:
        weapon_name_label        .grid(row = 0, column = 0)
        weapon_desc_label        .grid(row = 1, column = 0)
        weapon_base_damage_label .grid(row = 2, column = 0)

        weapon_name_text_field .grid(row = 0, column = 1)
        weapon_desc_text_field .grid(row = 1, column = 1)
        weapon_commit_1_label  .grid(row = 3, column = 0)
        weapon_commit_2_label  .grid(row = 4, column = 0)
        weapon_commit_3_label  .grid(row = 5, column = 0)

        weapon_base_damage     .grid(row = 2, column = 1)
        weapon_commit_1_damage .grid(row = 3, column = 1)
        weapon_commit_2_damage .grid(row = 4, column = 1)
        weapon_commit_3_damage .grid(row = 5, column = 1)

        weapons_list_scrollbar .grid(row = 6, column = 0, columnspan = TRUE)
        weapons_list           .grid(row = 6, column = 1)

        #Loop to add all names of each weapon in the game to this list displayed on the GUI's screen
        for name in Weapons.default_weapon_names:
            weapons_list.insert(END, name)



# FIX SCROLLBAR at some point?
# When you open the weapon file, delete all weapons in the weapons list that is already there then just append the ones currently in the weapons.asdf




#Open files must use the main folder where the game is stored as an exe or other type of executable.
def ProjectOpen():
    file_path = filedialog.askopenfile(
        title = "Open Morlequariat folder",
        filetypes = (("Morlequariat main folder", "*.asdf"), ("All files", "*.*"))
    )

    if file_path:
        print("================================================================================")
        print("\t\t\tLoading files...")
        print("================================================================================\n")
        print("Selected load file: ", file_path)
        if file_path.readable:

            file_open = open(file_path.name, "r+")
            Weapons.weapon_data = file_open.read()
            print(file_open)
            
            print("Weapon Data: " + Weapons.weapon_data)            
        
        else:
            print("File is not readable!")




#Save files must use the main folder where the game is stored as an exe or other type of executable.
def ProjectSave():
    file_path = filedialog.asksaveasfile(
        title = "Save Morlequariat folder",
        filetypes = (("Morlequariat main folder", "*.asdf"), ("All files", "*.*"))
    )

    if file_path:
        print("================================================================================")
        print("\t\t\tSaving files...")
        print("================================================================================\n")
        print("Selected save file: ", file_path)
        
        print("Weapon Data: " + Weapons.weapon_data)
        
        if file_path.readable:

            file_save = open(file_path.name, "r+")
            file_save.write(Weapons.weapon_data)
            file_save.seek(0,0)

            print(file_save.read())

            file_save.close()

        else:
            print("File is not readable!")





#Settings editor for the MQEditing software
def MQEditSettings():
    settings_window = Toplevel(root)
    settings_window.title(window_title + " Settings")
    settings_window.geometry("480x250")

    #Settings > Themes
    theme_settings = Combobox(settings_window, width = 16, textvariable = "N", state = "readonly")
    theme_settings['values'] = editor_styles
    theme_settings.grid(row = 1, column = 0)
    theme_settings.current(0)

    #Settings > Okay Button
    theme_settings_okay_button = Button(settings_window, text = "Okay")
    theme_settings_okay_button.grid(sticky = S)

    icon = PhotoImage(file = 'mqeditlogo.png')
    settings_window.iconphoto(False, icon)





#Where main program starts
menuBar = Menu(root)

#File dropdown menu
filemenu = Menu(menuBar, tearoff = 0)
menuBar  .add_cascade(label = "File", menu = filemenu)
filemenu .add_command(label = "Open Project", command = ProjectOpen)
filemenu .add_command(label = "Save Project", command = ProjectSave)
filemenu .add_separator()
filemenu .add_command(label = "Exit", command = None)

#Edit dropdown menu
editmenu = Menu(menuBar, tearoff = 0)
menuBar  .add_cascade(label = "Edit", menu = editmenu)
editmenu .add_command(label = "Weapons", command = WeaponEditor)

#Settings dropdown menu
settingsmenu = Menu(menuBar, tearoff = 0)
menuBar       .add_cascade(label = "Settings", menu = settingsmenu)
settingsmenu  .add_command(label = "Settings", command = MQEditSettings)

#Help dropdown menu
helpmenu = Menu(menuBar, tearoff = 0)
menuBar  .add_cascade(label =  "Help", menu = helpmenu)
helpmenu .add_command(label = "About", command = None)



#Window Properties
win_x      = (root.winfo_screenwidth()  // 2)
win_y      = (root.winfo_screenheight() // 2)
win_width  = (root.winfo_screenwidth()  // 2)
win_height = (root.winfo_screenheight() // 2)

root.geometry(f"{win_width}x{win_height}+{win_x // 2}+{win_y // 2}")
root.minsize(720, 480)

#Weirdly the icon must go under the geometry otherwise it will change the windows centered position?
icon = PhotoImage(file = 'mqeditlogo.png')
root.iconphoto(False, icon)



root.config(menu = menuBar)
root.mainloop(0)