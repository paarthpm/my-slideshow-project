import os
import random
from PIL import Image, ImageTk
import tkinter as tk

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Folder containing the images (update with your local path)
IMAGE_FOLDER = os.path.join(SCRIPT_DIR, 'images')

class ImageSlideshow:
    def __init__(self, root, folder_path, delay=2000):
        self.root = root
        self.folder_path = folder_path
        self.delay = delay  # Delay between images in milliseconds
        self.image_files = self.load_images()

        # Shuffle the images for random display
        random.shuffle(self.image_files)
        
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

    def load_images(self):
        # List all image files in the folder
        valid_extensions = ['.jpg', '.png', '.gif', '.jpeg']
        return [os.path.join(self.folder_path, f) for f in os.listdir(self.folder_path)
                if os.path.splitext(f)[1].lower() in valid_extensions]

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

            photo = ImageTk.PhotoImage(resized_image)

            self.label.config(image=photo)
            self.label.image = photo  # Keep a reference to avoid garbage collection

            # Update title label with the filename (without extension)
            filename = os.path.splitext(os.path.basename(image_path))[0]  # Remove the extension
            self.title_label.config(text=filename)

            self.index = (self.index + 1) % len(self.image_files)
            self.root.after(self.delay, self.show_image)  # Set the delay for the next image

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Image Slideshow")
    slideshow = ImageSlideshow(root, IMAGE_FOLDER, delay=20000)  # 20 seconds per image
    root.mainloop()
