import os
import requests
import zipfile
import shutil

# Define the URL of the ZIP file and the local filename
url = (
    "https://api.worldbank.org/v2/en/indicator/"
    "NY.GDP.MKTP.CD?downloadformat=csv"
)
zip_filename = "gdp_by_country.zip"
extracted_folder = "gdp_data"

# Function to delete a file or folder
def delete_path(path):
    if os.path.isfile(path):
        os.remove(path)
        print(f"Deleted file: {path}")
    elif os.path.isdir(path):
        shutil.rmtree(path)
        print(f"Deleted folder: {path}")
    else:
        print(f"Path not found: {path}")

# Function to move a folder
def move_folder(src, dst):
    shutil.move(src, dst)
    print(f"Moved folder from {src} to {dst}")

# Function to rename a file or folder
def rename_path(src, dst):
    os.rename(src, dst)
    print(f"Renamed from {src} to {dst}")

# Download the ZIP file using requests
response = requests.get(url)
with open(zip_filename, 'wb') as file:
    file.write(response.content)
print(f"Downloaded {zip_filename} from {url}")

# Extract the contents of the ZIP file into a specific folder
with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
    zip_ref.extractall(extracted_folder)
    extracted_files = zip_ref.namelist()  # Get the list of extracted files
    print(f"Extracted the following files into {extracted_folder}: {extracted_files}")

# Optional: Verify the CSV file content (print the first few lines of each CSV file)
for file in extracted_files:
    if file.endswith('.csv'):
        file_path = os.path.join(extracted_folder, file)
        with open(file_path, 'r', encoding='utf-8') as f:
            print(f"\nContent of {file_path}:")
            for _ in range(5):  # Print first 5 lines
                print(f.readline().strip())

# Clean up by removing the downloaded ZIP file
delete_path(zip_filename)

# Move the extracted folder to a new location
new_folder_location = "new_gdp_data_location"
move_folder(extracted_folder, new_folder_location)

# Rename the new folder
renamed_folder_location = "renamed_gdp_data"
rename_path(new_folder_location, renamed_folder_location)

# Optionally delete the renamed folder
# delete_path(renamed_folder_location)
