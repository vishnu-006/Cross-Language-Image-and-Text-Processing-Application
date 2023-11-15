#                                                                GETTING FILE PATH
import tkinter as tk
from tkinter import filedialog

def ChooseFile():
    root = tk.Tk()
    #root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

if __name__ == "__main__":
    file_path = choose_file()
    if file_path:
        print(f"Selected File: {file_path}")
    else:
        print("No file selected.")
