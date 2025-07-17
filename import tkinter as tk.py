import tkinter as tk
from tkinter import ttk
from matplotlib import colors

# Function to display color details
def show_color_details():
    color_name = color_var.get()
    if color_name:
        # Convert to RGB and HEX
        hex_value = colors.cnames[color_name]
        rgb_tuple = colors.to_rgb(hex_value)
        rgb_value = tuple(int(x * 255) for x in rgb_tuple)

        # Update labels
        hex_label.config(text=f"HEX: {hex_value}")
        rgb_label.config(text=f"RGB: {rgb_value}")

        # Update color preview
        color_preview.config(bg=hex_value)

# Create main window
root = tk.Tk()
root.title("Color Picker")
root.geometry("300x250")
root.resizable(False, False)

# Dropdown for color names
color_var = tk.StringVar()
color_names = sorted(colors.cnames.keys())
ttk.Label(root, text="Select a Color:", font=("Arial", 12)).pack(pady=10)
color_menu = ttk.Combobox(root, textvariable=color_var, values=color_names, state="readonly")
color_menu.pack(pady=5)

# Button
ttk.Button(root, text="Show Details", command=show_color_details).pack(pady=10)

# Labels for HEX and RGB
hex_label = tk.Label(root, text="HEX: ", font=("Arial", 12))
hex_label.pack()
rgb_label = tk.Label(root, text="RGB: ", font=("Arial", 12))
rgb_label.pack()

# Color preview box
color_preview = tk.Label(root, width=20, height=5, bg="white", relief="ridge", bd=2)
color_preview.pack(pady=10)

root.mainloop()
