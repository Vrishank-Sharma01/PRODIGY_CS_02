from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    image_array = np.array(image)

    # Simple encryption: Add key to each pixel value
    encrypted_array = (image_array + key) % 256

    encrypted_image = Image.fromarray(np.uint8(encrypted_array))
    encrypted_image.save(output_path)

def decrypt_image(encrypted_path, output_path, key):
    encrypted_image = Image.open(encrypted_path)
    encrypted_array = np.array(encrypted_image)

    # Simple decryption: Subtract key from each pixel value
    decrypted_array = (encrypted_array - key) % 256

    decrypted_image = Image.fromarray(np.uint8(decrypted_array))
    decrypted_image.save(output_path)

# Example usage
image_path = 'dress.png'  # Replace with your input image path
encrypted_path = 'encrypted_image.png'
decrypted_path = 'decrypted_image.png'
key = [50]  # Example key, can be any integer

encrypt_image(image_path, encrypted_path, key)
decrypt_image(encrypted_path, decrypted_path, key)

print("Encryption and Decryption completed.")
