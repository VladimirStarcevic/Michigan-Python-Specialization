from PIL import Image
import os

INPUT_FOLDER = "input_images"
OUTPUT_FOLDER = "output_images"
IMAGE_NAME = "marseille.jpg"
FILTER_TYPE = "GRAYSCALE"

# --- PATHS ---
input_path = os.path.join(INPUT_FOLDER, IMAGE_NAME)
output_path = os.path.join(OUTPUT_FOLDER, f"{FILTER_TYPE.lower()}_{IMAGE_NAME}")

# --- SETUP ---
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)
    print(f"Created directory: {OUTPUT_FOLDER}")

# --- PROCESSING ---
try:
    original_image = Image.open(input_path)
    width, height = original_image.size

    filtered_img = Image.new("RGB", (width, height))

    for x in range(width):
        for y in range(height):
            r, g, b = original_image.getpixel((x, y))
            avg = (r + g + b) // 3
            new_color = (avg, avg, avg)
            filtered_img.putpixel((x, y), new_color)
    filtered_img.save(output_path)

    print(f"Grayscale filter applied. Image saved to: {output_path}")
    print("Displaying the filtered image...")
    filtered_img.show()


except Exception as e:
    print(e)