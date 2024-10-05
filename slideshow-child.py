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

        # Create image label
        self.label = tk.Label(root)
        self.label.pack(fill=tk.BOTH, expand=True)  # Fill the window

        self.index = 0

        # Set to fullscreen
        self.root.attributes('-fullscreen', True)

        # Preload the first image to avoid flickering on start
        self.current_image = None
        self.preload_image()
        self.show_image()

    def preload_image(self):
        """Preloads the current image in the background."""
        if self.image_files:
            image_path = self.image_files[self.index]
            image = Image.open(image_path)

            # Get screen width and height
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()

            # Resize image maintaining aspect ratio and fill the entire screen
            image_ratio = image.width / image.height
            screen_ratio = screen_width / screen_height

            if image_ratio > screen_ratio:
                new_height = screen_height
                new_width = int(screen_height * image_ratio)
            else:
                new_width = screen_width
                new_height = int(screen_width / image_ratio)

            # Resize the image
            resized_image = image.resize((new_width, new_height), Image.LANCZOS)

            # Crop the image to fill the screen
            left = (new_width - screen_width) / 2
            top = (new_height - screen_height) / 2
            right = (new_width + screen_width) / 2
            bottom = (new_height + screen_height) / 2
            cropped_image = resized_image.crop((left, top, right, bottom))

            self.current_image = ImageTk.PhotoImage(cropped_image)

    def show_image(self):
        """Displays the preloaded image and sets up the next image preload."""
        if self.image_files and self.current_image:
            # Directly set the preloaded image to avoid flickering
            self.label.config(image=self.current_image)
            self.label.image = self.current_image  # Keep a reference to avoid garbage collection

            # Preload the next image in the background
            self.index = (self.index + 1) % len(self.image_files)
            self.preload_image()

            if self.index == 0:
                self.root.quit()  # Exit the slideshow after showing all images
            else:
                # Show the next image after the delay
                self.root.after(self.delay, self.show_image)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Image Slideshow")
    if image_files:
        slideshow = ImageSlideshow(root, image_files, delay=20000)  # 20 seconds per image
    root.mainloop()
