import tkinter as tk
from tkinter import filedialog
import os
def guii(down, main):    
    r = tk.Tk()
    r.title('DSSAT WTH File Generator From NASA Power data')
    icond =  os.path.dirname(os.path.abspath(__file__))
    down = os.path.join(icond,"down.png")
    fold = os.path.join(icond,"if.png")
    proc = os.path.join(icond,"dssat.png")
    def select_folder():
        selected_directory = filedialog.askdirectory()
    def download():
        down()

    def generate():
        main(dzz)  # Use the selected directory here
    
    select_button_icon = tk.PhotoImage(file= fold)  # Provide the path to your folder icon
    select_button = tk.Button(r, text='Select Folder', width=100, height=100, command=select_folder, image=select_button_icon, compound=tk.LEFT)
    select_button.pack(pady=100)

    download_button_icon = tk.PhotoImage(file= down)  # Provide the path to your download icon
    download_button = tk.Button(r, text='Download', width=200, height=50, command=download, image=download_button_icon, compound=tk.LEFT)
    download_button.pack(pady=100)

    generate_button_icon = tk.PhotoImage(file= down)  # Provide the path to your processing icon
    generate_button = tk.Button(r, text='Generate', width=200, height=50, command=generate, image=generate_button_icon, compound=tk.LEFT)
    generate_button.pack(pady=100)
    r.mainloop()

# Set a default value for the directory variable
dzz = ""

