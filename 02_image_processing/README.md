# Project: Python Image Filters

A Python application for applying various filters to images, created as a part of the University of Michigan "Python 3 Programming" course.

### A Story of Growth

This project is the next step in my programming journey. It is a new, Python-based version of a [similar image processing tool I previously built using JavaScript](https://github.com/VladimirStarcevic/JS-ImageProcessing).

While the JavaScript project was a fantastic introduction, this version demonstrates my transition to Python and its powerful, industry-standard libraries like **Pillow**.

---

## How It Works

The core logic uses nested loops to iterate through every pixel of an image. For each pixel, a mathematical function is applied to its RGB values to create the desired filter effect.

---

## Implemented Filters

*   Grayscale
*   Sepia
*   Negative
*   *(More filters will be added)*

---
## How to Run

1.  **Install requirements:** `pip install Pillow`
2.  **Prepare your image:** Place an image inside the `images` folder.
3.  **Run the script:** Execute `python image_filter.py` after setting your image name in the script.