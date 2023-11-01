from tkinter import *
from PIL import Image, ImageTk

def show_coords():
    # Get the window's position and size
    min_x = window.winfo_rootx()
    min_y = window.winfo_rooty()
    max_x = min_x + window.winfo_width()
    max_y = min_y + window.winfo_height()

    # Print the minimum and maximum coordinates
    print(f"Minimum x,y coord visible: ({min_x}, {min_y})")
    print(f"Maximum x,y coord visible: ({max_x}, {max_y})")

    # Call the function again after a short delay
    window.after(100, show_coords)

# Load the image using PIL
image2 = Image.open("C:/Users/210108/Downloads/Text-Based-Game/One.png")

# Keep the 'image2' object in the memory while it is being displayed
global_image2 = image2

# Convert the image to a PhotoImage
image_tk2 = ImageTk.PhotoImage(image2)

# Create a tkinter window
window = Tk()

# Create a label to display the image
image_label = Label(window, image=image_tk2)

# Place the image at a specific position in the window
image_label.place(x=100, y=200)