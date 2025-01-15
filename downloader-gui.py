import tkinter as tk
from tkinter import messagebox
import csv
import os

def create_csv_if_not_exists():
    """Create videos.csv if it doesn't exist"""
    if not os.path.exists('videos.csv'):
        with open('videos.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['url', 'title', 'status'])

def add_video():
    """Add video URL and title to the CSV file"""
    url = url_entry.get().strip()
    title = title_entry.get().strip()
    
    # Basic validation
    if not url or not title:
        messagebox.showerror("Error", "Please fill in both fields")
        return
    
    # Add to CSV
    with open('videos.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([url, title, 'pending'])
    
    # Clear the entries
    url_entry.delete(0, tk.END)
    title_entry.delete(0, tk.END)
    messagebox.showinfo("Success", "Video added to download list!")

# Create the main window
window = tk.Tk()
window.title("YouTube Video Downloader")
window.geometry("400x200")  # Set window size

# Create and place URL input
tk.Label(window, text="Video URL:").pack(pady=5)
url_entry = tk.Entry(window, width=50)
url_entry.pack(pady=5)

# Create and place title input
tk.Label(window, text="Video Title:").pack(pady=5)
title_entry = tk.Entry(window, width=50)
title_entry.pack(pady=5)

# Create and place Add button
add_button = tk.Button(window, text="Add to Download List", command=add_video)
add_button.pack(pady=20)

# Ensure CSV exists
create_csv_if_not_exists()

# Start the GUI
window.mainloop()