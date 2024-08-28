import os
from PIL import Image

def convert_images_to_binary(directory, threshold=50):
    # Ensure the directory exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):  # Add more formats if needed
            img_path = os.path.join(directory, filename)
            try:
                with Image.open(img_path) as img:
                    # Convert image to grayscale
                    img_gray = img.convert('L')
                    
                    # Apply threshold to create binary image
                    img_binary = img_gray.point(lambda p: 255 if p >= threshold else 0)
                    
                    # Save the binary image in the same directory, overwriting the original
                    img_binary.save(img_path)
                    
                    print(f"Converted and saved image to binary: {filename}")
            except Exception as e:
                print(f"Failed to convert image {filename} to binary: {e}")

if __name__ == "__main__":
    directory_path = ['/home/ameer/proj-computer-vision/Hand-Gesture-Recognition-Using-Background-Elllimination-and-Convolution-Neural-Network/Dataset/ThumbImages',
                      '/home/ameer/proj-computer-vision/Hand-Gesture-Recognition-Using-Background-Elllimination-and-Convolution-Neural-Network/Dataset/ThumbTest']
    for dir in directory_path:
        convert_images_to_binary(dir, 100)



