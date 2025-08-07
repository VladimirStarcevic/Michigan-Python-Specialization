from PIL import Image
import os

INPUT_FOLDER = "input_images"
OUTPUT_FOLDER = "output_images"
IMAGE_NAME = "marseille.jpg"


def apply_grayscale_filter(original_image):
    width, height = original_image.size
    new_img = Image.new("RGB", (width, height))

    print("-> Applying Grayscale: Processing pixels...")
    for x in range(width):
        for y in range(height):
            r, g, b = original_image.getpixel((x, y))
            avg = (r + g + b) // 3
            new_color = (avg, avg, avg)
            new_img.putpixel((x, y), new_color)

    return new_img


# --- PATHS ---
input_path = os.path.join(INPUT_FOLDER, IMAGE_NAME)

# --- SETUP ---
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)
    print(f"Created directory: {OUTPUT_FOLDER}")

# --- PROCESSING ---
try:
    print(f"Loading image from: {input_path}")
    original_image = Image.open(input_path)
    print("Image loaded successfully.")

    print("\nAvailable filters: GRAYSCALE, SEPIA, NEGATIVE")
    user_choice = input("Enter the filter name to apply: ").upper()

    filtered_image = None

    if user_choice == "GRAYSCALE":
        filtered_image = apply_grayscale_filter(original_image)
    else:
        print(f"Error: Unknown filter: '{user_choice}'.")

    if filtered_image:
        output_path = os.path.join(OUTPUT_FOLDER, f"{user_choice.lower()}_{IMAGE_NAME}")
        filtered_image.save(output_path)
        print(f"Image saved successfully to: {output_path}")

except FileNotFoundError:
    print(f"FATAL ERROR: The file {input_path} was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
