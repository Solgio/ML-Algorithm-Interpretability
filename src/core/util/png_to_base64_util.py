import base64
import os

def png_to_base64(image_path):
    # Validate file existence
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"File not found: {image_path}")

    # Validate PNG extension
    if not image_path.lower().endswith(".png"):
        raise ValueError("The file must be a PNG image.")

    # Read and encode the image
    with open(image_path, "rb") as image_file:
        encoded_bytes = base64.b64encode(image_file.read())
        encoded_str = encoded_bytes.decode("utf-8")  # Convert bytes to string
    return encoded_str


if __name__ == "__main__":
    try:
        path = input("Enter PNG file path: ").strip()
        base64_str = png_to_base64(path)
        print("\nBase64 string (first 100 chars):")
        print(base64_str[:100] + "...")
        
        # Optional: Save to a .txt file

        output_file = os.path.splitext(path)[0] + "_base64.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(base64_str)
        print(f"Base64 string saved to: {output_file}")

    except Exception as e:
        print(f"Error: {e}")