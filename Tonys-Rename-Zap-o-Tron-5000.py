import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox

selected_directories = []

def rename_files(directory):
    pattern = re.compile(r'^[0-3][0-9] - .+\.mp3$')
    for filename in os.listdir(directory):
        if pattern.match(filename):
            new_name = filename[5:]
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_name)
            os.rename(old_file, new_file)
            print(f'Renamed: {filename} to {new_name}')

def add_directory():
    directory = filedialog.askdirectory(mustexist=True, title="Select Directory")
    if directory:
        selected_directories.append(directory)
        listbox.insert(tk.END, directory)
        print(f'Selected: {directory}')
    else:
        messagebox.showwarning("No Selection", "No directory selected.")

def zap_files():
    if selected_directories:
        for directory in selected_directories:
            rename_files(directory)
        messagebox.showinfo("Success", "Files have been renamed successfully.")
    else:
        messagebox.showwarning("No Selection", "No directories selected.")

def create_gui():
    global listbox
    root = tk.Tk()
    root.title("Tonys Rename Zap-o-Tron 5000")
    root.geometry("400x300")

    select_button = tk.Button(root, text="Add a Directory", command=add_directory)
    select_button.pack(pady=10)

    listbox = tk.Listbox(root, width=50, height=10)
    listbox.pack(pady=10)

    zap_button = tk.Button(root, text="Zap Files", command=zap_files)
    zap_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()