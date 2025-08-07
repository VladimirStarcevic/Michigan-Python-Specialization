from PIL import Image
import os

SEPIA_MATRIX = (
    (0.393, 0.769, 0.189),
    (0.349, 0.686, 0.168),
    (0.272, 0.534, 0.131)
)


GRAYSCALE_LUMA_MATRIX = (
    (0.299, 0.587, 0.114),
    (0.299, 0.587, 0.114),
    (0.299, 0.587, 0.114)
)


IDENTITY_MATRIX = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1)
)

INPUT_FOLDER = "input_images"
OUTPUT_FOLDER = "output_images"
IMAGE_NAME = "marseille.jpg"


def multiply_color_by_matrix(color_tuple, matrix):
    r, g, b = color_tuple

    new_r = int((r * matrix[0][0]) + (g * matrix[0][1]) + (b * matrix[0][2]))
    new_g = int((r * matrix[1][0]) + (g * matrix[1][1]) + (b * matrix[1][2]))
    new_b = int((r * matrix[2][0]) + (g * matrix[2][1]) + (b * matrix[2][2]))

    new_r = max(0,min(255, new_r))
    new_g = max(0, min(255, new_g))
    new_b = max(0, min(255, new_b))

    return new_r, new_g, new_b

def apply_matrix_filter(original_image, matrix):
    width, height = original_image.size
    new_img = Image.new("RGB", (width, height))

    for x in range(width):
        for y in range(height):
            old_pixel = original_image.getpixel((x, y))

            new_pixel = multiply_color_by_matrix(old_pixel, matrix)
            new_img.putpixel((x, y), new_pixel)

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
        filtered_image = apply_matrix_filter(original_image, GRAYSCALE_LUMA_MATRIX)
    elif user_choice == "SEPIA":
        print("Applying Sepia filter...")
        filtered_image = apply_matrix_filter(original_image, SEPIA_MATRIX)

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
