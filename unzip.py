import zipfile
import os

def extract_zip(zip_path, extract_to):
    """
    Extracts a ZIP file to the specified directory.

    :param zip_path: The path to the ZIP file.
    :param extract_to: The directory to extract the contents to.
    """
    # Ensure the output directory exists
    os.makedirs(extract_to, exist_ok=True)

    # Open the ZIP file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Extract all the contents to the specified directory
        zip_ref.extractall(extract_to)
        print(f"Extracted all files to {extract_to}")

# Example usage
zip_path = 'TwitterAccountGenerator.zip'
extract_to = 'twt'
extract_zip(zip_path, extract_to)