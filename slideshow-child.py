import os
import random
from PIL import Image, ImageTk
import tkinter as tk
import sys

# Get the list of image files from command-line arguments
image_files = sys.argv[1:]  # Expecting a list of image paths as arguments

class ImageSlideshow:
    def __init__(self, root, image_files, delay=2000):
        self.root = root
        self.image_files = image_files
        self.delay = delay  # Delay between images in milliseconds

        # Hide the cursor
        self.root.config(cursor="none")

        # Create title label at the bottom
        self.title_label = tk.Label(root, font=('Arial', 20), bg='black', fg='white')
        self.title_label.pack(side=tk.BOTTOM, fill=tk.X)  # Title at the bottom

        # Create image label
        self.label = tk.Label(root)
        self.label.pack(fill=tk.BOTH, expand=True)  # Fill the window

        self.index = 0

        # Set to fullscreen
        self.root.attributes('-fullscreen', True)
        self.show_image()

    def zoom_effect(self, image, photo, steps=300, step_delay=100):
        """
        Gradually zooms into the image.
        :param image: Original PIL image.
        :param photo: Current ImageTk.PhotoImage object.
        :param steps: Number of steps for the zoom effect.
        :param step_delay: Delay in ms between each zoom step.
        """
        original_width, original_height = image.size
        zoom_factor = 1.2  # 20% zoom
        
        # Increment for each step
        width_step = int((original_width * zoom_factor - original_width) / steps)
        height_step = int((original_height * zoom_factor - original_height) / steps)

        def perform_zoom(step=0):
            if step <= steps:
                # Calculate new dimensions
                new_width = original_width + step * width_step
                new_height = original_height + step * height_step

                # Resize the image
                resized_image = image.resize((new_width, new_height), Image.LANCZOS)
                photo = ImageTk.PhotoImage(resized_image)

                # Update the label with the resized image
                self.label.config(image=photo)
                self.label.image = photo

                # Continue zooming
                self.root.after(step_delay, perform_zoom, step + 1)

        perform_zoom()  # Start the zoom effect


    def show_image(self):
        if self.image_files:
            image_path = self.image_files[self.index]
            image = Image.open(image_path)

            # Get screen width and height
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()

            # Resize image maintaining aspect ratio
            image_ratio = image.width / image.height
            screen_ratio = screen_width / screen_height

            if image_ratio > screen_ratio:
                new_width = screen_width
                new_height = int(screen_width / image_ratio)
            else:
                new_height = screen_height
                new_width = int(screen_height * image_ratio)

            resized_image = image.resize((new_width, new_height), Image.LANCZOS)
            # Release the previous image from the label
            self.label.image = None  # Release the previous image
            
            photo = ImageTk.PhotoImage(resized_image)

            self.label.config(image=photo)
            self.label.image = photo  # Keep a reference to avoid garbage collection
            
            # Apply zoom effect
            self.zoom_effect(resized_image, photo)

            # Update title label with the filename (without extension)
            filename = os.path.splitext(os.path.basename(image_path))[0]  # Remove the extension
            self.title_label.config(text=filename)

            self.index = (self.index + 1) % len(self.image_files)
            if self.index == 0:
                self.root.quit()  # Exit the slideshow after showing all images
            else:
                self.root.after(self.delay, self.show_image)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Image Slideshow")
    if image_files:
        slideshow = ImageSlideshow(root, image_files, delay=20000)  # 20 seconds per image
    root.mainloop()
