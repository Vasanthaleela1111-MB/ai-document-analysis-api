import base64
import os

file_path = input("Enter file path: ")

with open(file_path, "rb") as f:
    encoded = base64.b64encode(f.read()).decode()

print("\nBase64 String:\n")
print(encoded)

print("\nFile Name:", os.path.basename(file_path))
