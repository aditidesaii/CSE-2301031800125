from PIL import Image, ImageFilter
import os

def apply_grayscale(image):
    return image.convert("L")

def apply_blur(image):
    return image.filter(ImageFilter.BLUR)

def apply_edge_detect(image):
    return image.filter(ImageFilter.FIND_EDGES)

def save_image(image, original_path, suffix):
    base, ext = os.path.splitext(original_path)
    new_filename = f"{base}_{suffix}{ext}"
    image.save(new_filename)
    print(f"Saved image as: {new_filename}")

def main():
    print("=== Image Filter App ===")
    image_path = input("Enter the path to an image file: ")

    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        print("Image not found. Please check the path and try again.")
        return

    print("\nAvailable Filters:")
    print("1. Grayscale")
    print("2. Blur")
    print("3. Edge Detection")
    choice = input("Choose a filter (1-3): ")

    if choice == '1':
        filtered_image = apply_grayscale(image)
        save_image(filtered_image, image_path, "grayscale")
    elif choice == '2':
        filtered_image = apply_blur(image)
        save_image(filtered_image, image_path, "blur")
    elif choice == '3':
        filtered_image = apply_edge_detect(image)
        save_image(filtered_image, image_path, "edges")
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
