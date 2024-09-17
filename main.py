from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import Image, ImageTk  # Import from Pillow

root = Tk()
root.title("Weather App")
root.geometry("600x700+100+50")
root.resizable(False, False)
root.configure(bg='#808080')

# Function to center an element horizontally
def center_x(window_width, element_width):
    return (window_width - element_width) // 2

# Load and resize the home image
image_home = Image.open("weather_cloud-removebg-preview-Photoroom.png")
image_home = image_home.resize((200, 150), Image.LANCZOS)
image_home = ImageTk.PhotoImage(image_home)

# Calculate position for top-middle alignment
home_x = center_x(600, 200)  # Center horizontally based on root width and image width
home_y = 100  # Distance from the top

image_home_label = Label(root, image=image_home, bg='gray')
image_home_label.place(x=home_x, y=home_y - 90)

# Load and resize the search image and search zone
search_image = Image.open("search-removebg-preview.png")
search_zone = Image.open("Copyofsearch-removebg-preview.png")
search_image = search_image.resize((50, 50), Image.LANCZOS)
search_zone = search_zone.resize((300, 50), Image.LANCZOS)
search_photo = ImageTk.PhotoImage(search_image)
search_zone_photo = ImageTk.PhotoImage(search_zone)

# Display the search_zone first, then the search_image after the search_zone
search_zone_label = Label(root, image=search_zone_photo, bg='gray')
search_zone_label.place(x=home_x - 70, y=home_y + 70)  # Place the search zone

# Place the search_image after the search_zone
search_image_label = Label(root, image=search_photo, bg='gray')
search_image_label.place(x=home_x + 230, y=home_y + 70)  # Adjust x to place search_image after search_zone

textfield=tk.Entry(root,width=15,font=("poppins",20,"bold"),bg='#4F4F4F',border=0,fg="white")
textfield.place(x=home_x-35 , y=home_y + 80)






root.mainloop()
