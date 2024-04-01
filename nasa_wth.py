import importlib
import subprocess

def check_and_install(package):
    try:
        importlib.import_module(package)
        print(f"{package} is already installed.")
    except ImportError:
        print(f"{package} is not installed. Installing...")
        subprocess.check_call(["pip", "install", package])

# List of required packages
required_packages = ["tkinter", "webbrowser","pandas","requests","pillow"]

# Check and install each package
for package in required_packages:
    check_and_install(package)


import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import webbrowser
import datetime
from utils import utils
from libs import wth_handler
from nasapo import ndown1
from PIL import Image, ImageTk
default_headers = ["DATE", "SRAD", "TMAX", "TMIN", "RAIN", "DEWP", "WIND", "PAR", "EVAP", "RHUM"]
input_headers=["DATE", "TMAX", "TMIN", "SRAD", "RAIN", "RHUM", "WIND", "EVAP", "PAR", "DEWP"]





class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("GUI")
        self.root.geometry("900x350")  # Set window size
        self.root.resizable(False, False)  # Disable resizing
        
        # Define folder_var as an instance attribute
        self.folder_var1 = tk.StringVar()
        self.folder_var2 = tk.StringVar()
        self.csv_path = tk.StringVar()
        
        cd = os.path.dirname(os.path.abspath(__file__))
        """       
        # Background image
        bg_image = Image.open(cd+'\\gui\\2.jpg')# Provide path to your background image
        bg_image = bg_image.resize((900, 350), Image.ANTIALIAS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
"""
        # Main text
        main_text = tk.Label(self.root, text="NASA Power Data Download & DSSAT WTH Generator", font=("Arial", 12, "bold"))
        main_text.pack(pady=10)
        # Subtext
        sub_text = tk.Label(self.root, text="Written by KPJ", font=("Arial", 8))
        sub_text.place(relx=0, rely=1.0, anchor="sw")

        # Help button
        help_button = tk.Button(self.root, text="Readme", font=("Arial", 10), command=lambda:self.open_help_file(cd))
        help_button.place(relx=0.9, rely=0.1, anchor="c", width=80, height=40)
        
        select_button1 = tk.Button(self.root, text="Select Folder for Data download", command=self.select_folder1)
        select_button1.place(relx=0.1, rely=0.3, anchor="w", width=200, height=20)

        # Create a white rectangular box to display the selected folder path
        folder_entry = tk.Entry(self.root, textvariable=self.folder_var1, bg="white", width=50)
        folder_entry.place(relx=0.1, rely=0.4, anchor="w", width=300, height=20)
        
        select_csv_button = tk.Button(self.root, text="Select Coordinate CSV file", command=self.select_csv_file)
        select_csv_button.place(relx=0.8, rely=0.3, anchor="e", width=150, height=20)
        
        folder_entry = tk.Entry(self.root, textvariable=self.csv_path, bg="white", width=50)
        folder_entry.place(relx=0.8, rely=0.4, anchor="e", width=300, height=20)
        
        Download_button = tk.Button(self.root, text="↓",font=("Arial", 17, "bold"),command=self.download)
        Download_button.place(relx=0.9, rely=0.3, anchor="c", width=40, height=30)
        
        convert_label = tk.Label(self.root, text="Download", font=("Arial", 10))
        convert_label.place(relx=0.9, rely=0.4, anchor="c")
 
        start_year_label = tk.Label(self.root, text="Start Year:", font=("Arial", 10))
        start_year_label.place(relx=0.1, rely=0.5, anchor="w")

        # Entry widget for entering the date
        self.date_entry1 = tk.Entry(self.root, font=("Arial", 10))
        self.date_entry1.place(relx=0.18, rely=0.5, anchor="w")
        
        end_year_label = tk.Label(self.root, text="End Year:", font=("Arial", 10))
        end_year_label.place(relx=0.35, rely=0.5, anchor="w")
        
        self.date_entry2 = tk.Entry(self.root, font=("Arial", 10))
        self.date_entry2.place(relx=0.42, rely=0.5, anchor="w")
        
        self.error_label = tk.Label(self.root, text="", font=("Arial", 10), fg="red")
        self.error_label.place(relx=0.78, rely=0.5, anchor="c")
        
        # Bind function to check date format and range on key release
        self.date_entry1.bind("<KeyRelease>", lambda event: self.check_date(event, 1))
        self.date_entry2.bind("<KeyRelease>", lambda event: self.check_date(event, 2))
        date_value1 = self.date_entry1.get()
        date_value2 = self.date_entry2.get()
        
        
        select_button2 = tk.Button(self.root, text="Select Folder to save WTH Files", command=self.select_folder2)
        select_button2.place(relx=0.5, rely=0.7, anchor="c", width=200, height=20)

        # Create a white rectangular box to display the selected folder path
        folder_entry = tk.Entry(self.root, textvariable=self.folder_var2, bg="white", width=50)
        folder_entry.place(relx=0.5, rely=0.8, anchor="c", width=300, height=20)
        
        Convert_button = tk.Button(self.root, text="↻",font=("Arial", 24), command=self.convert_wth)
        Convert_button.place(relx=0.8, rely=0.7, anchor="c", width=40, height=30)
        
        convert_label = tk.Label(self.root, text="Convert", font=("Arial", 10))
        convert_label.place(relx=0.8, rely=0.8, anchor="c")

    # Add self parameter to make select_folder() a method of the GUI class
    def select_folder1(self):
        folder_path1 = filedialog.askdirectory()
        if folder_path1:
            self.folder_var1.set(folder_path1)
     
    def select_folder2(self):
        folder_path2 = filedialog.askdirectory()
        if folder_path2:
            self.folder_var2.set(folder_path2)
    
    def select_csv_file(self):
        csv_file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if csv_file_path:
            self.csv_path.set(csv_file_path)
            
    def open_help_file(self,cd):
        # Open a simple text file with help information
        webbrowser.open(cd+"//README.md")  # Provide path to your help text file

    def check_date(self, event, entry_id):
        # Clear previous error message
        self.error_label.config(text="")
         # Determine which entry widget was used based on the entry_id
        if entry_id == 1:
            date_entry = self.date_entry1
        elif entry_id == 2:
            date_entry = self.date_entry2
        else:
        # Handle invalid entry_id
            return
        # Get the date entered by the user
        date_str = date_entry.get()
        
        # Check if the date is in the correct format (dd/mm/yyyy)
        if len(date_str) == 10:
            try:
                date_obj = datetime.datetime.strptime(date_str, '%d/%m/%Y')
            except ValueError:
                self.error_label.config(text="Please enter the date in the format dd/mm/yyyy")
                return
            
            # Check if the year is within the range 1981 to the current year
            current_year = datetime.datetime.now().year
            if date_obj.year < 1981 or date_obj.year > current_year:
                self.error_label.config(text="Please enter a year between 1981 and the current year")
                return
   
    def download(self):
        dzz = self.folder_var1.get()
        if dzz:
            # Call the function to process the file
            csv = self.csv_path.get()
            sdate = self.date_entry1.get()
            edate = self.date_entry2.get()
            down(dzz,csv,sdate,edate)
            self.error_label.config(text="DONE DOWNLOADING")
        else:
            self.error_label.config(text="No folder Selected or CSV File Selected")
    def convert_wth(self):
        directory = self.folder_var2.get()
        if directory:
            dzz = self.folder_var1.get()
            main(dzz,directory)
            self.error_label.config(text="DONE CONVERSION")
        else:
            self.error_label.config(text="No folder Selected")


    def run(self):
        self.root.mainloop()



def main(directory,dzz):
    csvs=utils.get_csv_files(dzz)
    for csv_file in csvs:
        print("input_file",csv_file)
        wth_handler.format_wth(directory,csv_file,default_headers,input_headers)
        print("output",csv_file)

def down(dzz,csv,sdate,edate):
    ndown1.down(dzz,csv,sdate,edate)
   

# Create and run the GUI
gui = GUI()
gui.run()
