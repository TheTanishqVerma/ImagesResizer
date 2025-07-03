import os
from PIL import Image

# Set input and output directories
input_folder = "input_images"
output_folder = "output_images"
output_size = (800, 800)

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process each image in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        try:
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)

            # Resize the image
            img_resized = img.resize(output_size)

            # Save as PNG
            base_name = os.path.splitext(filename)[0]
            output_path = os.path.join(output_folder, f"{base_name}.png")
            img_resized.save(output_path)

            print(f"[✔] Processed {filename} -> {output_path}")

        except Exception as e:
            print(f"[✘] Failed to process {filename}: {e}")