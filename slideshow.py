import os
import random
import time
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_FOLDER = os.path.join(SCRIPT_DIR, 'images')

CHILD_SCRIPT = os.path.join(SCRIPT_DIR, 'slideshow-child.py')
def load_images(folder_path):
    # List all image files in the folder
    valid_extensions = ['.jpg', '.png', '.gif', '.jpeg']
    return [os.path.join(folder_path, f) for f in os.listdir(folder_path)
            if os.path.splitext(f)[1].lower() in valid_extensions]

def run_slideshow(images):
    # Launch the slideshow script with the selected images
    # print("calling child script")
    subprocess.run(['python', CHILD_SCRIPT] + images)

if __name__ == "__main__":
    images = load_images(IMAGE_FOLDER)
    
    # Run for 2 hours
    end_time = time.time() + 2 * 60 * 60  # 2 hours in seconds

    while time.time() < end_time:
        selected_images = random.sample(images, 2)  # Select 10 random images
        run_slideshow(selected_images)

        # Wait for the slideshow to complete (you might need to handle this differently)
        time.sleep(1)  # Optional: Add a short delay before the next slideshow
    
    # shutting down the device after loop is complete
    os.system('sudo shutdown -h now')