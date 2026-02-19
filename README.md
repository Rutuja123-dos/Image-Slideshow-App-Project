📸 Python Image Slideshow Creator
A dynamic, high-resolution image slideshow application built with Python, Tkinter, and the Pillow (PIL) library. This tool automates the process of resizing and cycling through a collection of images in a clean GUI window.

🚀 Features
Automatic Resizing: Automatically scales all input images to a standard 1080x1080 resolution for consistency.

Smart Cycling: Utilizes itertools.cycle to prepare for infinite looping through the image list.

Pillow Integration: Uses advanced image handling to support multiple formats like .jpg and .png.

Interactive Controls: Includes a "Start Slideshow" button to trigger the sequence.

Smooth Transitions: Built-in delay using the time module to control the pace of the show.

🛠️ Prerequisites
You will need to install the Pillow library to handle image processing:

Bash
pip install Pillow
📋 How to Use
Clone the repository.

Update the image_path list in the code with the actual file paths from your computer.

Run the script:

Bash
python slideshow.py
Click "Start Slideshow" to begin the sequence.

🧠 Technical Highlights
Image Processing: Implemented list comprehension to efficiently open and resize all images at once:
images = [Image.open(path).resize(image_size) for path in image_path]

GUI Label Updates: Uses label.config() and label.update() to refresh the UI in real-time during the loop.

Path Handling: Employs Raw Strings (r"path") to ensure Windows backslashes don't cause escape character errors.

Author
Rutuja Wagh
