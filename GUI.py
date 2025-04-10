import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Function to be called when the 'Upload Image' button is clicked
def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        original_image = Image.open(file_path)

        # Store the original image in the application state for later processing
        global current_image
        current_image = original_image

        # Convert the image to ImageTk format for Tkinter display
        original_image_tk = ImageTk.PhotoImage(original_image)

        # Update the label to show the original image
        label_original.config(image=original_image_tk)
        label_original.image = original_image_tk  # Keep a reference to avoid garbage collection

        # Clear the compressed image label initially
        label_compressed.config(image=None)

# Quadtree compression function (to be filled with your compression logic)
def quadtree_compress(image):
    # Implement Quadtree Decompression algorithm here
    # For now, we return the image as is (no compression)
    return image

# Function to compress and show the compressed image
def compress_image():
    if current_image:
        compressed_image = quadtree_compress(current_image)  # Compress the image
        
        # Convert the compressed image to ImageTk format for Tkinter display
        compressed_image_tk = ImageTk.PhotoImage(compressed_image)
        
        # Update the compressed image label
        label_compressed.config(image=compressed_image_tk)
        label_compressed.image = compressed_image_tk  # Keep a reference to avoid garbage collection

# Create the main application window
root = tk.Tk()
root.title("Image Compression with Quadtree")

# Set fixed window size (you can adjust the size as needed)
root.geometry("600x600")  # Fixed window size

# Create a frame to center the images in the window
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Create labels to display original and compressed images, placed inside the frame
label_original = tk.Label(frame, text="Original Image", bg="lightgray")
label_original.pack(side=tk.TOP, padx=10, pady=10)

label_compressed = tk.Label(frame, text="Compressed Image", bg="lightgray")
label_compressed.pack(side=tk.TOP, padx=10, pady=10)

# Create buttons for uploading and compressing images
button_upload = tk.Button(root, text="Upload Image", command=upload_image)
button_upload.pack(pady=10)

button_compress = tk.Button(root, text="Compress Image", command=compress_image)
button_compress.pack(pady=10)

# Global variable to store the current image (original image)
current_image = None

# Run the Tkinter event loop
root.mainloop()
