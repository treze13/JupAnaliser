from tkinter import filedialog
import tkinter as tk

root = tk.Tk()
root.withdraw()

folder_selected = filedialog.askdirectory()
print(folder_selected)
